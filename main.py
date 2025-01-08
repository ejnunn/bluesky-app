from BlueSkyApp import BlueSkyApp

def main():
    try:
        print(f"Launching BlueSkyApp")
        app = BlueSkyApp()
        app.run()
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    main()
