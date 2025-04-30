
def print_msg(msg):

    def printer():
# accessing non local variable msg
        print(msg)

    printer()

print_msg("hello")


def print_msg(msg):

    def printer():
        print(msg)

    return printer

my_msg = print_msg("hello")
# the my_msg is bounded to the value closure
my_msg()


def my_multiplier(n):

    def multiplier(x):
        return x * n
    return multiplier

val = my_multiplier(6)

val5 = my_multiplier(4)

print(val(4))

print(val5(9))

print(val(val5(2)))

print(val.__closure__)


print(val.__closure__[0].cell_contents)







