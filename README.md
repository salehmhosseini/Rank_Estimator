# Rank Estimation Project

**Rank Estimation** is a Python Flask application developed to calculate and estimate the likely rank of a student in the Konkour (Iranian university entrance exam). By inputting their GPA scores, exam scores, study group, and quota, candidates can get an early estimate of their rank, helping them plan their next steps efficiently.

The project is live on [Sahel Barati's website](https://sahelbaratii.com/takhmin-rotbeh/).

## Table of Contents
- [Screenshots](#screenshots)
- [Project Overview](#project-overview)
- [Purpose](#purpose)
- [Key Features](#key-features)
- [Planned Enhancements](#planned-enhancements)
- [Installation](#installation)
- [Usage](#usage)
- [License](#license)

---

## Screenshots

### Main Interface
![main screenshot](https://github.com/salehmhosseini/Rank_Estimator/blob/main/screenshots/main.png)
The main interface allows candidates to input their **taraz** scores and relevant data to estimate their rank.

### Results Page
![result screenshot](https://github.com/salehmhosseini/Rank_Estimator/blob/main/screenshots/result.png)
The results page displays the estimated rank based on the inputted scores and other relevant details.

---

## Project Overview

The **Rank Estimation** project is designed to assist students by predicting their ranks based on available academic data, including:
- **School GPA**
- **National Exam Scores**
- **Study Group**
- **Quota Category**

As students often receive their **GPA and exam scores** before the official rank announcement, this tool allows them to estimate their rank promptly, aiding them in planning their subject preferences and future academic steps.

## Purpose

The **Rank Estimation** tool provides valuable assistance to students by allowing them to:
- Gain early insight into their probable rank.
- Make informed choices regarding subject selection and admission preferences.
- Set realistic goals and expectations based on their estimated rank.

## Key Features

- **Rank Prediction**: Estimates rank using inputs like GPA score, exam score, study group, and quota category.
- **User-Friendly Interface**: Provides an intuitive layout for easy data entry.
- **Annual Updates**: Adapts to the latest exam and admission policies to ensure continued accuracy.

## Planned Enhancements

To further improve the accuracy, flexibility, and utility of this tool, the following updates are planned:

1. **UI/UX Improvements**: Enhance the design and layout of the front end for a more polished user experience.
2. **Integration with Admission Probability Calculator**: Link the rank estimator with an admission probability tool, offering comprehensive insights into admission chances.
3. **Algorithm Optimization**: Refine the algorithm for faster performance and increased accuracy in rank prediction.
4. **Flexible Code Structure**: Modularize the code for easier annual updates and maintenance.
5. **Subject Score-Based Prediction**: Introduce a feature for predicting rank based on individual subject scores, allowing for a more detailed analysis.

> **Note**: This tool currently supports the **2023 (1403) Entrance Exam** and will be updated each year to reflect any new policies or criteria set for the entrance exam.

---

## Installation

To set up and run the project locally, follow these steps:

```bash
# Clone the repository
git clone https://github.com/salehmhosseini/Rank_Estimator.git

# Navigate to the project directory
cd Rank_Estimator 

# Run the application
python app.py

```
## Usage
After starting the application, open a browser and go to http://localhost:5000 (or the designated port). Input your GPA score, exam score, study group, and quota details to get your estimated rank.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.
