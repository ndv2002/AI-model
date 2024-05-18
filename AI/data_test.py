# chạy phần này để test
# Save model
import joblib
import os
# filename = 'D:\Study\doancn\FireNet\Codes\TrainedModels\Fire_data.sav'
# joblib.dump(rf, filename)
 
# some time later...
 
# load the model from disk
def run_data_model(arg):
    filename = os.path.join(os.getcwd(),'AI', 'data_model','Fire_data.sav')
    loaded_model = joblib.load(filename)
    # test with sample data
    ab=[20.79,47.72,1210,400,12927,19426,938.709,0]
    bc=[20.015	,56.67	,0	,400	,12345	,18651	,939.744	,0
    ]

    result = loaded_model.predict([arg])
    return(result)

# filename = os.path.join(os.getcwd(),'AI', 'data_model','Fire_data.sav')
# loaded_model = joblib.load(filename)
# # test with sample data
# ab=[20.79,47.72,1210,400,12927,19426,938.709,0]
# bc=[20.015	,56.67	,0	,400	,12345	,18651	,939.744	,0
# ]

# result = loaded_model.predict([bc]])
# print(result)