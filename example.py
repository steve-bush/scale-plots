import scale_plots

plots = scale_plots.Plots()
# Parse the sdf file to create a pandas DataFrame
plots.sdf_to_df('KENO_slovenia_tsunami.sdf')
# Place keys in a list of lists or just a list if only one key
keys = [['KENO_slovenia_tsunami', 'zr90-zr5h8', 'total', '(0,0)'],['KENO_slovenia_tsunami', 'zr90-zr5h8', 'elastic', '(0,0)']]
legend = {tuple(keys[0]) : 'total', tuple(keys[1]) : 'elastic'}
# Can also pass plot_std_dev=False to remove error bars
plots.sensitivity_lethargy_plot(keys, plot_err_bar=True, plot_corr=True, legend_dict=legend)

# Parse the covariance file
filename = 'scale.rev05.44groupcov'
plots.parse_coverx(filename)
# Pick which material and interaction to plot
mat_mt_1 = (8001001, 102)
mat_mt_2 = (8001001, 102)
# Choose whether to plot the covariance for correlations
covariance = False
# Choose a high and low energy bound
elow = float('-inf')
ehigh = float('inf')
# Choose interval that labels are placed on the chart
tick_step = 2
# Choose either research or publication view
mode = 'publication'
# Choose a color mapping
cmap = 'viridis'
plots.heatmap_plot(mat_mt_1, mat_mt_2, filename, covariance=covariance, elow=elow,
                   ehigh=ehigh, cmap=cmap, tick_step=tick_step, mode=mode)