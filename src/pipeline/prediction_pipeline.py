import sys
import os
from src.exception import CustomException
from src.logger import logging
from src.utils import load_object
import pandas as pd





class PredictPipeline:
    
    def __init__(self):
        pass
    
    
    def predict(self,features):
        try:
                         
            pipeline=os.path.join(r"F:\study material\Data Science\modular coding assignment\loan prediction\src\pipeline\artifacts\LogisticRegressionModel.pkl")
      
            # we are giving path as os.path.join because this formate will run in both linux instead of doing /path/ this type
            
            
            pipe=load_object(pipeline)
            # consider it as a xtest data as we only tranform it
            
            
            pred=pipe.predict(features)
            return pred
        
        
        
        
        except Exception as e:
            logging.info("Exception occured in prediction")
            raise CustomException(e,sys)
        
        
        
class CustomData:
    
    def __init__(self,gender,married,dependents,education,self_employed,applicantincome,coapplicantincome,loanamount,loan_amount_term,credit_history,property_area):
        
        self.gender = gender
        self.married = married
        self.dependents = dependents
        self.education = education
        self.self_employed= self_employed
        self.applicantincome = applicantincome
        self.coapplicantincome = coapplicantincome
        self.loanamount = loanamount
        self.loan_amount_term = loan_amount_term  
        self.credit_history = credit_history
        self.property_area = property_area
        
        
        
        
        
    def get_data_as_dataframe(self):
        try :
            custom_data_input_dict = {
                'gender':[self.gender],
                'married':[self.married],
                'dependents':[self.dependents],
                'education':[self.education],
                'self_employed':[self.self_employed],
                'applicantincome':[self.applicantincome],
                'coapplicantincome':[self.coapplicantincome],
                'loanamount':[self.loanamount],
                'loan_amount_term':[self.loan_amount_term],
                'credit_history':[self.credit_history],
                'property_area':[self.property_area]
                
            }
        
            df = pd.DataFrame(custom_data_input_dict,index = [0])  
            logging.info('Dataframe Gathered')
            return df   
        
           
        except Exception as e:
            logging.info('Exception Occured in prediction pipeline')
            raise CustomException(e,sys)
            