import requests
import pandas as pd

class DadosRepositorios:

    def __init__(self, owner):
        self.owner = owner
        self.api_base_url = 'https://api.github.com'
        self.access_token = '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'
        self.headers = {'Authorization': 'Bearer ' + self.access_token,
                        'X-GitHub-Api-Version': '2022-11-28'}
        
    def lista_repositorios(self):
        repos_list = []

        for page_num in range(1, 20):
            try:
                url = f'{self.api_base_url}/users/{self.owner}/repos?page{page_num}'
                response = requests.get(url,headers=self.headers)
                repos_list.append(response.json())
            except:
                repos_list.append(None)

        return repos_list
    def nomes_repos(self, repos_list):
        repos_names=[]
        for page in repos_list:
            for repo in page:
                try:
                    repos_names.append(repo['name'])
                except:
                    pass
        
        return repos_names
    def nomes_linguagens(self, repos_list):
        repos_languages=[]
        for page in repos_list:
            for repo in page:
                try:
                    repos_languages.append(repo['language'])
                except:
                    pass
        
        return repos_languages
    
    def cria_df_linguagens(self):
        repositorios = self.lista_repositorios()
        nomes = self.nomes_repos(repositorios)
        linguagens = self.nomes_linguagens(repositorios)

        dados = pd.DataFrame()
        dados ['repository_name'] = nomes
        dados ['language'] = linguagens

        return dados
    

    


    