import os


# from .models import ReadDetail, ReadNum


def user_directory_path(instance, filename):
    ext = filename.split('.').pop()
    filename = '{0}{1}.{2}'.format(instance.real_name, instance.student_ID, ext)
    return os.path.join(instance.student_ID, filename)
