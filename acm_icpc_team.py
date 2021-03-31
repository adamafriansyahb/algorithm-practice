def acm_team(topic):
    highest = 0
    teams = 0
    for i in range(len(topic)-1):
        for j in range(i+1, len(topic)):
            subject = 0
            for k in range(len(topic[0])):
                if (topic[i][k] == '1' or topic[j][k] == '1'):
                    subject += 1

            if subject > highest:
                highest = subject
                teams = 1
            elif subject == highest:
                teams += 1

    return [highest, teams]


topic = ['1001', '0001', '1110']
print(acm_team(topic))
# a = '1'
# b = '0'
# print(int(a) or int(b), 'hehe')
