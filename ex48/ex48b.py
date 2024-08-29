class Parent(object):
    count = 0

    def override(self):
        print("PARENT override()")

    def increment(self):
        self.count += 1

    def print_count(self):
        print(f"COUNT: {self.count}")


class Child(Parent):

    def override(self):
        print("CHILD override()")

    def increment(self):
        self.count += 2


dad = Parent()
son = Child()

dad.override()
son.override()
dad.print_count()
son.print_count()
dad.increment()
son.increment()
dad.print_count()
son.print_count()
