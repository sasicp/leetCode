import re


def find_2sided(txt: str) -> str:
    lines = txt.split("\n")
    out_nn1 = []
    out_nn2 = []
    smooth_reg = re.compile(r"-acf\s+(\d+\.\d*\s+){3}")
    smooth = []
    ii = 0
    while ii < len(lines):
        line = lines[ii]
        if line.find("# 2-sided thresholding") != -1:
            mth = smooth_reg.search(lines[ii - 1])

            test = "\n".join(lines[ii+3:ii+11])
            if test.find("-NN 3") != -1:
                ii += 11
                continue
            smooth.append(lines[ii-1][mth.span()[0]:mth.span()[1]])
            out_nn1.append("\n".join(lines[ii+3:ii+11]))
            out_nn2.append("\n".join(lines[ii+15:ii+23]))
            ii += 23
        else:
            ii += 1
    out = zip(smooth, out_nn1, out_nn2)
    out = "\n\n".join("\n".join(x) for x in out)
    return out


if __name__ == "__main__":
    import sys
    output = open(sys.argv[1]).read()
    output = find_2sided(output)
    open(sys.argv[2], 'wt').write(output)
