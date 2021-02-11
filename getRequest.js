const https = require('https');

const getTitle = (judul) => {
    url = `https://jsonmock.hackerrank.com/api/movies/search/?Title=${judul}`;

    https.get(url, (res) => {
        
        let data = '';
        let titles = [];
    
        res.on('data', (chunk) => {
            data += chunk;
        });
    
        res.on('end', () => {
            let hehe = JSON.parse(data);
            myData = hehe.data;
            console.log(myData.length);
            for (i=0; i<myData.length; i++) {
                titles.push(myData[i].Title);
            }
            console.log(titles.sort());
        });
    
    }).on('error', error => {
        console.log(error);
    })
}

getTitle('spiderman');
