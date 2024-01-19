import pandas as pd
import matplotlib.pyplot as plt

import seaborn as sns


path_dict_log = {'BPI Challenge 2012': 'results/reproduced_results/BPI_challenge_2012','Sepsis_Cases': 'results/reproduced_results/Sepsis_Cases',
                 'BPI Challenge 2018': 'results/reproduced_results/BPI_challenge_2018'
                  }
results_name = ('fitness_BPI_Challenge_2012.xes.csv', 'fitness_Sepsis_Cases_-_Event_Log.xes.csv', 'fitness_BPI_Challenge_2018.xes.csv')

models = ('Random', 'Longest', 'Feature_Guided', 'Sequence_Guided')

fig, axes = plt.subplots(nrows=1, ncols=3, figsize=(18, 4))

for log, result, num_plot in zip(path_dict_log.keys(),results_name,(0,1,2)):
    combined_df = pd.DataFrame(columns=('sample_size','deviating_traces','Model'))
    for model in models:
        df = pd.read_csv(f'{path_dict_log[log]}/{model}/{result}')
        df = df[['sample_size', 'deviating_traces']]
        validierung = df.groupby(by='sample_size').mean()
        print(log)
        print(model)
        print(validierung)
        df.loc[:, 'Model'] = model
        combined_df = pd.concat([combined_df,df])

    sns.boxplot(x="sample_size", y="deviating_traces",
            hue="Model",
            data=combined_df,
            ax=axes[num_plot])
    axes[num_plot].set_title(log)
    axes[num_plot].set_yticks([0,100,200,300,400,500])
    axes[num_plot].set_yticklabels([0, 100, 200, 300, 400, 500])
    for i in range(1, 5):
        axes[num_plot].axvline(x=i - 0.5, color='grey', linestyle='--', linewidth=1)



plt.show()
pass





