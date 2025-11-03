import argparse


parser = argparse.ArgumentParser(description="Scrypt Description")


# required positional argument with help string
#parser.add_argument('pos1', help='first positional arg')

# # required positional argument with help string and type hint
# parser.add_argument('pos2', help='second positional arg with type', type=int)
#
# # required positional argument with help string
# # N - должно быть указанное количество аргументов. Аргументы будут в списке (даже если указан 1)
# # ? - 0 или 1 аргумент
# # * - все аргументы попадут в список
# # + - все аргументы попадут в список, но должен быть передан хотя бы один аргумент
#parser.add_argument('pos3', nargs='+', type=int, help='positional, some list of elements')
#
# # required keyword argument with choices and help string
parser.add_argument('-k', '--key', dest='aaaa',
                         choices=['mac', 'ip', 'vlan', 'interface', 'switch'],
                         help='host key (parameter) to search')
#
# # required keyword argument with destination name
parser.add_argument("-a", dest='ali', required=True)
#
# # non-required keyword argument without destination name, with help string
parser.add_argument("-b", help="B argument")
#
# # non-required keyword argument with destination name and default value and specified type
parser.add_argument("-c", dest="arg_c", default=2, type=int)
#
# # non-required keyword argument
parser.add_argument("-d", "--destination")



args = parser.parse_args()


print('Hello')
print(args)
# print(args.pos1)