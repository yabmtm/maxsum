def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

def lcmm(ls):
    return reduce(lcm, ls)

def subset_sum(numbers, target, partial=[]):

    s = sum(partial)

    if s == target:
        print lcmm(partial), target, partial

    if s >= target:
        return

    for i in range(len(numbers)):
        n = numbers[i]
        remaining = numbers[i+1:]
        subset_sum(remaining, target, partial + [n])

if __name__ == "__main__":
    for j in range(1,21):
        subset_sum(range(j),j)
