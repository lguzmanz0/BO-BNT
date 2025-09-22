#!/Library/Frameworks/Python.framework/Versions/3.12/bin/python3
import ipaddress


def load_prefixes(filename):
	with open(filename, 'r') as f:
		return [ipaddress.IPv4Network(line.strip()) for line in f if line.strip()]

def check_containment(file1_prefixes, file2_prefixes):
	results = {}
	for prefix1 in file1_prefixes:
		containing_prefix = next((prefix2 for prefix2 in file2_prefixes if prefix1.subnet_of(prefix2)), None)
		results[str(prefix1)] = str(containing_prefix) if containing_prefix else None
	return results

def main():
	file1 = 'file1.txt'
	file2 = 'file2.txt'

	try:
		prefixes1 = load_prefixes(file1)
		prefixes2 = load_prefixes(file2)
	except ValueError as e:
		print(f'Error parsing IP prefixes: {e}')
		return

	containment_results = check_containment(prefixes1, prefixes2)

	for prefix, container in containment_results.items():
		if container:
			print(f'{prefix} is contained in {container}')
		else:
			print(f'{prefix} is NOT contained in any prefix post-migration')

if __name__ == '__main__':
	main()
