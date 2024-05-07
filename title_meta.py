import os
import openai
import json

openai.api_type = os.getenv("api_type")
openai.api_base = os.getenv("api_base")
openai.api_version = os.getenv("api_version")
openai.api_key = os.getenv("api_key")


persona='''
You are a SEO Expert and your client is  an IT organisation which deals in these core services : IT consulting, business process outsourcing, digital transformation, application development, artificial intelligence, cloud services, data analytics, quality assurance, and IT infrastructure services.
and catered to clients across all sectors.
'''



#########################  Title ######################

def title(topic,keywords):
    system = f'''{persona}\n
        Instruction : You have to strictly generate only one title.
        
        '''
    user_prompt_title = f'Write one descriptive title for the topic {topic} and optimize it for keywords {keywords} with character limit of 50-60 characters.'
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
    return r_title
    


######################### Meta #######################
def meta(topic,keyword):
    system = f'''{persona}\n
        Instructions: You have to strictly generate only one meta description.
        
        '''
    user_prompt_meta = f'Write one descriptive Meta Description for the topic {topic} and optimize it for keywords {keyword} with character limit of 150 -160 characters'
    response_meta = openai.ChatCompletion.create(
            engine="AIKillsSEO",
            messages=[
                {"role": "system", "content": system},
                {"role": "user", "content": user_prompt_meta}
            ],
            temperature=0.8,
            max_tokens=1000,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
            stop=None
        )
    r_meta=response_meta.choices[0].message['content'].strip()
    return r_meta
        
    



############################ Alt Text #################

def alt(topic,keywords):
    system = f'''{persona}'''
    user_prompt = f'''Generate 5 ideas only for images with ALT text that can be added on blog post for the topic : {topic} And optimize it for the keyword : {keywords} for SEO.
            Give output in dictionary with key name as Idea Number,Idea description and ALT text only. In total there will be only these three keys in dictionary.
             Example:
          {{
    "Idea1":{{
      "Idea Description":"",
  "ALT text":""
    }}
  }}
            
            '''
              
            
    response_alt = openai.ChatCompletion.create(
            engine="AIKillsSEO",
            messages=[
                {"role": "system", "content": system},
                {"role": "user", "content": user_prompt}
            ],
            temperature=0.8,
            max_tokens=6000,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
            stop=None
        )
    r_alt=response_alt.choices[0].message['content'].strip()
    return r_alt



################################# Checking user choice #########################################

def content_generation(r1,r2,r3,Topic, finalized_keyword, content_type):
    results = {}
    try:
        
        if 'Title' in content_type:
            results['Title'] = title(Topic,finalized_keyword) 
        
        if "Meta Description" in content_type:
            results["Meta Description"] = meta(Topic,finalized_keyword) 
                
        if "Image Prompt" in content_type:
            results["Image Prompt"] = alt(Topic,finalized_keyword)

        return results
    
    
    
####################################### If any function fails then saving the error as exception ################################   

    except Exception as exe:
        results["Error"]=str(exe)
        return results

