# Final predictor

The final predictor is located in Codes folder under the name Predictor_PSSM.py. It does the following:

- Takes in an example sequence (example_sequence.txt, located in Datasets folder)

- Retrieves its PSSM profile from Codes/Proteins/PSSM_prediction/

- Uses a model to predict the feature (Model_PSSM.sav in Codes folder)


#
Another predictor which does not use PSSM information can be found in Codes folder under the name Predictor.py. It takes in the same example sequence but uses Model.sav to predict the feature.
