Iris Species Prediction App (Deployed with Streamlit)

This is a simple, interactive web app that predicts the species of an Iris flower based on user input for sepal and petal measurements. Built with **Scikit-learn**, **Streamlit**, and deployed on **Streamlit Cloud**.

### Live App
 [Click here to open the app](https://kshitisha-iris-streamlit-deployment-app-puaon5.streamlit.app/)

---

### Features

- Input sepal & petal measurements via sliders
- View real-time predictions using a trained **SVM classifier**
- See input summary and a bar chart of your data
- Fully deployed and interactive online

---

### Technologies Used

- Python
- Pandas, NumPy
- Scikit-learn
- Streamlit
- Joblib

---

###  Run Locally

```bash
git clone https://github.com/kshitisha/iris-streamlit-deployment.git
cd iris-streamlit-deployment
pip install -r requirements.txt
streamlit run streamlit_app.py
