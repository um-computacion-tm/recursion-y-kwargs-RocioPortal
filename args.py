import unittest
def buscar_datos(*args , **kwargs):
    for clave, persona in kwargs.items():
        coincide = True
        for arg in args:
            if arg not in persona.values():
                coincide = False
                break
        if coincide:
            return clave
    return False  


  #  for key, value in kwargs.items():
   #     print("key", key, "value", value)
    #    for k, v in value.items():
     #       print("k", k, "v", v)


database = {
    "persona1": {
        "Primer_nombre": "Pablo",
        "Segundo_nombre": "Diego",
        "Primer_apellido": "Ruiz",
        "Segundo_apellido": "Picasso"
    },
    "persona2": {
        "Primer_nombre": "Rocio",
        "Segundo_nombre": "Pilar",
        "Primer_apellido": "Portal",
        "Segundo_apellido": "Romano"
    },
    "persona3": {
        "Primer_nombre": "Martin",
        "Segundo_nombre": "Ignacio",
        "Primer_apellido": "Perez",
        "Segundo_apellido": "Martinez"
    },
    "persona4": {
        "Primer_nombre": "Luciana",
        "Segundo_nombre": "Agostina",
        "Primer_apellido": "Dimarco",
        "Segundo_apellido": "Gomez"
    }
}

class TestKwargs(unittest.TestCase):
       
    def test_persona1(self):
        resultado = buscar_datos("Pablo", "Diego", "Ruiz", "Picasso", **database)
        self.assertEqual(resultado, "persona1")

    def test_persona2(self):
        resultado = buscar_datos("Rocio", "Pilar", "Portal", "Romano", **database)
        self.assertEqual(resultado, "persona2")

    def test_persona3(self):
        resultado = buscar_datos("Martin", "Ignacio", "Perez", "Martinez", **database)
        self.assertEqual(resultado, "persona3")
    
    def test_persona4(self):
        resultado = buscar_datos("Luciana", "Agostina", "Dimarco", "Gomez", **database)
        self.assertEqual(resultado, "persona4")

    def test_persona4_desornedado(self):
        resultado = buscar_datos("Agostina", "Luciana", "Dimarco", "Gomez", **database)
        self.assertEqual(resultado, "persona4")

    def test_persona4_desornedado1(self):
        resultado = buscar_datos("Dimarco", "Gomez", "Luciana", "Agostina", **database)
        self.assertEqual(resultado, "persona4")

    def test_none(self):
        resultado = buscar_datos("Luci", "Agos", "Gomez", "Di", **database)
        self.assertEqual(resultado,False)

    def test_none1(self):
        resultado = buscar_datos("false", "Agos", "12", "Di", **database)
        self.assertEqual(resultado, False)

    def test_none2(self):
        resultado = buscar_datos("93", "Agos", "12", "Rocio", **database)
        self.assertEqual(resultado, False)

unittest.main() 
















