import BPTK_Py

from src.population_base import PopulationBase

bptk = BPTK_Py.bptk()
model_01 = PopulationBase()
scenario_manager = {
    'population_scenarios': {
        'model': model_01,
        'base_constants': {
            'Carrying Capacity': 17100,
            'Public Investment in Mobility': 2e9,
            'Available Transportation Modes': 3.0
        }
    }
}

bptk.register_scenario_manager(scenario_manager)

bptk.register_scenarios(
    scenarios={
            'base': {
            },
            'scenario20': {
                'constants': {
                    'Carrying Capacity': 20000
                }
            }
        }
    ,
    scenario_manager='population_scenarios')

population_results = bptk.plot_scenarios(
    scenarios='scenario20',
    scenario_managers='population_scenarios',
    equations='Number of Private Cars',
    return_df=True
)

print(population_results)
