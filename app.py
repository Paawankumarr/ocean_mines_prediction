#write s streamlit code ui for this prediction system
import streamlit as st
import numpy as np
import pickle

# Load the trained model
loaded_model = pickle.load(open('model.pkl', 'rb'))

# creating a function for prediction
def predict(input_data):
    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the np array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if prediction[0] == 'R':
        return 'The object is a Rock'
    else:
        return 'The object is a Mine'

def main():
    # giving a title
    st.title('Sonar Rock vs Mine Prediction App')

    # getting the input data from the user
    input_data = []
    st.write("Enter 60 numerical values separated by commas:")
    input_string = st.text_input("Input Values")
    if input_string:
        try:
            input_data = [float(x.strip()) for x in input_string.split(',')]
            if len(input_data) == 60:
                # code for prediction
                if st.button('Predict'):
                    prediction_result = predict(input_data)
                    st.success(prediction_result)
            else:
                st.error(f"Please enter exactly 60 numerical values. You entered {len(input_data)} values.")
        except ValueError:
            st.error("Invalid input. Please enter only numerical values.")


if __name__ == '__main__':
    main()