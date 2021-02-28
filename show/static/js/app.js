console.log('Connected');

function dislike(eventid){
    window.location.href = "/dislike/"+eventid;
}

function like(eventid){
    window.location.href = "/like/"+eventid;
}