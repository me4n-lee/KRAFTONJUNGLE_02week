## Stack Class

class stack:
    def __init__(self):  # 스택 객체 생성
        self.items = []

    def push(self, item):  # 스택 요소 추가 push(.append())
        self.items.append(item)

    def pop(self):  # 스택 맨 뒤 요소 삭제하고 리턴 pop()
        return self.items.pop()

    def peek(self):  # 스택 맨 뒤 요소 리턴
        return self.items[-1]

    def isEmpty(self):  # 스택이 비었는지 확인(비었으면 True 리턴)
        return not self.items


stk = stack()  # stack 객체 생성
print(stk)  # stack object 생성 확인

print(stk.isEmpty())  # 처음에는 아무것도 들어있지 않으므로 True 출력
stk.push(7)  # stk 에 7 넣음 : [7]
stk.push(8)  # stk 에 8 넣음 : [7,8]
stk.push(9)  # stk 에 9 넣음 : [7,8,9]
print(stk.items) #= > [7, 8, 9]

print(stk.pop())  # stk 맨 마지막 값을 꺼내온다. 9를 꺼냈으니 출력 : 9
print(stk.items)  # [7, 8] 꺼내지고 남은 값들

print(stk.peek())  # stk 맨 마지막 값을 꺼내지 않고 출력만한다 출력 : 8
print(stk.items)  # [7, 8] 아무 값도 사라지지 않은걸 알 수 있다

print(stk.pop())  # stk 마지막 값 8 꺼내지면서 출력 : 8
print(stk.pop())  # stk 마지막 값 7 꺼내지면서 출력 : 7

print(stk.isEmpty())  # 객체에 아무것도 들어있지 않으므로 True 출력
print(stk.items)  # 비어 있으므로 [] 출력