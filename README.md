Venn-Analysis
=============

Overview<a id="overview"></a>
-------------
A pipeline to facilitate to comparison of multiple lists using GNU Make and html.

Prerequisites<a id="prerequisites"></a>
-------------
* GNU make
* libxslt - LibXML (for xlstproc)
* python 2.2+

Usage<a id="usage"></a>
-------------
	<path-to-Venn-Tool-git-repository>/Venn-Tool init 
	make

Notes<a id="notes"></a>
-------------
* The lists of element to compare must be in a folder named "data" in the main directory selected for the analysis (see Documentation/data.txt).
* The samples to compare must be specified in the "config.txt" file (see Documentation/config.txt).
* You can use the "-j" option of make to launch the analysis in parallel.
* To view the results, open the "index.html" file using the browser of your choice.
* If you add data in the "data" directory or if you add new combinations of sample in "config.txt" file, you must re-run init if you want the changes to be added in the Makefiles.
