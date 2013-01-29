from django.shortcuts import render, get_object_or_404
from form_templates.models import FormTemplate, FieldData
import json

def detail(request, form_id):
	form_template = get_object_or_404(FormTemplate.objects.select_related(), pk=form_id)
	try:
		fielddata = form_template.fielddata
	except FieldData.DoesNotExist:
		# Create new json data
		fielddata = FieldData()
		fielddata.form = form_template
		stringfield_dict = {}
		numberfield_dict = {}
		listfield_dict = {}
		for string_field in form_template.stringfield_set.all():
			stringfield_dict[string_field.name] = ''
		for number_field in form_template.numberfield_set.all():
			numberfield_dict[number_field.name] = ''
		for list_field in form_template.listfield_set.all():
			listfield_dict[list_field.name] = ''
		json_data = {'StringFields': stringfield_dict, 'NumberFields': numberfield_dict, 'ListFields': listfield_dict}
		fielddata.field_data = json.dumps(json_data)
		fielddata.save()
	python_field_data = json.loads(fielddata.field_data)
	print python_field_data['NumberFields']['HP']
	return render(request, 'form_templates/detail.html', {'form_template': form_template, 'field_data': python_field_data})

