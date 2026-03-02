import sys


def modif_file(yaml_file):
    with open(yaml_file, 'r') as f:
        lines = f.readlines()

    with open(yaml_file, 'w') as f:
        for line in lines:
            try:
                f.write(line[:line.index('#') - 1] + '\n')
            except:
                f.write(line)

if __name__ == '__main__':

    modif_file(sys.argv[1])
