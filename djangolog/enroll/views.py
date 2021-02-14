from django.shortcuts import render
from django.conf import settings
import csv, io
import logging
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from enroll.models import EventsForm
from django.db import models

def success(request):
    return render(request, "success.html")


def error(request):
    return render(request, "error.html")


def upload_csv(request):
    data = {}
    if "GET" == request.method:
        return render(request, "upload_csv.html", data)

    try:
        print("helo")
        csv_file = request.FILES["csv_file"]
        if not csv_file.name.endswith('.log'):
            messages.error(request, 'File is not CSV type')
            return HttpResponseRedirect(reverse("upload_csv"))

        if csv_file.multiple_chunks():
            messages.error(request, "Uploaded file is too big (%.2f MB)." % (csv_file.size / (1000 * 1000),))
            return HttpResponseRedirect(reverse("upload_csv"))

        file_data = csv_file.read().decode("utf-8")
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
            # if form.is_valid():
            #	form.save()
            # else:
            #	logging.getLogger("error_logger").error(form.errors.as_json())
            except Exception as e:
                logging.getLogger("error_logger").error(repr(e))
                pass

    except Exception as e:
        logging.getLogger("error_logger").error("Unable to upload file. " + repr(e))
        messages.error(request, "Unable to upload file. " + repr(e))
        return HttpResponseRedirect(reverse("error"))

    return HttpResponseRedirect(reverse("success"))
