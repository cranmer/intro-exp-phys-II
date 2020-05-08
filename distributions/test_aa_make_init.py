def make_init():
    import sys

    from os import listdir
    from os.path import isfile, join

    mypath = './distributions'
    onlyfiles = [f for f in listdir(mypath) if (isfile(join(mypath, f)) and f.find('Dist')==0)]
    print(onlyfiles)
    dist_names = []
    for f in onlyfiles:
        with open('./distributions/'+f) as file:
            lines = file.readlines()
            for line in lines:
                if line.find('class')>-1:
                    #print(line.split('class'))
                    dist_name = line.split('class')[1].split('(')[0].strip()
                    #print(dist_name, f[:-3])
                    if dist_name == f[:-3]: #strip the .py from file name
                        #print('ok')
                        dist_names.append(dist_name)
                    continue

    outfile = open('distributions/__init__.py','w')
    preamble = """
\"\"\"
Collect distributions for demo of central limit theorem.

Add a new file that will return N samples from your distribution similar to example_dist.py.
Then add the name to the list below.


grep class Dist*py | sed 's/(BaseDistribution)://' | sed 's/class //' | sed 's/^Dist/from .Dist/' | sed 's/.py:/ import /'

grep -h class Dist*py | sed 's/(BaseDistribution):/\",/' | sed 's/class /\"/'

\"\"\"

from __future__ import absolute_import
"""
    outfile.write(preamble)

    for dist_name in dist_names:
        outfile.write("from .{} import {}\n".format(dist_name,dist_name))

    outfile.write("\n\n")


    outfile.write("__all__ = (\n")
    for dist_name in dist_names:
        outfile.write("\"{}\",\n".format(dist_name))
    outfile.write("\t)")


    outfile.close()

def test_make_init():
    make_init()


if __name__ == '__main__':
    make_init()