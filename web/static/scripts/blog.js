const blogContentEl = document.getElementById('blog-content');
const userData = JSON.parse(blogContentEl.getAttribute('data-user'));

$.ajax({
    url: 'http://localhost:5001/api/v1/posts',
    type: 'GET',
    contentType: 'application/json',
    headers: {
        'User-Id': userData.id,
        'School-Id': userData.school_id
    },
    success: (data) => {
        data.forEach(post => {
            blogContentEl.append(`
                <article>
                    <div>
                        <h2>${post.title}</h2>
                        <div>${post.content}</div>
                    </div>
                </article>
            `);
        });
    },
});
