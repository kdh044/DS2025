import serial
import pynmea2

# GPS 장치 설정
GPS_PORT = "/dev/ttyACM0"  # 확인된 GPS 포트
BAUD_RATE = 38400  # GPS 기본 통신 속도

def convert_nmea_to_decimal(nmea_value):
    """NMEA 좌표를 십진법(Decimal Degrees)으로 변환"""
    degrees = int(nmea_value) // 100
    minutes = nmea_value - (degrees * 100)
    return degrees + (minutes / 60)

def get_gps_location():
    try:
        print(f"🚀 GPS 장치 연결 시도: {GPS_PORT} ({BAUD_RATE} baud)")
        with serial.Serial(GPS_PORT, BAUD_RATE, timeout=3) as gps:
            print("✅ GPS 장치 연결 성공! 데이터를 읽기 시작합니다...")
            
            while True:
                line = gps.readline().decode('utf-8', errors='ignore').strip()
                
                # 디버깅: GPS 데이터가 들어오는지 확인
                if line:
                    print(f"📡 RAW 데이터: {line}")

                # GPGGA 또는 GNGGA 형식의 GPS 데이터 찾기
                if line.startswith("$GNGGA") or line.startswith("$GPGGA"):
                    try:
                        msg = pynmea2.parse(line)
                        latitude = convert_nmea_to_decimal(msg.latitude)
                        longitude = convert_nmea_to_decimal(msg.longitude)

                        print(f"📍 현재 위치 (십진법 좌표): 위도 {latitude:.6f}, 경도 {longitude:.6f}")
                        print(f"🌍 구글맵 링크: https://www.google.com/maps/place/{latitude},{longitude}")
                        print(f"📍 카카오맵 링크: https://map.kakao.com/link/map/{latitude},{longitude}")

                    except pynmea2.ParseError:
                        print("❌ GPS 데이터 파싱 오류!")
    except serial.SerialException as e:
        print(f"❌ GPS 장치를 찾을 수 없습니다: {e}")

if __name__ == "__main__":
    get_gps_location()
