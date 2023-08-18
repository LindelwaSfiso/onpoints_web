from django.shortcuts import render


def home(request):
    """
    View for displaying the public website of the project.
    Here other students can apply to our clients/schools registered.
    Parents can also get feedback from this public facing website.
    """
    return render(request, 'website/home.html', {})


def about_us(request):
    """
    View to display about page.
    Include all information about OPS here.
    """
    return render(request, 'website/about_us.html', {})
