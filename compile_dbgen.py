import json
import os
import argparse


def generate(logfile):
    print (logfile)
    entries = list()

    with open(logfile) as fp:
        lines = [x.strip() for x in fp.readlines() if x.startswith("gcc")]

        for line in lines:
            e = dict()
            e['directory'] = cwd
            e['command'] = line
            tokens = line.split()
            if "-c" not in tokens:
                continue
            index = tokens.index("-c")
            e['file'] = tokens[index + 1]
            entries.append(e)

    outfile = open(os.path.join(cwd, "compile_commands.json"), "w")
    outfile.write(json.dumps(entries, indent=4, sort_keys=True))
    outfile.close()
        

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate compile_commands.json")
    parser.add_argument('build_log', type=str, help="Output from python setup.py build")
    args = parser.parse_args()

    cwd = os.getcwd()
    generate(os.path.join(cwd, args.build_log))
    pass
