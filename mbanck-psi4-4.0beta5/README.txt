The default SCF implementation of PSI4 is "df", which utilizes density-fitting.
However, this results in a slightly higher energy (and energy of the optimzed
geometry), so the "out_of_core" algorithm was chosen and instead and
"df_scf_guess" was set to "false".
