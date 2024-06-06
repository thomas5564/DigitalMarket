from django.shortcuts import render, redirect
from item.models import Category,Item
from .forms import SignUpForm, LoginForm
from django.contrib.auth import logout,authenticate,login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q






def Search(request):
    categories = Category.objects.all()
    query = request.GET.get('query', '')
    selected_category = request.GET.get('cat', 0)

    # Filter items that are not sold
    items = Item.objects.filter(is_sold=False)

    # Filter items by query if provided
    if query:
        items = items.filter(Q(name__icontains=query) | Q(description__icontains=query))

    # Filter items by category if selected_category is provided and not zero
    if selected_category and selected_category != '0':
        items = items.filter(Category_id=selected_category)

    context = {
        'Categories': categories,
        'Items': items,
        'query': query,
        'selectcat': int(selected_category),
    }

    return render(request, 'core/search.html', context)





def index(req):

    Catergories=Category.objects.all()
    Items=Item.objects.filter(is_sold=False)[0:6]
    if req.user.is_authenticated:
        print('logged in')
    else:
        print('logged out')
    print("helloyou")
    username = None
    if req.user.is_authenticated:
        username = req.user.username
    return render(req,"core/index.html",{'Categories':Catergories,'Items':Items,'username':username})

def contacts(req):
    return render(req,'core/contacts.html')

def logout_view(req):
    Catergories=Category.objects.all()
    Items=Item.objects.filter(is_sold=False)[0:6]
    logout(req)
    print("logout")
    response = render(req, 'core/index.html',{'Categories': Catergories, 'Items': Items})  # Adjust 'home' to your desired URL name
    return response  # Adjust 'home' to your desired URL name




def login_view(req):
    print("logging in")
    
    if req.method == 'POST':
        username = req.POST['username']
        password = req.POST['password1']
        user = authenticate(req, username=username, password=password)
        if user is not None:
            Catergories=Category.objects.all()
            Items=Item.objects.filter(is_sold=False)[0:6]
            messages.success(req, "You have been logged in")
            login(req, user)  # Pass the request object as the first argument
            return render(req,"core/index.html",{'Categories':Catergories,'Items':Items,'username':username})

        else:
            messages.error(req, "There was an error logging in, try again")
            return render(req, 'core/login.html', {'form': LoginForm()})  # Ensure to pass request and form
    else:
        form = LoginForm()
        return render(req, 'core/login.html', {'form': form})


        

def SignUp(request):
    print("bellooo")
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        print("posting")
        if form.is_valid():  # Corrected this line
            form.save()
            return redirect('/login/')  # Assuming you have a URL pattern named 'login'
        else:
            print(form.errors)
    else:
        form = SignUpForm()
    return render(request, 'core/signup.html', {'form': form})
