import random
import pandas as pd

random.seed(20220903)




ls = []
for i in range(20):
    alpha = ''
    num = ''
    alpha += chr(random.randint(65,90)) + chr(random.randint(65,90))
    num += str(random.randint(100,999))+ chr(random.randint(65,90))
    ls.append(alpha+num)

data = pd.DataFrame(ls)

data.to_csv('/home/bio_kang/country.csv', index=None, encoding='utf-8')