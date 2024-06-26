class Dummy:
    def get_activation_memory_per_layer(
        self, a, b, c, d, ka=True, kb=1, kc=1.1, return_breakdown=False
    ):
        print("args", a, b, c, d)
        print("kwargs", ka, kb, kc, return_breakdown)

    def get_activation_memory_per_layer_with_return_breakdown(
        self, *args, **kwargs
    ):
        """Helper function to facilitate type hinting of the return values"""
        return self.get_activation_memory_per_layer(
            *args, **kwargs, return_breakdown=True
        )

    def partially_get_activation_memory_per_layer_with_return_breakdown(
        self, dummy_arg, *args, **kwargs
    ):
        """Helper function to facilitate type hinting of the return values"""
        print("dummy arg", dummy_arg)
        return self.get_activation_memory_per_layer(
            *args, **kwargs, return_breakdown=True
        )


if __name__ == "__main__":
    d = Dummy()
    d.get_activation_memory_per_layer_with_return_breakdown(
        1, 2, 3, 4, ka=False, kb=2, kc=3.1
    )
    d.get_activation_memory_per_layer(1, 2, 3, 4)
    d.partially_get_activation_memory_per_layer_with_return_breakdown(
        "dummy", 1, 2, 3, 4, kc="d"
    )
    d.get_activation_memory_per_layer_with_return_breakdown(
        **{"a": 12345, "b": 12345, "c": 12345, "d": 12345, "ka": 12345}
    )
