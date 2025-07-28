import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

np.random.seed(42)

# Random Value Generation

scores=np.random.normal(loc=70,scale=10,size=1000)
scores=np.clip(scores,0,100)

attendence=np.random.uniform(low=50,high=100,size=1000)

pass_fail=np.random.binomial(n=1,p=0.8,size=1000)

df=pd.DataFrame({
                "Score":scores,
                "Attendance (%)":attendence,
                "Passed":pass_fail
                 })

sns.histplot(df["Score"],kde=True,color="skyblue")
plt.title("Exam Score Distribution (Normal Distribution)")
plt.xlabel("Score")
plt.ylabel("Number of Students")
plt.grid(True)
plt.show()

sns.histplot(df["Attendance (%)"], bins=30, color="orange")
plt.title("Attendance Distribution (Uniform Distribution)")
plt.xlabel("Attendance %")
plt.ylabel("Students")
plt.grid(True)
plt.show()

sns.countplot(x="Passed", data=df, palette="Set2")
plt.title("Pass/Fail Outcome (Binomial)")
plt.xticks([0, 1], ['Failed', 'Passed'])
plt.grid(True)
plt.show()

df.to_csv("student_data.csv", index=False)


