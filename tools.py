from db import get_connection


def list_tables():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT table_name
        FROM information_schema.tables
        WHERE table_schema = 'public';
    """)
    tables = cur.fetchall()
    conn.close()
    return tables


def most_rented_movies(limit=5):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT f.title, COUNT(r.rental_id) AS rentals
        FROM film f
        JOIN inventory i ON f.film_id = i.film_id
        JOIN rental r ON i.inventory_id = r.inventory_id
        GROUP BY f.title
        ORDER BY rentals DESC
        LIMIT %s;
    """, (limit,))
    result = cur.fetchall()
    conn.close()
    return result


def top_customers(limit=5):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT c.first_name, c.last_name, COUNT(r.rental_id) AS rentals
        FROM customer c
        JOIN rental r ON c.customer_id = r.customer_id
        GROUP BY c.first_name, c.last_name
        ORDER BY rentals DESC
        LIMIT %s;
    """, (limit,))
    result = cur.fetchall()
    conn.close()
    return result


def top_categories_by_income(limit=5):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT c.name, SUM(p.amount) AS total_income
        FROM category c
        JOIN film_category fc ON c.category_id = fc.category_id
        JOIN inventory i ON fc.film_id = i.film_id
        JOIN rental r ON i.inventory_id = r.inventory_id
        JOIN payment p ON r.rental_id = p.rental_id
        GROUP BY c.name
        ORDER BY total_income DESC
        LIMIT %s;
    """, (limit,))
    result = cur.fetchall()
    conn.close()
    return result


def top_actors(limit=5):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT a.first_name, a.last_name, COUNT(fa.film_id) AS films
        FROM actor a
        JOIN film_actor fa ON a.actor_id = fa.actor_id
        GROUP BY a.first_name, a.last_name
        ORDER BY films DESC
        LIMIT %s;
    """, (limit,))
    result = cur.fetchall()
    conn.close()
    return result


# ===== FORMATO BONITO =====

def pretty_tables():
    tables = list_tables()
    print("TABLAS DISPONIBLES:")
    for t in tables:
        print(f"- {t[0]}")


def pretty_movies():
    movies = most_rented_movies()
    print("\nPELÍCULAS MÁS ALQUILADAS:")
    for i, (title, count) in enumerate(movies, start=1):
        print(f"{i}. {title} → {count} alquileres")


def pretty_customers():
    customers = top_customers()
    print("\nCLIENTES MÁS ACTIVOS:")
    for i, (first, last, count) in enumerate(customers, start=1):
        print(f"{i}. {first} {last} → {count} alquileres")


def pretty_categories():
    categories = top_categories_by_income()
    print("\nCATEGORÍAS CON MAYORES INGRESOS:")
    for i, (name, income) in enumerate(categories, start=1):
        print(f"{i}. {name} → ${income:.2f}")


def pretty_actors():
    actors = top_actors()
    print("\nACTORES MÁS FRECUENTES:")
    for i, (first, last, films) in enumerate(actors, start=1):
        print(f"{i}. {first} {last} → {films} películas")
