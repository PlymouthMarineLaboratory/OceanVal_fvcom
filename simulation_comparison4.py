# An OceanVal comparison of simulations, written by the oceanval window on 2026-11-03.
# Run it again with: python <this file>
import oceanval

oceanval.compare_simulations(
    simulations=[
        {'name': 'n1', 'sim_dir': '/data/thaumus2/scratch/hpo/COMFORT/baseline_archerfull/2000', 'n_dirs_down': 1, 'times_index': '/tmp/oceanval_times_a17pqzas/1.pkl'},
        {'name': 'n2', 'sim_dir': '/data/thaumus2/scratch/hpo/COMFORT/baseline_archerfull/2000', 'n_dirs_down': 1, 'times_index': '/tmp/oceanval_times_a17pqzas/2.pkl'},
    ],
    variables={
        'Temperature': {'n1': 'votemper', 'n2': 'votemper'},
    },
    climatology={
        'Temperature': {'start': 2000, 'end': 2000, 'surface': True, 'bottom': False, 'water_column': None},
    },
    phenology=None,
    thickness=None,
    out_dir='/users/modellers/maz/OceanVal_fvcom',
    cores=4,
    as_missing=[0.0, 0.0],
    figure_code=False,
)
