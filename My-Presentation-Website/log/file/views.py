from django.shortcuts import render
from django.conf import settings
import csv, io
import logging
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from file.models import EventsForm
from django.db import models

def success(request):
    return render(request, "success.html")
def error(request):
    return render(request, "error.html")

def upload(request):
    data = {}
    if "GET" == request.method:
        return render(request, "upload.html", data)


    try:
        print("helo")
        log_file = request.FILES["log_file"]
        if not log_file.name.endswith('.log'):
            messages.error(request,'File is not LOG type')
            return HttpResponseRedirect(reverse("upload"))

        if log_file.multiple_chunks():
            messages.error(request, "Uploaded file is too big (%.9f MB)." % (log_file.size / (10000 * 10000),))
            return HttpResponseRedirect(reverse("upload"))

        file_data=log_file.read().decode("utf-8")
        print(request)

        lines = file_data.split("\n")

        for line in lines:
            fields = line.split(",")
            data_dict = {}
            data_dict['time'] = fields[0]
            data_dict['error_type'] = fields[1]
            data_dict['message'] = fields[2]

            # df = pd.DataFrame(fields)
            try:
                form = EventsForm(time=fields[0], error_type=fields[1], message=fields[2])
                form.save()
            except Exception as e:
                logging.getLogger("error_logger").error(repr(e))
                pass

    except Exception as e:
        logging.getLogger("error_logger").error("Unable to upload file. " + repr(e))
        messages.error(request, "Unable to upload file. " + repr(e))
        return HttpResponseRedirect(reverse("error"))

    return HttpResponseRedirect(reverse("success"))