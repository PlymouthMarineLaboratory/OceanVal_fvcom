# An OceanVal comparison of simulations, written by the oceanval window on 2026-11-03.
# Run it again with: python <this file>
import oceanval

oceanval.compare_simulations(
    simulations=[
        {'name': 'n', 'sim_dir': '/data/thaumus2/scratch/hpo/COMFORT/baseline_archerfull', 'n_dirs_down': 2, 'times_index': '/tmp/oceanval_times_fnbybl48/1.pkl'},
        {'name': 'n2', 'sim_dir': '/data/thaumus2/scratch/hpo/COMFORT/baseline_archerfull', 'n_dirs_down': 2, 'times_index': '/tmp/oceanval_times_fnbybl48/2.pkl'},
    ],
    variables={
        'Temperature': {'n': 'votemper', 'n2': 'votemper'},
    },
    climatology={
        'Temperature': {'start': 2012, 'end': 2012, 'surface': True, 'bottom': False, 'water_column': None},
    },
    phenology=None,
    thickness=None,
    out_dir='/users/modellers/maz/OceanVal_fvcom',
    cores=6,
    as_missing=[0.0, 0.0],
    figure_code=False,
)
