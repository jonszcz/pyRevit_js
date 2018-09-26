from pyrevit import forms
from rpw.ui.forms import TextInput

# Forms using pyrevit
w = forms.TemplateUserInputWindow('context', title='User Input', width=500, height=400, x=input)
w.show(w)

# Forms using RPW
value = TextInput(
    'Starting Value',
    description='Begin renumbering with:',
    default="1",
    )
print('Starting renumbering with detail ' + value)
