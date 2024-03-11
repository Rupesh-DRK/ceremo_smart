from .models import userData1
def user_context(request):
    if request.user.is_authenticated:
        return {'user':request.user}
    else:
        return{'user':None}

def get_session_username(request):
    try:
        session_id = request.session.get('_auth_user_id')
        user = userData1.objects.get(pk=session_id)
        username = user.username
        email=user.email
    except userData1.DoesNotExist:
        username = None
        email=None
        user = None
    return {'user':user,'email':email,'session_username': username,'pk_id':session_id}