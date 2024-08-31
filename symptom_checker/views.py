# from django.shortcuts import render
#
# # Create your views here.

from django.shortcuts import render
from .models import Condition

# def symptom_checker(request):
#     if request.method == 'POST':
#         symptoms = request.POST.get('symptoms', '').lower().split(',')
#         matched_conditions = Condition.objects.filter(symptoms__icontains=symptoms[0])
#         for symptom in symptoms[1:]:
#             matched_conditions = matched_conditions.filter(symptoms__icontains=symptom)
#         return render(request, 'symptom_checker/results.html', {'conditions': matched_conditions})
#     return render(request, 'symptom_checker/index.html')


# symptom_checker/views.py
# from django.shortcuts import render
# from .models import Condition
# from .forms import SymptomForm
#
#
# def symptom_checker(request):
#     if request.method == 'POST':
#         form = SymptomForm(request.POST)
#         if form.is_valid():
#             input_symptoms = form.cleaned_data['symptoms'].lower().split(',')
#             input_symptoms = [symptom.strip() for symptom in input_symptoms]
#
#             conditions = Condition.objects.all()
#             matching_conditions = []
#
#             for condition in conditions:
#                 condition_symptoms = [symptom.strip().lower() for symptom in condition.symptoms.split(',')]
#                 if set(input_symptoms) & set(condition_symptoms):  # Check for intersection
#                     matching_conditions.append(condition)
#
#             return render(request, 'symptom_checker/results.html', {'conditions': matching_conditions})
#
#     else:
#         form = SymptomForm()
#
#     return render(request, 'symptom_checker/index.html', {'form': form})


# symptom_checker/views.py
from django.shortcuts import render
from .models import Condition, HealthcareFacility
from .forms import SymptomForm
from datetime import datetime, timedelta
from .models import SearchHistory
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .utils import fetch_external_data
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as auth_logout


# def symptom_checker(request):
#     if request.method == 'POST':
#         form = SymptomForm(request.POST)
#         if form.is_valid():
#             input_symptoms = form.cleaned_data['symptoms'].lower().split(',')
#             input_symptoms = [symptom.strip() for symptom in input_symptoms]
#
#             conditions = Condition.objects.all()
#             matching_conditions = []
#
#             for condition in conditions:
#                 condition_symptoms = [symptom.strip().lower() for symptom in condition.symptoms.split(',')]
#                 if set(input_symptoms) & set(condition_symptoms):  # Check for intersection
#                     matching_conditions.append(condition)
#
#             # Fetch associated healthcare facilities
#             facilities = HealthcareFacility.objects.filter(condition__in=matching_conditions)
#
#             return render(request, 'symptom_checker/results.html', {
#                 'conditions': matching_conditions,
#                 'facilities': facilities
#             })
#
#     else:
#         form = SymptomForm()
#
#     return render(request, 'symptom_checker/index.html', {'form': form})
def suggest_conditions(user, search_terms):
    recent_searches = SearchHistory.objects.filter(
        user=user,
        timestamp__gte=datetime.now() - timedelta(days=30)
    ).values_list('search_terms', flat=True)
    # Implement logic to analyze recent searches and suggest conditions
    # This can be done with a simple frequency count or a more complex algorithm
#
# def symptom_checker(request):
#     if request.method == 'POST':
#         form = SymptomForm(request.POST)
#         if form.is_valid():
#             input_symptoms = form.cleaned_data['symptoms'].lower().split(',')
#             input_symptoms = [symptom.strip() for symptom in input_symptoms]
#
#             # Track the search
#             if request.user.is_authenticated:
#                 SearchHistory.objects.create(user=request.user, search_terms=','.join(input_symptoms))
#
#             conditions = Condition.objects.all()
#             matching_conditions = []
#
#             for condition in conditions:
#                 condition_symptoms = [symptom.strip().lower() for symptom in condition.symptoms.split(',')]
#                 if set(input_symptoms) & set(condition_symptoms):  # Check for intersection
#                     matching_conditions.append(condition)
#
#             # Suggest based on history
#             if request.user.is_authenticated:
#                 suggest_conditions(request.user, input_symptoms)
#
#             facilities = HealthcareFacility.objects.filter(condition__in=matching_conditions)
#
#             return render(request, 'symptom_checker/results.html', {
#                 'conditions': matching_conditions,
#                 'facilities': facilities
#             })
#
#     else:
#         form = SymptomForm()
#
#     return render(request, 'symptom_checker/index.html', {'form': form})

def symptom_checker(request):
    if request.method == 'POST':
        form = SymptomForm(request.POST)
        if form.is_valid():
            input_symptoms = form.cleaned_data['symptoms'].lower().split(',')
            input_symptoms = [symptom.strip() for symptom in input_symptoms]

            # Fetch external data
            external_data = fetch_external_data(input_symptoms)
            # Process external data as needed

            conditions = Condition.objects.all()
            matching_conditions = []

            for condition in conditions:
                condition_symptoms = [symptom.strip().lower() for symptom in condition.symptoms.split(',')]
                if set(input_symptoms) & set(condition_symptoms):  # Check for intersection
                    matching_conditions.append(condition)

            facilities = HealthcareFacility.objects.filter(condition__in=matching_conditions)

            return render(request, 'symptom_checker/results.html', {
                'conditions': matching_conditions,
                'facilities': facilities,
                'external_data': external_data
            })

    else:
        form = SymptomForm()

    return render(request, 'symptom_checker/index.html', {'form': form})


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


@login_required
def profile(request):
    # Fetch user-specific data, e.g., search history
    # Example: search_history = SearchHistory.objects.filter(user=request.user)
    return render(request, 'profile.html')

def logout(request):
    auth_logout(request)
    return redirect('login')