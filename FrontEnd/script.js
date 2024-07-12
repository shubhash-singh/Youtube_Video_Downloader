function searchVideo() {
    const videoUrl = document.getElementById('videoUrl').value;

    // Simulate an API call to get video details and download links
    const videoDetails = getVideoDetails(videoUrl);
    
    if (videoDetails) {
        document.getElementById('videoTitle').innerText = videoDetails.title;
        document.getElementById('thumbnail').src = videoDetails.thumbnail;
        document.getElementById('duration').innerText = videoDetails.duration;
        document.getElementById('views').innerText = videoDetails.views;
        document.getElementById('likes').innerText = videoDetails.likes;
        document.getElementById('dislikes').innerText = videoDetails.dislikes;

        const tableBody = document.getElementById('downloadTable').querySelector('tbody');
        tableBody.innerHTML = '';

        videoDetails.downloadLinks.forEach(link => {
            const row = document.createElement('tr');
            row.innerHTML = `
                <td>${link.resolution}</td>
                <td>${link.fileSize}</td>
                <td>${link.extension}</td>
                <td><a href="${link.url}" download>Download</a></td>
            `;
            tableBody.appendChild(row);
        });

        document.getElementById('videoInfo').style.display = 'block';
    } else {
        document.getElementById('videoInfo').style.display = 'none';
    }
}

function getVideoDetails(url) {
    // This function simulates an API call to get video details.
    // Replace this with actual API call logic.
    if (url === 'https://youtu.be/v-JNBwX2OTk') {
        return {
            title: 'Sara Kays - Remember That Night? [Official Lyric Video]',
            thumbnail: 'https://img.youtube.com/vi/v-JNBwX2OTk/0.jpg',
            duration: '3.78',
            views: '1,199,900',
            likes: '55,163',
            dislikes: '177',
            downloadLinks: [
                { resolution: '360x640', fileSize: '10.94 mb', extension: 'mp4', url: '#' },
                { resolution: '1080x1920', fileSize: '78.27 mb', extension: 'mp4', url: '#' },
                // Add more download links as needed
            ]
        };
    } else {
        return null;
    }
}
