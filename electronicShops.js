const getMoneySpent = (keyboards, drives, b) => {
    let prices = []

    for (let i=0; i<keyboards.length; i++) {
        for (let j=0; j<drives.length; j++) {
            let price = keyboards[i] + drives[j]
            if (price <= b) prices.push(price)
        }
    }

    if (prices.length > 0) {
        return Math.max(...prices)
    } else {
        return -1
    }
}