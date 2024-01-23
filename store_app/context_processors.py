from .models import Department


def get_department(request):
    departments = Department.objects.all()
    return {'departments': departments}
