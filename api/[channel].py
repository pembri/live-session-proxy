import re
import math
import xml.etree.ElementTree as ET
from http.server import BaseHTTPRequestHandler
import urllib.request
from urllib.parse import urlparse, parse_qs

CHANNELS = {
    "btv": "https://cdnbal1.indihometv.com/atm/DASH/beritasatu/beritasatu-avc1_2500000=7-3277707030000000.mpd",
    "gtv": "https://cdnbal1.indihometv.com/atm/DASH/globaltv/globaltv-avc1_2500000=7-3277707030000000.mpd",
    "idx-channel": "https://cdnbal1.indihometv.com/atm/DASH/idx/idx-avc1_2500000=7-3277707030000000.mpd",
    "indosiar": "https://cdnbal1.indihometv.com/atm/DASH/indosiar/indosiar-avc1_2500000=7-3277707030000000.mpd",
    "inews": "https://cdnbal1.indihometv.com/atm/DASH/inews/inews-avc1_2500000=7-3277707030000000.mpd",
    "kompas-tv": "https://cdnbal1.indihometv.com/atm/DASH/KOMPAS_TV/KOMPAS_TV-avc1_2500000=7-3277707030000000.mpd",
    "mdtv": "https://cdnbal1.indihometv.com/dassdvr/134/net/manifest_wuseetv.mpd",
    "metro-tv": "https://cdnbal1.indihometv.com/dassdvr/134/metrotv/manifest_wuseetv.mpd",
    "mnctv": "https://cdnbal1.indihometv.com/atm/DASH/mnctv/mnctv-avc1_2500000=7-3277707030000000.mpd",
    "nusantara-tv": "https://cdnbal1.indihometv.com/atm/DASH/nusantaratv/nusantaratv-avc1_2500000=7-3277707030000000.mpd",
    "rcti": "https://cdnbal1.indihometv.com/atm/DASH/rcti/rcti-avc1_2500000=7-3277707030000000.mpd",
    "rtv": "https://cdnbal1.indihometv.com/atm/DASH/RAJAWALI_TV/RAJAWALI_TV-avc1_2500000=7-3277707030000000.mpd",
    "sctv": "https://cdnbal1.indihometv.com/atm/DASH/sctv/sctv-avc1_2500000=7-3277707030000000.mpd",
    "sin-po-tv": "https://cdnbal1.indihometv.com/atm/DASH/sinpotv/sinpotv-avc1_2500000=7-3277707030000000.mpd",
    "sindonews": "https://cdnbal1.indihometv.com/atm/DASH/mncnews/mncnews-avc1_2500000=7-3277707030000000.mpd",
    "trans7": "https://cdnbal1.indihometv.com/dassdvr/130/trans7/manifest_wuseetv.mpd",
    "transtv": "https://cdnbal1.indihometv.com/dassdvr/130/transtv/manifest_wuseetv.mpd",
    "tvone": "https://cdnbal1.indihometv.com/atm/DASH/tvone/tvone-avc1_2500000=7-3277707030000000.mpd",
    "tvri": "https://cdnbal1.indihometv.com/atm/DASH/TVRI/TVRI-avc1_2500000=7-3277707030000000.mpd",
    "tvri-world": "https://cdnbal1.indihometv.com/atm/DASH/tvriworld/tvriworld-avc1_2500000=7-3277707030000000.mpd",
    "antara": "https://cdnbal1.indihometv.com/atm/DASH/antara/antara-avc1_2500000=7-3277707030000000.mpd",
    "bali-tv": "https://cdnbal1.indihometv.com/atm/DASH/balitv/balitv-avc1_2500000=7-3277707030000000.mpd",
    "jaktv": "https://cdnbal1.indihometv.com/atm/DASH/JAK_TV/JAK_TV-avc1_2500000=7-3277707030000000.mpd",
    "jawa-pos-tv": "https://cdnbal1.indihometv.com/atm/DASH/jawapos/jawapos-avc1_2500000=7-3277707030000000.mpd",
    "jtv": "https://cdnbal1.indihometv.com/atm/DASH/jtv/jtv-avc1_2500000=7-3277707030000000.mpd",
    "al-jazeera-english": "https://cdnbal1.indihometv.com/atm/DASH/aljazeera/aljazeera-avc1_2500000=7-3277707030000000.mpd",
    "bbc-news": "https://cdnbal1.indihometv.com/atm/DASH/bbcnews/bbcnews-avc1_2500000=7-3277707030000000.mpd",
    "bloomberg": "https://cdnbal1.indihometv.com/atm/DASH/BLOOMBERG_AT/BLOOMBERG_AT-avc1_2500000=7-3277707030000000.mpd",
    "channel-news-asia": "https://cdnbal1.indihometv.com/atm/DASH/newsasia/newsasia-avc1_2500000=7-3277707030000000.mpd",
    "dw-english": "https://cdnbal1.indihometv.com/atm/DASH/DWTV/DWTV-avc1_2500000=7-3277707030000000.mpd",
    "france24": "https://cdnbal1.indihometv.com/atm/DASH/FRANCE_24/FRANCE_24-avc1_2500000=7-3277707030000000.mpd",
    "nhk-world-japan": "https://cdnbal1.indihometv.com/atm/DASH/NHK_WORLD_JAPAN/NHK_WORLD_JAPAN-avc1_2500000=7-3277707030000000.mpd",
    "phoenix-chinese": "https://cdnbal1.indihometv.com/atm/DASH/phoenixchinese/phoenixchinese-avc1_2500000=7-3277707030000000.mpd",
    "phoenix-infonews": "https://cdnbal1.indihometv.com/atm/DASH/phoenixinfonews/phoenixinfonews-avc1_2500000=7-3277707030000000.mpd",
    "russia-today": "https://cdnbal1.indihometv.com/atm/DASH/rusiatv/rusiatv-avc1_2500000=7-3277707030000000.mpd",
    "tvbs-news": "https://cdnbal1.indihometv.com/atm/DASH/TVBS_NEWS/TVBS_NEWS-avc1_2500000=7-3277707030000000.mpd",
    "abc-australia": "https://cdnbal1.indihometv.com/atm/DASH/ABC_AUSTRALIA/ABC_AUSTRALIA-avc1_2500000=7-3277707030000000.mpd",
    "arirang": "https://cdnbal1.indihometv.com/atm/DASH/ARIRANG/ARIRANG-avc1_2500000=7-3277707030000000.mpd",
    "axn": "https://cdnbal1.indihometv.com/atm/DASH/axn/axn-avc1_2500000=7-3277707030000000.mpd",
    "cctv4": "https://cdnbal1.indihometv.com/atm/DASH/CCTV_4/CCTV_4-avc1_2500000=7-3277707030000000.mpd",
    "dunia-lain": "https://cdnbal1.indihometv.com/dassdvr/130/dunialain/manifest_wuseetv.mpd",
    "hits": "https://cdnbal1.indihometv.com/atm/DASH/hits/hits-avc1_2500000=7-3277707030000000.mpd",
    "k-plus": "https://cdnbal1.indihometv.com/atm/DASH/kplus/kplus-avc1_2500000=7-3277707030000000.mpd",
    "kix": "https://cdnbal1.indihometv.com/atm/DASH/kix/kix-avc1_2500000=7-3277707030000000.mpd",
    "max-reels": "https://cdnbal1.indihometv.com/atm/DASH/useeprime/useeprime-avc1_2500000=7-3277707030000000.mpd",
    "new-tv-comprehensive": "https://cdnbal1.indihometv.com/atm/DASH/newtvcomprehensive/newtvcomprehensive-avc1_2500000=7-3277707030000000.mpd",
    "new-tv-finance": "https://cdnbal1.indihometv.com/atm/DASH/newtvfinance/newtvfinance-avc1_2500000=7-3277707030000000.mpd",
    "new-tv-variety": "https://cdnbal1.indihometv.com/atm/DASH/newtvvariety/newtvvariety-avc1_2500000=7-3277707030000000.mpd",
    "rock-entertainment": "https://cdnbal1.indihometv.com/atm/DASH/rock_entertainment/rock_entertainment-avc1_2500000=7-3277707030000000.mpd",
    "tv5monde": "https://cdnbal1.indihometv.com/atm/DASH/tv5monde/tv5monde-avc1_2500000=7-3277707030000000.mpd",
    "warner-tv": "https://cdnbal1.indihometv.com/atm/DASH/warner/warner-avc1_2500000=7-3277707030000000.mpd",
    "asian-food-network": "https://cdnbal1.indihometv.com/dassdvr/130/afc/manifest_wuseetv.mpd",
    "fashiontv": "https://cdnbal1.indihometv.com/atm/DASH/fashiontv/fashiontv-avc1_2500000=7-3277707030000000.mpd",
    "hgtv": "https://cdnbal1.indihometv.com/dassdvr/134/hgtv/manifest_wuseetv.mpd",
    "max-eats": "https://cdnbal1.indihometv.com/atm/DASH/maxeats/maxeats-avc1_2500000=7-3277707030000000.mpd",
    "max-streak": "https://cdnbal1.indihometv.com/atm/DASH/maxstreak/maxstreak-avc1_2500000=7-3277707030000000.mpd",
    "tlc": "https://cdnbal1.indihometv.com/dassdvr/133/tlc/manifest_wuseetv.mpd",
    "cgtn-documentary": "https://cdnbal1.indihometv.com/atm/DASH/CGTN_DOCUMENTARY/CGTN_DOCUMENTARY-avc1_2500000=7-3277707030000000.mpd",
    "curiosity": "https://cdnbal1.indihometv.com/dassdvr/130/curiosity/manifest_wuseetv.mpd",
    "discovery-channel": "https://cdnbal1.indihometv.com/atm/DASH/disco/disco-avc1_2500000=7-3277707030000000.mpd",
    "animax": "https://cdnbal1.indihometv.com/dassdvr/130/animax/manifest_wuseetv.mpd",
    "aniplus": "https://cdnbal1.indihometv.com/dassdvr/134/aniplus/manifest_wuseetv.mpd",
    "cartoonito": "https://cdnbal1.indihometv.com/atm/DASH/boomerang/boomerang-avc1_2500000=7-3277707030000000.mpd",
    "cbeebies": "https://cdnbal1.indihometv.com/atm/DASH/cbeebies/cbeebies-avc1_2500000=7-3277707030000000.mpd",
    "dunia-anak": "https://cdnbal1.indihometv.com/dassdvr/130/duniaanak/manifest_wuseetv.mpd",
    "horee": "https://cdnbal1.indihometv.com/dassdvr/130/horee/manifest_wuseetv.mpd",
    "max-kids": "https://cdnbal1.indihometv.com/atm/DASH/indikids/indikids-avc1_2500000=7-3277707030000000.mpd",
    "mentari-tv": "https://cdnbal1.indihometv.com/dassdvr/134/mentaritv/manifest_wuseetv.mpd",
    "my-kidz": "https://cdnbal1.indihometv.com/atm/DASH/mykids/mykids-avc1_2500000=7-3277707030000000.mpd",
    "nick-jr": "https://cdnbal1.indihometv.com/dassdvr/130/nickjr/manifest_wuseetv.mpd",
    "nickelodeon": "https://cdnbal1.indihometv.com/atm/DASH/nickelodeon/nickelodeon-avc1_2500000=7-3277707030000000.mpd",
    "bioskop-indonesia": "https://cdnbal1.indihometv.com/dassdvr/130/bioskopindonesia/manifest_wuseetv.mpd",
    "flik": "https://cdnbal1.indihometv.com/dassdvr/130/flik/manifest_wuseetv.mpd",
    "hits-movies": "https://cdnbal1.indihometv.com/atm/DASH/hitsmovie/hitsmovie-avc1_2500000=7-3277707030000000.mpd",
    "imc": "https://cdnbal1.indihometv.com/dassdvr/130/imc/manifest_wuseetv.mpd",
    "max-stream": "https://cdnbal1.indihometv.com/dassdvr/134/maxstream/manifest_wuseetv.mpd",
    "rock-action": "https://cdnbal1.indihometv.com/atm/DASH/ROCK_ACTION/ROCK_ACTION-avc1_2500000=7-3277707030000000.mpd",
    "thrill": "https://cdnbal1.indihometv.com/atm/DASH/thrill/thrill-avc1_2500000=7-3277707030000000.mpd",
    "tvn-movies": "https://cdnbal1.indihometv.com/dassdvr/130/tvnmovies/manifest_wuseetv.mpd",
    "zee-bioskop": "https://cdnbal1.indihometv.com/atm/DASH/zbioskop/zbioskop-avc1_2500000=7-3277707030000000.mpd",
    "cinemax": "https://cdnbal1.indihometv.com/atm/DASH/cinemax/cinemax-avc1_2500000=7-3277707030000000.mpd",
    "hbo": "https://cdnbal1.indihometv.com/atm/DASH/hbo/hbo-avc1_2500000=7-3277707030000000.mpd",
    "hbo-family": "https://cdnbal1.indihometv.com/atm/DASH/hbofamily/hbofamily-avc1_2500000=7-3277707030000000.mpd",
    "hbo-hits": "https://cdnbal1.indihometv.com/atm/DASH/hbohits/hbohits-avc1_2500000=7-3277707030000000.mpd",
    "hbo-signature": "https://cdnbal1.indihometv.com/atm/DASH/hbosignature/hbosignature-avc1_2500000=7-3277707030000000.mpd",
    "prambors": "https://cdnbal1.indihometv.com/atm/DASH/pramborstv/pramborstv-avc1_2500000=7-3277707030000000.mpd",
    "fight-sports": "https://cdnbal1.indihometv.com/atm/DASH/fightsport/fightsport-avc1_2500000=7-3277707030000000.mpd",
    "horizon-sports": "https://cdnbal1.indihometv.com/dassdvr/130/horizonsport/manifest_wuseetv.mpd",
    "max-sports": "https://cdnbal1.indihometv.com/atm/DASH/useesport/useesport-avc1_2500000=7-3277707030000000.mpd",
    "nba-tv": "https://cdnbal1.indihometv.com/dassdvr/130/nba/manifest_wuseetv.mpd",
    "spotv": "https://cdnbal1.indihometv.com/dassdvr/130/beib1/manifest_wuseetv.mpd",
    "spotv-2": "https://cdnbal1.indihometv.com/dassdvr/130/beib2/manifest_wuseetv.mpd",
    "al-quran-al-kareem": "https://cdnbal1.indihometv.com/atm/DASH/alquran/alquran-avc1_2500000=7-3277707030000000.mpd",
    "dmi-tv": "https://cdnbal1.indihometv.com/atm/DASH/tawaftv/tawaftv-avc1_2500000=7-3277707030000000.mpd",
    "mqtv": "https://cdnbal1.indihometv.com/atm/DASH/mqtv/mqtv-avc1_2500000=7-3277707030000000.mpd",
    "mtatv": "https://cdnbal1.indihometv.com/atm/DASH/mtatv/mtatv-avc1_2500000=7-3277707030000000.mpd",
    "mui-tv": "https://cdnbal1.indihometv.com/atm/DASH/muitv/muitv-avc1_2500000=7-3277707030000000.mpd",
    "rodja-tv": "https://cdnbal1.indihometv.com/atm/DASH/rodjatv/rodjatv-avc1_2500000=7-3277707030000000.mpd",
    "tv9-nu": "https://cdnbal1.indihometv.com/atm/DASH/tv9/tv9-avc1_2500000=7-3277707030000000.mpd",
    "tvmu": "https://cdnbal1.indihometv.com/atm/DASH/muhammadiyahtv/muhammadiyahtv-avc1_2500000=7-3277707030000000.mpd",
    "uchannel": "https://cdnbal1.indihometv.com/atm/DASH/uchannel/uchannel-avc1_2500000=7-3277707030000000.mpd",
}

