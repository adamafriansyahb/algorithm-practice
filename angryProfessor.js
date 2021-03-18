const angryProfessor = (k, a) => {
    let onTimeCounter = 0;
    for (let i=0; i<a.length; i++) {
        if (a[i] <= 0) {
            onTimeCounter++;
        }
    }

    if (onTimeCounter >= k) {
        return 'NO';
    } else {
        return 'YES';
    }
}