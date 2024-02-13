import os
import openai
import json

openai.api_type = "azure"
openai.api_base = "https://seorevolution-gpt4.openai.azure.com/"
openai.api_version = "2023-03-15-preview"
openai.api_key = "2acafeb8501f41e2a7f3cf3c5854287a"

def content_generation(r1,r2,r3,Topic, finalized_keyword, content_type):
    results = {}
    try:
        
        
    #results=[]
    
        if 'Title' in content_type:
            system = '''
        You are a SEO Expert and your client is  an IT organisation which deals in these core services : IT consulting, business process outsourcing, digital transformation, application development, artificial intelligence, cloud services, data analytics, quality assurance, and IT infrastructure services.
        and catered to clients across all sectors.
        -----------------------------------------------
        Instruction : You have to strictly generate only one title.
        
        '''
            user_prompt_title = f'Write one descriptive title for the topic {Topic} and optimize it for keywords {finalized_keyword} with character limit of 50-60 characters.'
            response_title = openai.ChatCompletion.create(
            engine="AIKillsSEO",
            messages=[
                {"role": "system", "content": system},
                {"role": "user", "content": user_prompt_title}
            ],
            temperature=0.8,
            max_tokens=1000,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
            stop=None
        )
            r_title=response_title.choices[0].message['content'].strip()
            results['Title'] =r_title 
        #results.append(r_title)
        
        
        
        if "Meta Description" in content_type:
            system = '''
        You are a SEO Expert and your client is  an IT organisation which deals in these core services : IT consulting, business process outsourcing, digital transformation, application development, artificial intelligence, cloud services, data analytics, quality assurance, and IT infrastructure services.
        and catered to clients across all sectors.
        
        ---------------------------------------
        Instructions: You have to strictly generate only one meta description.
        
        '''
            user_prompt_meta = f'Write one descriptive Meta Description for the topic {Topic} and optimize it for keywords {finalized_keyword} with character limit of 150 -160 characters.'
            response_meta = openai.ChatCompletion.create(
            engine="AIKillsSEO",
            messages=[
                {"role": "system", "content": system},
                {"role": "user", "content": user_prompt_meta}
            ],
            temperature=0.8,
            max_tokens=5000,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
            stop=None
        )
            r_meta=response_meta.choices[0].message['content'].strip()
            results["Meta Description"] = r_meta
        #results.append(r_meta)
        
    
    
        if "Alt Text" in content_type:
            system = '''You are a SEO Expert and your client is  an IT organisation which deals in these core services : IT consulting, business process outsourcing, digital transformation, application development, artificial intelligence, cloud services, data analytics, quality assurance, and IT infrastructure services.
        and catered to clients across all sectors.
        '''
            user_prompt = f'''Generate 5 ideas only for images with ALT text that can be added on blog post for the topic : {Topic} And optimize it for the keyword : {finalized_keyword} for SEO.
            Give output in dictionary with key name as Idea , Idea Description and ALT text.
            
            '''
        #Give me a table with column names as Idea, Idea Description and ALT text.
              
            
            response_alt = openai.ChatCompletion.create(
            engine="AIKillsSEO",
            messages=[
                {"role": "system", "content": system},
                {"role": "user", "content": user_prompt}
            ],
            temperature=0.8,
            max_tokens=1000,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
            stop=None
        )
            r_alt=response_alt.choices[0].message['content'].strip()
            results["Alt Text"] = r_alt
        #results.append(r_alt)
        
    
    
    
    #return {results["Title"], results["Meta Description"], results["Alt Text"]}
    #final_results=json.dumps(results)
        return results
    
    except Exception as exe:
        results["Error"]=str(exe)
        return results

