const player = videojs('interview-media');

player.ready(function() {
    this.on('timeupdate', function() {
        const event = new CustomEvent('timeupdate', { detail: this.currentTime() });
        document.dispatchEvent(event);
    })

    document.addEventListener('timerequest', (e) => {
        this.currentTime(e.detail);
    });
});


player.one('canplaythrough', function() {
    const paramsString = window.location.search;
    const searchParams = new URLSearchParams(paramsString);
    const tc = searchParams.get('tc');

    if (tc) {
        this.currentTime(Number.parseFloat(tc));
    }
});
