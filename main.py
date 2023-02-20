import csv
import pandas
import datetime
from PIL import Image
def graph():
    df = pandas.read_csv('Data/data.csv')
    input_lotes = input("Pon los lotes que quieras graficar separados por coma. ej PB34822-04, PB34822-03\n")
    input_lotes = input_lotes.split(",")
    input_lotes = [l.strip() for l in input_lotes]
    # input_lotes = ["PB34822-04"]
    for lote in input_lotes:
        new_df = df[df["Lote"].str.contains(lote)]
        new_df = new_df[["Lote","Fecha","Tazas de alimento","Litros de agua"]]
        new_df['Fecha'] = pandas.to_datetime(new_df['Fecha'])
        for i in new_df.index:
            new_df.loc[i, "Fecha"] = pandas.to_datetime(new_df.loc[i,"Fecha"])
        new_df["Tazas de alimento"] = new_df["Tazas de alimento"].fillna(0)
        new_df["Litros de agua"] = new_df["Litros de agua"].fillna(0)
        import matplotlib.pyplot as plt
        import statistics
        new_df = new_df.sort_values(by=["Fecha"])
        new_df["Tazas de alimento Accumulado"] = new_df["Tazas de alimento"].cumsum()
        new_df["Litros de agua Accumulado"] = new_df["Litros de agua"].cumsum()
        plt.figure()
        ax = new_df.plot(x="Fecha", y=["Tazas de alimento Accumulado", "Litros de agua Accumulado"])
        plt.xlabel("Fecha")
        plt.ylabel("Consumo")
        plt.title(lote)
        plt.savefig("Results/" + lote + ".jpg", dpi=72)
if __name__ == "__main__":
    graph()