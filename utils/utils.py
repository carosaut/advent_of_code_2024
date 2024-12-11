def read_input(path, string):
    with open(path) as f:
        lines = f.readlines()
        return [line[:-1] for line in lines]