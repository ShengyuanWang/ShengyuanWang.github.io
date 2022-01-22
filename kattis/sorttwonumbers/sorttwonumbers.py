def main():
	a, b = map(int, input().strip().split())
	a, b = min(a, b), max(a, b)
	print(str(a) + " " + str(b))
	return

if __name__ == "__main__":
	main()



