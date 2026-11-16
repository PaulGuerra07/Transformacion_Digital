# Transformación Digital

Repositorio de la actividad de **Cultura Digital y Sociedad**, Ingeniería en
Ciencia de Datos e Inteligencia Artificial, UNACH.

## La importancia de la Transformación Digital en la Ciencia de Datos

La Transformación Digital no consiste solo en pasar los procesos del papel a
la computadora (eso es digitalización). Implica rediseñar cómo una
organización crea valor y toma decisiones usando tecnologías como la
inteligencia artificial, la nube y el análisis de datos.

La Ciencia de Datos es el motor de ese cambio:

- **Convierte datos en decisiones.** Cada pago con código QR, cada consulta
  médica en línea o cada clase virtual genera datos. Con ellos se puede
  predecir la demanda, detectar fraudes o identificar a los estudiantes que
  necesitan apoyo a tiempo.
- **Necesita la infraestructura digital.** Sin datos digitalizados,
  almacenados en la nube y disponibles, no hay modelos que entrenar.
- **Exige responsabilidad.** Mientras más decisiones se automatizan, más
  importante es que los modelos sean justos, transparentes y respeten la
  privacidad, como lo exige en Ecuador la Ley Orgánica de Protección de
  Datos Personales.
- **Depende del trabajo colaborativo.** Herramientas como Git y GitHub
  permiten que un equipo trabaje sobre el mismo código, con un historial de
  cambios y revisiones antes de integrar cada aporte.

En resumen, la Transformación Digital genera los datos y la Ciencia de Datos
los convierte en conocimiento útil para la sociedad.

## Contenido del repositorio

| Archivo        | Descripción                                                |
|----------------|------------------------------------------------------------|
| `promedio.py`  | Función documentada con docstrings que calcula el promedio |
| `README.md`    | Este archivo                                               |

## Uso

Requiere Python 3.8 o superior. No necesita librerías adicionales.

```bash
python promedio.py
```

Salida:

```text
Calificaciones: [8.5, 9.0, 7.75, 10, 9.25]
Promedio: 8.90
```

Para usar la función desde otro archivo:

```python
from promedio import calcular_promedio

calcular_promedio([8, 9, 10])   # 9.0
```

Para comprobar los ejemplos incluidos en el docstring:

```bash
python -m doctest -v promedio.py
```

## Autor

Paúl Andrés Guerra Vicuña
