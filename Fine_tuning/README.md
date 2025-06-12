# Fine-tuning Project

이 디렉토리는 **Qwen3-8B 모델**을 활용한 **M&A(인수합병) 분야 특화 파인튜닝** 프로젝트입니다. AI Hub 데이터셋과 자체 크롤링 데이터를 활용하여 금융, 법률, M&A 분야 전문 AI 모델을 구축합니다.

## 📁 프로젝트 구조

```
Fine_tuning/
├── README.md                           # 이 파일 (프로젝트 가이드)
└── notebook/                          # Jupyter 노트북 디렉토리
    ├── qwen3_finetune.ipynb           # Qwen3-8B 모델 파인튜닝 메인 노트북
    ├── ai_hub_data_preocessing.ipynb  # AI Hub 데이터셋 전처리 노트북
    └── assets/                        # 학습 결과 이미지
        ├── train.png                  # 학습 과정 시각화
        └── system.png                 # 시스템 구성도
```

## 🎯 프로젝트 목표

1. **도메인 특화 모델 구축**: M&A, 금융, 법률 분야 전문 지식 학습
2. **한국어 최적화**: 한국어 질의응답 성능 향상
3. **실용적 활용**: 실제 업무에 활용 가능한 수준의 모델 개발
4. **효율적 학습**: LoRA 기법을 통한 효율적인 파인튜닝

## 🔧 기술 스택

### 모델 & 프레임워크
- **Base Model**: Qwen3-8B (Alibaba Cloud)
- **Fine-tuning**: LoRA (Low-Rank Adaptation)
- **Framework**: Transformers, PEFT, TRL
- **Monitoring**: Weights & Biases (WandB)

### 데이터
- **AI Hub**: 한국어 질의응답 데이터셋
- **자체 데이터**: M&A 관련 크롤링 데이터
- **전처리**: 품질 필터링, 카테고리 분류

### 환경
- **Python**: 3.10.16
- **GPU**: CUDA 지원 환경
- **Storage**: 로컬 PC 기반 학습

## 📊 데이터셋 정보

