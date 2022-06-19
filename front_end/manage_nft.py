from adminui import *

app = AdminApp(use_fastapi=True)

def on_submit(form_data):
    print(form_data)



app.set_menu(
    [
        MenuItem('Home', '/', icon="dashboard", children=[
            MenuItem('10 Academy Staff', '/', icon="setting"),
            MenuItem('Trainee', '/trainee_opt_in', icon="setting")
        ]),
        MenuItem('About', '/about', icon="info-circle")
    ]
  )


@app.page('/', 'Form')
def form_page():
    return [

        Card('Upload Form', [
            Upload(on_data=on_upload)  # use Upload individually
        ]),

        Form(on_submit = on_submit, content = [
            Upload(name='upload', on_data=on_upload),     # embed uploads in a form
            FormActions(content = [
                SubmitButton('Submit File')
            ])
        ]),


        Form(on_submit = on_submit, content = [
            TextField('Name', required_message="The title is required!", placeholder = "Name of the Asset"),

            TextField('Unit Name', required_message="The title is required!", placeholder = "Asset unit name"),

            TextArea('Description'),

            FormActions(content = [
                SubmitButton('Mint')
            ]),

            TextField('Unsigned Token', required_message="You should receive the url to unsigned token", placeholder = "Received unsigned token")

        ]),


        Form(on_submit = on_submit, content = [
            TextField('Private Key', required_message="Private key required for signing!", placeholder = "Input private key to sign"),
            FormActions(content = [
                SubmitButton('Sign')
            ])

        ])

    ]



@app.page('/check_certificate_requests', 'Form')
def check_request(values):
    return [
        Form(on_submit = on_submit, content = [
            TextField('Certificate Request', required_message="populated request", placeholder = "Request prompt"),

            SelectBox('Type', data=['Approve', 'Disapprove'], placeholder="Determine Action"),

            FormActions(content = [
                SubmitButton('Submit')

            ])
        ])
    ]

@app.page('/trainee_opt_in', 'Form')
def on_detail(values):
    return [
        Form(on_submit = on_submit, content = [
            TextField('Certificate Request', required_message="populated request", placeholder = "Request prompt"),

            SelectBox('Type', data=['Approve', 'Disapprove'], placeholder="Determine Action"),

            FormActions(content = [
                SubmitButton('Submit')

            ])
        ])
    ]



def on_upload(file):
    print("=== file name will be: ===")
    print(file['file_name'])
    print('=== the file is stored in: ===')
    print(app.uploaded_file_location(file))


def on_submit(form_data):
    print(app.uploaded_file_location(form_data['upload'])) # e.g. the upload component's name is 'upload'



fastapi_app = app.prepare()
