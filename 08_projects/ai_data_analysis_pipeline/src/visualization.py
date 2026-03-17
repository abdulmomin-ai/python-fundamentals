
import matplotlib.pyplot as plt
import os 


def plot_marks_vs_hours(df):
    fig , ax = plt.subplots()
    ax.plot(df['StudyHours'], df['Marks'], marker='o', linestyle='--')
    ax.grid(True)
    ax.set_title("Marks vs Study Hours")
    ax.set_xlabel("Study Hours")
    ax.set_ylabel("Marks")
    plt.show()



# Bar Plot
def plot_deaprtment_average(df):
    fig, ax = plt.subplots()
    dept_avg  = df.groupby('Department')['Marks'].mean()
    ax.bar(dept_avg.index, dept_avg.values)
    ax.set_title("Average Marks per Department")
    ax.set_xlabel("Department")
    ax.set_ylabel("Average Marks")
 
    plt.show()


# Scatter Plot 
def plot_scatter(df):
    fig, ax = plt.subplots()
    ax.scatter(df['StudyHours'], df['Marks'])
    ax.set_title("StudyHours vs Marks")
    ax.set_xlabel("Study Hours")
    ax.set_ylabel("Marks")
   
    plt.show()
     


def save_plot(df):
    fig, ax = plt.subplots()

    dept_avg  = df.groupby('Department')['Marks'].mean()
    ax.bar(dept_avg.index, dept_avg.values)
    ax.set_title("Average Marks per Department")
    ax.set_xlabel("Department")
    ax.set_ylabel("Average Marks")

    if not os.path.exists("output"):
        os.mkdir("output")

    file_path = os.path.join("output", "marks_plot.png")
    plt.savefig(file_path)
    print("plot saved successfully")

    plt.close()



def dashboard(df):
    fig, axs = plt.subplots(1, 2, figsize=(10, 4))
    axs[0].bar(df['Name'], df['Marks'])
    axs[0].set_title("Student Marks")

    axs[1].scatter(df['StudyHours'], df['Marks'])
    axs[1].set_title("Hours vs Marks")

    plt.tight_layout()
    plt.show()


def plot_dustribution(df):
    fig, ax = plt.subplots()

    ax.hist(df['Marks'], bins=5)

    ax.set_title("Marks Distribution")
    ax.set_xlabel("Marks")
    ax.set_ylabel("Frequency")

    plt.show()


def marks_histogram(df):
    print("Histogram function running...")

    plt.hist(df["Marks"].decribe(), bins=5)

    plt.title("Marks Distribution")
    plt.xlabel("Marks")
    plt.ylabel("Number of Students")

    plt.show()









