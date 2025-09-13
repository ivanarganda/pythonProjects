def generate_menu_items(menu_dict):
    return "\n".join([f"{k}. {v}" for k, v in menu_dict.items()])
def mostrar_menu_principal():
        
        return {
            "1": "Jugar como invitado",
            "2": "Jugar como usuario registrado",
            "3": "Salir"
        }

def juego_niveles():

    return {
        "1": {
            "label": "Fácil",
            "intentos": 10,
            "min": 1,
            "max": 10,
            "handicap": True
        },
        "2": {
            "label": "Medio",
            "intentos": 8,
            "min": 1,
            "max": 20,
            "handicap": False
        },
        "3": {
            "label": "Difícil",
            "intentos": 4,
            "min": 1,
            "max": 30,
            "handicap": False
        }
    }

def mostrar_menu_niveles():
    # En un diccionario
    return {
        "1": "Fácil (1-10, 10 intentos, con pista)",
        "2": "Medio (1-20, 8 intentos, sin pista)",
        "3": "Difícil (1-30, 4 intentos, sin pista)",
        "4": "Volver al menú principal"
    }  