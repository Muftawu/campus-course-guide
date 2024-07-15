
def redirect_if_authenticated(request, redirect):
    if request.user.is_authenticated:
        return redirect('users:dashboard')