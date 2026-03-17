import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

def analyze_data(df):
    avg_marks = df['Marks'].mean()
    print("Average Marks:", avg_marks)

    top_student = df.loc[df['Marks'].idxmax(), 'Name']
    print("Top Student:", top_student)

    print("\nDepartment Wise Average:")
    print(df.groupby('Department')['Marks'].mean())


    median_marks = df['Marks'].median()
    print("Median marks", median_marks)

    standard_dev =  df["Marks"].std()
    print("Standard Deviation", standard_dev)


    # Detect Weak Students
    weak_students = df[df['Marks'] < 70]
    print("Weak Students", weak_students)

    # Save to new CSV
    weak_students.to_csv("weak_students.csv", index=False)
    print("\nFile weak_students.csv created successfully")

    plt.hist(df["Marks"], bins=5)
# Labels
    plt.title("Marks Distribution")
    plt.xlabel("Marks")
    plt.ylabel("Number of Students")

# Show graph
    plt.show()

def add_performance(df):
    def performance(marks):
        if marks >= 90:
            return "Excellent"
        elif marks >= 75:
            return "Good"
        elif marks < 70:
            return "Weak Students"
        else:
            return "Need Improvement"
    df['Performance'] = df['Marks'].apply(performance)
    return df   


def top_department(df):
    dept = df.groupby('Department')['Marks'].mean().idxmax()
    print("\n Best Performing Department", dept)




def plot_marks(df):
    print("Plot function running...")
    df.groupby('Department')['Marks'].mean().plot(kind='bar')
    plt.title("Department Performance")
    plt.xlabel("Department")
    plt.ylabel("Average Marks")
    plt.show(block=True)