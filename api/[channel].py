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


def parse_segments(seg_template, rep_id, base_url, timescale):
    """Parse SegmentTimeline into list of (url, duration_seconds)."""
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
            seg_name = (
                media_pattern
                .replace("$RepresentationID$", rep_id)
                .replace("$Time$", str(current_t))
            )
            segments.append((base_url + seg_name, d / timescale, current_t))
            current_t += d
    return segments


def pick_best_rep(adapt, base_url):
    """
    From an AdaptationSet, pick the Representation with highest bandwidth.
    Returns (rep, seg_template, timescale) or None.
    """
    seg_template_adapt = adapt.find(f"{{{NS}}}SegmentTemplate")
    timescale_adapt = int(seg_template_adapt.get("timescale", "1")) if seg_template_adapt is not None else 1

    best_rep = None
    best_bw = -1
    best_seg_template = None
    best_timescale = timescale_adapt

    for rep in adapt.findall(f"{{{NS}}}Representation"):
        bw = int(rep.get("bandwidth", "0"))
        if bw > best_bw:
            rep_seg = rep.find(f"{{{NS}}}SegmentTemplate")
            best_rep = rep
            best_bw = bw
            best_seg_template = rep_seg if rep_seg is not None else seg_template_adapt
            best_timescale = int(best_seg_template.get("timescale", str(timescale_adapt))) if best_seg_template is not None else timescale_adapt

    return (best_rep, best_seg_template, best_timescale) if best_rep else None


def mpd_to_m3u8(mpd_url):
    req = urllib.request.Request(mpd_url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=10) as resp:
        mpd_content = resp.read()

    root = ET.fromstring(mpd_content)
    base_url = get_base_url(mpd_url)

    # Determine if live stream
    mpd_type = root.get("type", "static")
    is_live = (mpd_type == "dynamic")

    video_rep = audio_rep = None
    video_seg_tmpl = audio_seg_tmpl = None
    video_timescale = audio_timescale = 1
    video_init = audio_init = None

    for period in root.findall(f"{{{NS}}}Period"):
        for adapt in period.findall(f"{{{NS}}}AdaptationSet"):
            mime = adapt.get("mimeType", "")
            content_type = adapt.get("contentType", "")
            lang = adapt.get("lang", "")

            is_video = "video" in mime or "video" in content_type
            is_audio = "audio" in mime or "audio" in content_type

            result = pick_best_rep(adapt, base_url)
            if result is None:
                continue
            rep, seg_tmpl, timescale = result

            if is_video and video_rep is None:
                video_rep = rep
                video_seg_tmpl = seg_tmpl
                video_timescale = timescale
                init_pattern = seg_tmpl.get("initialization", "")
                video_init = base_url + init_pattern.replace("$RepresentationID$", rep.get("id"))

            elif is_audio and audio_rep is None:
                audio_rep = rep
                audio_seg_tmpl = seg_tmpl
                audio_timescale = timescale
                init_pattern = seg_tmpl.get("initialization", "")
                audio_init = base_url + init_pattern.replace("$RepresentationID$", rep.get("id"))

    if video_rep is None:
        return None, "No video representation found"

    # Parse video segments
    video_segs = parse_segments(video_seg_tmpl, video_rep.get("id"), base_url, video_timescale)
    if not video_segs:
        return None, "No video segments found"

    # Parse audio segments (if separate AdaptationSet)
    audio_segs = []
    if audio_rep is not None and audio_seg_tmpl is not None:
        audio_segs = parse_segments(audio_seg_tmpl, audio_rep.get("id"), base_url, audio_timescale)

    # Compute target duration (max segment duration, ceiling)
    max_duration = max(d for _, d, _ in video_segs)
    target_duration = math.ceil(max_duration)

    # Media sequence: based on first segment timestamp / segment duration (for live positioning)
    first_t = video_segs[0][2]
    seg_dur_ticks = int(video_segs[0][1] * video_timescale)
    media_sequence = first_t // seg_dur_ticks if seg_dur_ticks > 0 else 0

    # Build video codecs string
    video_codecs = video_rep.get("codecs", "avc1.64001f")
    width = video_rep.get("width", "1280")
    height = video_rep.get("height", "720")
    bandwidth = video_rep.get("bandwidth", "2500000")

    # Build audio codecs string
    audio_codecs = ""
    if audio_rep is not None:
        audio_codecs = audio_rep.get("codecs", "mp4a.40.2")

    # Combined codecs for STREAM-INF
    combined_codecs = f"{video_codecs},{audio_codecs}" if audio_codecs else video_codecs

    # -----------------------------------------------------------------
    # If there is a separate audio track, build a multi-variant master
    # playlist that references two separate media playlists — BUT since
    # Vercel serverless can't serve multiple sub-routes from one handler,
    # we embed both tracks inline using EXT-X-MEDIA + byte-range tricks.
    #
    # Simpler approach for compatibility: produce a single media playlist
    # that interleaves #EXT-X-MAP for audio init then video init.
    # Most players (hls.js, VLC, ExoPlayer) handle muxed-like playlists
    # when audio segs map 1:1 with video segs.
    # -----------------------------------------------------------------

    lines = []
    lines.append("#EXTM3U")
    lines.append("#EXT-X-VERSION:7")
    lines.append(f"#EXT-X-TARGETDURATION:{target_duration}")
    lines.append(f"#EXT-X-MEDIA-SEQUENCE:{media_sequence}")

    if is_live:
        # Live: tell player this is an event/live playlist, keep refreshing
        lines.append("#EXT-X-PLAYLIST-TYPE:EVENT")
    else:
        lines.append("#EXT-X-PLAYLIST-TYPE:VOD")

    # Audio init map (must come before first audio segment reference)
    if audio_init:
        lines.append(f'#EXT-X-MAP:URI="{audio_init}"')
        # Audio segments interleaved before video init
        for seg_url, duration, _ in audio_segs:
            lines.append(f"#EXTINF:{duration:.5f},")
            lines.append(seg_url)

    # Video init map
    lines.append(f'#EXT-X-MAP:URI="{video_init}"')

    # Video segments
    for seg_url, duration, _ in video_segs:
        lines.append(f"#EXTINF:{duration:.5f},")
        lines.append(seg_url)

    if not is_live:
        lines.append("#EXT-X-ENDLIST")

    return "\n".join(lines), None


