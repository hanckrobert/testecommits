import sys
sys.path.append("../../")
import pickle
import os.path
import os
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import pandas as pd
from pymongo import MongoClient
import json
from core.data_access.utils_mongo import *
from datetime import datetime
from totalvoice.cliente import Cliente
import pathlib
from core.utils.export_relatorio import resultado_por_email
from datetime import datetime

# If modifying these scopes, delete the file token.pickle.
# SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

# # The ID and range of a sample spreadsheet.
# SAMPLE_SPREADSHEET_ID = '1PpWIrT9P8L3cdGpSF7YyG9pbulInsuUtxnzUg0lpkd0'
# SMS_TAB_VIA_VAREJO = 'Via Varejo (SMS de Rastreio)'
# #MONGO_COLLECTION_OUTPUT =  'b2w_cancelamento'



# now = datetime.now().strftime(format='%d-%m-%Y')
# f = open("finalizado.txt", "w")
# file_path = os.path.join(pathlib.Path().absolute(), 'relatorio_SMS'+now+'.xlsx')
# print(file_path)
# df_csv = pd.DataFrame(experiences)
# df_csv.to_excel(file_path , index=False)
# emails = ['robert.hanck@elogroup.com.br', 'vicente.lotufo@elogroup.com.br', 'alberto.bravo@olist.com', 'francisco.fontoura@elogroup.com.br']
# resultado_por_email(emails, filename=file_path, subject="relatorio diario sms via varejo")
def main():    
    now = datetime.now().strftime(format='%d-%m-%Y')
    file_path = os.path.join(pathlib.Path().absolute(), 'relatorio_Cancelamento_magalu'+now+'.xlsx')
    print(file_path)
    sms_db = connect(MONGO_DATABASE, 'magalu_cancelamento')
    sms = pd.DataFrame(sms_db.find({'status_processamento':'ERRO - Nome Divergente'}))
    sms.to_excel(file_path , index=False)
    emails = ['robert.hanck@elogroup.com.br']
    resultado_por_email(emails, filename=file_path, subject="relatorio Cancelamento")

if __name__ == '__main__':
    main()

    