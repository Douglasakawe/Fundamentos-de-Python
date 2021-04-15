#!/usr/bin/env python
# coding: utf-8

# # <font color='Purple'>Python Fundamentos</font>
# 

# In[1]:


# Versão da Linguagem Python
from platform import python_version
print('Versão da Linguagem Python Usada Neste Jupyter Notebook:', python_version())


# ### Condicional If

# In[2]:


# Condicional If
if 5 > 2:
    print("Python funciona!")


# In[3]:


# Statement If...Else
if 5 < 2:
   print("Python funciona!")
else:
   print("Algo está errado!")


# In[4]:


6 > 3


# In[5]:


3 > 7


# In[6]:


4 < 8


# In[7]:


4 >= 4


# In[8]:


if 5 == 5:
  print("Testando Python!")


# In[10]:


if 5 = 5:


# In[9]:


if True:
    print('Parece que Python funciona!')


# In[11]:


# Atenção com a sintaxe
if 4 > 3
  print("Tudo funciona!")


# In[13]:


# Atenção com a sintaxe
if 4 > 3:
    print("Tudo funciona!")


# ### Condicionais Aninhados

# In[14]:


idade = 21
if idade > 17:
   print("Você pode dirigir!")


# In[15]:


Nome = "Leo"
if idade > 13:
 if Nome == "Leo":
   print("Ok Leo, você está autorizado a entrar!")
 else:
   print("Desculpe, mas você não pode entrar!")


# In[18]:


idade = 13
Nome = "Leo"
if idade >= 13 and Nome == "Leo":
    print("Ok Leo, você está autorizado a entrar!")


# In[19]:


idade = 12
Nome = "Robert"
if (idade >= 13) or (Nome == "Robert"):
    print("Ok Robert, você está autorizado a entrar!")


# ### Elif

# In[20]:


dia = "Terça"
if dia == "Segunda":
  print("Hoje fará sol!")
else:
  print("Hoje vai chover!")


# In[21]:


if dia == "Segunda":
  print("Hoje fará sol!")
elif dia == "Terça":
  print("Hoje vai chover!")
else:
  print("Sem previsão do tempo para o dia selecionado")


# ### Operadores Lógicos

# In[22]:


idade = 18
nome = "Bob"
if idade > 17:
   print("Você pode dirigir!")


# In[25]:


idade = 18
if idade > 17 and nome == "Bob":
   print("Autorizado!")


# In[26]:


# Usando mais de uma condição na cláusula if 

disciplina = input('Digite o nome da disciplina: ')
nota_final = input('Digite a nota final (entre 0 e 100): ')

if disciplina == 'Artes' and nota_final >= '70':
    print('Você foi aprovado!')
else:
    print('Lamento, acho que você precisa estudar mais!')


# In[30]:


# Usando mais de uma condição na cláusula if e introduzindo Placeholders

disciplina = input('Digite o nome da disciplina: ')
nota_final = input('Digite a nota final (entre 0 e 100): ')
semestre = input('Digite o semestre (1 a 6): ')

if disciplina == 'Artes' and nota_final >= '60' and int(semestre) != 1:
    print('Você foi aprovado em %s com média final %r!' %(disciplina, nota_final))
else:
    print('Lamento, acho que você precisa estudar mais!')

