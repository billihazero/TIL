#매일의 온도를 나타내는 int형 배열 temperature 가 주어진다. 
# answer 배열의 원소 answer[i]는 i번째 날의 온도보다 더 따뜻해지기까지 며칠을 기다려야하는지 나타낸다.
#만약 더 따뜻해지는 날이 없다면 answer[i]==0 이다.
# answer 배열을 반환하는 함수를 구현하시오

def dailyTemperatures(temperatures):
    stack = []
    ans = [0] * len(temperatures) #temperatures 개수 만큼 answer 배열을 초기화 [0, 0, 0, 0 ....]
    for cur_day, cur_temp in enumerate(temperatures): # cur_day = 현재날짜, cur_temp = 현재온도 enumertate(temperature) = 온도리스트 요소별로 순회
        while stack and stack[-1][1] < cur_temp:  #stack 마지막의 배열의 1번째 요소(cur_day, cur_temp) = cur_temp / 넣어놨던 데이터와 지금의 데이터 비교
            prev_day, _ = stack.pop()
            ans[prev_day] = cur_day - prev_day
        stack.append((cur_day, cur_temp))
    return ans

print(dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))