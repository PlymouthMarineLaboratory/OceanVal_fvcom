# An OceanVal analysis, written by the oceanval window on 2026-11-03.
# Run it again with: python <this file>
import oceanval

oceanval.analyze(
    sim_dir='/data/thaumus2/scratch/hpo/COMFORT/baseline_archerfull/2013',
    variables={
        'jhgjg': 'B1_fB1N1p',
    },
    climatology={
        'jhgjg': {'start': 2013, 'end': 2013, 'surface': True, 'bottom': False, 'water_column': None},
    },
    phenology=None,
    n_dirs_down=1,
    exclude=None,
    require=['1m'],
    thickness=None,
    time_shift=None,
    out_dir='/users/modellers/maz/OceanVal_fvcom',
    cores=6,
    as_missing=[0.0, 0.0],
    figure_code=False,
    times_index='/tmp/oceanval_times_hr7gsw10/1.pkl',
)
