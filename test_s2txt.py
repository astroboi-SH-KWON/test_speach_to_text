import whisper
import os
import time
from datetime import timedelta

from config import config


def format_timestamp(seconds: float):
    """초 단위 시간을 SRT 타임스탬프 형식(HH:MM:SS,mmm)으로 변환"""
    td = timedelta(seconds=seconds)
    total_seconds = int(td.total_seconds())
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    secs = total_seconds % 60
    millis = int((seconds - total_seconds) * 1000)
    return f"{hours:02}:{minutes:02}:{secs:02},{millis:03}"

def create_srt(audio_path, output_srt_path):
    # 1. 모델 로드
    model = whisper.load_model(config.s2txt_model_id)

    print(f"음성 분석 중: {audio_path}")
    # 2. 음성 인식 수행 (타임스탬프 포함)
    result = model.transcribe(audio_path, verbose=False, language="ko", fp16=False)  # CPU 환경일 경우 fp16=False 설정

    # 3. SRT 파일 작성
    with open(output_srt_path, "w", encoding="utf-8") as f:
        for i, segment in enumerate(result['segments'], start=1):
            start = format_timestamp(segment['start'])
            end = format_timestamp(segment['end'])
            text = segment['text'].strip()

            # SRT 형식: 순번 \n 시간 -> 시간 \n 내용 \n\n
            f.write(f"{i}\n")
            f.write(f"{start} --> {end}\n")
            f.write(f"{text}\n\n")

    print(f"자막 파일 생성 완료: {output_srt_path}")

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
    output_srt = f"./output/{wav_fl.replace('.WAV', '')}.srt"

    st_time = time.perf_counter()
    # script_obj = transcribe_wav_to_text(input_wav)
    # print("음성 변환 완료, 파일 생성 시작")
    # make_text_to_file(script_obj, output_txt)
    create_srt(input_wav, output_srt)
    print(f"DONE :::::::::{time.perf_counter() - st_time} secs")