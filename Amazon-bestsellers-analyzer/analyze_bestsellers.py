import pandas as pd
import numpy as np
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')


def load_data(filepath):
    """
    Load the bestsellers CSV data into a pandas DataFrame
    
    Parameters:
    -----------
    filepath : str
        Path to the CSV file
    
    Returns:
    --------
    pd.DataFrame
        Loaded data
    """
    print("Loading Amazon Bestsellers Data...")
    df = pd.read_csv(filepath)
    print(f"Successfully loaded {len(df)} records\n")
    return df


def explore_data(df):
    """
    Perform initial data exploration
    
    Parameters:
    -----------
    df : pd.DataFrame
        The bestsellers dataframe
    """
    print("=" * 70)
    print("DATA EXPLORATION")
    print("=" * 70)
    
    print("\n1 Dataset Shape:")
    print(f"   Rows: {df.shape[0]}")
    print(f"   Columns: {df.shape[1]}")
    
    print("\n2 Column Names and Types:")
    print(df.dtypes)
    
    print("\n3 First 5 Rows:")
    print(df.head())
    
    print("\n4 Dataset Info:")
    print(df.info())
    
    print("\n5 Missing Values:")
    missing = df.isnull().sum()
    if missing.sum() == 0:
        print("   No missing values detected!")
    else:
        print(missing[missing > 0])
    
    print("\n6 Duplicate Rows:")
    duplicates = df.duplicated().sum()
    print(f"   Found {duplicates} duplicate rows")
    
    print("\n")


def statistical_summary(df):
    """
    Generate statistical summaries for numerical columns
    
    Parameters:
    -----------
    df : pd.DataFrame
        The bestsellers dataframe
    """
    print("=" * 70)
    print("STATISTICAL SUMMARY")
    print("=" * 70)
    
    print("\n1 Numerical Columns Summary:")
    print(df.describe())
    
    print("\n2 Price Statistics:")
    print(f"   Mean Price: ${df['Price'].mean():.2f}")
    print(f"   Median Price: ${df['Price'].median():.2f}")
    print(f"   Min Price: ${df['Price'].min():.2f}")
    print(f"   Max Price: ${df['Price'].max():.2f}")
    print(f"   Std Dev: ${df['Price'].std():.2f}")
    
    print("\n3 Rating Statistics:")
    print(f"   Mean Rating: {df['User Rating'].mean():.2f}")
    print(f"   Median Rating: {df['User Rating'].median():.2f}")
    print(f"   Min Rating: {df['User Rating'].min():.1f}")
    print(f"   Max Rating: {df['User Rating'].max():.1f}")
    
    print("\n4 Reviews Statistics:")
    print(f"   Mean Reviews: {df['Reviews'].mean():.0f}")
    print(f"   Median Reviews: {df['Reviews'].median():.0f}")
    print(f"   Max Reviews: {df['Reviews'].max():.0f}")
    
    print("\n")


def genre_analysis(df):
    """
    Analyze books by genre
    
    Parameters:
    -----------
    df : pd.DataFrame
        The bestsellers dataframe
    """
    print("=" * 70)
    print("GENRE ANALYSIS")
    print("=" * 70)
    
    print("\n1 Books by Genre:")
    genre_counts = df['Genre'].value_counts()
    print(genre_counts)
    print(f"\n   Fiction: {genre_counts.get('Fiction', 0)} books ({genre_counts.get('Fiction', 0)/len(df)*100:.1f}%)")
    print(f"   Non Fiction: {genre_counts.get('Non Fiction', 0)} books ({genre_counts.get('Non Fiction', 0)/len(df)*100:.1f}%)")
    
    print("\n2 Average Price by Genre:")
    avg_price_by_genre = df.groupby('Genre')['Price'].mean().sort_values(ascending=False)
    for genre, price in avg_price_by_genre.items():
        print(f"   {genre}: ${price:.2f}")
    
    print("\n3 Average Rating by Genre:")
    avg_rating_by_genre = df.groupby('Genre')['User Rating'].mean().sort_values(ascending=False)
    for genre, rating in avg_rating_by_genre.items():
        print(f"   {genre}: {rating:.2f} ⭐")
    
    print("\n4 Average Reviews by Genre:")
    avg_reviews_by_genre = df.groupby('Genre')['Reviews'].mean().sort_values(ascending=False)
    for genre, reviews in avg_reviews_by_genre.items():
        print(f"   {genre}: {reviews:.0f} reviews")
    
    print("\n")


