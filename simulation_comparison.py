# An OceanVal comparison of simulations, written by the oceanval window on 2026-11-03.
# Run it again with: python <this file>
import oceanval

oceanval.compare_simulations(
    simulations=[
        {'name': 'fvcom', 'sim_dir': '/data/thaumus2/scratch/maz/Models/FVCOM/run/aqua_v16_trawl/output/aqua_v16_trawl/tide_wind_nest_ersem/2012_2014_val', 'n_dirs_down': 0, 'times_index': '/tmp/oceanval_times_6het5fp9/1.pkl'},
        {'name': 'nemo', 'sim_dir': '/data/thaumus2/scratch/hpo/COMFORT/baseline_archerfull', 'n_dirs_down': 2, 'times_index': '/tmp/oceanval_times_6het5fp9/2.pkl'},
    ],
    variables={
        'Temperature': {'fvcom': 'temp', 'nemo': 'votemper'},
    },
    climatology={
        'Temperature': {'start': 2013, 'end': 2013, 'surface': True, 'bottom': False, 'water_column': None},
    },
    phenology=None,
    thickness=None,
    out_dir='/users/modellers/maz/OceanVal_fvcom',
    cores=6,
    as_missing=[0.0, 0.0],
    figure_code=False,
    unify={
        'baseline': 'nemo',
    },
    unit_conversions={
        'Temperature': {'nemo': {'multiplier': 1, 'adder': 0}},
    },
)
