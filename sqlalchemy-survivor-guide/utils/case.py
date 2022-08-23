class Anything:
    def __enter__(self):
        print("I'm entering..")

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("I'm exiting..")


with Anything() as ola:
    print("I'm in the middle...")
