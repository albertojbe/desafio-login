from django.shortcuts import redirect

# Decorator para redirecionar para menu caso ja esteja logado
def redireciona_se_logado(view_func):
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('menu') 
        return view_func(request, *args, **kwargs)
    return wrapper