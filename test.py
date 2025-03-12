from flask import Flask, render_template
import webbrowser
from threading import Timer
import os

# 현재 파일의 디렉토리 경로를 가져옵니다.
base_dir = os.path.abspath(os.path.dirname(__file__))

# Flask 애플리케이션 생성 시, templates 폴더 경로를 명시적으로 지정합니다.
app = Flask(__name__, template_folder=os.path.join(base_dir, 'templates'))

# HTML 템플릿 문자열
HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8"/>
    <title>실시간 GPS 위치 추적</title>
    <!-- Kakao Maps API 스크립트: JavaScript 키 사용 -->
    <script type="text/javascript" src="5aefe0539358793ca2935a52f01e03db03"></script>
</head>
<body>
    <div id="map" style="width:100%;height:400px;"></div>

    <script>
        let map;
        let marker;
        let watchId;

        function initMap() {
            const container = document.getElementById('map');
            const options = {
                center: new kakao.maps.LatLng(37.566826, 126.978656),
                level: 3
            };
            map = new kakao.maps.Map(container, options);
            
            marker = new kakao.maps.Marker({
                map: map,
                position: map.getCenter()
            });

            startTracking();
        }

        function startTracking() {
            if ("geolocation" in navigator) {
                const options = {
                    enableHighAccuracy: true,
                    timeout: 5000,
                    maximumAge: 0
                };

                watchId = navigator.geolocation.watchPosition(
                    updatePosition,
                    handleError,
                    options
                );
            } else {
                alert("이 브라우저에서는 위치 추적을 지원하지 않습니다.");
            }
        }

        function updatePosition(position) {
            const lat = position.coords.latitude;
            const lng = position.coords.longitude;
            const newPosition = new kakao.maps.LatLng(lat, lng);

            marker.setPosition(newPosition);
            map.setCenter(newPosition);
        }

        function handleError(error) {
            let message;
            switch(error.code) {
                case error.PERMISSION_DENIED:
                    message = "위치 정보 접근 권한이 거부되었습니다.";
                    break;
                case error.POSITION_UNAVAILABLE:
                    message = "위치 정보를 사용할 수 없습니다.";
                    break;
                case error.TIMEOUT:
                    message = "위치 정보 요청 시간이 초과되었습니다.";
                    break;
                default:
                    message = "알 수 없는 오류가 발생했습니다.";
                    break;
            }
            alert(message);
        }

        window.onload = initMap;
    </script>
</body>
</html>
"""

# templates 폴더 경로
templates_dir = os.path.join(base_dir, 'templates')

# templates 폴더가 없으면 생성
if not os.path.exists(templates_dir):
    os.makedirs(templates_dir)

# templates 폴더 내에 map.html 파일 생성
with open(os.path.join(templates_dir, 'map.html'), 'w', encoding='utf-8') as f:
    f.write(HTML_TEMPLATE)

@app.route('/')
def map_page():
    return render_template('map.html')

def open_browser():
    webbrowser.open_new('http://127.0.0.1:8080/')

if __name__ == '__main__':
    # 1초 후 브라우저를 여는 타이머 실행
    Timer(1.0, open_browser).start()
    # Flask 앱을 포트 8000에서 실행
    app.run(debug=True, port=8080)
