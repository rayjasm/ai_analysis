from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from .forms import Form
from .models import AiAnalysisLog
import requests
import json
import datetime

# 静的ファイルを読み込む
def index(request):
    params = {
        'form': Form(),
        'result': ' '
    }
    return render(request, 'app/index.html', params)

# APIにリクエスト送る
def req(img_path):
    url = "http://127.0.0.1:8010"
    img_path = {'image_path': img_path}
    headers = {'Content-Type': 'application/json'}
    # リクエスト時間取得
    now = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    try:
        result = requests.post(url, data=json.dumps(img_path), headers=headers).json()
        result['request_timestamp'] = now
    except requests.exceptions.RequestException:
        # テスト用のレスポンス
        result = { 'success': False, 'message': 'Error:E50012'}
        result['request_timestamp'] = now

    # レスポンス時間取得
    result['response_timestamp'] = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    return result

# DBに保存
def createRecord(result, img_path):
    estimated_data=result.get('estimated_data', {})
    
    ai_analysis_log = AiAnalysisLog(image_path=img_path, \
        success=str(result.get('success')),\
            message=result.get('message'), \
                returnclass=estimated_data.get('class')or None, \
                    confidence=estimated_data.get('confidence')or None, \
                        request_timestamp=result.get('request_timestamp'), \
                            response_timestamp=result.get('response_timestamp'))
    ai_analysis_log.save()

# フォーム機能
def form(request):
    img_path = request.POST['img_path']
    params = {
        'form': Form(),
        'result': ' '
    }
    
    result = req(img_path)
    createRecord(result, img_path)
    
    # リクエストの結果を分類
    if result['success']:
        result = 'image class is: ' + str(result['estimated_data']['class']) + '.'
    else:
        result = 'API request failed'

    # 結果を画面の変数に渡す
    params['result'] = result
    return render(request, 'app/index.html', params)