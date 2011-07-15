from flaskext import wtf
from collection.documents import Task

class TaskForm(wtf.Form):
    document_class = Task
    task = wtf.TextField(validators=[wtf.Required()])
    start = wtf.IntegerField(validators=[wtf.Required()])
    time=wtf.IntegerField(validators=[wtf.required()])

    instance = None

    def __init__(self, document=None, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)
        if document is not None:
            self.instance = document
            self._copy_data_to_form()

    def _copy_data_to_form(self):
        self.task.data = self.instance.task
        self.start.data = self.instance.start
	self.time.date=self.instance.time
	
    def save(self):
        if self.instance is None:
            self.instance = self.document_class()
        self.instance.task = self.task.data
        self.instance.start = self.start.data
        self.instance.time=self.time.data

        self.instance.save()
        return self.instance
