import paralleldots as pd
pd.set_api_key('zmGrZL6tjy19qBc4DVit439MYW5sT7lakOQt7QqKtTQ')
def ner(text):
    ner = pd.ner(text)
    return ner
def senti(text):
    sa = pd.sentiment(text)
    return sa
def abuse(text):
    ab = pd.abuse(text)
    return ab
