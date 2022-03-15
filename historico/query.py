db = connect(MONGO_DATABASE, 'send_message')
myquery = {"marketplace":"magalu", "status_processamento":"ERRO - ao processar o pedido"}
newvalues = { "$inc": { "repeticoes": 1} } 
db.update_many(myquery, newvalues)

myquery = {"marketplace":"magalu", "status_processamento":"ERRO - ao processar o pedido","repeticoes":{"$lt":4}}
newvalues = { "$set": { "status_processamento": "novo" } }
db.update_many(myquery, newvalues)
