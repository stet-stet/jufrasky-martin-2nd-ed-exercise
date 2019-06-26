# implement an ELIZA-like program, using substitutions such as those described on page 60.
# You may choose a different domain than a Rogerian psychologist, if you wish,
# although keep in mind that you would need a domain in which your program can
# engage in a lot of simple repitition.

# my domain: a twitter troll bot(Korean)
import re
while True:
    sen = input("Q: ")
    if re.compile("씨발").search(sen):
        print("A. 씨발쓰지마세요~~~")
    elif re.compile("((근거)|(증거)|(논거)) ((입니다)|(가져왔))").search(sen):
        print("A. 근거를 가져오신 건 기쁜데, 그래서 뭐 어쩌라는 건가요?")
    else:
        print("A. 왜 그렇게 생각하시나요? 이해할 수 없습니다. 통계적, 학술적 근거를 가져오시겠어요?")