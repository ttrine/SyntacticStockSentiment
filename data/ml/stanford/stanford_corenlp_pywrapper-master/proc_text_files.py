"""
Input is multiple text files.  Each text file represents one document.
Output is just as many text files, with the ".anno" extension instead.
Each output file consists of one JSON object.

USAGE
proc_text_files.py MODE  [files...]

e.g.
python proc_text_files.py pos *.txt
"""

import sys, re
mode = sys.argv[1]

from stanford_corenlp_pywrapper import CoreNLP
ss = CoreNLP(mode, corenlp_jars=["/Users/Doctor_Einstein/Documents/stockMartket/analysis/nlp/stanford/*"])

for filename in sys.argv[2:]:
    outfile = re.sub(r'\.txt$',"", filename) + ".anno"
    print>>sys.stderr, "%s  ->   %s" % (filename, outfile)

    text = open(filename).read().decode('utf8', 'replace')
    jdoc = ss.parse_doc(text, raw=True)
    with open(outfile, 'w') as fp:
        print>>fp, jdoc


