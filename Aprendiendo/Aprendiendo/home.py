from django.http import HttpResponse;

#Aqui voy a probar como funciona esta vaina

def holamundo(Request): #Ahora con la vista hecha hay que crear una URL en urls.py <
    return HttpResponse("Hola Mundo")