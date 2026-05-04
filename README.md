Sistema modular en Python diseñado bajo principios de Programación Orientada a Objetos,
separando lógica de dominio, motor de estados e interfaz.
1. Estructura de Módulos
DOMINIO.py: Lógica base. Implementa clases abstractas ( ABC ), encapsulamiento de
atributos y polimorfismo en tipos de suelo.
MOTOR.py: Controlador del juego. Gestiona el ciclo de vida, contadores de energía/pasos y
validación de estados.
UICONSOLA.py: Punto de entrada. Ejecuta la instancia del juego.
2. Componentes Clave
Clase Función
Matriz Gestión del tablero (Grid) y renderizado.
personaje Control de posición, vidas y agotamiento.
piso_lava Especialización de suelo con lógica de daño aleatorio.

3. Ejecución
python UICONSOLA.py

Nota técnica: El diseño utiliza herencia para extender funcionalidades sin modificar el núcleo de la matriz.
