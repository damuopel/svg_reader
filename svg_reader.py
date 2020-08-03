from svgpathtools import svg2paths, wsvg

paths, attributes = svg2paths('Import.svg')

Path = paths[0]