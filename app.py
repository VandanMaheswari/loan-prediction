from flask import Flask,request,render_template,jsonify
from src.pipeline.prediction_pipeline import CustomData,PredictPipeline


application=Flask(__name__)

app=application



@app.route('/')
def home_page():
    return render_template('index.html')


@app.route('/predict',methods=['GET','POST'])

def predict_datapoint():
    
    if request.method=='GET':
        return render_template('form.html')
    
    # when we call predict_datapoint from form then it is get method and that time it call form.html and as we press submit it
    # goes in the else section and then intializing the all variables here
    
    else :
        
        data = CustomData(
            gender = request.form.get('gender'),    # we are converting them into float because bydafault it become string because of form
            married = request.form.get('married'),
            dependents = request.form.get('dependents'),
            education = request.form.get('education'),
            self_employed = request.form.get('self_employed'),
            applicantincome = float(request.form.get('applicantincome')),
            coapplicantincome = float(request.form.get('coapplicantincome')),
            loanamount= float(request.form.get('loanamount')),
            loan_amount_term= float(request.form.get('loan_amount_term')),
            credit_history= request.form.get('credit_history'),
            property_area= request.form.get('property_area'),
        )
        
        final_new_data=data.get_data_as_dataframe()
        predict_pipeline=PredictPipeline()
        pred=predict_pipeline.predict(final_new_data)
        
        # results=str(pred)
        # int(pred[0])
        
        # if int(pred[0]) == 1:
        if pred[0] == "Y":
            results = "Eligible For Loan"
            
        else:
            results = "Not Eligible For Loan"    
            
        
        
        return render_template('results.html',final_result=results)



if __name__=="__main__":
    # app.run(host='0.0.0.0',port=5001)
    app.run(host='0.0.0.0',debug=True,port=5001)
    # http://127.0.0.1:5001/
  