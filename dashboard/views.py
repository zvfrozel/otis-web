# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse, reverse_lazy
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from django.views.generic.edit import UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

import core
import dashboard
import exams
import roster, roster.utils
import forms


@login_required
def main(request, student_id):
	student = get_object_or_404(roster.models.Student.objects, id = student_id)
	if not student.can_view_by(request.user):
		context = {}
		context['student'] = student
		return render(request, "roster/denied.html", context)
	
	context = {}
	context['title'] = "Dashboard for " + student.name
	context['student'] = student
	context['omniscient'] = student.is_taught_by(request.user)
	context['olympiads'] = exams.models.MockOlympiad.objects.filter(due_date__isnull=False)
	context['assignments'] = exams.models.Assignment.objects.filter(semester__active=True)
	return render(request, "dashboard/main.html", context)

@login_required
def uploads(request, student_id, unit_id):
	student = get_object_or_404(roster.models.Student.objects, id = student_id)
	if unit_id == "0":
		unit = None
	else:
		unit = get_object_or_404(core.models.Unit.objects, id = unit_id)\
				if unit_id else None
	if not student.can_view_by(request.user):
		context = {}
		context['student'] = student
		return render(request, "roster/denied.html", context)

	if request.method == "POST":
		form = forms.NewUploadForm(request.POST, request.FILES)
		if form.is_valid():
			new_upload = form.save(commit=False)
			new_upload.benefactor = student
			new_upload.owner = request.user
			new_upload.save()
			messages.success(request, "New file has been uploaded.")
	else:
		form = forms.NewUploadForm(initial = {'unit' : unit})


	context = {}
	context['title'] = 'File Uploads'
	context['student'] = student
	context['unit'] = unit
	context['form'] = form
	context['files'] = dashboard.models.UploadedFile.objects\
			.filter(benefactor=student, unit=unit)
	# TODO form for adding new files
	return render(request, "dashboard/uploads.html", context)

@login_required
def index(request):
	# Check if active student
	try:
		student = roster.models.Student.objects.get(user = request.user, semester__active = True)
		return HttpResponseRedirect(reverse("dashboard", args=(student.id,)))
	except ObjectDoesNotExist:
		pass

	# Otherwise, do listing
	students = roster.utils.get_visible(request.user,
		roster.models.Student.objects.filter(semester__active = True))
	context = {}
	context['title'] = "Current Semester Listing"
	context['students'] = students
	context['show_past_link'] = True
	return render(request, "dashboard/stulist.html", context)

@login_required
def past(request):
	students = roster.utils.get_visible(request.user, roster.models.Student.objects.all())
	context = {}
	context['title'] = "Previous Semester Listing"
	context['students'] = students
	return render(request, "dashboard/stulist.html", context)

class UpdateFile(LoginRequiredMixin, UpdateView):
	model = dashboard.models.UploadedFile
	fields = ('category', 'content', 'unit',)
class DeleteFile(LoginRequiredMixin, DeleteView):
	model = dashboard.models.UploadedFile
	success_url = reverse_lazy("index")
