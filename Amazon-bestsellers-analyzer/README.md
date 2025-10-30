# Amazon Bestsellers Data Analysis with Pandas

A comprehensive data analysis project examining Amazon's bestselling books from 2009-2019 using Python and Pandas.

## Project Overview

This project analyzes a dataset of Amazon bestselling books spanning 11 years (2009-2019). The analysis explores various aspects including:

- **Genre Distribution**: Fiction vs Non-Fiction trends
- **Price Analysis**: Pricing patterns and trends over time
- **Rating Analysis**: User rating distributions and correlations
- **Author Insights**: Most prolific and popular authors
- **Temporal Trends**: Year-by-year changes in the book market

## Dataset

**File**: `bestsellers.csv`

**Structure**:
- **Name**: Book title
- **Author**: Book author
- **User Rating**: Average rating (0-5 scale)
- **Reviews**: Number of user reviews
- **Price**: Book price in USD
- **Year**: Year of bestseller listing (2009-2019)
- **Genre**: Fiction or Non Fiction

**Size**: 550 entries (books)

## Getting Started

### Prerequisites

- Python 3.7 or higher
- pip package manager

### Installation

1. **Clone the repository**:
```bash
git clone https://github.com/yourusername/amazon-bestsellers-analysis.git
cd amazon-bestsellers-analysis
```

2. **Install dependencies**:
```bash
pip install -r requirements.txt
```

3. **Ensure the dataset is in the project directory**:
```
amazon-bestsellers-analysis/
├── bestsellers.csv         # Your dataset
├── analyze_bestsellers.py  # Main analysis script
├── requirements.txt        # Dependencies
└── README.md              # This file
```

### Running the Analysis

Execute the main script:

```bash
python analyze_bestsellers.py
```

The script will:
1. Load the data
2. Perform comprehensive analysis
3. Display results in the terminal
4. Generate a summary file (`analysis_summary.txt`)

##  Analysis Features

### 1. Data Exploration
- Dataset dimensions and structure
- Data types and missing values
- Duplicate detection

### 2. Statistical Summary
- Descriptive statistics for all numerical columns
- Mean, median, min, max, and standard deviation
- Price, rating, and review statistics

### 3. Genre Analysis
- Distribution of Fiction vs Non-Fiction
- Average prices by genre
- Average ratings by genre
- Review counts by genre

### 4. Top Books and Authors
- Most reviewed books
- Highest-rated books
- Most prolific authors
- Most expensive books

### 5. Year-by-Year Analysis
- Books published per year
- Price trends over time
- Rating trends over time
- Genre distribution changes

### 6. Price Analysis
- Price range distributions
- Common price points
- Price by genre and year

### 7. Rating Analysis
- Rating distribution with visual bars
- Perfect 4.9-rated books
- Lowest-rated books

### 8. Correlation Analysis
- Relationships between variables
- Price vs ratings
- Reviews vs ratings
- Temporal correlations

### 9. Key Insights
- Automated insight generation
- Market trend identification
- Summary statistics

## Sample Output

```
 AMAZON BESTSELLERS DATA ANALYSIS (2009-2019)
======================================================================

 Loading Amazon Bestsellers Data...
 Successfully loaded 550 records

======================================================================
 DATA EXPLORATION
======================================================================

1️ Dataset Shape:
   Rows: 550
   Columns: 7

2️ Column Names and Types:
   Name           object
   Author         object
   User Rating    float64
   Reviews        int64
   Price          int64
   Year           int64
   Genre          object

...
```


##  Technologies Used

- **Python 3.x**: Core programming language
- **Pandas**: Data manipulation and analysis
- **NumPy**: Numerical computations
- **Built-in libraries**: datetime, warnings

##  Key Findings

After running the analysis, you'll discover insights such as:

- The most popular genres over the decade
- Price trends in the book market
- Correlation between reviews and ratings
- Most successful authors and titles
- Changes in consumer preferences over time

##  Code Walkthrough

### Main Functions

1. **`load_data(filepath)`**: Loads CSV data into a Pandas DataFrame
2. **`explore_data(df)`**: Initial data exploration and validation
3. **`statistical_summary(df)`**: Generates comprehensive statistics
4. **`genre_analysis(df)`**: Analyzes books by genre
5. **`top_books_and_authors(df)`**: Identifies top performers
6. **`year_analysis(df)`**: Examines temporal trends
7. **`price_analysis(df)`**: Detailed price breakdown
8. **`rating_analysis(df)`**: Rating distribution analysis
9. **`correlation_analysis(df)`**: Variable correlations
10. **`generate_insights(df)`**: Automated insight generation
11. **`export_summary(df)`**: Exports findings to text file

### Analysis Flow

```python
df = load_data('bestsellers.csv')
    ↓
explore_data(df)
    ↓
statistical_summary(df)
    ↓
[Multiple Analysis Functions]
    ↓
export_summary(df)
```

##  Output Files

- **`analysis_summary.txt`**: Text file containing key findings and statistics

##  Contributing

Contributions are welcome! To contribute:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



## 📧 Contact

Soufiane Tarifit ~ Soufiane.tarifit@gmail.com

Project Link: [https://github.com/soufiane-1080302/amazon-bestsellers-analyzer](https://github.com/soufiane-1080302/amazon-bestsellers-analyzer)



##  Acknowledgments

- Dataset sourced from Kaggle's Amazon Bestsellers dataset
- Inspired by data analysis tutorials from Codedex.io
- Built as part of a portfolio project for data analysis skills demonstration

## References

- [Panda's Documentatie](https://pandas.pydata.org/docs/)
- [Python-gegevensanalyse](https://www.python.org/)
- [Best practices voor datavisualisatie](https://www.tableau.com/learn/articles/data-visualization)
- [Github Amazon Bestsellers-dataset source](https://github.com/codedex-io/projects/blob/main/projects/analyze-spreadsheet-data-with-pandas-chatgpt/amazon-best-sellers-analysis/bestsellers.csv)
- [License-project](https://choosealicense.com/)
