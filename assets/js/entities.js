const entitiesEl = document.getElementById('entities');

if (entitiesEl) {
  entitiesEl.addEventListener('click', (e) => {
    if (e.target.className !== 'timecode__link') {
      return;
    }

    e.preventDefault();
    const timecode = Number.parseFloat(e.target.dataset.start);
    const url = new URL(window.location);
    url.searchParams.set("tc", String(timecode));
    history.replaceState({}, "", url);

    const event = new CustomEvent("timerequest", { detail: timecode });
    document.dispatchEvent(event);
  });
}
