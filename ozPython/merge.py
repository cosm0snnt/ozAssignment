# 혹시 오류가 난다면 파이썬 버전 3.13.3인지 확인하기
import nbformat
from pathlib import Path

# 병합 대상 폴더 경로
folder_path = Path(r"D:\ozCoding\ozAssignment\ozPython\mainTask\day12-250425_Python")

# 폴더 안의 모든 .ipynb 파일을 정렬된 순서로 가져오기
notebooks = sorted(folder_path.glob("*.ipynb"))

# 새 노트북 생성
merged = nbformat.v4.new_notebook()
merged_cells = []

# 각 노트북 파일에서 셀 가져와 병합
for nb_file in notebooks:
    with open(nb_file, 'r', encoding='utf-8') as f:
        nb = nbformat.read(f, as_version=4)
        merged_cells.extend(nb.cells)

merged.cells = merged_cells

# 결과 파일 저장 경로
output_path = folder_path / "merged_notebook.ipynb"

# 병합된 노트북 저장
with open(output_path, 'w', encoding='utf-8') as f:
    nbformat.write(merged, f)

print(f"✅ 병합 완료! 파일 위치: {output_path}")