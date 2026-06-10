const CHANNELS = {
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
};

const HEADERS = {
  "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
  "Referer": "https://www.indihometv.com/",
  "Origin": "https://www.indihometv.com",
};

const CORS = {
  "Access-Control-Allow-Origin": "*",
  "Access-Control-Allow-Methods": "GET, OPTIONS",
  "Access-Control-Allow-Headers": "*",
};

const NS = "urn:mpeg:dash:schema:mpd:2011";
const WINDOW = 20; // 20 segmen x 2 detik = 40 detik buffer

function getBaseUrl(mpdUrl) {
  return mpdUrl.substring(0, mpdUrl.lastIndexOf("/") + 1);
}

function parseSegments(segTmpl, repId, baseUrl, timescale) {
  const media = segTmpl.getAttribute("media") || "";
  const timeline = segTmpl.getElementsByTagNameNS(NS, "SegmentTimeline")[0]
    || segTmpl.getElementsByTagName("SegmentTimeline")[0];
  if (!timeline) return [];

  const segs = [];
  let currentT = null;
  const sList = timeline.getElementsByTagNameNS
    ? [...timeline.getElementsByTagNameNS(NS, "S")]
    : [...timeline.getElementsByTagName("S")];

  for (const s of sList) {
    const t = s.getAttribute("t");
    const d = parseInt(s.getAttribute("d"));
    const r = parseInt(s.getAttribute("r") || "0");
    if (t !== null) currentT = parseInt(t);
    for (let i = 0; i <= r; i++) {
      const name = media
        .replace("$RepresentationID$", repId)
        .replace("$Time$", String(currentT));
      segs.push({ url: baseUrl + name, dur: d / timescale, t: currentT });
      currentT += d;
    }
  }
  return segs;
}

function buildMediaPlaylist(initUrl, segs, totalSegs) {
  const win = segs.slice(-WINDOW);
  const seq = totalSegs - win.length;
  const target = Math.ceil(Math.max(...win.map(s => s.dur))) + 1;

  const lines = [
    "#EXTM3U",
    "#EXT-X-VERSION:7",
    `#EXT-X-TARGETDURATION:${target}`,
    `#EXT-X-MEDIA-SEQUENCE:${seq}`,
    "#EXT-X-INDEPENDENT-SEGMENTS",
    `#EXT-X-MAP:URI="${initUrl}"`,
  ];

  for (const seg of win) {
    lines.push(`#EXTINF:${seg.dur.toFixed(5)},`);
    lines.push(seg.url);
  }

  return lines.join("\n");
}

async function parseMpd(mpdUrl) {
  const resp = await fetch(mpdUrl, { headers: HEADERS });
  if (!resp.ok) throw new Error(`MPD fetch failed: ${resp.status}`);
  const text = await resp.text();

  const parser = new DOMParser();
  const doc = parser.parseFromString(text, "application/xml");
  const baseUrl = getBaseUrl(mpdUrl);

  let videoRep = null, videoTmpl = null, videoTs = 1, bestBw = 0;
  let audioRep = null, audioTmpl = null, audioTs = 1;

  const adaptSets = [...doc.getElementsByTagNameNS(NS, "AdaptationSet"),
                     ...doc.getElementsByTagName("AdaptationSet")];
  const seen = new Set();
  const uniqueAdapts = adaptSets.filter(a => { if (seen.has(a)) return false; seen.add(a); return true; });

  for (const adapt of uniqueAdapts) {
    const mime = adapt.getAttribute("mimeType") || "";
    const ctype = adapt.getAttribute("contentType") || "";
    const adaptTmpl = adapt.getElementsByTagNameNS(NS, "SegmentTemplate")[0]
      || adapt.getElementsByTagName("SegmentTemplate")[0];
    if (!adaptTmpl) continue;
    const ts = parseInt(adaptTmpl.getAttribute("timescale") || "1");

    const isAudio = mime.includes("audio") || ctype.includes("audio");
    const isVideo = mime.includes("video") || ctype.includes("video");

    const reps = [...(adapt.getElementsByTagNameNS(NS, "Representation").length
      ? adapt.getElementsByTagNameNS(NS, "Representation")
      : adapt.getElementsByTagName("Representation"))];

    if (isAudio && !audioRep) {
      audioRep = reps[0];
      audioTmpl = audioRep?.getElementsByTagNameNS(NS, "SegmentTemplate")[0]
        || audioRep?.getElementsByTagName("SegmentTemplate")[0]
        || adaptTmpl;
      audioTs = ts;
    } else if (isVideo) {
      for (const rep of reps) {
        const bw = parseInt(rep.getAttribute("bandwidth") || "0");
        if (bw > bestBw) {
          bestBw = bw;
          videoRep = rep;
          videoTmpl = rep.getElementsByTagNameNS(NS, "SegmentTemplate")[0]
            || rep.getElementsByTagName("SegmentTemplate")[0]
            || adaptTmpl;
          videoTs = ts;
        }
      }
    }
  }

  if (!videoRep) throw new Error("No video representation found");

  const vidId = videoRep.getAttribute("id");
  const vidCodecs = videoRep.getAttribute("codecs") || "avc1.64001f";
  const vidBw = videoRep.getAttribute("bandwidth") || "1500000";
  const vidW = videoRep.getAttribute("width") || "1280";
  const vidH = videoRep.getAttribute("height") || "720";
  const vidInit = baseUrl + (videoTmpl.getAttribute("initialization") || "").replace("$RepresentationID$", vidId);
  const vidSegs = parseSegments(videoTmpl, vidId, baseUrl, videoTs);

  let audId, audCodecs, audInit, audSegs;
  if (audioRep) {
    audId = audioRep.getAttribute("id");
    audCodecs = audioRep.getAttribute("codecs") || "mp4a.40.2";
    audInit = baseUrl + (audioTmpl.getAttribute("initialization") || "").replace("$RepresentationID$", audId);
    audSegs = parseSegments(audioTmpl, audId, baseUrl, audioTs);
  }

  return { vidId, vidCodecs, vidBw, vidW, vidH, vidInit, vidSegs, audId, audCodecs, audInit, audSegs };
}