def top_books_and_authors(df):
    """
    Identify top books and most prolific authors
    
    Parameters:
    -----------
    df : pd.DataFrame
        The bestsellers dataframe
    """
    print("=" * 70)
    print("🏆 TOP BOOKS AND AUTHORS")
    print("=" * 70)
    
    print("\n1 Top 10 Most Reviewed Books:")
    top_reviewed = df.nlargest(10, 'Reviews')[['Name', 'Author', 'Reviews', 'User Rating']]
    for idx, (_, row) in enumerate(top_reviewed.iterrows(), 1):
        print(f"   {idx}. {row['Name'][:50]}...")
        print(f"      by {row['Author']} | {row['Reviews']:,} reviews | {row['User Rating']} ⭐")
    
    print("\n2 Top 10 Highest Rated Books (with 1000+ reviews):")
    high_rated = df[df['Reviews'] >= 1000].nlargest(10, 'User Rating')[['Name', 'Author', 'User Rating', 'Reviews']]
    for idx, (_, row) in enumerate(high_rated.iterrows(), 1):
        print(f"   {idx}. {row['Name'][:50]}...")
        print(f"      by {row['Author']} | {row['User Rating']} ⭐ | {row['Reviews']:,} reviews")
    
    print("\n3 Most Prolific Authors (Top 15):")
    author_counts = df['Author'].value_counts().head(15)
    for idx, (author, count) in enumerate(author_counts.items(), 1):
        print(f"   {idx}. {author}: {count} books")
    
    print("\n4 Most Expensive Books (Top 10):")
    expensive = df.nlargest(10, 'Price')[['Name', 'Author', 'Price', 'Year']]
    for idx, (_, row) in enumerate(expensive.iterrows(), 1):
        print(f"   {idx}. {row['Name'][:50]}...")
        print(f"      ${row['Price']} ({row['Year']}) by {row['Author']}")
    
    print("\n")


def year_analysis(df):
    """
    Analyze trends over years
    
    Parameters:
    -----------
    df : pd.DataFrame
        The bestsellers dataframe
    """
    print("=" * 70)
    print("YEAR-BY-YEAR ANALYSIS")
    print("=" * 70)
    
    print("\n1 Books per Year:")
    books_per_year = df['Year'].value_counts().sort_index()
    for year, count in books_per_year.items():
        print(f"   {year}: {count} books")
    
    print("\n2 Average Price by Year:")
    avg_price_by_year = df.groupby('Year')['Price'].mean().sort_index()
    for year, price in avg_price_by_year.items():
        print(f"   {year}: ${price:.2f}")
    
    print("\n3 Average Rating by Year:")
    avg_rating_by_year = df.groupby('Year')['User Rating'].mean().sort_index()
    for year, rating in avg_rating_by_year.items():
        print(f"   {year}: {rating:.2f} ⭐")
    
    print("\n4 Genre Distribution by Year:")
    genre_by_year = pd.crosstab(df['Year'], df['Genre'])
    print(genre_by_year)
    
    print("\n")


