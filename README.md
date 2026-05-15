# ids-project
# Project Proposal  
## **Movie Recommender System using TMDB Dataset and Flask GUI**

### **Group Members**
- Azfar Abbasi (24K-2576)  
- M. Arham (24K-2529)  
- Ashhad (24K-2544)

---

## **Problem Statement**
With a vast number of movies available across platforms, users often find it difficult to choose what to watch. A movie recommender system helps users discover films aligned with their preferences by analyzing patterns within movie features and user interactions.

This project aims to build a content-based movie recommender system using the **TMDB dataset**, using movie metadata such as genres, keywords, cast, crew, popularity, and textual overview. The final system will be deployed using a **Flask-based GUI**.

---

## **Importance of the Problem**
Recommendation systems play an essential role in enhancing user experience and improving engagement on digital platforms.

This project will:
- Help users easily find movies matching their interests  
- Support streaming platforms by providing personalized recommendations  
- Demonstrate how data science and machine learning simplify decision-making in entertainment  

By leveraging data-driven techniques, this project contributes to building intelligent tools that improve user satisfaction.

---

## **Role of Data and Machine Learning**
Data science techniques will be used to:
- Clean and preprocess TMDB datasets  
- Merge movie and credits data  
- Extract meaningful features  
- Apply machine learning/NLP concepts such as **TF-IDF** and **cosine similarity**  

The Flask GUI will enable interactive exploration of recommendations.

---

## **Dataset Information**
**Dataset Name:** TMDB Movies Dataset  
**Source:** Kaggle  

The dataset contains two files:
- **movies.csv**  
- **credits.csv**

### **Important Features**

| Feature | Description |
|--------|-------------|
| budget | Production cost of the movie |
| genres | List of movie genres |
| homepage | Official movie website |
| id | Unique identifier for each movie |
| keywords | Thematic tags associated with the movie |
| original_language | Language in which the movie was originally produced |
| original_title | Official movie title |
| overview | Short plot summary |
| popularity | Popularity score |
| production_companies | Companies involved in production |
| movie_id | ID linking credits to movies |
| title | Movie title |
| cast | Main actors |
| crew | Crew members such as directors |

### **Target Variable**
There is no traditional target variable.  
Recommendations are generated using similarity measures in a content-based filtering approach.

---

## **Approach**

### **1. Data Collection & Cleaning**
- Load movies.csv and credits.csv  
- Handle missing values  
- Merge datasets using *id* and *movie_id*  
- Clean and preprocess text data  

### **2. Feature Engineering**
- Extract essential attributes:  
  genres, keywords, cast, crew, overview  
- Combine them into a **single metadata column**

### **3. Similarity Calculation**
- Use **TF-IDF** or **CountVectorizer**  
- Convert metadata into vectors  
- Compute **cosine similarity** to find similar movies  

### **4. Flask GUI Integration**
- Build a web interface using Flask  
- Allow users to enter a movie name  
- Display top recommended movies with details  

### **5. Visualization**
Use Matplotlib/Seaborn to visualize:
- Genre distribution  
- Language trends  
- Popularity patterns  

---

## **Expected Outcome**
By the end of this project, we aim to:

- Complete data preprocessing and feature engineering  
- Implement a full content-based recommender system  
- Create an interactive Flask GUI for movie recommendations  
- Demonstrate ML and data science application in entertainment personalization  
