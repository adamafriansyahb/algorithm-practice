const libraryFine = (d1, m1, y1, d2, m2, y2) => {
    const dayDifference = d1 - d2;
    const monthDifference = m1 - m2;
    const yearDifference = y1 - y2;
    let fine = 0;
    
    if (dayDifference > 0) {
        if (monthDifference < 0 && yearDifference < 0) {
            fine += 0;
        }
        else if (monthDifference == 0 && yearDifference == 0) {
            fine += 15 * dayDifference;
        }
        else if (monthDifference > 0 && yearDifference == 0) {
            fine += 500 * monthDifference;
        }
        else if (yearDifference > 0) {
            fine += 10000
        }
    } else {
        if (monthDifference <= 0 && yearDifference <= 0) {
            fine += 0
        }
        else if (monthDifference > 0 && yearDifference == 0) {
            fine += 500 * monthDifference
        }
        else if (yearDifference > 0) {
            fine += 10000
        }
    }

    console.log('day', dayDifference)
    console.log('month', monthDifference)
    console.log('year', yearDifference)
    console.log(fine);
}

d1 = 9;
m1 = 6;
y1 = 2015;
d2 = 6;
m2 = 6;
y2 = 2015;

libraryFine(d1, m1, y1, d2, m2, y2);

