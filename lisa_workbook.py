def workbook(n, k, arr):
    special = 0
    page = 1

    for problem in arr:
        for i in range(1, problem + 1):
            if i == page:
                special += 1

            page += 1 if i == problem or i % k == 0 else 0

    return special
