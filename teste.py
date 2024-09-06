#%%

dic = {
    'chave1': 'valor',
    'chave2': [1,2,3,4],
    'chave3': {'valor_chave': 'valor'},
    }
#len(dic)

# %%
for chave, valor in dic.items():
    print(f'{chave}: {valor}')
# %%
