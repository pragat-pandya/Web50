// start with first post
let counter = 1;

// Load 20 posts at a time
const quantity = 20;

// When DOM loads load the first 20 posts
document.addEventListener('DOMContentLoaded', load);

// If scrolled to the bottom load 20 more posts
window.onscroll = () => {
    if (window.innerHeight+window.scrollY >= document.body.offsetHeight) {
        load();
    }
};

// Loads next set of posts
function load() {
    // Set start and end variables and update the counter
    let start = counter;
    let end = start + quantity - 1;
    counter = end + 1;

    // Get new posts and add it to the DOM
    fetch(`posts/?start=${start}&end=${end}`)
    .then(response => response.json())
    .then (data => {
        data.posts.forEach(add_post);
    })
};

// Add a new post with given content to the DOM
function add_post (contents) {
    // create new post
    const post = document.createElement('div');
    post.className = "post";
    post.innerHTML = contents;

    // Add post to the DOM
    document.querySelector('#posts').append(post);
};