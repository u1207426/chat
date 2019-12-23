# 讀取檔案
def read_file(filename):
	lines = []
	with open(filename, 'r', encoding='utf-8') as f:
		for line in f:
			lines.append(line.strip())
	return lines

# 轉換對話格式
def convert(lines):
	new = []
	name = None # 預設值目前還沒有的意思
	for line in lines:
		if line == 'Allen':
			name = 'Allen'
			continue
		elif line == 'Tom':
			name = 'Tom'
			continue
		if name:
			new.append(name + ': '+ line)
	return new

# 寫入檔案
def write_file(filename, lines):
	with open(filename, 'w', encoding='utf-8') as f:
		for line in lines:
			f.write(line + '\n')

def main():
	filename = 'input.txt'
	lines = read_file(filename)
	lines = convert(lines)
	write_file('output.txt', lines)

main()