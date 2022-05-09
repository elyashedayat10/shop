from django.http import Http404


class OwnerMixin:
    def dispatch(self, request, user_id, *args, **kwargs):
        if user_id == request.user.id:
            return super(OwnerMixin, self).dispatch(request, *args, **kwargs)
        raise Http404
