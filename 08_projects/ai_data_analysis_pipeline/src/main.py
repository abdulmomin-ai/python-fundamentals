print("MAIN FILE RUNNING...")


import os 
print("Main running from:", os.getcwd())
print("Visualization file path:", os.path.abspath("visualization.py"))
from src.loader import load_data
from src.cleaner import clean_data
from src.analyzer import analyze_data, add_performance, top_department, plot_marks
from src.visualization import plot_marks_vs_hours, plot_deaprtment_average, plot_scatter, save_plot, dashboard, plot_dustribution, marks_histogram

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
DATA_PATH = os.path.join(BASE_DIR, "data", "students.csv")
OUTPUT_PATH = os.path.join(BASE_DIR, "output", "processed_students.csv")

def run_pipeline():
    print("Pipeline started")

    df = load_data(DATA_PATH)
    print("After load")

    df = clean_data(df)
    print("After clean")

    df = add_performance(df)
    print("After Performance")

    analyze_data(df)
    print("After Analyze")

    top_department(df)
    print("After Top Department")

    plot_marks(df)
    print("After plot")

    plot_marks_vs_hours(df)
    print("2nd Graph")


    plot_deaprtment_average(df)

    plot_scatter(df)

    save_plot(df)

    dashboard(df)
    print("Dashboard")

    plot_dustribution(df)
    print("History of graphs")

    marks_histogram(df)
    print("After histogram")

    print("\nData with Performance Column:\n")
    print(df)  

    df.to_csv(OUTPUT_PATH, index=False)
    print("\n Processed Data saved to output folder successfully")

if __name__ == "__main__":
    run_pipeline()


