
class Factory:
    def obtener_servicio(value):
        if (value == 0):
            return "csv"
        elif (value == 1):
            return "api"
        else:
            return "mock"