def price_analysis(df):
    """
    Detailed price analysis
    
    Parameters:
    -----------
    df : pd.DataFrame
        The bestsellers dataframe
    """
    print("=" * 70)
    print("PRICE ANALYSIS")
    print("=" * 70)
    
    print("\n1️⃣ Price Ranges:")
    bins = [0, 5, 10, 15, 20, 30, 50, 200]
    labels = ['$0-5', '$5-10', '$10-15', '$15-20', '$20-30', '$30-50', '$50+']
    df['Price Range'] = pd.cut(df['Price'], bins=bins, labels=labels)
    price_range_counts = df['Price Range'].value_counts().sort_index()
    for price_range, count in price_range_counts.items():
        print(f"   {price_range}: {count} books ({count/len(df)*100:.1f}%)")
    
    print("\n2️⃣ Most Common Price Points:")
    common_prices = df['Price'].value_counts().head(10)
    for price, count in common_prices.items():
        print(f"   ${price}: {count} books")
    
    print("\n3️⃣ Price by Genre and Year:")
    price_genre_year = df.groupby(['Year', 'Genre'])['Price'].mean().unstack()
    print(price_genre_year)
    
    print("\n")


def rating_analysis(df):
    """
    Analyze rating distributions
    
    Parameters:
    -----------
    df : pd.DataFrame
        The bestsellers dataframe
    """
    print("=" * 70)
    print("⭐ RATING ANALYSIS")
    print("=" * 70)
    
    print("\n1️⃣ Rating Distribution:")
    rating_counts = df['User Rating'].value_counts().sort_index(ascending=False)
    for rating, count in rating_counts.items():
        bar_length = int(count / len(df) * 50)
        bar = '█' * bar_length
        print(f"   {rating} ⭐ | {bar} {count} books ({count/len(df)*100:.1f}%)")
    
    print("\n2️⃣ Books with Perfect 4.9 Rating:")
    perfect_rating = df[df['User Rating'] == 4.9]
    print(f"   Total: {len(perfect_rating)} books")
    print("\n   Top books with 4.9 rating:")
    for idx, (_, row) in enumerate(perfect_rating.nlargest(5, 'Reviews').iterrows(), 1):
        print(f"   {idx}. {row['Name'][:50]}...")
        print(f"      by {row['Author']} | {row['Reviews']:,} reviews")
    
    print("\n3️⃣ Lowest Rated Books:")
    lowest_rated = df.nsmallest(10, 'User Rating')[['Name', 'Author', 'User Rating', 'Reviews']]
    for idx, (_, row) in enumerate(lowest_rated.iterrows(), 1):
        print(f"   {idx}. {row['Name'][:50]}...")
        print(f"      {row['User Rating']} ⭐ | {row['Reviews']:,} reviews | by {row['Author']}")
    
    print("\n")


def correlation_analysis(df):
    """
    Analyze correlations between numerical variables
    
    Parameters:
    -----------
    df : pd.DataFrame
        The bestsellers dataframe
    """
    print("=" * 70)
    print("🔗 CORRELATION ANALYSIS")
    print("=" * 70)
    
    numerical_cols = ['User Rating', 'Reviews', 'Price', 'Year']
    correlation_matrix = df[numerical_cols].corr()
    
    print("\n1️⃣ Correlation Matrix:")
    print(correlation_matrix.round(3))
    
    print("\n2️⃣ Key Insights:")
    print(f"   • User Rating vs Reviews: {correlation_matrix.loc['User Rating', 'Reviews']:.3f}")
    print(f"   • User Rating vs Price: {correlation_matrix.loc['User Rating', 'Price']:.3f}")
    print(f"   • Price vs Reviews: {correlation_matrix.loc['Price', 'Reviews']:.3f}")
    print(f"   • Price vs Year: {correlation_matrix.loc['Price', 'Year']:.3f}")
    
    print("\n")


