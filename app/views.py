from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from .forms import Form
from .models import AiAnalysisLog
import requests
import json
import pprint

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
    try:
        result = requests.post(url, data=json.dumps(img_path), headers=headers).json()
    except requests.exceptions.RequestException:
        # テスト用のレスポンス
        result = { 'success': False, 'message': 'Error:E50012'}
    return result

# DBに保存
def createRecord(result):
    estimated_data=result.get('estimated_data', {})
    ai_analysis_log = AiAnalysisLog(image_path=result.get('image_path')or None, \
        success=str(result.get('success'))or None,\
            message=result.get('message')or None, \
                returnclass=estimated_data.get('class')or None, \
                    confidence=estimated_data.get('confidence')or None, \
                        request_timestamp=result.get('request_timestamp')or None, \
                            response_timestamp=result.get('response_timestamp')or None)
    ai_analysis_log.save()

# フォーム機能
def form(request):
    img_path = request.POST['img_path']
    params = {
        'form': Form(),
        'result': ' '
    }
    
    result = req(img_path)
    createRecord(result)
    
    # リクエストの結果を分類
    if result['success']:
        result = 'image class is: ' + str(result['estimated_data']['class']) + '.'
    else:
        result = 'API request failed'

    # 結果を画面の変数に渡す
    params['result'] = result
    return render(request, 'app/index.html', params)