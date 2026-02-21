import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.gridspec import GridSpec
import warnings
warnings.filterwarnings('ignore')

# ============================================================
#         MOVIE RECOMMENDATION SYSTEM
#         By Sarthak Midhotiya
#         Libraries: Pandas, NumPy, Matplotlib
# ============================================================

# ─────────────────────────────────────────
# STEP 1: CREATE MOVIE DATASET
# ─────────────────────────────────────────

data = {
    'Movie': [
        'The Dark Knight', 'Inception', 'Interstellar', 'The Matrix',
        'Avengers: Endgame', 'Iron Man', 'Thor', 'Spider-Man',
        'The Godfather', 'Pulp Fiction', 'Forrest Gump', 'Shawshank Redemption',
        'Titanic', 'Avatar', 'La La Land', 'The Notebook',
        'The Conjuring', 'It', 'A Quiet Place', 'Get Out',
        'The Grand Budapest Hotel', 'Superbad', 'Home Alone', 'Dumb and Dumber',
        'Finding Nemo', 'The Lion King', 'Toy Story', 'Frozen',
        'John Wick', 'Mad Max: Fury Road', 'Mission Impossible', 'Die Hard'
    ],
    'Genre': [
        'Action', 'Sci-Fi', 'Sci-Fi', 'Sci-Fi',
        'Action', 'Action', 'Action', 'Action',
        'Drama', 'Drama', 'Drama', 'Drama',
        'Romance', 'Sci-Fi', 'Romance', 'Romance',
        'Horror', 'Horror', 'Horror', 'Horror',
        'Comedy', 'Comedy', 'Comedy', 'Comedy',
        'Animation', 'Animation', 'Animation', 'Animation',
        'Action', 'Action', 'Action', 'Action'
    ],
    'Rating': [
        9.0, 8.8, 8.6, 8.7,
        8.4, 7.9, 7.0, 7.4,
        9.2, 8.9, 8.8, 9.3,
        7.8, 7.9, 8.0, 7.2,
        7.5, 7.3, 7.5, 7.7,
        8.1, 7.6, 7.7, 7.3,
        8.1, 8.5, 8.3, 7.4,
        7.4, 8.1, 7.4, 8.2
    ],
    'Year': [
        2008, 2010, 2014, 1999,
        2019, 2008, 2011, 2002,
        1972, 1994, 1994, 1994,
        1997, 2009, 2016, 2004,
        2013, 2017, 2018, 2017,
        2014, 2007, 1990, 1994,
        2003, 1994, 1995, 2013,
        2014, 2015, 1996, 1988
    ],
    'Votes': [
        2700000, 2400000, 1900000, 1900000,
        1200000, 1000000, 800000, 750000,
        1900000, 2100000, 2000000, 2700000,
        1200000, 1300000, 700000, 400000,
        500000, 600000, 450000, 650000,
        700000, 800000, 600000, 500000,
        1100000, 1000000, 1000000, 750000,
        900000, 900000, 700000, 850000
    ]
}

df = pd.DataFrame(data)

# ─────────────────────────────────────────
# STEP 2: DATA ANALYSIS WITH NUMPY
# ─────────────────────────────────────────

print("=" * 60)
print("       🎬 MOVIE RECOMMENDATION SYSTEM")
print("=" * 60)

print("\n📊 DATASET OVERVIEW")
print(f"   Total Movies   : {len(df)}")
print(f"   Total Genres   : {df['Genre'].nunique()}")
print(f"   Average Rating : {np.mean(df['Rating']):.2f}")
print(f"   Highest Rating : {np.max(df['Rating'])}")
print(f"   Lowest Rating  : {np.min(df['Rating'])}")

# ─────────────────────────────────────────
# STEP 3: SEPARATE MOVIES BY GENRE
# ─────────────────────────────────────────

print("\n" + "=" * 60)
print("🎭 MOVIES SEPARATED BY GENRE")
print("=" * 60)

genre_groups = df.groupby('Genre')

