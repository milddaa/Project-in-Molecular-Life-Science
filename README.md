# Final predictors

Two predictors have been built: one using single sequence information and one using PSSM.

# 1. Predictor using single sequence information

This predictor is located in Codes folder under the name Predictor.py. It does the following:

- Takes in an example sequence (example_sequence.txt, located in Datasets folder)

- Uses Model.sav in Codes folder to predict the feature

# 2. Predictor using PSSM

This predictor is also located in Codes folder, under the name Predictor_PSSM.py. It does the following:

- Takes in the same example sequence (example_sequence.txt, located in Datasets folder)

- Retrieves its PSSM profile from Codes/Proteins/PSSM_prediction/

- Uses Model_PSSM.sav in Codes folder to predict the feature
