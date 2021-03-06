from django.core.exceptions import PermissionDenied


class OwnerMixin:
    def dispatch(self, request, profile_id, *args, **kwargs):
        if profile_id == request.user.id:
            return super(OwnerMixin, self).dispatch(request, *args, **kwargs)
        raise PermissionDenied
