from sistema import Sistema
from nodo_dinamico import ListaDinamica
import os

def main():
    gestor = Sistema()

    while True:
        print("\n" + "=" * 80)
        print(" SISTEMA DE OPTIMIZACIÓN AGRÍCOLA DE PRECISIÓN")
        print("=" * 80)
        print("1. Cargar archivo de datos")
        print("2. Procesar y optimizar zonas")
        print("3.Exportar resultados optimizados")
        print("4.Información del desarrollador")
        print("5.Generar visualización gráfica")
        print("6.Salir del sistema")
        print("=" * 80)

        opcion_seleccionada = input("Seleccione una opción (1-6): ").strip()

        if opcion_seleccionada == "1":
            print("\n CARGA DE ARCHIVO DE DATOS")
            print("-" * 40)
            
            # Método para pedir ruta de archivo
            ruta_archivo = input("Ingrese la ruta completa del archivo XML: ").strip()
            
            # Remover comillas si las hay
            ruta_archivo = ruta_archivo.strip('"\'')
            
            if ruta_archivo:
                exito = gestor.cargar_datos_xml(ruta_archivo)
                if not exito:
                    print("Verifique que la ruta sea correcta y el archivo sea XML válido")
            else:
                print("Debe ingresar una ruta de archivo")

        elif opcion_seleccionada == "2":
            print("\nPROCESAMIENTO Y OPTIMIZACIÓN")
            print("-" * 40)
            
            if gestor.zonas_agricolas.tamaño == 0:
                print("No hay zonas cargadas. Cargue un archivo primero.")
                continue
            
            nodo_actual = gestor.zonas_agricolas.cabeza
            while nodo_actual:
                zona = nodo_actual.contenido
                print(f" Optimizando zona {zona.codigo_zona}...")
                
                # Crear tablas optimizadas
                zona.crear_tablas_optimizadas()
                
                # Mostrar resultados
                grupos = zona.optimizar_bases_transmision()
                print(f"Bases originales: {zona.bases_transmision.tamaño}")
                print(f"Bases optimizadas: {len(grupos)}")
                print(f"Reducción: {zona.bases_transmision.tamaño - len(grupos)} bases")
                
                # Mostrar tablas
                zona.visualizar_tablas()
                
                nodo_actual = nodo_actual.proximo
            
            print("Todas las zonas han sido procesadas y optimizadas")

        elif opcion_seleccionada == "3":
            print("\n EXPORTACIÓN DE RESULTADOS")
            print("-" * 40)
            
            if gestor.zonas_agricolas.tamaño == 0:
                print("No hay datos para exportar. Cargue y procese un archivo primero.")
                continue
            
            ruta_salida = input("Ingrese la ruta para el archivo de salida (ej: resultados.xml): ").strip()
            
            if ruta_salida:
                # Agregar extensión si no la tiene
                if not ruta_salida.lower().endswith('.xml'):
                    ruta_salida += '.xml'
                
                exito = gestor.exportar_resultados_xml(ruta_salida)
                if exito:
                    print(f"Archivo guardado en: {os.path.abspath(ruta_salida)}")
            else:
                print("Debe especificar una ruta de salida")

        elif opcion_seleccionada == "4":
            print("\n👤 INFORMACIÓN DEL DESARROLLADOR")
            print("=" * 50)
            print("Nombre: Erwin Alejandro Girón Menéndez")
            print("Carné: 202405935")
            print("Curso: Introducción a la Programación y Computación 2")
            print("Carrera: Ingeniería en Ciencias y Sistemas")
            print("Semestre: 4to. Semestre")
            print("=" * 50)

        elif opcion_seleccionada == "5":
            print("\n GENERACIÓN DE GRÁFICOS")
            print("-" * 40)
            
            if gestor.zonas_agricolas.tamaño == 0:
                print("No hay zonas cargadas para graficar")
                continue
            
            gestor.listar_zonas_disponibles()
            codigo_zona = input("Ingrese el código de la zona: ").strip()
            
            print("Tipos de gráfico disponibles:")
            print("1. frecuencia - Tablas de frecuencia originales")
            print("2. optimizada - Tablas optimizadas")
            
            tipo_grafico = input("Seleccione el tipo (frecuencia/optimizada): ").strip().lower()

            # Buscar la zona
            nodo_actual = gestor.zonas_agricolas.cabeza
            zona_encontrada = None
            while nodo_actual:
                zona = nodo_actual.contenido
                if zona.codigo_zona == codigo_zona:
                    zona_encontrada = zona
                    break
                nodo_actual = nodo_actual.proximo

            if zona_encontrada:
                if tipo_grafico == "frecuencia":
                    if zona_encontrada.tabla_suelo:
                        print(f"\nFrecuencias Suelo - Zona {codigo_zona}")
                        zona_encontrada.tabla_suelo.mostrar_matriz()
                    if zona_encontrada.tabla_cultivo:
                        print(f"\nFrecuencias Cultivo - Zona {codigo_zona}")
                        zona_encontrada.tabla_cultivo.mostrar_matriz()
                elif tipo_grafico == "optimizada":
                    if hasattr(zona_encontrada, 'tabla_suelo_optimizada') and zona_encontrada.tabla_suelo_optimizada:
                        print(f"\nOptimizada Suelo - Zona {codigo_zona}")
                        zona_encontrada.tabla_suelo_optimizada.mostrar_matriz()
                    if hasattr(zona_encontrada, 'tabla_cultivo_optimizada') and zona_encontrada.tabla_cultivo_optimizada:
                        print(f"\nOptimizada Cultivo - Zona {codigo_zona}")
                        zona_encontrada.tabla_cultivo_optimizada.mostrar_matriz()
                else:
                    print(" Tipo de gráfico no válido")
            else:
                print(f" Zona {codigo_zona} no encontrada")

        elif opcion_seleccionada == "6":
            print("\n Saliendo del sistema...")
            print("¡Gracias por usar el Sistema de Optimización Agrícola!")
            break

        else:
            print(" Opción no válida. Seleccione una opción del 1 al 6.")

if __name__ == "__main__":
    main()
