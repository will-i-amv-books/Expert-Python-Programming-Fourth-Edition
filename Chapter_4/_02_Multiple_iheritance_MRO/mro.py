from pprint import pprint


class CommonBase:
    pass


class Base1(CommonBase):
    pass


class Base2(CommonBase):
    def method(self):
        print("Base2.method() called")


class MyClass(Base1, Base2):
    pass


if __name__ == "__main__":
    pprint(f"MyClass's MRO: \n{MyClass.__mro__}")
