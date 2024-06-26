const entitiesEl = document.getElementById('entities');

if (entitiesEl) {
  entitiesEl.addEventListener('click', (e) => {
    e.preventDefault();
    const target = e.target;
    if (target.className !== 'timecode__link') {
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
