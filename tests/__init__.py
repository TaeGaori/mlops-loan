'''
tests/test_api.py
-------------------
대출 심사 예측-API 테스트 코드

실행 방법 - 프로젝트 루트(mlops-loan/)에서 실행한다.
핵심 전략 - 학습된 모델 파일(.pkl)이 없어도 예측결과를 우리가 원하는 값으로 고정하고 테스트

단계
1. 준비 (헬퍼 함수 + fixture)
2. 단위 테스트 - LoanModel 클래스 (가장 작은 단위)
3. 통합 테스트 - GET / , /health
4. 통합 테스트 - POST /predict
5. 통합 테스트 - POST /predict/batch
6. 통합 테스트 - GET /model/info
'''
import uuid
from datetime import datetime, timedelta
from unitest.mock import MagicMock
import numpy as np
import pytest
from fastapi.testclient import TestClient

# tests 폴더를 "패키지"로 인식시키기 위한 파일
# 내용은 비워있어도 괜찮다.
# 이 팔일이 있으면 pytest가 프로젝트 루트를 import 경로에 자동으로 추가해줘서 test_api.pi안의
# from app.main import app 이 잘 동작하게 된다.