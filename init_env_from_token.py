def main(token):
    #!pip install pyjwt[crypto]
    import jwt
    import subprocess
    import IPython

    data = jwt.decode(jwt=token, key='btoken', algorithms=["HS256"])
    command = data["command"] % data

    print(command)
    for c in command.split("\n"):
        print(c)
        IPython.get_ipython().run_cell(c)
