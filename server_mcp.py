from tools import (
    pretty_tables,
    pretty_movies,
    pretty_customers,
    pretty_categories,
    pretty_actors
)

def run_demo():
    print("SERVIDOR MCP - PAGILA")
    print("Acceso controlado | Solo lectura")
    print("=" * 42)

    print("\nPregunta 1: ¿Qué áreas del negocio de alquiler de películas se pueden analizar?")
    print("ÁREAS DISPONIBLES PARA ANÁLISIS:")
    print("- Películas")
    print("- Actores")
    print("- Categorías")
    print("- Clientes")
    print("- Alquileres")
    print("- Pagos")
    print("- Inventario")
    print("- Tiendas")



    print("\nPregunta 2: ¿Cuáles son las películas más alquiladas por los clientes?")
    pretty_movies()

    print("\nPregunta 3: ¿Quiénes son los clientes más activos del sistema de alquiler?")
    pretty_customers()

    print("\nPregunta 4: ¿Qué categorías de películas generan mayores ingresos?")
    pretty_categories()

    print("\nPregunta 5: ¿Qué actores participan en más películas del catálogo?")
    pretty_actors()


if __name__ == "__main__":
    run_demo()
