# Servidor MCP para Consultas sobre Pagila

## Descripción
Este proyecto implementa un servidor basado en el Model Context Protocol (MCP) que permite
a un modelo de lenguaje consultar de forma segura una base de datos PostgreSQL (Pagila),
sin acceso directo al motor de base de datos.

## Objetivo
Permitir consultas en lenguaje natural sobre información de películas, clientes, categorías
y actores, garantizando seguridad, control y trazabilidad.

## Arquitectura
Usuario / LLM
→ Servidor MCP (Python)
→ Tools controladas
→ Base de datos PostgreSQL (Pagila - Read Only)

## Seguridad
- Usuario de base de datos en modo solo lectura
- Consultas SQL predefinidas
- Sin ejecución de SQL dinámico
- Separación entre modelo y base de datos

## Funcionalidades
- Descubrimiento de tablas
- Películas más alquiladas
- Clientes más activos
- Categorías con mayores ingresos
- Actores más frecuentes

## Ejecución
1. Instalar dependencias:
```bash
pip install psycopg2-binary