### 1. AI Hub 데이터셋
- **출처**: [AI Hub 한국어 말뭉치 데이터](https://www.aihub.or.kr/aihubdata/data/view.do?currMenu=&topMenu=&aihubDataSe=data&dataSetSn=71748)
- **구성**: Training, Validation, Other 데이터
- **전처리**: 품질 점수 30점 이상 필터링 (9,605개 샘플)
- **카테고리**: 인문, 사회, 자연과학 등 (예체능, 종교, 보건 제외)

### 2. M&A 전용 데이터
- **형태**: JSON 형식의 질의응답 쌍
- **내용**: M&A 관련 전문 지식, 법률 정보, 절차 안내
- **특징**: 도메인 특화 고품질 데이터

### 3. 데이터 통합
- **총 샘플 수**: 약 14,000개 (AI Hub + M&A 데이터)
- **형식**: Question-Answer 쌍
- **언어**: 한국어 전용
- **품질 관리**: 중복 제거, 형식 통일

## 🚀 사용법

### 1. 환경 설정

```bash
# 필요 라이브러리 설치
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
pip install transformers datasets accelerate peft bitsandbytes trl wandb huggingface_hub
```

### 2. 데이터 전처리

```bash
# AI Hub 데이터 전처리 실행
jupyter notebook ai_hub_data_preocessing.ipynb
```

**주요 전처리 과정**:
- AI Hub 데이터셋 압축 해제 및 파싱
- 품질 점수 기반 필터링 (score > 30)
- 카테고리별 분류 및 불필요 카테고리 제거
- M&A 데이터와 통합
- 중복 데이터 제거

### 3. 모델 파인튜닝

```bash
# 파인튜닝 실행
jupyter notebook qwen3_finetune.ipynb
```

**주요 학습 과정**:
1. **데이터 로드**: 전처리된 QA 데이터셋 로드
2. **토크나이저 설정**: Qwen3 전용 토크나이저 구성
3. **모델 로드**: Qwen3-8B 베이스 모델 로드
4. **LoRA 설정**: 효율적 파인튜닝을 위한 LoRA 구성
5. **학습 실행**: SFTTrainer를 통한 지도 학습
6. **모델 저장**: 파인튜닝된 모델 저장

## ⚙️ 핵심 설정

### LoRA 구성
```python
config = LoraConfig(
    task_type=TaskType.CAUSAL_LM,
    target_modules=["q_proj", "k_proj", "v_proj", "o_proj", 
                   "gate_proj", "up_proj", "down_proj"],
    r=8,                    # LoRA rank
    lora_alpha=32,          # LoRA alpha
    lora_dropout=0.1,       # Dropout rate
    inference_mode=False    # Training mode
)
```

### 학습 파라미터
```python
training_args = TrainingArguments(
    output_dir="./models/Qwen3-8B-mna-Finetuned",
    num_train_epochs=3,
    per_device_train_batch_size=1,
    gradient_accumulation_steps=8,
    learning_rate=1e-4,
    max_grad_norm=0.3,
    warmup_ratio=0.03,
    lr_scheduler_type="linear"
)
```

### 프롬프트 템플릿
```
<|im_start|>system
당신은 금융,법률 및 M&A 분야 전문가입니다.
사용자 질문에 대해 반드시 한국어로만 답변하세요.
<|im_end|>
<|im_start|>user
{question}/no_think
<|im_end|>
<|im_start|>assistant
<think>

</think>

{answer}
<|im_end|>
```

## 📈 학습 모니터링

### WandB 통합
- **프로젝트명**: Qwen3-8B-M&A
- **실험명**: qlora_finetuning-qwen3-8B-mna
- **추적 지표**: Loss, Learning Rate, Gradient Norm

### 저장 전략
- **체크포인트**: 10 스텝마다 저장
- **로깅**: 10 스텝마다 로그 기록
- **최종 모델**: `./models/Qwen3-8B-mna-Finetuned`

## 🔍 모델 평가

### 테스트 함수
```python
def generate_answer(question):
    # 질문에 대한 답변 생성
    # 시스템 프롬프트와 사용자 질문을 템플릿에 적용
    # 모델 추론 실행
    return generated_answer
```

### 평가 기준
- **도메인 정확성**: M&A 관련 질문에 대한 정확한 답변
- **언어 품질**: 자연스러운 한국어 생성
- **일관성**: 동일한 질문에 대한 일관된 답변
- **전문성**: 금융, 법률 용어의 적절한 사용

## 💡 주요 특징

### 1. 도메인 특화
- M&A, 금융, 법률 분야 전문 지식 학습
- 업계 용어와 개념에 대한 정확한 이해
- 실무진이 활용 가능한 수준의 답변 품질

### 2. 한국어 최적화
- 한국어 질의응답에 특화된 학습
- 한국의 법률, 제도적 맥락 반영
- 자연스러운 한국어 표현 생성

### 3. 효율적 학습
- LoRA 기법으로 메모리 효율성 확보
- 로컬 PC 환경에서 학습 가능
- 빠른 수렴과 안정적인 학습

### 4. 실용적 활용
- 실제 업무 환경에서 활용 가능
- API 형태로 서비스 배포 가능
- 지속적인 모델 개선 가능

## 🔧 문제 해결

### 자주 발생하는 문제

1. **메모리 부족**
   - 배치 크기 조정: `per_device_train_batch_size=1`
   - Gradient Accumulation 활용: `gradient_accumulation_steps=8`

2. **CUDA 오류**
   - PyTorch CUDA 버전 확인
   - GPU 메모리 정리: `torch.cuda.empty_cache()`

3. **토크나이저 오류**
   - `use_fast=False` 설정
   - `trust_remote_code=True` 설정

4. **WandB 연결 오류**
   - API 키 재설정: `wandb login`
   - 프록시 설정 확인

### 디버깅 팁
- 작은 데이터셋으로 먼저 테스트
- 학습률 조정으로 수렴 개선
- 정기적인 체크포인트 저장

## 📚 참고 자료

### 참고 문서
- [Qwen3 모델 문서](https://huggingface.co/Qwen/Qwen3-8B)
- [Self-LLM Qwen2 튜토리얼](https://github.com/datawhalechina/self-llm/blob/master/models/Qwen2/05-Qwen2-7B-Instruct%20Lora.ipynb)