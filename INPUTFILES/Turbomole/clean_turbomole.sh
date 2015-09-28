#!/usr/bin/env sh

files=(
    GEO_OPT_RUNNING
    ddens
    dens
    energy
    errvec
    fock
    gradient
    hessapprox
    job.4
    job.27
    job.last
    job.start
    mos
    nextstep
    not.converged
    oldfock
    optinfo
    restartg
    statistics
)

for f in ${files[@]}; do
    rm -f "${f}"
done
