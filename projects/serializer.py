"""
Description: EndPoints
"""

from rest_framework import serializers
from .models import Projects

"""
    Desde este modulo Python sabra que debe de responder cuando se le pida una peticion
    POST - GET - PUSH - DELETE
    ViewSet: Nos permite estableceer quien puede consultar la informacion de nuestro EndPoint
    
"""


class ProjectSerializers(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = ("id", "titulo", "descripcion",
                  "tecnologia", "fecha_creacion")
        read_only_fields = ("fecha_creacion", )
