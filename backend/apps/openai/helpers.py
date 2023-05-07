import os
import openai
import numpy as np
from datetime import datetime

class OpenAIHelpers:
    def __init__(self) -> None:
        self.openai = None
        self.openai_authenticate()
        self.min_prob = float(os.getenv("MIN_PROB")) if os.getenv("MIN_PROB") else 80.0

    def openai_authenticate(self):
        openai.organization = os.getenv("OPENAI_ORGANIZATION_ID")
        openai.api_key = os.getenv("OPENAI_API_KEY")
        self.openai = openai

    def get_models(self):
        models = self.openai.Model.list()
        return models
    
    def match_datas(self, datas:list = []):
        result = dict()
        execution_index_list = list()
        enumerate_datas = enumerate(datas)
        for i, d in enumerate_datas:
            code_time = str((datetime.now()).timestamp())
            execution_index_list.append(i)
            result_matching = list()
            for mi, md in enumerate_datas:
                if mi not in execution_index_list:
                    result_matching.append(np.dot(d['embedding'], md['embedding']))
            result[code_time] = result_matching
        
        return result


    
    def test_merge_ticket(self):
        res = self.openai.Embedding.create(
            input=self.test_data(),
            model="text-similarity-davinci-001"
        )
        
        embeddings = list()
        for res_data in res['data']:
            embedding = res_data['embedding']
            embeddings.append(embedding)

        e1 = res['data'][0]['embedding']
        e2 = res['data'][1]['embedding']
        e3 = res['data'][2]['embedding']
        e4 = res['data'][3]['embedding']
        e5 = res['data'][4]['embedding']

        print("1")
        print(np.dot(e1, e2))
        print(np.dot(e1, e3))
        print(np.dot(e1, e4))
        print(np.dot(e1, e5))

        print("2")
        print(np.dot(e2, e3))
        print(np.dot(e2, e4))
        print(np.dot(e2, e5))

        print("3")
        print(np.dot(e3, e4))
        print(np.dot(e3, e5))

        print("4")
        print(np.dot(e4, e5))

        # for e in embeddings:


    def test_data(self):
        datas = [
            "saya tidak bisa membuka file",
            "button untuk open file tidak bisa di klik",
            "saya tidak bisa menjalankan script saya",
            "lisensi saya sudah habis, bagaimana cara memperpanjangnya",
            "bagaimana cara membuat project baru"
        ]
        return datas