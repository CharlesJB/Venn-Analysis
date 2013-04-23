Venn-Analysis
=============

Overview<a id="overview"></a>
-------------
A pipeline to facilitate to comparison of multiple lists using GNU Make and html.

Prerequisites<a id="prerequisites"></a>
-------------
* GNU make
* libxslt - LibXML (for xlstproc)

Usage<a id="usage"></a>
-------------
	Venn-Tool init
	make

Notes<a id="notes"></a>
-------------
* By default, init will search for a folder named "data" and will do every possible file combinations.
* To use a different folder than the default folder, or to specify which samples to compare, you can create a "config.xml" file (see Documentation/config.txt)
* You can use the "-j" option of make to launch the analysis in parallel.
* To view the results, open the "venn-analysis.html" file using the browser of your choice.
