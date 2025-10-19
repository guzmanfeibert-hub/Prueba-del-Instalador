def mostrar_tutorial():
    print("\n" + "=" * 60)
    print("🔧 TUTORIAL: Instalación de Python, VS Code, Jupyter, Git y Extensiones")
    print("=" * 60)

    pasos = {
        1: "📥 Instalar Python",
        2: "💻 Instalar Visual Studio Code (VS Code)",
        3: "🧩 Instalar Extensiones Recomendadas en VS Code",
        4: "🧪 Instalar Jupyter (para notebooks)",
        5: "🐙 Instalar y Configurar Git",
    }

    for num, titulo in pasos.items():
        print(f"\n{num}. {titulo}")
        print("-" * 40)

        if num == 1:
            print("1. Ve a https://www.python.org/downloads/")
            print("2. Descarga la última versión estable para tu sistema operativo.")
            print("3. Ejecuta el instalador y asegúrate de marcar 'Add Python to PATH'.")
            print("4. Verifica la instalación abriendo una terminal y escribiendo:")
            print("   python --version   o   python3 --version")

        elif num == 2:
            print("1. Ve a https://code.visualstudio.com/")
            print("2. Descarga e instala VS Code para tu sistema operativo.")
            print("3. Ábrelo y asegúrate de que funcione correctamente.")

        elif num == 3:
            print("En VS Code, ve a la pestaña de extensiones (Ctrl+Shift+X) y busca e instala:")
            print("• Python (por Microsoft)")
            print("• Jupyter (por Microsoft)")
            print("• Pylance (para mejor autocompletado)")
            print("• GitLens (para integración avanzada con Git)")

        elif num == 4:
            print("1. Abre una terminal.")
            print("2. Ejecuta el siguiente comando para instalar Jupyter:")
            print("   pip install jupyter")
            print("3. Para probarlo, ejecuta:")
            print("   jupyter notebook")
            print("   (Esto abrirá el notebook en tu navegador)")

        elif num == 5:
            print("1. Ve a https://git-scm.com/downloads y descarga Git.")
            print("2. Instálalo con las opciones predeterminadas.")
            print("3. Abre una terminal y configura tu nombre y correo:")
            print("   git config --global user.name 'TuNombre'")
            print("   git config --global user.email 'tu@email.com'")
            print("4. Verifica con: git --version")

    print("\n✅ ¡Listo! Ahora tienes todo configurado para programar en Python con VS Code, Jupyter y Git.")
    print("💡 Recuerda reiniciar tu terminal o VS Code si los comandos no funcionan al instante.")


def menu_principal():
    while True:
        print("\n" + "=" * 40)
        print("📘 MENÚ PRINCIPAL")
        print("=" * 40)
        print("1. Mostrar tutorial de instalación")
        print("2. Salir")
        opcion = input("\nElige una opción (1 o 2): ").strip()

        if opcion == "1":
            mostrar_tutorial()
        elif opcion == "2":
            print("\n👋 ¡Gracias por usar el tutorial! Hasta luego.")
            break
        else:
            print("\n⚠️ Opción no válida. Por favor, elige 1 o 2.")


if __name__ == "__main__":
    menu_principal()