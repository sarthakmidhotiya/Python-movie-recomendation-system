# 🎬 Movie Recommendation System

> A Python-based Movie Recommendation System that filters and recommends movies by **Genre** and **Rating** — with beautiful visualizations!

---

## 📌 About the Project

This project analyzes a dataset of **32 popular movies** across **7 genres** and recommends movies based on:
- 🎭 **Genre** — Action, Drama, Sci-Fi, Romance, Horror, Comedy, Animation
- ⭐ **Rating Category** — Masterpiece, Excellent, Great, Good, Average

Built using only **Python core libraries** — no machine learning required!

---

## 🛠️ Built With

![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white&style=for-the-badge)
![Pandas](https://img.shields.io/badge/Pandas-150458?logo=pandas&logoColor=white&style=for-the-badge)
![NumPy](https://img.shields.io/badge/NumPy-013243?logo=numpy&logoColor=white&style=for-the-badge)
![Matplotlib](https://img.shields.io/badge/Matplotlib-11557C?logo=plotly&logoColor=white&style=for-the-badge)

---

## 📂 Project Structure

```
movie-recommendation-system/
│
├── movie_recommendation.py   # Main Python script
├── movie_recommendation.png  # Auto-generated charts
└── README.md                 # Project documentation
```

---

## ⚙️ How It Works

### 1️⃣ Dataset
A custom dataset of 32 movies with these columns:

| Column | Description |
|--------|-------------|
| Movie | Name of the movie |
| Genre | Category (Action, Drama, etc.) |
| Rating | IMDb-style rating (out of 10) |
| Year | Release year |
| Votes | Number of votes |

---

### 2️⃣ Movies Separated by Genre

Movies are grouped using `pandas.groupby()` and sorted by rating:

```python
genre_groups = df.groupby('Genre')
for genre, group in genre_groups:
    print(group.sort_values('Rating', ascending=False))
```

---

### 3️⃣ Movies Separated by Rating Category

Each movie is assigned a category using `numpy`:

| Category | Rating Range |
|----------|-------------|
| 🏆 Masterpiece | 9.0 and above |
| ⭐ Excellent | 8.5 – 8.9 |
| 👍 Great | 8.0 – 8.4 |
| 😊 Good | 7.5 – 7.9 |
| 🙂 Average | Below 7.5 |

---

### 4️⃣ Recommendation Function

```python
recommend_movies(genre='Action', min_rating=8.0, top_n=5)
```

Filter movies by genre and minimum rating and get top N results instantly!

---

## 📊 Visualizations

The project auto-generates a dark-themed chart dashboard with **5 graphs**:

| Chart | Description |
|-------|-------------|
| 📊 Bar Chart | Average rating per genre |
| 🥧 Pie Chart | Genre distribution |
| 📈 Histogram | Rating distribution of all movies |
| 🥧 Pie Chart | Rating category breakdown |
| 📉 Horizontal Bar | Top 10 highest rated movies |

---

## 🚀 How to Run

### Step 1 — Clone the repo
```bash
git clone https://github.com/sarthakmidhotiya/movie-recommendation-system.git
cd movie-recommendation-system
```

### Step 2 — Install libraries
```bash
pip install pandas numpy matplotlib
```

### Step 3 — Run the script
```bash
python movie_recommendation.py
```

---

## 📸 Output Preview

> Charts are saved automatically as `movie_recommendation.png`

The dashboard includes genre-wise analysis, rating distribution, and top 10 movies — all in a dark theme! 🖤

---

## 🎯 Sample Output

```
🎬 MOVIES SEPARATED BY GENRE

  ACTION (9 movies)
  The Dark Knight          ⭐ 9.0  (2008)
  Avengers: Endgame        ⭐ 8.4  (2019)
  Die Hard                 ⭐ 8.2  (1988)

⭐ MOVIES SEPARATED BY RATING

  🏆 Masterpiece (9.0+)
  Shawshank Redemption     Drama    ⭐ 9.3
  The Godfather            Drama    ⭐ 9.2
  The Dark Knight          Action   ⭐ 9.0
```

---

## 👨‍💻 Author

**Sarthak Midhotiya**
Student at Global Engineering College, Jabalpur

[![GitHub](https://img.shields.io/badge/-GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/sarthakmidhotiya)
[![LinkedIn](https://img.shields.io/badge/-LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/sarthakmidhotiya)
[![LeetCode](https://img.shields.io/badge/-LeetCode-FFA116?style=for-the-badge&logo=leetcode&logoColor=black)](https://leetcode.com/u/sarthak_midhotiya/)

---

## 📄 License

This project is open source and free to use for learning purposes.

---

> ⭐ If you found this helpful, consider giving it a star on GitHub!
