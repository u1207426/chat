# 讀取檔案
def read_file(filename):
	lines = []
	with open(filename, 'r', encoding='utf-8') as f:
		for line in f:
			lines.append(line.strip())
	return lines

# 計數功能
def count(lines):
	lee_word_count = 0
	lee_sticker_count = 0
	lee_image_count = 0
	jean_word_count = 0
	jean_sticker_count = 0
	jean_image_count = 0
	#name = None # 預設值目前還沒有的意思
	for line in lines:
		s = line.split(' ') # 把每一行對話用空格分割，分割後存在s的清單中，s[2]後才是對話內容
		time = s[0]
		name = s[1]
		if name == '李宏君':
			if s[2] == '貼圖':
				lee_sticker_count += 1
			elif s[2] == '圖片':
				lee_image_count += 1
			else:
				for i in s[2:]: # 取s[2]後的所有清單內容一個一個作加總
					lee_word_count += len(i)
		elif name == '菁':
			if s[2] == '貼圖':
				jean_sticker_count += 1
			elif s[2] == '圖片':
				jean_image_count += 1
			else:
				for i in s[2:]: # 取s[2]後的所有清單內容一個一個作加總
					jean_word_count += len(i)
	print('李宏君共輸入： ', lee_word_count, '字')
	print('李宏君共輸入： ', lee_sticker_count, '個貼圖')
	print('李宏君共輸入： ', lee_image_count, '張圖片')
	print('菁共輸入： ', jean_word_count, '字')
	print('菁共輸入： ', jean_sticker_count, '個貼圖')
	print('菁共輸入： ', jean_image_count, '張圖片')

# 寫入檔案
def write_file(filename, lines):
	with open(filename, 'w', encoding='utf-8') as f:
		for line in lines:
			f.write(line + '\n')

def main():
	filename = 'input_line.txt'
	lines = read_file(filename)
	count(lines)
	# write_file('output.txt', lines)

main()