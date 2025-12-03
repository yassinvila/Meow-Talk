// Basic message fetcher
fetch('/api/messages')
  .then(res => res.json())
  .then(data => {
    document.getElementById('messages').innerText = JSON.stringify(data);
  });
