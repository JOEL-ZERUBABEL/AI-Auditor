from groq import Groq
import os
from dotenv import load_dotenv
load_dotenv()

client=Groq(api_key=os.getenv('GROQ_API_KEY'))
from pydantic import BaseModel
import json
from typing import List




#CAREER
class CareerModel(BaseModel):
    courses:list[str]
    interest:list[str]

class Career:
        

    def analyzer(self,data:CareerModel):
        prompt=f'''
            You are a strict advisor to take decision regrading on that 
            specific person's future give analyze current market value ,
            Analayze:{data.courses} , and give better decision , Decision:{data.interest}'''
        
        completions=client.chat.completions.create(model='llama-3.3-70b-versatile',messages=[{"role":'system','content':'You are a Career advsior'},{
                                                              'role':'user',"content":prompt}])
        return completions.choices[0].message.content
    
    
#STARTUP
class StarupModel(BaseModel):
    startup_name:str    
    industry:str
    year:int
    budget:int
    team_size:int

class Starup:
    def advisor(self,data:StarupModel):
        prompt=f"""You are strict advisor give decision based on providing industry related 
        Startup name:{data.startup_name},
        Checking status of Current industry level , Industry level:{data.industry},
        Consider year:{data.year},
        budget:{data.budget}
        team size:{data.team_size},"""

        completions=client.chat.completions.create(model='llama-3.3-70b-versatile',messages=[{"role":'system','content':'you are strict officer'},
                {'role':'user','content':prompt}])
        return completions.choices[0].message.content
    
class CEOAGENT(BaseModel):
    score:int
    response:str
    rating_percentage:int
    next_steps:list[str]
    timeline:list


class CEO:
    def Ceoo(self,report):
        prompt=f"""You are CEO reviewing the advisor report . Advisor Report:{report}     
                Return only in  Valid JSON.
                
                Do not add explanations.
                Do not add markdown.
                Do not add text before JSON.
                Do not add text after JSON.
                Schema:
                {{
                "score": 0,
                "response": "",
                "rating_percentage": 0,
                "next_steps": [""],
                "timeline": [""]
                }}"""

                
        
        
        completions=client.chat.completions.create(model='llama-3.3-70b-versatile',response_format={'type':'json_object'},messages=[{"role":'system','content':'you are strict CEO'},
                                                    {'role':'user','content':prompt}])
        return completions.choices[0].message.content
    

class RISKAGENT(BaseModel):
    risk_score:int
    competitions:list[str]
    risks:list[str]

class Risk:
    def Risk(self,report):
        prompt=f""" Analyze risk. return as Report:
                {report} return only in JSON formula,
                {{'risk_score':0,"competitons":[""],"risks":'risks'}}"""
        
        completions=client.chat.completions.create(model='llama-3.3-70b-versatile',messages=[{"role":'system','content':'you are strict Risk analyzer'},
                                                    {'role':'user','content':prompt}])
        return completions.choices[0].message.content
    
class FINALAGENT(BaseModel):
    decision:str
    confidence:int

class Final:
    def finalise(self,decision,data:FINALAGENT):
        prompt=f"""
                Generate decision decision{decision}
                return in JSON Format{{'decision':'decision','confidence','confidence'}}"""
        completions=client.chat.completions.create(model='llama-3.3-70b-versatile',messages=[{"role":'system','content':'you are strict Risk analyzer'},
                                                    {'role':'user','content':prompt}])
        return completions.choices[0].message.content
    
#INVESTMENT 
class INVESTMENT(BaseModel):
    asset_name:str
    investment_amount:float
    investment_duration:int
    risk_tolerance:str
    investment_goal: str

class INVESTANALYSER(BaseModel):
    pros:str
    growth_potential:str
    market_outlook:str
    recommendation:str

class Investment:
    def analyzer(self,data:INVESTMENT):
        prompt=f"""
        Imagine youself as investment agent and generate response
        Asset Name: {data.asset_name}
        Investment Amount: {data.investment_amount}
        Investment Duration: {data.investment_duration}
        Risk Tolerance: {data.risk_tolerance}
        Investment Goal: {data.investment_goal}

        return only in JSON {{'pros':"",'growth_potential':"","markket_outlook:"",
        "recommendation":""}}"""
            
        
        completions=client.chat.completions.create(model='llama-3.3-70b-versatile',messages=[
            {"role":'system','content':'You are an investment advisor'},{"role":'system','content':prompt}
        ])

        return completions.choices[0].message.content   
        '''return client.chat.completions.create(model='llama-3.3-70b-versatile',messages=[
            {"role":'system','content':prompt},{"role":'system','content':input}
        ]).choices[0].message.content   
    '''


class RISKANALYSTAGENT(BaseModel):
    risk_score:int
    market_risks:str
    economic_risks:str
    volatility:str

class RiskAnalyst:
    def analyzer(self,report):
        prompt=f"""
            Imagine youself as investment agent and generate response:{report} return only in JSON
            {{'risk_score','0',
             'market_risks','',
             'economic_risks','',
             'volatility',''}}"""
        
        completions=client.chat.completions.create(model='llama-3.3-70b-versatile',messages=[
            {"role":'system','content':'You are a strict risk analyst'},{"role":'system','content':prompt}
        ])

        return completions.choices[0].message.content   
        
   
'''class PORTFOLIOMANAGER_AGENT(BaseModel):
    allocation:float
    diversification_advice:str
    investment_strategy:str

class Portfolio:
    def analyzer(self,data:PORTFOLIOMANAGER_AGENT):
        prompt=f"""Now you are a Portfolio agent try to give your advise
        'allocation':{data.allocation},
        'diversification_advice',{data.diversification_advice},
        'investment_strategy:{data.investment_strategy}"""

        completions=client.chat.completions.create(model='llama-3.3-70b-versatile',messages=[
            {"role":'system','content':prompt},{"role":'system','content':input}
        ])

        return completions.choices[0].message.content  '''     
    
    
    

class VERDICTAGENT(BaseModel):   
    confidence_score:int
    reasoning:str

class Verdict:
    def analyzer(self,investmentreport,riskresport):
        prompt=f'''You are a Senior advisor by checking confidence score and reasoning give your commands
        Investmentreport:{investmentreport} Risk Report:{riskresport}
        return only in JSON
        {"confidence_score":""},
        {"reasoning":""}
        '''
    
        completions=client.chat.completions.create(model='llama-3.3-70b-versatile',messages=[
            {"role":'system','content':'you are a senior investment advsior'},{"role":'system','content':prompt}
        ])

        return completions.choices[0].message.content       
   
investment = Investment()
'''data = INVESTMENT(
    asset_name="NVIDIA",
    investment_amount=10000,
    investment_duration=5,
    risk_tolerance="Medium",
    investment_goal="Long Term Wealth"
)

report = investment.analyzer(data)

risk = RiskAnalyst()

risk_report = risk.analyzer(report)

verdict = Verdict()

final_report = verdict.analyzer(
    report,
    risk_report
)

print('FINAL REPORT',final_report)
print()
print('RISK REPORT',risk_report)
print()
print('report',report)'''


'''startup=Starup()
report=startup.advisor(data)
ceo=CEO()
result=ceo.CEO(report)
data=json.loads(result)
ceo_report = CEOAGENT(**data)
'''

