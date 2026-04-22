import os
from dotenv import load_dotenv
from langchain_upstage import ChatUpstage
from langchain_core.prompts import ChatPromptTemplate
from prompts.templates import PROMPTS

load_dotenv()

class ToneConverter:
    def __init__(self):
        self.llm = ChatUpstage(model="solar-pro2")

    async def convert(self, text: str, target_audience: str) -> str:
        system_prompt = PROMPTS.get(target_audience, PROMPTS["team"])
        prompt = ChatPromptTemplate.from_messages([
            ("system", system_prompt),
            ("human", "{text}")
        ])
        chain = prompt | self.llm
        response = await chain.ainvoke({"text": text})
        return response.content
