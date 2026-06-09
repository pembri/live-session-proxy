import re
import time
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
WINDOW = 5
CACHE_TTL = 2
_cache = {}


def fetch_mpd(mpd_url):
    now = time.time()
    if mpd_url in _cache:
        ts, data = _cache[mpd_url]
        if now - ts < CACHE_TTL:
            return data
    req = urllib.request.Request(mpd_url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=10) as resp:
        data = resp.read()
    _cache[mpd_url] = (now, data)
    return data


def get_base_url(mpd_url):
    return mpd_url.rsplit("/", 1)[0] + "/"


def parse_segment_timeline(seg_template, rep_id, base_url, timescale):
    media_pattern = seg_template.get("media", "")
    seg_timeline = seg_template.find(f"{{{NS}}}SegmentTimeline")
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
            seg_name = media_pattern \
                .replace("$RepresentationID$", rep_id) \
                .replace("$Time$", str(current_t))
            seg_url = base_url + seg_name
            duration = d / timescale
            segments.append((seg_url, duration, current_t))
            current_t += d
    return segments


def mpd_to_m3u8(mpd_url):
    mpd_bytes = fetch_mpd(mpd_url)
    root = ET.fromstring(mpd_bytes)
    base_url = get_base_url(mpd_url)

    best_rep = None
    best_bw = 0
    best_seg_template = None
    best_timescale = 1

    for period in root.findall(f"{{{NS}}}Period"):
        for adapt in period.findall(f"{{{NS}}}AdaptationSet"):
            mime = adapt.get("mimeType", "")
            content_type = adapt.get("contentType", "")
            if "video" not in mime and "video" not in content_type:
                continue
            seg_template = adapt.find(f"{{{NS}}}SegmentTemplate")
            if seg_template is None:
                continue
            timescale = int(seg_template.get("timescale", "1"))
            for rep in adapt.findall(f"{{{NS}}}Representation"):
                bw = int(rep.get("bandwidth", "0"))
                if bw > best_bw:
                    rep_seg = rep.find(f"{{{NS}}}SegmentTemplate")
                    best_rep = rep
                    best_bw = bw
                    best_seg_template = rep_seg if rep_seg is not None else seg_template
                    best_timescale = timescale

    if best_rep is None:
        return None, "No video representation found"

    rep_id = best_rep.get("id")
    bandwidth = best_rep.get("bandwidth", "1500000")

    init_pattern = best_seg_template.get("initialization", "")
    init_url = base_url + init_pattern.replace("$RepresentationID$", rep_id)

    all_segments = parse_segment_timeline(best_seg_template, rep_id, base_url, best_timescale)
    if not all_segments:
        return None, "No segments found"

    # Ambil WINDOW segment terakhir (live edge)
    window = all_segments[-WINDOW:]

    # MEDIA-SEQUENCE = index absolut segment pertama di window
    # Gunakan t/timescale sebagai sequence number agar naik tiap poll
    first_t = window[0][2]
    d_per_seg = window[0][1]  # durasi detik
    # seq = posisi waktu / durasi per segment (integer increment per segment)
    media_seq = int(first_t / best_timescale / d_per_seg)

    max_dur = max(d for _, d, _ in window)
    target_dur = int(max_dur) + 1

    lines = []
    lines.append("#EXTM3U")
    lines.append("#EXT-X-VERSION:7")
    lines.append(f"#EXT-X-TARGETDURATION:{target_dur}")
    lines.append(f"#EXT-X-MEDIA-SEQUENCE:{media_seq}")
    lines.append(f'#EXT-X-MAP:URI="{init_url}"')

    for seg_url, duration, _ in window:
        lines.append(f"#EXTINF:{duration:.5f},")
        lines.append(seg_url)

    return "\n".join(lines), None


class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed = urlparse(self.path)
        qs = parse_qs(parsed.query)

        if "channel" in qs:
            channel = qs["channel"][0].lower()
        else:
            path = parsed.path.lstrip("/")
            channel = re.sub(r"\.m3u8$", "", path).lower()

        if channel not in CHANNELS:
            self.send_response(404)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(f"Channel '{channel}' not found.".encode())
            return

        mpd_url = CHANNELS[channel]

        try:
            m3u8_content, error = mpd_to_m3u8(mpd_url)
            if error:
                self.send_response(500)
                self.send_header("Content-Type", "text/plain")
                self.end_headers()
                self.wfile.write(f"Error: {error}".encode())
                return

            self.send_response(200)
            self.send_header("Content-Type", "application/vnd.apple.mpegurl")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.send_header("Cache-Control", "no-cache, no-store")
            self.end_headers()
            self.wfile.write(m3u8_content.encode())

        except Exception as e:
            self.send_response(500)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(f"Error: {str(e)}".encode())
