import os
import datetime
from django.utils import timezone
from django.db.models import Sum
from .models import ReadDetail, ReadNum


def read_statistics_once_read(request, obj):
    # ct = ContentType.objects.get_for_model(obj)
    key = "%s_%s_read" % ('teacher', obj.pk)

    if not request.COOKIES.get(key):
        # 总阅读数 +1
        # readnum, created = ReadNum.objects.get_or_create(content_type=ct, object_id=obj.pk)
        # readnum.read_num += 1
        # readnum.save()
        # date = models.DateField(default=timezone.now)
        # read_num = models.IntegerField(default=0)
        # teacher = models.ForeignKey(Teacher, on_delete=models.DO_NOTHING)
        if ReadNum.objects.filter(teacher=obj).count():
            readnum = ReadNum.objects.get(teacher=obj)
        else:
            readnum = ReadNum(teacher=obj)
        readnum.read_num += 1
        readnum.save()

        # 当天阅读数 +1
        date = timezone.now().date()
        readDetail, created = ReadDetail.objects.get_or_create(teacher=obj, date=date)
        readDetail.read_num += 1
        readDetail.save()
    return key


def get_seven_days_read_data(teacher):
    today = timezone.now().date()
    dates = []
    read_nums = []
    for i in range(6, -1, -1):
        date = today - datetime.timedelta(days=i)
        dates.append(date.strftime('%m/%d'))
        try:
            read_details = ReadDetail.objects.get(teacher=teacher, date=date)
            # result = read_details.aggregate(read_num_sum=Sum('read_num'))
            read_nums.append(read_details.read_num)
        except Exception as e:
            read_nums.append(0)
    return dates, read_nums
