#!/usr/bin/env python
# coding: utf-8

# In[41]:


from flask import Flask
from flask import request, render_template

from keras.models import load_model


# In[42]:


app = Flask(__name__) #if you use something else, it won't be main. You use __name__ to cover all


# In[43]:


@app.route("/", methods = ["GET", "POST"])
def index():
    if request.method == "POST":
        NPTA = request.form.get("NPTA")
        TLTA = request.form.get("TLTA")
        WCTA = request.form.get("WCTA")
        print(NPTA, TLTA, WCTA)
        model = load_model("bankruptcy_model")
        pred = model.predict([[float(NPTA), float(TLTA), float(WCTA)]])
        print(pred)
        s = "The precicted bankruptcy score is " + str(pred)
        return(render_template("index.html", result = s))
    else:
        return(render_template("index.html", result = "Hello you dreaming is it pls key in something"))


# In[ ]:


if __name__ == "__main__":
    app.run()


# In[ ]:




