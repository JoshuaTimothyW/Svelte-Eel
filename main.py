import eel

@eel.expose
def hello_world():
    print("hello world")
    return "Hello from python"

@eel.expose
def print_string(string):
    if len(string) > 1:
        print(string)
        return "Success!"
    else:
        return "Too few characters. Please type more than 20 characters."


eel.init('public')
# eel.start('index.html', size=(600, 400), options={
#     'port': 8080
# })
eel.start('index.html', size=(600, 400))