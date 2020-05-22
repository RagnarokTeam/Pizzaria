from datetime import datetime


def GETDATE():
    data = datetime.now().strftime("%d/%m/%Y")
    return data


print(GETDATE())
