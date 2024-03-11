
from django.shortcuts import render
from django.contrib import messages

def anonymous_required(view_function):
    def _wrapped_view(request, *args, **kwargs):
        if request.user.is_authenticated:
            # Redirect authenticated users to the events page
            return view_function(request, *args, **kwargs)
        else:
            # Show a message to anonymous users
            messages.warning(request, 'Please login first.')
            return render(request, 'sign_in.html')  # Replace 'login.html' with your login page URL
    return _wrapped_view
