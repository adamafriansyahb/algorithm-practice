// learning source: beiatrix (YouTube)

class Queue {
    constructor() {
        this.items = {};
        this.head = 0;
        this.tail = 0;
    }

    enqueue(item) {
        this.items[this.tail] = item;
        console.log(`${item} enqueued to ${this.tail}`);
        this.tail++;
    }

    dequeue() {
        let removedItem = this.items[this.head];
        delete this.items[this.head];
        console.log(`${removedItem} dequeued from ${this.head}`);
        this.head++;
        return removedItem;
    }

    print() {
        let queues = 'ITEM\t-\tORDER\n';
        const itemsLength = Object.keys(this.items).length + this.head;
        for (let i=this.head; i<itemsLength; i++) {
            queues += `${this.items[i]}\t-\t${i-this.head+1}\n`;
        }
        return queues;
    }
}

const queue = new Queue();

queue.enqueue('A');
queue.enqueue('B');
queue.enqueue('C');
queue.enqueue('D');
queue.enqueue('E');
queue.enqueue('F');
queue.enqueue('G');
queue.enqueue('H');
console.log(`----------------`);
queue.dequeue();
queue.dequeue();
console.log(`----------------`);
console.log(queue.print());