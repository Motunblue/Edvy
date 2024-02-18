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
            const parsedDate = moment.utc(post.updated_at);
            post.content = post.content.replace(/\n/g, "<br>");
            post_by = userData.school_id === "null" ? post.by.name : `${post.by.first_name} ${post.by.lastname}`

            $('#blog-content').append(`
                <article>
                    <div>
                        <div class="blog-content-title">
                            <h5>${post.title}</h5>
                            <div>posted on ${parsedDate.format('L LT')} by ${post.by.name}</div>
                        </div>
                        <p class="blog-content-content">${post.content}</p>
                    </div>
                </article>
            `);
        });
    },
});

$(".blog").css("background-color", "#F0F7FF");