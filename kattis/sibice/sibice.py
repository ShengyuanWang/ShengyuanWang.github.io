def main():
	n, w, h = map(int, input().strip().split())
	max_length = (w**2 + h**2)**0.5
	for i in range(n):
		t = int(input())
		if t <= max_length:
			print("DA")
		else:
			print("NE")
	return

if __name__ == "__main__":
	main()


