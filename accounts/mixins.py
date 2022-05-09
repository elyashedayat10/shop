from django.contrib.auth.mixins import UserPassesTestMixin


class AdminMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_admin
