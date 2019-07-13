Formatter "CSS Prefixer" for CudaText.
It allows to insert needed vendor prefixes into CSS code.
Uses Python library "cssprefixer" (corrected manually for Python 3).

Example. Such CSS code:

#wrapper {
    border-radius: 1em;
    transform: rotate(45deg)
}

will be changed to:

#wrapper {
    -webkit-border-radius: 1em;
    -moz-border-radius: 1em;
    border-radius: 1em;
    -webkit-transform: rotate(45deg);
    -moz-transform: rotate(45deg);
    -o-transform: rotate(45deg);
    -ms-transform: rotate(45deg);
    transform: rotate(45deg)
    }


Author: Alexey Torgashin (CudaText)
License: MIT
