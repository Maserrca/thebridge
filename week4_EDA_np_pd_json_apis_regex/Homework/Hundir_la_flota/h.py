import pandas as pd
tablero1 = pd.DataFrame({1: "~", 2: "~",3: "~",4: "~",5: "~",6: "~",7: "~",8: "~",9: "~",10: "~"},index=[1, 2,3,4,5,6,7,8,9,10])

while "#" in tablero1.values:
    print(tablero1)
    break
else:
    print("finish")