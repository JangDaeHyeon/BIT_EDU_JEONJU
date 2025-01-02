# -*- coding: utf-8 -*-
"""07_07_SPLITCODE_HTML.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1keSmKPJ_awEScxUjNuiGJ_RzJ0dPYqkm
"""

from bs4 import BeautifulSoup
from langchain_text_splitters import RecursiveCharacterTextSplitter, HTMLHeaderTextSplitter

# 로컬 HTML 파일 경로를 지정
html_file_path = "JANG DAEHYEON(Resume).html"

# HTML 파일에서 텍스트를 가져오는 함수
def get_text_from_html(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        html_content = file.read()
    soup = BeautifulSoup(html_content, "html.parser")
    return soup

# HTML 파일 읽기
soup = get_text_from_html(html_file_path)

# 헤더와 텍스트를 분리하여 HTMLHeaderTextSplitter를 이용
headers_to_split_on = [  # 분할할 HTML 헤더 태그와 해당 헤더의 이름을 지정
    ("h1", "Heading H1"),
    ("h2", "Heading H2"),
    ("h3", "Heading H3"),
]

# HTML 헤더를 기준으로 텍스트를 분할하는 HTMLHeaderTextSplitter 객체를 생성
html_splitter = HTMLHeaderTextSplitter(headers_to_split_on=headers_to_split_on)

# HTML 파일에서 텍스트를 추출하고 분할
html_header_splits = html_splitter.split_text(str(soup))

chunk_size = 500  # 텍스트를 분할할 청크의 크기를 지정
chunk_overlap = 30  # 분할된 청크 간의 중복되는 문자 수를 지정

# 텍스트를 재귀적으로 분할하는 RecursiveCharacterTextSplitter 객체를 생성
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=chunk_size, chunk_overlap=chunk_overlap
)

# 결과를 파일로 저장
output_file_path = "htmlheadertextsplitter_result.txt"
with open(output_file_path, "w", encoding="utf-8") as file:
    for idx, chunk in enumerate(html_header_splits):
        file.write(f"Chunk {idx+1}:\n")
        file.write(chunk.page_content + "\n")  # Document 객체에서 텍스트를 추출
        file.write("-" * 50 + "\n")

print(f"분할된 결과가 '{output_file_path}' 파일에 저장되었습니다.")