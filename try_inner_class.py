class Hello:
    class ActivationContext:
        sequence_id: int

    def print(self):
        print("Hello", self.ActivationContext())


if __name__ == "__main__":
    a = Hello()
    a.print()
