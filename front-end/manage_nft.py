from adminui import *

app = AdminApp(use_fastapi=True)

def on_submit(form_data):
    print(form_data)



app.set_menu(
    [
        MenuItem('Home', '/', icon="dashboard", children=[
            MenuItem('10 Academy Staff', '/admin', icon="setting"),
            MenuItem('Trainee', '/admin', icon="setting")
        ]),
        MenuItem('About', '/about', icon="info-circle")
    ]
  )

@app.page('/', 'Form')
def form_page():
    return [
        Form(on_submit = on_submit, content = [
            TextField('Title', required_message="The title is required!"),
            TextArea('Description'),
            FormActions(content = [
                SubmitButton('Submit')
            ])
        ])
    ]

fastapi_app = app.prepare()
