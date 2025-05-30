# SpaceX Launch Data Analysis and Machine Learning

This project explores and analyzes historical SpaceX Falcon 9 launches using data from the official SpaceX API and supplementary Wikipedia data. 
It includes data wrangling, exploratory analysis, SQL querying, interactive maps, dashboards, and predictive modeling using machine learning.


## Summary

The objective of this capstone project was to:
- Collect and clean SpaceX launch data.
- Perform exploratory data analysis (EDA) using Python, SQL, and visual tools.
- Build interactive dashboards using Folium and Plotly Dash.
- Train classification models to predict launch success.
- Derive insights from model performance and geospatial analysis.

##  Data Sources

- **SpaceX REST API**: [https://api.spacexdata.com/v4/launches](https://api.spacexdata.com/v4/launches)
- **Wikipedia**: [List of Falcon 9 and Falcon Heavy launches](https://en.wikipedia.org/wiki/List_of_Falcon_9_and_Falcon_Heavy_launches)

##  Tools & Technologies

- Python (Pandas, NumPy, Matplotlib, Seaborn)
- SQL (via ipython-sql and SQLite)
- BeautifulSoup (for web scraping)
- Folium (for interactive maps)
- Plotly Dash (for dashboard app)
- Scikit-learn (for ML models)

## Key Results

- Launch site and booster version were key indicators of success.
- Folium maps showed geospatial distribution of launch sites and success outcomes.
- Logistic Regression achieved the highest classification accuracy (83.3%).
- Dashboards enabled site filtering, launch outcomes, and trend visualizations.

## Insights

- KSC LC-39A had high success rates.
- Higher payload mass didn't always reduce success likelihood.
- Interactive tools helped identify high-performing launch configurations.

## 📑 License

This project is for educational purposes (IBM Data Science Capstone). Data sources are publicly available from SpaceX and Wikipedia.

## Author

**Maneesh Ujji**  
Graduate Student, Cleveland State University  
[My Website](https://www.maneeshujji.com) | [LinkedIn](https://www.linkedin.com/in/maneesh-ujji/) | [Email](mailto:maneesh.ujji30@gmail.com)



