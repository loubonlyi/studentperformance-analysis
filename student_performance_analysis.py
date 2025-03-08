import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Симуляция данных
np.random.seed(42)  # Для воспроизводимости

# Количество студентов
n_students = 100

# Генерация данных
grades = np.random.randint(50, 100, size=n_students)  # Оценки от 50 до 100
study_hours_per_week = np.random.randint(1, 20, size=n_students)  # Часы учебы в неделю от 1 до 20

# Создание DataFrame
simulated_data = pd.DataFrame({
    'Grade': grades,
    'Average study hours per week': study_hours_per_week
})

# Рассчитываем корреляцию между оценками и часами учебы
correlation = simulated_data['Grade'].corr(simulated_data['Average study hours per week'])

# Визуализация данных
plt.figure(figsize=(10, 6))
sns.regplot(x='Average study hours per week', y='Grade', data=simulated_data, scatter_kws={'color':'blue'}, line_kws={'color':'red'})
plt.title(f'Correlation between Study Hours and Grades (r = {correlation:.2f})', fontsize=14)
plt.xlabel('Average Study Hours per Week')
plt.ylabel('Grade')
plt.grid(True)
plt.show()

print(f"Correlation: {correlation:.2f}")

