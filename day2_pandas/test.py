import pandas as pd
import numpy as np
if __name__ == '__main__':
    # lt1 = [["li", 80, 70, 100], ["yang", 70, 80, 99], ["zhang", 60, 70, 100]]
    # lt2 = ["uid", "en", "cn", "ma"]
    # new=list(zip(*lt1))
    #
    # dic={j:list(new[i]) for i,j in enumerate(lt2)}
    # print(dic)

    # np01=np.array(lt1)
    # np02=np01.transpose()
    # dic={lt2[i]:list(np02[i]) for i in range(len(lt2))}
    # print(dic)
    # dic={lt2[i]:lt1[i] for i in range(len(lt2))}


    # 期望输出 {'uid': ['li', 'yang', 'zhang'],
    # 'en': [80, 70, 60], 'cn': [70, 80, 70],
    # 'ma': [100, 99, 100]}
    pass