# -----------------------------------------------------------------
# ALTERNATIVE: proper muxed approach using separate audio/video tracks
# Build a MASTER playlist + inline media playlists via path suffix
# This is commented out above in favor of the simpler approach.
# Uncomment this block and adjust routing in vercel.json if needed.
# -----------------------------------------------------------------

def mpd_to_master_m3u8(mpd_url, base_request_url, channel):
    """
    Returns a proper HLS master playlist that references:
      - video media playlist: /channel.m3u8?type=video
      - audio media playlist: /channel.m3u8?type=audio
    Player fetches both and muxes them client-side (standard HLS).
    """
    req = urllib.request.Request(mpd_url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=10) as resp:
        mpd_content = resp.read()

    root = ET.fromstring(mpd_content)
    base_url = get_base_url(mpd_url)

    video_rep = audio_rep = None
    video_seg_tmpl = audio_seg_tmpl = None
    video_timescale = audio_timescale = 1
    video_init = audio_init = None
    audio_lang = "und"

    for period in root.findall(f"{{{NS}}}Period"):
        for adapt in period.findall(f"{{{NS}}}AdaptationSet"):
            mime = adapt.get("mimeType", "")
            content_type = adapt.get("contentType", "")
            is_video = "video" in mime or "video" in content_type
            is_audio = "audio" in mime or "audio" in content_type

            result = pick_best_rep(adapt, base_url)
            if result is None:
                continue
            rep, seg_tmpl, timescale = result

            if is_video and video_rep is None:
                video_rep, video_seg_tmpl, video_timescale = rep, seg_tmpl, timescale
                init_pat = seg_tmpl.get("initialization", "")
                video_init = base_url + init_pat.replace("$RepresentationID$", rep.get("id"))

            elif is_audio and audio_rep is None:
                audio_rep, audio_seg_tmpl, audio_timescale = rep, seg_tmpl, timescale
                audio_lang = adapt.get("lang", "und")
                init_pat = seg_tmpl.get("initialization", "")
                audio_init = base_url + init_pat.replace("$RepresentationID$", rep.get("id"))

    if video_rep is None:
        return None, None, "No video representation found"

    video_codecs = video_rep.get("codecs", "avc1.64001f")
    audio_codecs = audio_rep.get("codecs", "mp4a.40.2") if audio_rep else "mp4a.40.2"
    width = video_rep.get("width", "1280")
    height = video_rep.get("height", "720")
    bandwidth = video_rep.get("bandwidth", "2500000")

    audio_url = f"/{channel}.m3u8?type=audio"
    video_url = f"/{channel}.m3u8?type=video"

    master_lines = ["#EXTM3U", "#EXT-X-VERSION:7"]
    if audio_rep is not None:
        master_lines.append(
            f'#EXT-X-MEDIA:TYPE=AUDIO,GROUP-ID="audio",LANGUAGE="{audio_lang}",'
            f'NAME="Audio",DEFAULT=YES,AUTOSELECT=YES,URI="{audio_url}"'
        )
        master_lines.append(
            f'#EXT-X-STREAM-INF:BANDWIDTH={bandwidth},CODECS="{video_codecs},{audio_codecs}",'
            f'RESOLUTION={width}x{height},AUDIO="audio"'
        )
    else:
        master_lines.append(
            f'#EXT-X-STREAM-INF:BANDWIDTH={bandwidth},CODECS="{video_codecs}",'
            f'RESOLUTION={width}x{height}'
        )
    master_lines.append(video_url)

    # Build video media playlist
    video_segs = parse_segments(video_seg_tmpl, video_rep.get("id"), base_url, video_timescale)
    mpd_type = root.get("type", "static")
    is_live = mpd_type == "dynamic"
    max_dur = max(d for _, d, _ in video_segs) if video_segs else 4
    target_dur = math.ceil(max_dur)
    first_t = video_segs[0][2] if video_segs else 0
    seg_ticks = int(video_segs[0][1] * video_timescale) if video_segs else 1
    media_seq = first_t // seg_ticks if seg_ticks else 0

    vlines = [
        "#EXTM3U", "#EXT-X-VERSION:7",
        f"#EXT-X-TARGETDURATION:{target_dur}",
        f"#EXT-X-MEDIA-SEQUENCE:{media_seq}",
        "#EXT-X-PLAYLIST-TYPE:EVENT" if is_live else "#EXT-X-PLAYLIST-TYPE:VOD",
        f'#EXT-X-MAP:URI="{video_init}"',
    ]
    for seg_url, duration, _ in video_segs:
        vlines.append(f"#EXTINF:{duration:.5f},")
        vlines.append(seg_url)
    if not is_live:
        vlines.append("#EXT-X-ENDLIST")

    # Build audio media playlist
    alines = None
    if audio_rep is not None:
        audio_segs = parse_segments(audio_seg_tmpl, audio_rep.get("id"), base_url, audio_timescale)
        a_max_dur = max(d for _, d, _ in audio_segs) if audio_segs else 4
        a_target_dur = math.ceil(a_max_dur)
        a_first_t = audio_segs[0][2] if audio_segs else 0
        a_seg_ticks = int(audio_segs[0][1] * audio_timescale) if audio_segs else 1
        a_media_seq = a_first_t // a_seg_ticks if a_seg_ticks else 0
        alines = [
            "#EXTM3U", "#EXT-X-VERSION:7",
            f"#EXT-X-TARGETDURATION:{a_target_dur}",
            f"#EXT-X-MEDIA-SEQUENCE:{a_media_seq}",
            "#EXT-X-PLAYLIST-TYPE:EVENT" if is_live else "#EXT-X-PLAYLIST-TYPE:VOD",
            f'#EXT-X-MAP:URI="{audio_init}"',
        ]
        for seg_url, duration, _ in audio_segs:
            alines.append(f"#EXTINF:{duration:.5f},")
            alines.append(seg_url)
        if not is_live:
            alines.append("#EXT-X-ENDLIST")

    return "\n".join(master_lines), "\n".join(vlines), "\n".join(alines) if alines else None, None


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
        track_type = qs.get("type", [None])[0]  # "video", "audio", or None (master)

        try:
            master, video_pl, audio_pl, error = mpd_to_master_m3u8(
                mpd_url, self.path, channel
            )
            if error:
                self._send(500, "text/plain", f"Error: {error}")
                return

            if track_type == "audio":
                if audio_pl:
                    self._send(200, "application/vnd.apple.mpegurl", audio_pl)
                else:
                    self._send(404, "text/plain", "No audio track available.")
            elif track_type == "video":
                self._send(200, "application/vnd.apple.mpegurl", video_pl)
            else:
                # Default: serve master playlist
                self._send(200, "application/vnd.apple.mpegurl", master)

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
        pass  # suppress default stderr logging on Vercel
