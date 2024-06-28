from django.urls import path
from mytodo.views import IndexView, AddView, UpdateTaskCompleteView, EditTaskView, DeleteTaskView

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("add/", AddView.as_view(), name="add"),
    path("update_task_complete/", UpdateTaskCompleteView.as_view(), name="update_task_complete"),
    path("edit_task/<int:task_id>/", EditTaskView.as_view(), name="edit_task"),
    path("delete_task/<int:task_id>/", DeleteTaskView.as_view(), name="delete_task"),
]
