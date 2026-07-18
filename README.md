# Namgang Landscape System Project(NLSP)

남강조경의 업무 관리 시스템을 개발하기 위한 프로젝트입니다.

## Current Scope

현재 저장소에서는 Python 기반 애플리케이션을 우선 개발하고 있습니다.

## Planned Components

- Python application
- SQLite database design
- Obsidian-based ERP structure
- Business document automation


# Person Registration Flow

## 프로그램 시작

1. `main()` 함수를 실행한다.
2. 데이터베이스 연결을 준비한다.
3. 필요한 데이터베이스 테이블을 생성한다.

   * 성별 테이블
   * 사람 테이블
4. 사람 정보를 입력할 방법을 선택한다.

## 입력 방법 선택

### 1. 직접 입력

1. 사용자에게 이름을 입력받는다.
2. 사용자에게 전화번호를 입력받는다.
3. 사용자에게 성별을 선택받는다.
4. 사용자에게 주소를 입력받는다.
5. 입력값을 정규화한다.
6. 정규화된 값을 검증한다.
7. `PersonCreate` 객체를 생성한다.
8. 사람 등록 서비스를 호출한다.
9. 저장소를 통해 데이터베이스에 저장한다.
10. 등록 결과를 출력한다.

### 2. CSV 파일 입력

1. CSV 파일 경로를 입력받거나 선택한다.
2. CSV 파일을 읽는다.
3. 각 행의 사람 정보를 가져온다.
4. 각 입력값을 정규화한다.
5. 정규화된 값을 검증한다.
6. `PersonCreate` 객체를 생성한다.
7. 사람 등록 서비스를 호출한다.
8. 저장소를 통해 데이터베이스에 저장한다.
9. 성공 및 실패 결과를 정리한다.

## 사람 정보 처리 흐름

```text
원본 입력값
    ↓
정규화
    ↓
검증
    ↓
PersonCreate 생성
    ↓
등록 서비스
    ↓
저장소
    ↓
SQLite 데이터베이스
```

## 각 구성요소의 역할

* `main.py`

  * 프로그램 실행 시작
  * 메뉴 출력
  * 입력 방법 분기

* `input_person.py`

  * 사용자 직접 입력 처리

* `person_csv_importer.py`

  * CSV 파일 읽기
  * 행 단위 데이터 추출

* `normalizer_person.py`

  * 이름, 전화번호, 주소 등의 입력값 형식 통일

* `validator_person.py`

  * 정규화된 값이 규칙에 맞는지 검사

* `person_import_service.py`

  * 입력 데이터를 사람 등록 절차로 연결
  * 정규화, 검증, 객체 생성, 저장 과정 조정

* `person_repository.py`

  * 사람 데이터를 SQLite에 저장
  * 사람 조회 및 데이터베이스 작업 처리

* `models/person.py`

  * `PersonCreate`
  * `Person`
  * 사람 데이터 구조 정의
