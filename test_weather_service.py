from unittest.mock import patch, Mock
from pyowm import OWM

# 本来の関数
def fetch_weather(city):
    # 本来は外部APIを呼び出します（今回はモックを使うので実装不要）
    pass

# テスト用の関数
def test_fetch_weather():
    mock_response = ('曇り', 19.5)  # モックが返す値を設定
    
    with patch('__main__.fetch_weather', Mock(return_value=mock_response)):
        result = fetch_weather('福岡')
        
        # モックで設定した値が返っているか確認
        assert result == ('曇り', 19.5)
        print(f"モックで取得した天気: {result[0]}, 気温: {result[1]}℃")

# テストを実行
test_fetch_weather()

