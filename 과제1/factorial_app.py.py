import time

# 반복문 기반 팩토리얼
def factorial_iter(n: int) -> int:
    if n < 0:
        raise ValueError("n은 0 이상의 정수여야 합니다.")
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# 재귀 기반 팩토리얼
def factorial_rec(n: int) -> int:
    if n < 0:
        raise ValueError("n은 0 이상의 정수여야 합니다.")
    if n == 0 or n == 1:
        return 1
    return n * factorial_rec(n - 1)


# 실행 시간 측정 함수
def run_with_time(func, n: int):
    start = time.perf_counter()
    result = func(n)
    end = time.perf_counter()
    return result, end - start


# n 입력받기 (유효성 검사 포함)
def get_input_n():
    raw = input("n 값(정수, 0 이상)을 입력하세요: ").strip()
    if raw.lower() in ("q", "quit"):
        return None
    if not raw.isdigit():
        print("정수(0 이상의 숫자)만 입력하세요.")
        return None
    n = int(raw)
    if n < 0:
        print("정수(0 이상의 숫자)만 입력하세요.")
        return None
    return n

# 테스트 데이터
TEST_DATA = [0, 1, 2, 3, 5, 10, 15, 20, 30, 50, 100]

# 메인 인터랙티브 메뉴
def main():
    print("팩토리얼 계산기 (반복/재귀) - 정수 n>=0 을 입력하세요.")

    while True:
        print("\n================ Factorial Tester ================")
        print("1) 반복법으로 n! 계산")
        print("2) 재귀로 n! 계산")
        print("3) 두 방식 모두 계산 후 결과/시간 비교")
        print("4) 준비된 테스트 데이터 일괄 실행")
        print("q) 종료")
        print("=================================================")

        choice = input("선택: ").strip()

        if choice == "q":
            print("종료합니다.")
            break

        elif choice in ("1", "2", "3"):
            n = get_input_n()
            if n is None:
                continue

            if choice == "1":
                try:
                    result, elapsed = run_with_time(factorial_iter, n)
                    print(f"[반복] {n}! = {result}")
                    print(f"[반복] 시간: {elapsed:.6f} s")
                except ValueError as e:
                    print(e)

            elif choice == "2":
                try:
                    result, elapsed = run_with_time(factorial_rec, n)
                    print(f"[재귀] {n}! = {result}")
                    print(f"[재귀] 시간: {elapsed:.6f} s")
                except RecursionError:
                    print("입력값이 너무 커서 재귀 계산은 불가능합니다.")
                except ValueError as e:
                    print(e)

            elif choice == "3":
                try:
                    res_iter, time_iter = run_with_time(factorial_iter, n)
                    res_rec, time_rec = run_with_time(factorial_rec, n)
                    same = (res_iter == res_rec)
                    print(f"[반복] {n}! = {res_iter}")
                    print(f"[재귀] {n}! = {res_rec}")
                    print(f"결과 일치 여부: {same}")
                    print(f"[반복] 시간: {time_iter:.6f} s | [재귀] 시간: {time_rec:.6f} s")
                except RecursionError:
                    print("재귀 계산에서 RecursionError 발생.")
                except ValueError as e:
                    print(e)

        elif choice == "4":
            for n in TEST_DATA:
                try:
                    res_iter, time_iter = run_with_time(factorial_iter, n)
                    res_rec, time_rec = run_with_time(factorial_rec, n)
                    same = (res_iter == res_rec)
                    print(f"n={n} | same={same} | iter={time_iter:.6f}s, rec={time_rec:.6f}s")
                except RecursionError:
                    print(f"n={n} | 재귀 계산 불가(RecursionError)")
                except Exception as e:
                    print(f"n={n} | 오류 발생: {e}")

        else:
            print("메뉴에서 올바른 항목을 선택하세요.")

# 실행 시작
if __name__ == "__main__":
    main()
