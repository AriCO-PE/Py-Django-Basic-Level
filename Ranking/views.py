from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.db.models import Q
from students.models import CustomUser

@login_required
def student_ranking(request):
    
    order = request.GET.get("order", "aura_desc") 
    search = request.GET.get("search", "").strip()


    students = CustomUser.objects.filter(aura__isnull=False)

   
    if search:
        students = students.filter(
            Q(first_name__icontains=search) |
            Q(last_name__icontains=search)
        )

    
    if order == "aura_desc":
        students = students.order_by('-aura')
    elif order == "aura_asc":
        students = students.order_by('aura')
    elif order == "name_asc":
        students = students.order_by('first_name', 'last_name')
    elif order == "name_desc":
        students = students.order_by('-first_name', '-last_name')

    
    context = {
        "students": students,
        "order": order,
        "search": search
    }
    return render(request, "ranking.html", context)
