from tools import (
    pretty_tables,
    pretty_movies,
    pretty_customers,
    pretty_categories,
    pretty_actors
)

def mcp_server():
    print("==========================================")
    print(" SERVIDOR MCP - PAGILA")
    print(" Acceso controlado | Solo lectura")
    print("==========================================\n")

    print("Pregunta 1: ¿Qué tablas existen en la base de datos?")
    pretty_tables()

    print("\nPregunta 2: ¿Cuáles son las películas más alquiladas?")
    pretty_movies()

    print("\nPregunta 3: ¿Quiénes son los clientes más activos?")
    pretty_customers()

    print("\nPregunta 4: ¿Qué categorías generan más ingresos?")
    pretty_categories()

    print("\nPregunta 5: ¿Qué actores aparecen en más películas?")
    pretty_actors()

    print("\n==========================================")
    print(" FIN DE DEMOSTRACIÓN MCP")
    print("==========================================")

if __name__ == "__main__":
    mcp_server()
