# Used Car Price Prediction

## Project objective
Predict the estimated selling price of a used car using supervised machine learning and the supplied Cardekho Kaggle dataset.

## Dataset
- File: `cardekho.csv`
- Original shape: 8128 rows × 12 columns
- Target: `selling_price` (Indian rupees)
- Exact duplicate rows removed before training: 1202
- Features used: car age, kilometres driven, fuel, seller type, transmission, owner history, mileage, engine capacity, maximum power, seats and an approximate brand extracted from the first word of the car name.

## Mentor-required workflow
1. Dataset loading and understanding (`head`, `tail`, `shape`, `info`, `describe`)
2. EDA: missing values, duplicates, target distribution, univariate/bivariate analysis, correlations and outlier inspection
3. Data cleaning and missing-value imputation
4. Feature engineering: `car_age = 2026 - year`; approximate brand extracted from `name`
5. Feature selection with rationale
6. 80/20 train/test split (random state 42)
7. Linear Regression model
8. Evaluation using MAE, MSE, RMSE and R²
9. Prediction on unseen test rows and new user input
10. Optional Streamlit frontend included

## Evaluation
See `outputs/evaluation_summary.json` and `outputs/model_comparison.csv` for measured results from this dataset. Linear Regression is the required primary model. Random Forest is included only as a comparison model.

## Run locally
Install packages:
```bash
pip install -r requirements.txt
```
Launch notebook:
```bash
jupyter notebook Used_Car_Price_Prediction.ipynb
```
Launch app from the project folder:
```bash
streamlit run app.py
```

## Important notes
- Missing numerical values are imputed with the training-set median and missing categorical values with the training-set most frequent category inside the pipeline.
- Categorical columns are one-hot encoded. Unseen categories are handled without crashing.
- The year reference for car age is fixed at 2026 to keep notebook and app consistent. Update it consistently if the project is reused in a later year.
- Outliers are visualized and discussed; they are not automatically deleted because expensive vehicles may be genuine observations.
- The extracted brand is approximate: the first token in a car name is used, so some multi-word brand names may be imperfectly represented.
- Predictions are estimates for academic demonstration, not guaranteed real-world market prices.
