from abc import ABC, abstractmethod


class DummyInterface(ABC):
    @abstractmethod
    def dummy_method(self):
        ...

    @property
    @abstractmethod
    def dummy_property(self):
        ...


class InvalidDummy(DummyInterface):
    pass


class MissingPropertyDummy(DummyInterface):
    def dummy_method(self):
        pass


class MissingMethodDummy(DummyInterface):
    @property
    def dummy_property(self):
        return None


class Dummy(DummyInterface):
    def dummy_method(self):
        pass

    @property
    def dummy_property(self):
        return None


def instantiate(cls):
    print(f"\nInstantiating ABC: {cls}")
    try:
        cls()
    except Exception as err:
        print(f"ERROR: {repr(err)}")
    else:
        print("SUCCESS")


if __name__ == "__main__":
    instantiate(DummyInterface)
    instantiate(InvalidDummy)
    instantiate(MissingMethodDummy)
    instantiate(MissingPropertyDummy)
    instantiate(Dummy)