export default async function handler(req) {
  const url = new URL(req.url);
  const channel = url.searchParams.get("channel") || url.pathname.replace(/^\//, "").replace(/\.m3u8$/, "").replace(/-?(video|audio)$/, "");
  const type = url.searchParams.get("type") || "master";

  if (req.method === "OPTIONS") {
    return new Response(null, { status: 204, headers: CORS });
  }

  if (!CHANNELS[channel]) {
    return new Response(`Channel '${channel}' not found`, { status: 404, headers: CORS });
  }

  try {
    const mpd = await parseMpd(CHANNELS[channel]);

    if (type === "video") {
      const playlist = buildMediaPlaylist(mpd.vidInit, mpd.vidSegs, mpd.vidSegs.length);
      return new Response(playlist, {
        headers: { ...CORS, "Content-Type": "application/vnd.apple.mpegurl", "Cache-Control": "no-cache" }
      });
    }

    if (type === "audio") {
      if (!mpd.audSegs) return new Response("No audio", { status: 404, headers: CORS });
      const playlist = buildMediaPlaylist(mpd.audInit, mpd.audSegs, mpd.audSegs.length);
      return new Response(playlist, {
        headers: { ...CORS, "Content-Type": "application/vnd.apple.mpegurl", "Cache-Control": "no-cache" }
      });
    }

    // master
    const lines = ["#EXTM3U", "#EXT-X-VERSION:7", "#EXT-X-INDEPENDENT-SEGMENTS"];
    if (mpd.audSegs) {
      lines.push(`#EXT-X-MEDIA:TYPE=AUDIO,GROUP-ID="audio",NAME="Audio",DEFAULT=YES,URI="${channel}-audio.m3u8"`);
      lines.push(`#EXT-X-STREAM-INF:BANDWIDTH=${mpd.vidBw},CODECS="${mpd.vidCodecs},${mpd.audCodecs}",RESOLUTION=${mpd.vidW}x${mpd.vidH},AUDIO="audio"`);
    } else {
      lines.push(`#EXT-X-STREAM-INF:BANDWIDTH=${mpd.vidBw},CODECS="${mpd.vidCodecs}",RESOLUTION=${mpd.vidW}x${mpd.vidH}`);
    }
    lines.push(`${channel}-video.m3u8`);

    return new Response(lines.join("\n"), {
      headers: { ...CORS, "Content-Type": "application/vnd.apple.mpegurl", "Cache-Control": "no-cache" }
    });

  } catch (e) {
    return new Response(`Error: ${e.message}`, { status: 500, headers: CORS });
  }
}

export const config = { runtime: "edge" };
