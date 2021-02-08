class Node {
    constructor(data, next = null) {
        this.data = data;
        this.next = next;
    }
}

class LinkedList {
    constructor() {
        this.head = null;
        this.size = 0;
    }

    // insert node into the first index
    insertFirst(data) {
        this.head = new Node(data, this.head);
        this.size++;
    }

    // insert node into the last index
    insertLast(data) {
        let node = new Node(data);
        let current;

        // check if the linked list is empty or not
        if (!this.head) {
            this.head = node;
        }
        else {
            current = this.head;
            while (current.next) {
                current = current.next;
            }
            current.next = node;
        }
        this.size++;
    }

    // insert at a specific index
    insertAt(data, index) {
        //  If data is inserted to non-existing index
        if (index > 0 && index > this.size) {
            return;
        }
        // if data is inserted to the first index
        else if (index === 0) {
            this.insertFirst(data);
            this.size++;
        }
        else{
            const node = new Node(data);
            let previous;
            let current = this.head;
            let count = 0;
    
            while (count < index) {
                previous = current; 
                current = current.next; 
                count++;
            }
    
            node.next = current;
            previous.next = node;

            this.size++;
        }
    }

    // get data from a specific index
    getData(index) {
        let current = this.head;

        if (index > this.size && index > 0) {
            console.log("Index out of range");
        }
        else if (index === 0) {
            console.log(current.data);
        }
        else {
            let count = 0;
            let data;
    
            while (count < index) {
                current = current.next
                count++;
            }
    
            console.log(current.data);
        }
    }

    // print list data 
    printData() {
        let current = this.head;
        let arr = '';
        while (current) {
            // console.log(current.data);
            arr += current.data
            current = current.next; 
            if (current) {
                arr += '-'
            }
        }
        console.log(arr);
    }
}

const ll = new LinkedList();
ll.insertFirst(10);
ll.insertFirst(20);
ll.insertFirst(30);
ll.insertLast(40);
ll.insertAt(50, 2);

ll.printData();
console.log('------------');
ll.getData(3)


