import matplotlib
import matplotlib.pyplot as plt

import BPTK_Py

from src.population_exponential import PopulationExponential

matplotlib.use('TkAgg')

bptk = BPTK_Py.bptk()
model_01 = PopulationExponential()
scenario_manager = {
    'population_scenarios': {
        'model': model_01,
        'base_constants': {
            'Initial Population': 10370,
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
                    'Initial Population': 1370
                }
            }
        },
    scenario_manager='population_scenarios')

population_results = bptk.plot_scenarios(
    scenarios='base,scenario20',
    scenario_managers='population_scenarios',
    series_names={
        'population_scenarios_base_Number of Private Cars': 'base',
        'population_scenarios_scenario20_Number of Private Cars': 'scenario20'
    },
    equations='Number of Private Cars',
    return_df=False
)

# print(population_results)
plt.show()
