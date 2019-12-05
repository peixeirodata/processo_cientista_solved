def countplot_top_prop_label(graph,df,size):
    """
        This function plots the proportion value when plotting a countplot with seaborn.
        Params:
        graph: The instance created with seaborn
        df: dataframe
        size: size of the labels to be placed in the graph
    """
    for elem in graph.patches:
        h = elem.get_height()
        total = len(df)
        graph.text(elem.get_x()+elem.get_width()/2., h + 3, '{:1.2f}%'.format(h/total*100), ha="center", fontsize=size) 