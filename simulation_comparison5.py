# An OceanVal comparison of simulations, written by the oceanval window on 2026-11-03.
# Run it again with: python <this file>
import oceanval

oceanval.compare_simulations(
    simulations=[
        {'name': 't1', 'sim_dir': '/data/thaumus2/scratch/hpo/COMFORT/baseline_archerfull/2000', 'n_dirs_down': 1, 'times_index': '/tmp/oceanval_times_cpem45_e/1.pkl'},
        {'name': 't2', 'sim_dir': '/data/thaumus2/scratch/hpo/COMFORT/baseline_archerfull/2000', 'n_dirs_down': 1, 'times_index': '/tmp/oceanval_times_cpem45_e/2.pkl'},
    ],
    variables={
        'Temperature': {'t1': 'votemper', 't2': 'votemper'},
    },
    climatology={
        'Temperature': {'start': 2000, 'end': 2000, 'surface': True, 'bottom': False, 'water_column': None},
    },
    phenology=None,
    thickness=None,
    out_dir='/users/modellers/maz/OceanVal_fvcom',
    cores=6,
    as_missing=[0.0, 0.0],
    figure_code=True,
)
