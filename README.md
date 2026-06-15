# Sprint Analytics — 부트캠프 학습 성과 모니터링 시스템

부트캠프 수강생의 학습 몰입도를 실시간으로 파악하고,
중도 이탈을 사전에 예방하기 위한 데이터 분석 대시보드 MVP

---

## 프로젝트 구조
```
sprint-analytics/
├── app.py
├── requirements.txt
├── README.md
├── data/
│   └── online_learning_engagement_dropout_risk.csv
├── utils/
│   ├── init.py
│   ├── preprocess.py
│   └── kpi.py
└── pages/
├── 1_overview.py
├── 2_risk.py
└── 3_bottleneck.py
```
---

## 실행 방법

```bash
# 패키지 설치
pip install -r requirements.txt

# 앱 실행
streamlit run app.py
```

실행 후 브라우저에서 `http://localhost:8501` 접속

---

## KPI 정의

| 지표 | 설명 | 산출 방식 |
|------|------|-----------|
| **Engagement Score** | 학습 몰입도 점수 (0~100) | 세션 시간 정규화 × 0.4 + 진도율 × 0.6 |
| **Dropout Risk Index** | 이탈 위험 등급 | Low / Medium / High |
| **완주 예상률** | High 위험군 제외 비율 | (전체 - High) / 전체 × 100 |

---

## 데이터셋

- **출처**: Online Learning Engagement Dataset (Kaggle)
- **규모**: 2,800명 · 11개 컬럼

| 컬럼명 | 설명 |
|--------|------|
| `student_id` | 수강생 고유 ID |
| `course_category` | 강의 카테고리 (AI & ML, Data Science, Design, Programming, Business) |
| `login_frequency_per_week` | 주간 접속 횟수 |
| `avg_session_minutes` | 평균 세션 시간 (분) |
| `course_progress_percent` | 강의 진도율 (%) |
| `quiz_average_score` | 퀴즈 평균 점수 |
| `dropout_risk` | 이탈 위험 등급 (Low / Medium / High) |

---

## 주요 기능

### app.py — 메인 현황판
- 완주 예상률 · 평균 진도율 · 위험군 비율 · 평균 몰입도 KPI 4종

### 1_overview.py — 전체 현황판
- 이탈 위험 등급 Donut 차트
- 카테고리별 평균 진도율 Bar 차트
- 몰입도 점수 분포 Histogram

### 2_risk.py — 위험군 타겟팅
- 위험 등급 · 카테고리 필터 조합
- 몰입도 점수 오름차순 정렬 (즉각 개입 우선순위)

### 3_bottleneck.py — 학습 병목 구간 분석
- 카테고리별 High 위험군 비율 Bar 차트
- 퀴즈 점수 vs 위험군 비율 Scatter 차트
- 상위 3개 카테고리 커리큘럼 개선 제언 카드

---

## 기술 스택

| 구분 | 사용 기술 |
|------|-----------|
| 언어 | Python 3.10 |
| 대시보드 | Streamlit 1.35 |
| 데이터 처리 | Pandas 2.2, Numpy 1.26 |
| 시각화 | Plotly 5.22 |

---

## 포트폴리오 포인트

- **비즈니스 마인드**: 운영 프로세스 반영에 집중
- **바이브 코딩**: Streamlit 기반 MVP를 빠르게 프로토타이핑
- **협업 설계**: 대시보드 데이터를 공유하여 커리큘럼 난이도를 조정하는 운영 플로우 제언을 넣었음

<img width="816" height="738" alt="overview" src="https://github.com/user-attachments/assets/0c1bc35e-49bb-4da6-8bb8-1d5a2a76b831" />
