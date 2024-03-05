import redis from 'redis';

const client = redis.createClient();

client.on('connect', function() {
    console.log('Redis client connected to the server');
});

client.on('error', function(err) {
    console.log(`Redis client not connected to the server: ${err.message}`);
});

function setHashValue(hashKey, key, value) {
    client.hset(hashKey, key, value, redis.print);
}

function displayHashValue(hashKey) {
    client.hgetall(hashKey, function(err, object) {
        console.log(object);
    });
}

setHashValue('HolbertonSchools', 'Portland', '50');
setHashValue('HolbertonSchools', 'Seattle', '80');
setHashValue('HolbertonSchools', 'New York', '20');
setHashValue('HolbertonSchools', 'Bogota', '20');
setHashValue('HolbertonSchools', 'Cali', '40');
setHashValue('HolbertonSchools', 'Paris', '2');

displayHashValue('HolbertonSchools');
