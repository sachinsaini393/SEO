import os
import openai
import json
openai.api_type = os.getenv("api_type")
openai.api_base = os.getenv("api_base")
openai.api_version = os.getenv("api_version")
openai.api_key = os.getenv("api_key")

####################################  Topic Generation #############################

def content_extraction(reference1,reference2,reference3):
    results={}
    try:
        
    
        system='''
        You are a SEO Expert and your client is  an IT organisation which deals in these core services : IT consulting, business process outsourcing, digital transformation, application development, artificial intelligence, cloud services, data analytics, quality assurance, and IT infrastructure services.
        and catered to clients across all sectors.
        '''

        user_prompt = f'Extract top 5 Topic from these three given articles/blog post for SEO : {reference1},{reference2},{reference3}. '
        response = openai.ChatCompletion.create(
            engine="AIKillsSEO",
            messages=[
                {"role": "system", "content": system},
                {"role": "user", "content": user_prompt}
            ],
            temperature=0.8,
            max_tokens=4000,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
            stop=None
        )
        results['Topic']=response.choices[0].message['content'].strip() 

        return results
 
####################################### If any function fails then saving the error as exception ################################   
    except Exception as ex:
        results['Error']=str(ex)
        return results
