#!/usr/bin/env python

from __future__ import print_function
from __future__ import division

import os.path

import cclib


def getargs():

    import argparse

    parser = argparse.ArgumentParser()

    parser.add_argument('qmoutputfile', nargs='+')

    args = parser.parse_args()

    return args


def determine_job_type(job):

    if isinstance(job, cclib.parser.qchemparser.QChem):
        return 'QChem'
    elif isinstance(job, cclib.parser.orcaparser.ORCA):
        return 'ORCA'
    elif isinstance(job, cclib.parser.gamessparser.GAMESS):
        return 'GAMESS'
    elif isinstance(job, cclib.parser.nwchemparser.NWChem):
        return 'NWChem'
    elif isinstance(job, cclib.parser.daltonparser.DALTON):
        return 'DALTON'
    else:
        return None


def extract_total_time(outputfilename, job_type):

    with open(outputfilename) as outputfile:

        if job_type == 'QChem':
            for line in outputfile:
                if 'Total job time:' in line:
                    sline = line.split()
                    total_time = float(sline[-2][:-8]) / 60

        elif job_type == 'ORCA':
            for line in outputfile:
                if 'TOTAL RUN TIME:' in line:
                    sline = line.split()
                    days = int(sline[3])
                    hours = int(sline[5])
                    minutes = int(sline[7])
                    seconds = int(sline[9])
                    msec = int(sline[11])
                    total_time = (days * 1440) + \
                                 (hours * 60) + \
                                 minutes + \
                                 (seconds / 60) + \
                                 (msec / 60000)

        elif job_type == 'GAMESS':
            for line in outputfile:
                if ' TOTAL WALL CLOCK TIME=' in line:
                    # Be lazy; this will capture the very last one,
                    # which is the answer we want.
                    total_time = float(line.split()[4]) / 60

        elif job_type == 'NWChem':
            total_time = 0.0

        elif job_type == 'DALTON':
            total_time = 0.0

        else:
            total_time = 0.0

    return total_time


if __name__ == '__main__':

    import cclib
    from cclib.parser import ccopen
    from cclib.parser.utils import convertor

    args = getargs()

    for qmoutputfile in args.qmoutputfile:

        qmoutputfile = os.path.abspath(qmoutputfile)
        print(qmoutputfile)

        job = ccopen(qmoutputfile)

        if job:
            data = job.parse()

            idx_homo = data.homos[-1]
            idx_lumo = idx_homo + 1

            steps = len(data.scfenergies)
            total_e = convertor(data.scfenergies[-1], 'eV', 'hartree')
            homo = convertor(data.moenergies[-1][idx_homo], 'eV', 'hartree')
            lumo = convertor(data.moenergies[-1][idx_lumo], 'eV', 'hartree')

            job_type = determine_job_type(job)
            total_time = extract_total_time(qmoutputfile, job_type)
            time_per_step = total_time / steps
        else:
            data = parse_non_cclib_output(qmoutputfile)

        print('Time (min): {}'.format(total_time))
        print('Steps     : {}'.format(steps))
        print('per step  : {}'.format(time_per_step))
        print('Total E   : {}'.format(total_e))
        print('HOMO      : {}'.format(homo))
        print('LUMO      : {}'.format(lumo))