NS = "urn:mpeg:dash:schema:mpd:2011"


def get_base_url(mpd_url):
    return mpd_url.rsplit("/", 1)[0] + "/"


def detect_track_type(adapt, rep):
    mime = adapt.get("mimeType", "")
    content_type = adapt.get("contentType", "")
    codecs = rep.get("codecs", adapt.get("codecs", ""))

    if "video" in mime or "video" in content_type:
        return "video"
    if "audio" in mime or "audio" in content_type:
        return "audio"

    video_prefixes = ("avc", "hvc", "hev", "vp8", "vp9", "av01")
    audio_prefixes = ("mp4a", "ac-3", "ec-3", "opus", "vorbis")

    codecs_lower = codecs.lower()
    if any(codecs_lower.startswith(p) for p in video_prefixes):
        return "video"
    if any(codecs_lower.startswith(p) for p in audio_prefixes):
        return "audio"

    if rep.get("width") or rep.get("height") or adapt.get("width") or adapt.get("height"):
        return "video"

    return None


def pick_best_rep(adapt):
    seg_tmpl_adapt = adapt.find(f"{{{NS}}}SegmentTemplate")
    ts_adapt = int(seg_tmpl_adapt.get("timescale", "1")) if seg_tmpl_adapt is not None else 1

    best_rep = None
    best_bw = -1
    best_seg_tmpl = None
    best_ts = ts_adapt

    for rep in adapt.findall(f"{{{NS}}}Representation"):
        bw = int(rep.get("bandwidth", "0"))
        if bw > best_bw:
            rep_seg = rep.find(f"{{{NS}}}SegmentTemplate")
            chosen = rep_seg if rep_seg is not None else seg_tmpl_adapt
            best_rep = rep
            best_bw = bw
            best_seg_tmpl = chosen
            best_ts = int(chosen.get("timescale", str(ts_adapt))) if chosen is not None else ts_adapt

    if best_rep is None or best_seg_tmpl is None:
        return None
    return best_rep, best_seg_tmpl, best_ts


