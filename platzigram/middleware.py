"""[summary]
"""

from django.shortcuts import redirect
from django.urls import reverse

class ProfileCompletionMeddleware:
    """ Profile completion middleware
    """
    def __init__(self, get_response):
        """middleware initialization

        Args:
            get_response ([type]): [description]
        """
        self.get_response = get_response


    def __call__(self, request):
        """  Code to executed for each request before
        the view is called

        Args:
            request ([type]): [description]
        """
        if not request.user.is_anonymous:
            if not request.user.is_staff:
                profile = request.user.profile
                if not profile.picture or not profile.biography:
                    if request.path not in [reverse('update_profile'), reverse('logout')]:
                        return redirect('update_profile')

        response = self.get_response(request)
        return response
