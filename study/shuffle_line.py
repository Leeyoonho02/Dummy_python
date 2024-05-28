import random

def shuffle_file_lines(input_file, output_file):
    try:
        # 파일 읽기
        with open(input_file, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        
        # 행이 없는 경우 처리
        if not lines:
            print("파일이 비어 있습니다.")
            return
        
        # 행 순서 섞기
        random.shuffle(lines)
        
        # 섞인 행을 새로운 파일에 쓰기
        with open(output_file, 'w', encoding='utf-8') as file:
            file.writelines(lines)
        
        print(f"{output_file}에 섞인 행을 저장했습니다.")
    
    except FileNotFoundError:
        print(f"파일을 찾을 수 없습니다: {input_file}")
    except Exception as e:
        print(f"오류 발생: {e}")

# 예시 사용법
input_file = 'shuffled_input.txt'
output_file = 'shuffled_output.txt'
shuffle_file_lines(input_file, output_file)