for genre, group in genre_groups:
    print(f"\n  🎬 {genre.upper()} ({len(group)} movies)")
    print(f"  {'Movie':<35} {'Rating':>6}  {'Year':>5}")
    print(f"  {'-'*50}")
    for _, row in group.sort_values('Rating', ascending=False).iterrows():
        print(f"  {row['Movie']:<35} ⭐ {row['Rating']:>4}  ({row['Year']})")

# ─────────────────────────────────────────
# STEP 4: SEPARATE BY RATING CATEGORY
# ─────────────────────────────────────────

def rating_category(rating):
    if rating >= 9.0:
        return '🏆 Masterpiece (9.0+)'
    elif rating >= 8.5:
        return '⭐ Excellent (8.5-8.9)'
    elif rating >= 8.0:
        return '👍 Great (8.0-8.4)'
    elif rating >= 7.5:
        return '😊 Good (7.5-7.9)'
    else:
        return '🙂 Average (Below 7.5)'

df['Rating_Category'] = df['Rating'].apply(rating_category)

print("\n" + "=" * 60)
print("⭐ MOVIES SEPARATED BY RATING")
print("=" * 60)

for category, group in df.groupby('Rating_Category', sort=False):
    sorted_group = group.sort_values('Rating', ascending=False)
    print(f"\n  {category}")
    print(f"  {'Movie':<35} {'Genre':<12} {'Rating':>6}")
    print(f"  {'-'*55}")
    for _, row in sorted_group.iterrows():
        print(f"  {row['Movie']:<35} {row['Genre']:<12} ⭐ {row['Rating']}")

# ─────────────────────────────────────────
# STEP 5: RECOMMENDATION FUNCTION
# ─────────────────────────────────────────

def recommend_movies(genre=None, min_rating=7.0, top_n=5):
    filtered = df.copy()
    if genre:
        filtered = filtered[filtered['Genre'].str.lower() == genre.lower()]
    filtered = filtered[filtered['Rating'] >= min_rating]
    filtered = filtered.sort_values('Rating', ascending=False).head(top_n)
    return filtered[['Movie', 'Genre', 'Rating', 'Year']]

print("\n" + "=" * 60)
print("🔍 RECOMMENDATIONS")
print("=" * 60)

print("\n  🎬 Top 5 Action Movies (Rating ≥ 8.0):")
print(recommend_movies(genre='Action', min_rating=8.0).to_string(index=False))

print("\n  🎬 Top 5 Drama Movies (Rating ≥ 8.5):")
print(recommend_movies(genre='Drama', min_rating=8.5).to_string(index=False))

print("\n  🎬 Top 5 All Genres (Rating ≥ 9.0):")
print(recommend_movies(min_rating=9.0).to_string(index=False))

# ─────────────────────────────────────────
# STEP 6: VISUALIZATIONS WITH MATPLOTLIB
# ─────────────────────────────────────────

colors = {
    'Action':    '#E74C3C',
    'Sci-Fi':    '#3498DB',
    'Drama':     '#2ECC71',
    'Romance':   '#E91E8C',
    'Horror':    '#9B59B6',
    'Comedy':    '#F39C12',
    'Animation': '#1ABC9C'
}

fig = plt.figure(figsize=(20, 16))
fig.patch.set_facecolor('#0D1117')
gs = GridSpec(3, 3, figure=fig, hspace=0.45, wspace=0.35)

# ── CHART 1: Average Rating by Genre (Bar Chart) ──
ax1 = fig.add_subplot(gs[0, :2])
ax1.set_facecolor('#161B22')
genre_avg = df.groupby('Genre')['Rating'].mean().sort_values(ascending=False)
bars = ax1.bar(genre_avg.index, genre_avg.values,
               color=[colors[g] for g in genre_avg.index], edgecolor='white', linewidth=0.5)
for bar, val in zip(bars, genre_avg.values):
    ax1.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.02,
             f'{val:.1f}', ha='center', va='bottom', color='white', fontsize=9, fontweight='bold')
ax1.set_title('📊 Average Rating by Genre', color='white', fontsize=13, fontweight='bold', pad=10)
ax1.set_ylabel('Average Rating', color='white')
ax1.tick_params(colors='white')
ax1.set_ylim(6.5, 9.8)
for spine in ax1.spines.values(): spine.set_color('#30363D')
ax1.set_facecolor('#161B22')