def parse_segments(seg_tmpl, rep_id, base_url, timescale):
    """Returns list of (url, duration_seconds, timestamp)."""
    media_pattern = seg_tmpl.get("media", "")
    seg_timeline = seg_tmpl.find(f"{{{NS}}}SegmentTimeline")
    if seg_timeline is None:
        return []

    segments = []
    current_t = None
    for s in seg_timeline.findall(f"{{{NS}}}S"):
        t = s.get("t")
        d = int(s.get("d"))
        r = int(s.get("r", "0"))
        if t is not None:
            current_t = int(t)
        for _ in range(r + 1):
            name = (
                media_pattern
                .replace("$RepresentationID$", rep_id)
                .replace("$Time$", str(current_t))
            )
            segments.append((base_url + name, d / timescale, current_t))
            current_t += d
    return segments


def build_media_playlist(segs, init_url, is_live, timescale):
    if not segs:
        return None

    if is_live and len(segs) > 5:
        segs = segs[-5:]

    max_dur = max(d for _, d, _ in segs)
    target_dur = math.ceil(max_dur)
    first_t = segs[0][2]
    seg_d_ticks = int(segs[0][1] * timescale)
    media_seq = (first_t // seg_d_ticks) if seg_d_ticks > 0 else 0

    lines = [
        "#EXTM3U",
        "#EXT-X-VERSION:7",
        f"#EXT-X-TARGETDURATION:{target_dur}",
        f"#EXT-X-MEDIA-SEQUENCE:{media_seq}",
    ]
    if not is_live:
        lines.append("#EXT-X-PLAYLIST-TYPE:VOD")

    lines.append(f'#EXT-X-MAP:URI="{init_url}"')
    for seg_url, duration, _ in segs:
        lines.append(f"#EXTINF:{duration:.5f},")
        lines.append(seg_url)
    if not is_live:
        lines.append("#EXT-X-ENDLIST")
    return "\n".join(lines)


def parse_mpd(mpd_url):
    req = urllib.request.Request(mpd_url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=10) as resp:
        content = resp.read()
    root = ET.fromstring(content)
    base_url = get_base_url(mpd_url)
    is_live = root.get("type", "static") == "dynamic"
    return root, base_url, is_live


def get_tracks(root, base_url):
    video_track = None
    audio_track = None

    for period in root.findall(f"{{{NS}}}Period"):
        for adapt in period.findall(f"{{{NS}}}AdaptationSet"):
            result = pick_best_rep(adapt)
            if result is None:
                continue
            rep, seg_tmpl, timescale = result
            track_type = detect_track_type(adapt, rep)

            if track_type == "video" and video_track is None:
                init_pat = seg_tmpl.get("initialization", "")
                init_url = base_url + init_pat.replace("$RepresentationID$", rep.get("id", ""))
                segs = parse_segments(seg_tmpl, rep.get("id", ""), base_url, timescale)
                video_track = {"rep": rep, "seg_tmpl": seg_tmpl, "timescale": timescale,
                               "init_url": init_url, "segs": segs, "adapt": adapt}

            elif track_type == "audio" and audio_track is None:
                init_pat = seg_tmpl.get("initialization", "")
                init_url = base_url + init_pat.replace("$RepresentationID$", rep.get("id", ""))
                segs = parse_segments(seg_tmpl, rep.get("id", ""), base_url, timescale)
                audio_track = {"rep": rep, "seg_tmpl": seg_tmpl, "timescale": timescale,
                               "init_url": init_url, "segs": segs, "adapt": adapt,
                               "lang": adapt.get("lang", "und")}

        if video_track is not None:
            break

    return video_track, audio_track


class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        parsed = urlparse(self.path)
        qs = parse_qs(parsed.query)

        # Resolve channel name
        if "channel" in qs:
            channel = qs["channel"][0].lower()
        else:
            path = parsed.path.lstrip("/")
            channel = re.sub(r"\.m3u8$", "", path).lower()

        if channel not in CHANNELS:
            self._send(404, "text/plain", f"Channel '{channel}' not found.")
            return

        mpd_url = CHANNELS[channel]
        track_type = qs.get("type", [None])[0]  # "video", "audio", or None

        # FIX: Build absolute base URL from Host header so media playlist URIs
        # resolve correctly on all players (mobile browser, VLC, etc.)
        host = self.headers.get("Host", "")
        # Detect scheme: Vercel always serves HTTPS in production
        x_forwarded_proto = self.headers.get("X-Forwarded-Proto", "https")
        scheme = x_forwarded_proto if x_forwarded_proto else "https"
        proxy_base = f"{scheme}://{host}"

        try:
            root, base_url, is_live = parse_mpd(mpd_url)
            video_track, audio_track = get_tracks(root, base_url)

            if video_track is None:
                self._send(500, "text/plain", "Error: No video track found in MPD.")
                return

            v = video_track
            a = audio_track

            if track_type == "video":
                pl = build_media_playlist(v["segs"], v["init_url"], is_live, v["timescale"])
                if pl is None:
                    self._send(500, "text/plain", "Error: No video segments.")
                    return
                self._send(200, "application/vnd.apple.mpegurl", pl)

            elif track_type == "audio":
                if a is None:
                    self._send(404, "text/plain", "No audio track.")
                    return
                pl = build_media_playlist(a["segs"], a["init_url"], is_live, a["timescale"])
                if pl is None:
                    self._send(500, "text/plain", "Error: No audio segments.")
                    return
                self._send(200, "application/vnd.apple.mpegurl", pl)

            else:
                # FIX: Use absolute URLs in master playlist so player can
                # correctly fetch sub-playlists regardless of how it was opened
                v_rep = v["rep"]
                v_codecs = v_rep.get("codecs", "avc1.64001f")
                width = v_rep.get("width", v["adapt"].get("width", "1280"))
                height = v_rep.get("height", v["adapt"].get("height", "720"))
                bandwidth = v_rep.get("bandwidth", "2500000")
                a_codecs = a["rep"].get("codecs", "mp4a.40.2") if a else "mp4a.40.2"

                # Absolute URLs — critical fix for mobile players
                video_uri = f"{proxy_base}/{channel}.m3u8?type=video"
                audio_uri = f"{proxy_base}/{channel}.m3u8?type=audio"

                lines = ["#EXTM3U", "#EXT-X-VERSION:7"]
                if a:
                    lang = a.get("lang", "und")
                    lines.append(
                        f'#EXT-X-MEDIA:TYPE=AUDIO,GROUP-ID="audio",LANGUAGE="{lang}",'
                        f'NAME="Audio",DEFAULT=YES,AUTOSELECT=YES,URI="{audio_uri}"'
                    )
                    lines.append(
                        f'#EXT-X-STREAM-INF:BANDWIDTH={bandwidth},CODECS="{v_codecs},{a_codecs}",'
                        f'RESOLUTION={width}x{height},AUDIO="audio"'
                    )
                else:
                    lines.append(
                        f'#EXT-X-STREAM-INF:BANDWIDTH={bandwidth},CODECS="{v_codecs}",RESOLUTION={width}x{height}'
                    )
                lines.append(video_uri)
                self._send(200, "application/vnd.apple.mpegurl", "\n".join(lines))

        except Exception as e:
            self._send(500, "text/plain", f"Error: {str(e)}")

    def _send(self, code, content_type, body):
        encoded = body.encode("utf-8") if isinstance(body, str) else body
        self.send_response(code)
        self.send_header("Content-Type", content_type)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Cache-Control", "no-cache, no-store")
        self.send_header("Content-Length", str(len(encoded)))
        self.end_headers()
        self.wfile.write(encoded)

    def log_message(self, format, *args):
        pass
