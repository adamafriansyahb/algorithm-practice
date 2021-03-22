// this code does not pass some of the test cases on hackerrank due to its time complexity. 

const rotateArray = (a, k, queries) => {
    let result = []

    for (let i=0; i<k; i++) {

        let head = a[a.length-1]
        let tail = a.slice(0, a.length-1)
        
        a = []
        a = a.concat(head)
        a = a.concat(tail)
    }

    for (let j=0; j<queries.length; j++) {
        result.push(a[queries[j]])
    }

    return result
}

a = [1,2,3,4,5]
k = 2
queries = [1,2]

console.log(rotateArray(a, k, queries))