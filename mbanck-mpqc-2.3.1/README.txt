MPQC has two input formats, simple and object-oriented.

The simple format implies a maximum of 10 geometry steps, and there appears to
be no way to change this.  Thus, the object oriented format had to be used,
which has been automatically generated from the simple input file:
 
$ mpqc -i hf.in.simple | grep -v Reading.file | grep -v Generated.object-oriented > hf.in
$ mpqc -i b3lyp.in.simple | grep -v Reading.file | grep -v Generated.object-oriented > b3lyp.in

And afterwards the line "max_iterations = 120" has been added to the geometry
optimization section.
