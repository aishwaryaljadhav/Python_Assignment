from src.assignment15.util import filter_mail

def main():
    n = int(input())
    emails = []

    for i in range(n):
        emails.append(input().strip())

    result = filter_mail(emails)
    print(result)

if __name__ == "__main__":
    main()
