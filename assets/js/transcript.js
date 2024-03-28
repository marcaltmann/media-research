import $ from "jquery";

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

        if (currentLink && !currentLink.classList.contains('transcript__link--current')) {
            currentLink.classList.add('transcript__link--current');

            /* Scroll */
            const segmentDiv = currentLink.parentElement;
            const container = segmentDiv.parentElement;
            $(container).animate({
                scrollTop: (segmentDiv.offsetTop - container.offsetTop),
            }, 125);
        };
    });

    transcriptEl.addEventListener('click', (e) => {
        e.preventDefault();
        const target = e.target;
        if (target.className !== 'transcript__link') {
            return;
        }

        const timecode = Number.parseFloat(target.dataset.start);
        const url = new URL(window.location);
        url.searchParams.set("tc", String(timecode));
        history.replaceState({}, "", url);

        const event = new CustomEvent("timerequest", { detail: timecode });
        document.dispatchEvent(event);
    });
}
