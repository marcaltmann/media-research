const transcriptEl = document.getElementById('transcript');

if (transcriptEl) {
    document.addEventListener('timeupdate', (e) => {
        const links = transcriptEl.getElementsByClassName('transcript__link');
        const linkArr = Array.from(links);

        linkArr.forEach((el) => {
            el.classList.remove('transcript__link--current');
        });

        const currentLink = linkArr.find((el) => {
            const startTime = Number.parseFloat(el.dataset.start);
            const endTime = Number.parseFloat(el.dataset.end);
            return (startTime < e.detail)
                && (e.detail < endTime);
        })

        if (currentLink) {
            currentLink.classList.add('transcript__link--current');

            /* Scroll */
            const segmentDiv = currentLink.parentElement;
            const container = segmentDiv.parentElement;
            container.scrollTop = segmentDiv.offsetTop - container.offsetTop;
        };
    });

    transcriptEl.addEventListener('click', (e) => {
        e.preventDefault();
        const target = e.target;
        if (target.className !== 'transcript__link') {
            return;
        }

        timecode = Number.parseFloat(target.dataset.start);
        console.log(timecode);

        const event = new CustomEvent("timerequest", { detail: timecode });
        document.dispatchEvent(event);
    });
}
