import os

file_path = r'd:\MyProject\index.html'

with open(file_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_lines = []
target_line_index = 3180 # 3181 in 1-indexed

q1_text = "Bầu cử các đại biểu Quốc hội và Hội đồng Nhân dân các cấp vào các cơ quan quyền lực nhà nước thuộc loại hình dân chủ:"
q1_old_ans = '"ans": 3'
q1_new_ans = '"ans": 1'
q1_old_exp = '"exp": "Đáp án đúng: D. Dân chủ trực tiếp."'
q1_new_exp = '"exp": "Đáp án đúng: B. Dân chủ gián tiếp."'

q2_text = "Điền vào chỗ trống đúng theo Hồ Chí Minh, “Làm cách mệnh rồi thì quyền trao cho […] chớ để trong tay một bọn ít người”."
q2_old_ans = '"ans": 1'
q2_new_ans = '"ans": 2'
q2_old_exp = '"exp": "Đáp án đúng: B. Dân chúng số nhiều."'
q2_new_exp = '"exp": "Đáp án đúng: C. Quần chúng nhân dân."'

line = lines[target_line_index]

# Update Question 1
if q1_text in line:
    # We need to find the specific question block to avoid wrong replacements if multiple questions are similar
    # But these are long unique strings.
    # To be safe, we split by question blocks if possible or just use string replacement if unique enough.
    
    # Check if unique enough
    if line.count(q1_text) == 1:
        # Find the part after q1_text until the next question or end of object
        start_idx = line.find(q1_text)
        end_idx = line.find('}', start_idx)
        block = line[start_idx:end_idx]
        
        new_block = block.replace(q1_old_ans, q1_new_ans).replace(q1_old_exp, q1_new_exp)
        line = line[:start_idx] + new_block + line[end_idx:]
    else:
        print("Error: Question 1 text is not unique on the line.")
        exit(1)

# Update Question 2
if q2_text in line:
    if line.count(q2_text) == 1:
        start_idx = line.find(q2_text)
        end_idx = line.find('}', start_idx)
        block = line[start_idx:end_idx]
        
        new_block = block.replace(q2_old_ans, q2_new_ans).replace(q2_old_exp, q2_new_exp)
        line = line[:start_idx] + new_block + line[end_idx:]
    else:
        print("Error: Question 2 text is not unique on the line.")
        exit(1)

lines[target_line_index] = line

with open(file_path, 'w', encoding='utf-8') as f:
    f.writelines(lines)

print("Successfully updated index.html")
