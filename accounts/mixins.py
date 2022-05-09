from django.contrib.auth.mixins import UserPassesTestMixin


class AccessMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_anonymous
