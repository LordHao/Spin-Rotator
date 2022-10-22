This Jupyter script is created for tuning the linear chromaticity for the Rotator ring by adjusting the sextupole  strength.
All the touchable sextupoles are listed in the file "sextupole_tuning.txt". Note: For the lattice file "Rot.bmad", SF4TREA should not be adjusted.
Once all the sextupoles are computed from this algorithm, you can use them as the initial guess for the BMAD optimization.

Other than the Gradient descent algorithm antoher approach is shown in the file "chrom tuning".

NOTE: The sign of all sextupoles can NOT be changed.
