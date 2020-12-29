from rest_framework.generics import GenericAPIView


class SerializerControlAPIView(GenericAPIView):
    """
    """

    def get_serializer(self, *args, action=None, **kwargs):

        # autodetect action: view action or HTTP method based
        if action is None:
            # assume view action
            try:
                action = self.action

            # method-based detection
            except AttributeError:
                if self.request is not None:
                    if self.request.method in ("POST",):
                        action = "create"
                    elif self.request.method in ("GET",):
                        action = "view"
                    elif self.request.method in ("PUT", "PATCH",):
                        action = "update"

        serializer_class = self.get_serializer_class(action=action)
        kwargs["context"] = self.get_serializer_context()
        return serializer_class(*args, **kwargs)

    def get_serializer_class(self, action=None):

        # try to substitute 'list' or 'retrieve' with a more generic 'view'
        # if no respective field defined
        if action and action in ("retrieve", "list"):
            target_serializer_class = getattr(
                self, "{}_serializer_class".format(action), None
            )
            action = action if target_serializer_class else "view"
        elif action and action in ("create", "update", "partial_update"):
            target_serializer_class = getattr(
                self, "{}_serializer_class".format(action), None
            )
            action = action if target_serializer_class else "edit"

        serializer_class_field = (
            "{}_serializer_class".format(action) if action else "serializer_class"
        )
        serializer_class = getattr(self, serializer_class_field, None)

        return serializer_class or super().get_serializer_class()

    def get_create_response(self, serializer, **kwargs):
        # get view representation before returning response:
        retrieve_serializer_class = getattr(
            self, "{}_serializer_class".format("retrieve"), None
        )
        action = "retrieve" if retrieve_serializer_class else "view"
        serializer = self.get_serializer(serializer.instance, action=action)
        return super().get_create_response(serializer, **kwargs)

    def get_update_response(self, serializer, **kwargs):
        # get view representation before returning response
        retrieve_serializer_class = getattr(
            self, "{}_serializer_class".format("retrieve"), None
        )
        action = "retrieve" if retrieve_serializer_class else "view"
        serializer = self.get_serializer(serializer.instance, action=action)
        return super().get_update_response(serializer, **kwargs)


__all__ = ("SerializerControlAPIView",)
