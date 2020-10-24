from rest_framework import serializers


class ModelCleanSerializer(serializers.Serializer):
    """
    ModelCleanMixin is different from usual understanding of the model ``clean``
    method. The key difference is that in usual understanding the ``clean``
    method is called on an instance to validate or set values while here, at the
    moment of calling the ``clean`` method the target instance does not exist
    yet, so it won't set any values on the target model instance.
    """
    def validate(self, attrs):
        request = self.context.get('request', None)
        method = getattr(request, 'method', None)
        instance = None

        # simulating instance creation: we need to pop relation data and set is
        # separately
        if method == 'POST':
            info = model_meta.get_field_info(self.Meta.model)
            model_attrs = dict()
            relation_attrs = dict()

            for attr, value in attrs.items():

                # any data outside the ORM scope will be ignored
                if attr not in info.relations and attr not in info.fields:
                    continue

                if attr in info.relations and info.relations[attr].to_many:
                    relation_attrs[attr] = attrs[attr]
                else:
                    model_attrs[attr] = attrs[attr]

            instance = self.Meta.model(**model_attrs)

            # depending on teh DB version this may work or not
            # self.bind_data_to_instance(instance, relation_attrs)

        # simulating instance update: simply bind data to the instance
        elif method in ('PUT', 'PATCH'):
            instance = self.Meta.model.objects.get(id=self.instance.id)
            self.bind_data_to_instance(instance, attrs)

        if instance:
            try:
                instance.clean()
            except ValidationError as e:
                raise serializers.ValidationError(e.args[0])

        return super().validate(attrs)

    @classmethod
    def bind_data_to_instance(cls, instance, attrs: dict):
        info = model_meta.get_field_info(instance)
        for attr, value in attrs.items():

            # patch GenericForeignKey fields:
            # loop will be skipped without value binding
            if attr not in info.relations and attr not in info.fields:
                continue

            if attr in info.relations and info.relations[attr].to_many:
                field = getattr(instance, attr)
                field.set(value)
            else:
                setattr(instance, attr, value)


class ViewerUserMixinSerializer(serializers.Serializer):
    def to_representation(self, instance):
        user = getattr(self.context.get('request'), 'user', None)
        if user and hasattr(instance, 'set_viewer_user'):
            instance.set_viewer_user(user)
        return super().to_representation(instance)
