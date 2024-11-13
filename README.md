# Rank_Estimator
this is a python flask application to calculate and estimate the rank of the Konkour  
# Rank Estimation Project

## screenahots

### Main Interface
![main screenshot](https://github.com/salehmhosseini/Rank_Estimator/blob/main/screenshots/main.png)
Candidates can input their taraz to estimate their rank

### Results Page
![result screenshot](https://github.com/salehmhosseini/Rank_Estimator/blob/main/screenshots/result.png)
Display the estimated rank

## Project Overview

**Rank Estimation** is a tool designed to predict a student’s rank based on their academic performance metrics, such as school GPA score, national exam score, study group, and quota category. This project aids students in estimating their likely rank after receiving their GPA scores, which are typically available before the official rank results are announced. This timely prediction allows students to start planning their course selection in advance, making it a valuable resource for those preparing for their next academic steps.

The tool is currently live on Sahel Barati's website and can be accessed [here](https://sahelbaratii.com/takhmin-rotbeh/).

## Purpose

The **Rank Estimation** tool provides students with the opportunity to:
- Gain insights into their probable rank before the official results.
- Strategically plan for their subject selection and admission preferences.
- Use early prediction data to manage their expectations and set realistic goals.

## Key Features

- **Rank Prediction**: Predicts a student's rank using inputs like GPA score, exam score, study group, and quota.
- **Interactive Interface**: User-friendly design enabling students to easily enter and update their data.
- **Live Updating**: Annually updated to reflect the latest exam and admission policies, ensuring relevance and accuracy.

## Planned Enhancements

To improve accuracy, flexibility, and usability, the following updates are planned:

1. **UI/UX Improvements**: Enhance the appearance and layout of the front end for a more engaging user experience.
2. **Integration with Admission Probability Calculator**: Connect the rank estimation tool with an acceptance probability tool, giving students comprehensive insights into their admission chances.
3. **Algorithm Optimization**: Analyze and refine the algorithm for faster and more accurate predictions.
4. **Flexible Code Structure**: Make the code more modular and adaptable to accommodate annual updates with minimal rework.
5. **Rank Prediction by Subject Scores**: Add a feature for rank estimation based on individual subject scores and grades, providing a more detailed analysis for students.

> **Note**: This tool currently supports rank prediction for the **2023 (1403) Entrance Exam**. Each year, the tool’s algorithm will be updated to reflect any new policies or changes in admission criteria.

## Installation

To set up the project locally, follow these steps:

```bash
# Clone the repository
git clone https://github.com/salehmhosseini/Rank_Estimator.git

# Navigate to the project directory
cd Rank_Estimator 

# Run the application
python app.py
```
## Usage
Once the application is running, navigate to http://localhost:5000 (or the specified port) in your browser. Input your details for GPA score, exam score, study group, and quota to get an estimated rank.

## License
This project is licensed under the MIT License.
