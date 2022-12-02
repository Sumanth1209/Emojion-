from django.shortcuts import render
import pandas as pd
import json
import plotly.express as px
from plotly.offline import plot
from user.models import emo
import user
import datetime
import seaborn as sns
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
from datetime import date
from datetime import datetime, date, timedelta
import plotly.graph_objects as go


emoji_df = pd.read_csv('/data_emoji.csv')

def ave(l1):
	sum =0
	for x in l1:
		sum = sum + x
	if len(l1)>0:
		return round(sum/len(l1),2)
	else:
		return 0 


def weekname(x):
    return x.weekday()

# Create your views here.

def data_extraction():
	qs = emo.objects.all()
	data1 = [
		{
			"uname" : x.uname,		
			"date": x.date,
			"time":x.time,
			"emotion":x.emotion,
			"EU":x.EU,
			"source":x.source
		} for x in qs
	]

	return pd.DataFrame(data1)

def timelist(x):
	time =[]
	for i in range(x):
		my_str = '09-24-2021'
		date_1 = datetime.strptime(my_str, '%m-%d-%Y')
		result_1 = date_1 + timedelta(days=i)
		time.append(result_1)
	return time

def forecast1(x):
	time = timelist(x.size)
	x1 = pd.DataFrame({"score":x,"time":time})
	x1['time']=pd.to_datetime(x1['time'])
	x1 = x1.set_index('time')
	model = ARIMA(x1,order=(2,1,2))
	model_fit = model.fit()
	forecast = model_fit.forecast()[0]
	return round(float(forecast),2)

def dash(request):

	df1 =data_extraction()

	df1['WeekDay']=df1['date'].apply(weekname)
	df1['date'] = df1['date'].astype(str)
	df1['time'] = df1['time'].astype(str)
	
	df2 = df1
	df2['date_time'] = df2['date'] + " " + df2['time']
	df2['date_time'] = pd.to_datetime(df2['date_time'], format="%Y-%m-%d %H:%M:%S")
	df3 =pd.merge(df2,emoji_df,how='inner', left_on = 'EU' , right_on='unicode')
	df3 = df3.sort_values(by=['date_time'])
	df4 = df3[df3['uname']==str(request.user.username)]
	
	
	weekDays = {0:"Monday",1:"Tuesday",2:"Wednesday",3:"Thursday",4:"Friday",5:"Saturday",6:"Sunday"}
	
	df4['WeekDay']=df4['WeekDay'].replace(weekDays)
	df4['emotion'] = df4['emotion'].replace({0:'Joy',2:'Sadness',3:'Suprise',1:'Fear',5:'Angry',4:'Disgust'})
	df4['source']=df4['source'].replace({0:'Internal',1:'External'})

	json_records = df4[['date','time','WeekDay','emotion','source','anger', 'anticipation', 'disgust', 'fear', 'joy', 'sadness',
       'surprise', 'trust']].reset_index().to_json(orient ='records')
	data = json.loads(json_records)
	
	df_user = df4
	
	#postive 

	df_pos = df_user[["date_time","anticipation","joy","surprise","trust"]]
	fig_postive = plot(px.line(df_pos, x ="date_time", y=df_pos.columns,markers=True, line_shape="spline"),output_type="div")
	
	#negitive 
	df_neg = df_user[['date_time','anger','disgust', 'sadness','fear']]
	fig_neg = plot(px.line(df_neg, x ="date_time", y=df_neg.columns,markers=True,line_shape="spline"),output_type="div")

	#pie_emotions
	pie_emo= plot(px.pie(df_user, names = 'emotion',hole=.3),output_type="div")
	pie_so = plot(px.pie(df_user, names = 'source',hole=.3),output_type="div")

	fig_sad = plot(px.line(df_user, x ="date_time", y="sadness"),output_type="div")
	fig_surprise = plot(px.line(df_user, x ="date_time", y="surprise"),output_type="div")
	fig_fear = plot(px.line(df_user, x ="date_time", y="fear"),output_type="div")
	fig_angry = plot(px.line(df_user, x ="date_time", y="anger"),output_type="div")
	fig_disgust = plot(px.line(df_user, x ="date_time", y="disgust"),output_type="div")
	df = pd.crosstab(df4['emotion'], df4['WeekDay'])
	dff = pd.crosstab(df4['emotion'], df4['source'])
	heatplot1 = plot(px.imshow(df,text_auto=True,color_continuous_scale='greens'),output_type ="div")
	heatplot2 = plot(px.imshow(dff,text_auto=True,color_continuous_scale='blues'),output_type ="div")

	
	if df_user.shape[0] >15:
		joy = df_user['joy']
		sad = df_user['sadness']
		fear = df_user['fear']
		angry = df_user['anger']
		
		ave_joy = forecast1(joy)
		ave_sad = forecast1(sad)
		ave_fear = forecast1(fear)
		ave_ang = forecast1(angry)

	else:
		ave_joy = ave(df_user['joy'])
		ave_sad = ave(df_user['sadness'])
		ave_fear = ave(df_user['fear'])
		ave_ang = ave(df_user['anger'])



	context = {'d': data, 'p_pos':fig_postive,
			'p_neg':fig_neg,'p_pie_emo':pie_emo,'p_pie_so':pie_so,'heatmap1':heatplot1,'heatmap2':heatplot2,
			'p_angry':fig_angry,'p_disgust':fig_disgust,
			'ave_happy':ave_joy,'ave_sad':ave_sad,'ave_fear':ave_fear,'ave_ang':ave_ang
			}

	return render(request,'index1.html',context)


def table1(request):
	return render(request,'table.html')

def charts(request):
	return render(request,'charts.html')

def print1(request):
	return print(df)


