from add_new_task import AddTaskView
from task_list_view import TaskListView

class UI:
    def __init__(self, root):
        self._root = root
        self._current_view = None

    def start(self):
        self._show_task_list_view()


    def _hide_current_view(self):
        if self._current_view:
            self._current_view.destroy()
            self._current_view = None


    def _show_task_list_view(self):
        self._hide_current_view()
        self._current_view = TaskListView(self._root, self. _handle_open_add)
        self._current_view.pack()


    def _handle_open_add(self):
        AddTaskView(self._root, self._handle_add_task)


    def _handle_add_task(self):
        print(f"New task: ")