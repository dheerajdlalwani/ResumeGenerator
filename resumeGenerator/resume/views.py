from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . models import UserDetails
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.


def home(request):
    return render(request, 'resume/base.html')


@login_required(login_url='login')
def user_details(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        date_of_birth = request.POST['date_of_birth']
        current_position = request.POST['current_position']
        intro = request.POST['intro']
        linkedin = request.POST['linkedin']
        github = request.POST['github']
        twitter = request.POST['twitter']
        contact = request.POST['contact']
        skill_1 = request.POST['skill_1']
        skill_2 = request.POST['skill_2']
        skill_3 = request.POST['skill_3']
        skill_4 = request.POST['skill_4']
        skill_5 = request.POST['skill_5']
        skill_6 = request.POST['skill_6']
        skill_7 = request.POST['skill_7']
        project_1_name = request.POST['project_1_name']
        project_1_description = request.POST['project_1_description']
        project_1_github = request.POST['project_1_github']
        project_2_name = request.POST['project_2_name']
        project_2_description = request.POST['project_2_description']
        project_2_github = request.POST['project_2_github']
        project_3_name = request.POST['project_3_name']
        project_3_description = request.POST['project_3_description']
        project_3_github = request.POST['project_3_github']
        project_4_name = request.POST['project_4_name']
        project_4_description = request.POST['project_4_description']
        project_4_github = request.POST['project_4_github']
        internship_1_title = request.POST['internship_1_title']
        internship_1_duration = request.POST['internship_1_duration']
        internship_1_description = request.POST['internship_1_description']
        internship_2_title = request.POST['internship_2_title']
        internship_2_duration = request.POST['internship_2_duration']
        internship_2_description = request.POST['internship_2_description']
        internship_3_title = request.POST['internship_3_title']
        internship_3_duration = request.POST['internship_3_duration']
        internship_3_description = request.POST['internship_3_description']
        education_current_title = request.POST['education_current_title']
        education_current_marks = request.POST['education_current_marks']
        education_current_description = request.POST['education_current_description']
        education_previous_title = request.POST['education_previous_title']
        education_previous_description = request.POST['education_previous_description']
        education_previous_marks = request.POST['education_previous_marks']
        community = request.POST['community']
        certification_1 = request.POST['certification_1']
        certification_2 = request.POST['certification_2']
        certification_3 = request.POST['certification_3']
        certification_4 = request.POST['certification_4']
        hobbies = request.POST['hobbies']
        user_id = request.user.id
        user = User.objects.get(id=user_id)

        userdata = UserDetails(
            user=user,
            first_name=first_name,
            last_name=last_name, 
            email=email, 
            date_of_birth=date_of_birth,
            current_position=current_position,
            intro=intro,
            linkedin=linkedin, 
            github=github,
            twitter=twitter,
            contact=contact,
            skill_1=skill_1,
            skill_2=skill_2,
            skill_3=skill_3,
            skill_4=skill_4,
            skill_5=skill_5,
            skill_6=skill_6,
            skill_7=skill_7,
            project_1_name=project_1_name,
            project_1_description=project_1_description,
            project_1_github=project_1_github,
            project_2_name=project_2_name,
            project_2_description=project_2_description,
            project_2_github=project_2_github,
            project_3_name=project_3_name,
            project_3_description=project_3_description,
            project_3_github=project_3_github,
            project_4_name=project_4_name,
            project_4_description=project_4_description,
            project_4_github=project_4_github,
            internship_1_title=internship_1_title,
            internship_1_duration=internship_1_duration,
            internship_1_description=internship_1_description,
            internship_2_title=internship_2_title,
            internship_2_duration=internship_2_duration,
            internship_2_description=internship_2_description,
            internship_3_title=internship_3_title,
            internship_3_duration=internship_3_duration,
            internship_3_description=internship_3_description,
            education_current_title=education_current_title,
            education_current_marks=education_current_marks,
            education_current_description=education_current_description,
            education_previous_title=education_previous_title,
            education_previous_marks=education_previous_marks,
            education_previous_description=education_previous_description,
            community=community,
            certification_1=certification_1,
            certification_2=certification_2,
            certification_3=certification_3,
            certification_4=certification_4,
            hobbies=hobbies)
        userdata.save()
        messages.info(request, 'Data Saved in database successfully!')
    return render(request, 'resume/userdetails.html')


@login_required(login_url='login')
def preview_data(request):
    user_id = request.user.id
    user = User.objects.get(id=user_id)
    obj = UserDetails.objects.get(user=user)
    return render(request, 'resume/previewdata.html', {'obj': obj})


