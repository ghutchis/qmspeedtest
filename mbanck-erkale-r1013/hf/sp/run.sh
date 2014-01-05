#!/bin/bash

OMP_NUM_THREADS=1 erkale_omp runfile > out.log 2>&1 &
