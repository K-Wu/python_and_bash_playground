class A:

    @classmethod
    def get_name(cls) -> str:
        return "A"
  
    def print(self):
        print(self.get_name())


if __name__ == "__main__":
    a = A()
    a.print()
    pass