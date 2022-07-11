import seaborn as sb
import matplotlib.pyplot as plt
from matplotlib import rcParams
from collections import Counter
import pandas as pd
import numpy as np
import os

# start plotting
def plot_heatmap(group, count_type, size, filename, temp_output):

    y_length = len(group.keys())
    x_length = len(list(group.values())[0])
    data = np.array(list(group.values())).reshape(y_length, x_length)
#     print(data)
#     print(y_length, x_length)
    
#     print(group.keys())
    keys = list(group.keys())
    df = pd.DataFrame(data, index=keys)
    df = df.sort_index(ascending=False)


    # print(df)
    
#     rcParams["figure.autolayout"] = True
    rcParams['figure.figsize'] = 15,8
    ax = sb.heatmap(df, cmap="RdPu") # , cmap="RdPu"
    sb.set(font_scale=1.5)
    # ax.legend(fontsize = 20)
    plt.title(f"{count_type} Count", fontsize = 20)
    
#     plt.ylim(0, 130)
#     print(bottom,top)
    plt.ylabel("TB")
    locs, labels = plt.yticks()
#     print(locs, labels)
    up,bottom = plt.ylim()
    up = int(up)
    bottom = int(bottom)
    # print(up,bottom)
#     print(np.arange(bottom,up,10.0))
#     print(np.arange(up,bottom,10.0))
    plt.yticks(np.arange(bottom,up,10),np.arange(up,bottom,-10), fontsize=20)
    plt.xticks(fontsize=20)
    plt.xlabel("Time (Interval 5s)", fontsize = 20)
    plt.ylabel(f"{size}",fontsize = 20)



    MYDIR = "heatmap"
    CHECK_FOLDER = os.path.isdir(MYDIR)

    # If folder doesn't exist, then create it.
    if not CHECK_FOLDER:
        os.makedirs(MYDIR)
    else:
        pass

    count_type = count_type.lower()
    try:
        count_type = "_".join(count_type.split(" ")).lower()
    except:
        count_type = count_type

    df.to_pickle(f"pickles/{filename}/{filename}.plot.{count_type}.pickle")



    # plt.show(block=False)
    # plt.show()
    plt.savefig(f"./{MYDIR}/{filename}.{count_type}.svg", dpi=100)
    plt.savefig(f"./{temp_output}/{filename}.{count_type}.svg", dpi=100)
    plt.close()