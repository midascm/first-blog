from django.urls import path, re_path
from .views import line_chart, line_chart_json
from chartjs import views

app_name = 'chartjs'

urlpatterns = [
  '...',
  path('chart/', line_chart, name='chartjs/line_chart'),
  path('chartJSON/', line_chart_json, name='line_chart_json'),
]