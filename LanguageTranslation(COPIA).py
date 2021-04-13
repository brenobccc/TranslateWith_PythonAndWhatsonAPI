#!/usr/bin/env python
# coding: utf-8

# # 1 Authenticate

# In[11]:


#get_ipython().system('pip install ibm_watson')


# In[12]:


apikey = ''#put your apikey here
url = '' #put the url here


# In[13]:


#import deps
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator


# In[14]:


#Setup Service
authenticator = IAMAuthenticator(apikey)
lt = LanguageTranslatorV3(version='2018-05-01',authenticator=authenticator)
lt.set_service_url(url)


# # 2. Translate

# In[15]:


translation = lt.translate(text='Hello World', model_id='en-de').get_result()


# In[16]:


print(translation)