def generate_insights(df):
    """
    Generate key insights from the data
    
    Parameters:
    -----------
    df : pd.DataFrame
        The bestsellers dataframe
    """
    print("=" * 70)
    print("💡 KEY INSIGHTS")
    print("=" * 70)
    
    print("\n1 Most Popular Author:")
    top_author = df['Author'].value_counts().index[0]
    top_author_count = df['Author'].value_counts().values[0]
    print(f"   {top_author} with {top_author_count} bestselling books")
    
    print("\n2 Year with Most Bestsellers:")
    top_year = df['Year'].value_counts().index[0]
    top_year_count = df['Year'].value_counts().values[0]
    print(f"   {top_year} with {top_year_count} books")
    
    print("\n3 Most Common Price:")
    most_common_price = df['Price'].mode()[0]
    print(f"   ${most_common_price}")
    
    print("\n4 Average Book Characteristics:")
    print(f"   • Average Rating: {df['User Rating'].mean():.2f} ⭐")
    print(f"   • Average Price: ${df['Price'].mean():.2f}")
    print(f"   • Average Reviews: {df['Reviews'].mean():.0f}")
    
    print("\n5 Genre Preferences:")
    genre_pct = df['Genre'].value_counts(normalize=True) * 100
    print(f"   • Fiction: {genre_pct.get('Fiction', 0):.1f}%")
    print(f"   • Non Fiction: {genre_pct.get('Non Fiction', 0):.1f}%")
    
    print("\n6 Price Trends:")
    price_by_year = df.groupby('Year')['Price'].mean()
    price_change = ((price_by_year.iloc[-1] - price_by_year.iloc[0]) / price_by_year.iloc[0]) * 100
    print(f"   Average price changed by {price_change:.1f}% from 2009 to 2019")
    
    print("\n7 Rating Trends:")
    rating_by_year = df.groupby('Year')['User Rating'].mean()
    print(f"   Average rating ranged from {rating_by_year.min():.2f} to {rating_by_year.max():.2f}")
    
    print("\n8 Most Reviewed Book:")
    most_reviewed = df.loc[df['Reviews'].idxmax()]
    print(f"   '{most_reviewed['Name']}' by {most_reviewed['Author']}")
    print(f"   {most_reviewed['Reviews']:,} reviews | {most_reviewed['User Rating']} ⭐")
    
    print("\n")


def export_summary(df, output_file='analysis_summary.txt'):
    """
    Export analysis summary to a text file
    
    Parameters:
    -----------
    df : pd.DataFrame
        The bestsellers dataframe
    output_file : str
        Output filename
    """
    print("=" * 70)
    print("EXPORTING SUMMARY")
    print("=" * 70)
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("AMAZON BESTSELLERS DATA ANALYSIS SUMMARY\n")
        f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write("=" * 70 + "\n\n")
        
        f.write("DATASET OVERVIEW\n")
        f.write(f"Total Books: {len(df)}\n")
        f.write(f"Years Covered: {df['Year'].min()} - {df['Year'].max()}\n")
        f.write(f"Unique Authors: {df['Author'].nunique()}\n")
        f.write(f"Unique Titles: {df['Name'].nunique()}\n\n")
        
        f.write("STATISTICAL SUMMARY\n")
        f.write(df.describe().to_string())
        f.write("\n\n")
        
        f.write("TOP 10 AUTHORS\n")
        f.write(df['Author'].value_counts().head(10).to_string())
        f.write("\n\n")
        
        f.write("GENRE DISTRIBUTION\n")
        f.write(df['Genre'].value_counts().to_string())
        f.write("\n\n")
    
    print(f"Summary exported to '{output_file}'")
    print()


def main():
    """
    Main execution function
    """
    print("\n" + "=" * 70)
    print("📖 AMAZON BESTSELLERS DATA ANALYSIS (2009-2019)")
    print("=" * 70)
    print()
    
    # Load data
    df = load_data('bestsellers.csv')
    
    # Run all analyses
    explore_data(df)
    statistical_summary(df)
    genre_analysis(df)
    top_books_and_authors(df)
    year_analysis(df)
    price_analysis(df)
    rating_analysis(df)
    correlation_analysis(df)
    generate_insights(df)
    
    # Export summary
    export_summary(df)
    
    print("=" * 70)
    print("✨ ANALYSIS COMPLETE!")
    print("=" * 70)
    print()


if __name__ == "__main__":
    main()
