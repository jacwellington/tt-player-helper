from django.shortcuts import render, get_object_or_404
from form_templates.models import FormTemplate, FieldData

def detail(request, form_id):
	form_template = get_object_or_404(FormTemplate, pk=form_id)
	if(form_template):
		try:
			fielddata = form_template.fielddata
		except FieldData.DoesNotExist:
			fielddata = FieldData()
			fielddata.field_data = ''
			fielddata.formtemplate = form_template
			fielddata.sa
	return render(request, 'form_template/detail.html', {'form_template': form_template})

