# PDF Splitter
## Purpose
This program is made to transform scans on A3 sheets. It splits the images on the file in 2 columns and rearrange them with a "gamma" ordre

## How it works
The usage of this program is pretty simple. Juste follow those steps :
- Make a blank folder wherever you want (ex : split/ )
- create 3 folders : "output", "input", "pages" (ex : split/input/ & split/output/ & split/pages/)
- put the 2 scripts ("splitter.sh" and "order.py") in your new folder (ex : split/splitter.sh & split/order.py)
- make 3 new folders : input, output & pages (ex : split/input, split/output, split/pages)
- put all the pdf you want into the "input" folder
- run the "splitter.sh" script (order.py will be called automatically by the first script)
- You'll find all your outputs int the "output" folder. You can remove them as thei appear in the "output" folder.

## Prerequire
- python3
- pdftoppm
- convert
