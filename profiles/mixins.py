from django.core.exceptions import PermissionDenied


class OwnerMixin:
    def dispatch(self, request, user_id, *args, **kwargs):
        if user_id == request.user.id:
            return super(OwnerMixin, self).dispatch(request, *args, **kwargs)
        raise PermissionDenied