# ── CHART 2: Genre Distribution (Pie Chart) ──
ax2 = fig.add_subplot(gs[0, 2])
ax2.set_facecolor('#161B22')
genre_counts = df['Genre'].value_counts()
wedges, texts, autotexts = ax2.pie(
    genre_counts.values,
    labels=genre_counts.index,
    colors=[colors[g] for g in genre_counts.index],
    autopct='%1.0f%%',
    startangle=140,
    textprops={'color': 'white', 'fontsize': 8}
)
for at in autotexts: at.set_fontsize(7)
ax2.set_title('🎭 Genre Distribution', color='white', fontsize=13, fontweight='bold', pad=10)

# ── CHART 3: Rating Distribution (Histogram) ──
ax3 = fig.add_subplot(gs[1, :2])
ax3.set_facecolor('#161B22')
ax3.hist(df['Rating'], bins=10, color='#3498DB', edgecolor='white', linewidth=0.7, alpha=0.85)
ax3.axvline(df['Rating'].mean(), color='#F39C12', linestyle='--', linewidth=2, label=f"Mean: {df['Rating'].mean():.2f}")
ax3.set_title('📈 Rating Distribution of All Movies', color='white', fontsize=13, fontweight='bold', pad=10)
ax3.set_xlabel('Rating', color='white')
ax3.set_ylabel('Number of Movies', color='white')
ax3.tick_params(colors='white')
ax3.legend(facecolor='#30363D', labelcolor='white')
for spine in ax3.spines.values(): spine.set_color('#30363D')

# ── CHART 4: Rating Category Pie ──
ax4 = fig.add_subplot(gs[1, 2])
ax4.set_facecolor('#161B22')
cat_counts = df['Rating_Category'].value_counts()
cat_colors = ['#FFD700', '#C0C0C0', '#CD7F32', '#3498DB', '#2ECC71']
wedges2, texts2, autotexts2 = ax4.pie(
    cat_counts.values,
    labels=[c.split('(')[0].strip() for c in cat_counts.index],
    colors=cat_colors[:len(cat_counts)],
    autopct='%1.0f%%',
    startangle=90,
    textprops={'color': 'white', 'fontsize': 7.5}
)
ax4.set_title('⭐ Rating Categories', color='white', fontsize=13, fontweight='bold', pad=10)

# ── CHART 5: Top 10 Movies by Rating (Horizontal Bar) ──
ax5 = fig.add_subplot(gs[2, :])
ax5.set_facecolor('#161B22')
top10 = df.nlargest(10, 'Rating').sort_values('Rating')
bar_colors = [colors[g] for g in top10['Genre']]
bars2 = ax5.barh(top10['Movie'], top10['Rating'], color=bar_colors, edgecolor='white', linewidth=0.5)
for bar, val in zip(bars2, top10['Rating']):
    ax5.text(bar.get_width() + 0.02, bar.get_y() + bar.get_height()/2,
             f'⭐ {val}', va='center', color='white', fontsize=9, fontweight='bold')
ax5.set_title('🏆 Top 10 Highest Rated Movies', color='white', fontsize=13, fontweight='bold', pad=10)
ax5.set_xlabel('Rating', color='white')
ax5.tick_params(colors='white')
ax5.set_xlim(8.4, 9.8)
for spine in ax5.spines.values(): spine.set_color('#30363D')
legend_patches = [mpatches.Patch(color=colors[g], label=g) for g in colors]
ax5.legend(handles=legend_patches, loc='lower right', facecolor='#30363D',
           labelcolor='white', fontsize=8, ncol=4)

fig.suptitle('🎬 Movie Recommendation System — Sarthak Midhotiya',
             color='white', fontsize=16, fontweight='bold', y=0.98)

plt.savefig('/home/claude/movie_recommendation.png', dpi=150,
            bbox_inches='tight', facecolor='#0D1117')
plt.close()
print("\n✅ Charts saved as movie_recommendation.png")
print("\n" + "=" * 60)
print("  ✅ MOVIE RECOMMENDATION SYSTEM COMPLETE!")
print("=" * 60)
