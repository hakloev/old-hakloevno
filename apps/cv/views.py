from django.shortcuts import render
from models import education, work, organization

# Create your views here.

def cv(request):
    edu = education.objects.all().order_by('-started')
    works = work.objects.all().order_by('-started')
    org = organization.objects.all().order_by('-started')
    return render(request, u'cv/cv.html', {
        'request': request,
        'educations': edu,
        'works': works,
        'orgs': org})
