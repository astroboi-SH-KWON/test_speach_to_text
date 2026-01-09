import whisper
import os
import time

from config import config

def transcribe_wav_to_text(input_file):
    # 1. 모델 로드
    print(f"{config.s2txt_model_id} 모델 로딩 중...")
    model = whisper.load_model(config.s2txt_model_id)

    # 2. 오디오 파일 텍스트 변환 (Transcribe)
    if not os.path.exists(input_file):
        print(f"[ERROR] {input_file} 파일을 찾을 수 없습니다.")
        return

    print(f"'{input_file}' 음성 파일 변환 GO!!!")
    result = model.transcribe(input_file, fp16=False)  # CPU 환경일 경우 fp16=False 설정
    # result = model.transcribe(input_file, fp16=False, language="ko")  # 한국어 지정하고 싶은 경우, default는 언어 자동 감지

    # 3. 결과 텍스트 추출 및 반환
    return result['text']

def make_text_to_file(text_obj, output_file):
    text_obj = text_obj.replace("니다", "니다\n")  # # 줄바꿈 규칙

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(text_obj)

    print(f"파일 저장 완료! {output_file}")


if __name__ == "__main__":
    wav_fl = "R20260104-174919.WAV"
    input_wav = f"./input/{wav_fl}"
    output_txt = f"./output/result_{wav_fl.replace('.WAV', '')}.txt"

    st_time = time.perf_counter()
    script_obj = transcribe_wav_to_text(input_wav)
    print("음성 변환 완료, 파일 생성 시작")
    make_text_to_file(script_obj, output_txt)
    print(f"DONE :::::::::{time.perf_counter() - st_time} secs")