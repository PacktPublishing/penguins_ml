import streamlit as st
st.title('Penguin Classifier')
st.write("This app uses 6 inputs to predict the species of penguin using "
         "a model built on the Palmer's Penguin's dataset. Use the form below"
         " to get started!")
 
password_guess = st.text_input('What is the Password?')
if password_guess != st.secrets["password"]:
  st.stop()
 
penguin_file = st.file_uploader('Upload your own penguin data')

<<<<<<< HEAD
=======
st.write("This app uses 6 inputs to predict the species of penguin using " 

         "a model built on the Palmer's Penguin's dataset. Use the form below" 

         " to get started!") 


password_guess = st.text_input('What is the Password?') 

if password_guess != 'streamlit_is_great': 
  st.stop() 

penguin_file = st.file_uploader('Upload your own penguin data') 

penguin_df = pd.read_csv('penguins.csv')
rf_pickle = open('random_forest_penguin.pickle', 'rb')
map_pickle = open('output_penguin.pickle', 'rb')
rfc = pickle.load(rf_pickle)
unique_penguin_mapping = pickle.load(map_pickle)
rf_pickle.close()
map_pickle.close()

>>>>>>> 28cb14d8043a559bccd0e510ef9f24262e743c9f
