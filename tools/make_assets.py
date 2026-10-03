"""Generate original SVG assets for four steps and GIFs for steps 1–3."""
from pathlib import Path
from xml.sax.saxutils import escape
import sys

try:
    from PIL import Image, ImageDraw, ImageFont
except ImportError as exc:
    raise SystemExit("Install Pillow to regenerate GIFs: python3 -m pip install pillow") from exc

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "assets"
OUT.mkdir(exist_ok=True)

DATA = [
    ("01", "접속 지역 확인", "연결 상태 확인", "US", ["지원 지역 확인", "접속 상태 점검", "가입 화면 열기"], "#D9F1DC", "#3B9970"),
    ("02", "공식 페이지 열기", "ai.meta.com/muse", "↗", ["데스크톱 사이트 보기", "Get inspired 아래 MUSE FOR SMALL BUSINESS 안의 Try Muse 선택"], "#E7E3FB", "#7666B2"),
    ("03", "카드로 연령 확인", "$1 임시 승인 확인", "✓", ["Visa·Mastercard", "$1 승인 확인", "환불 내역 확인"], "#FBEACC", "#B4853C"),
    ("04", "초대 코드 등록", "설정에서 코드 찾기", "★", ["메뉴 열기", "설정 → 일반", "코드 입력"], "#D9EEF4", "#34819C"),
]

def svg(i, number, title, sub, symbol, labels, bg, accent):
    cards = []
    if number == "02":
        cards.append('<rect x="291" y="205" width="263" height="43" rx="12" fill="#F1F4EE"/><text x="305" y="232" font-size="15" font-weight="700" fill="#53665E">데스크톱 사이트 보기</text>')
        cards.append(f'<rect x="291" y="259" width="263" height="96" rx="12" fill="{accent}"/><text x="306" y="284" font-size="14" font-weight="700" fill="#FFFFFF">Get inspired 아래</text><text x="306" y="308" font-size="13" font-weight="700" fill="#FFFFFF">MUSE FOR SMALL BUSINESS</text><text x="306" y="333" font-size="14" font-weight="700" fill="#FFFFFF">안의 Try Muse 선택</text>')
    else:
        for n, label in enumerate(labels):
            y = 205 + 54*n
            fill = accent if n == i else "#F1F4EE"
            fg = "#FFFFFF" if n == i else "#53665E"
            cards.append(f'<rect x="291" y="{y}" width="263" height="43" rx="12" fill="{fill}"/><text x="311" y="{y+27}" font-size="16" font-weight="700" fill="{fg}">{escape(label)}</text><text x="527" y="{y+27}" text-anchor="end" font-size="16" fill="{fg}">↗</text>')
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 620 420" role="img" aria-label="{escape(title)} 예시 그림">
<rect width="620" height="420" rx="24" fill="{bg}"/><circle cx="72" cy="49" r="57" fill="#FFFFFF" opacity=".35"/><circle cx="570" cy="395" r="105" fill="#FFFFFF" opacity=".3"/>
<text x="42" y="62" font-family="Arial,sans-serif" font-size="12" font-weight="800" letter-spacing="3" fill="{accent}">MUSE GUIDE / {number}</text>
<rect x="40" y="92" width="200" height="290" rx="29" fill="#24443C" opacity=".14"/><rect x="34" y="84" width="200" height="290" rx="29" fill="#203E37"/><rect x="44" y="96" width="180" height="265" rx="22" fill="#FFFFFF"/>
<rect x="100" y="102" width="62" height="9" rx="4" fill="#203E37"/><text x="65" y="148" font-family="Arial,sans-serif" font-size="12" font-weight="800" fill="#587468">{number} / 04</text>
<circle cx="134" cy="221" r="58" fill="{bg}"/><text x="134" y="241" text-anchor="middle" font-family="Arial,sans-serif" font-size="47" font-weight="800" fill="{accent}">{escape(symbol)}</text>
<rect x="67" y="302" width="133" height="26" rx="13" fill="{accent}"/><text x="134" y="320" text-anchor="middle" font-family="Arial,sans-serif" font-size="11" font-weight="700" fill="#FFFFFF">STEP {number}</text>
<text x="290" y="126" font-family="Arial,sans-serif" font-size="27" font-weight="800" fill="#243C34">{escape(title)}</text><text x="292" y="158" font-family="Arial,sans-serif" font-size="14" fill="#64786C">{escape(sub)}</text>
{''.join(cards)}<text x="290" y="389" font-family="Arial,sans-serif" font-size="11" fill="#71847A">ILLUSTRATION · NOT AN ACTUAL MUSE SCREEN</text></svg>'''

for i, values in enumerate(DATA):
    (OUT / f"step-{i+1}.svg").write_text(svg(i, *values), encoding="utf-8")

(OUT / "favicon.svg").write_text('''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" rx="17" fill="#173D37"/><text x="8" y="43" font-family="Arial,sans-serif" font-size="39" font-weight="800" fill="#DFF7A1">m·</text></svg>''', encoding="utf-8")
(OUT / "og-cover.svg").write_text('''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 630"><rect width="1200" height="630" fill="#173D37"/><circle cx="1040" cy="270" r="285" fill="#315B4A"/><circle cx="1040" cy="270" r="205" fill="#4F8968"/><text x="75" y="145" font-family="Arial,sans-serif" font-size="29" letter-spacing="5" fill="#DFF7A1">KOREAN QUICK GUIDE</text><text x="72" y="310" font-family="Arial,sans-serif" font-size="95" font-weight="800" fill="#FFFFFF">Muse 시작 가이드</text><text x="77" y="390" font-family="Arial,sans-serif" font-size="35" fill="#B8D0C3">가입 절차를 4단계로 살펴보세요</text><text x="855" y="347" font-family="Arial,sans-serif" font-size="210" font-weight="800" fill="#DFF7A1">m·</text></svg>''', encoding="utf-8")

FONT_PATH = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
try:
    FONT_L = ImageFont.truetype(FONT_PATH, 28)
    FONT_M = ImageFont.truetype(FONT_PATH, 18)
    FONT_S = ImageFont.truetype(FONT_PATH, 15)
except OSError:
    FONT_L = FONT_M = FONT_S = ImageFont.load_default()

def hexrgb(h):
    return tuple(int(h[j:j+2], 16) for j in (1, 3, 5))

for idx, (number, title, sub, symbol, labels, bg, accent) in enumerate(DATA, 1):
    if number == "04":
        continue
    frames = []
    for active in range(len(labels)):
        im = Image.new("RGB", (620, 220), hexrgb(bg))
        d = ImageDraw.Draw(im)
        d.rounded_rectangle((17, 15, 603, 204), radius=18, fill="#FFFDF9")
        d.text((39, 33), f"STEP {number}", font=FONT_S, fill=hexrgb(accent))
        d.text((39, 67), title, font=FONT_L, fill="#243C34")
        if number == "02":
            for j, (x, width) in enumerate(((40, 225), (285, 295))):
                fill = accent if j == active else "#EBF0EA"
                fg = "#FFFFFF" if j == active else "#65766B"
                d.rounded_rectangle((x, 120, x+width, 191), radius=10, fill=fill)
                lines = ("1. 데스크톱 사이트 보기",) if j == 0 else ("2. Get inspired 아래", "MUSE FOR SMALL BUSINESS", "안의 Try Muse 선택")
                for line_idx, line in enumerate(lines):
                    d.text((x+11, 128+line_idx*18), line, font=FONT_S, fill=fg)
        else:
            for j, label in enumerate(labels):
                x = 40 + j*186
                fill = accent if j == active else "#EBF0EA"
                fg = "#FFFFFF" if j == active else "#65766B"
                d.rounded_rectangle((x, 132, x+168, 178), radius=10, fill=fill)
                d.text((x+12, 144), f"{j+1}. {label}", font=FONT_M, fill=fg)
                if j < 2:
                    d.text((x+170, 144), "›", font=FONT_M, fill="#789284")
        frames.extend([im] * 3)
    frames[0].save(OUT / f"step-{idx}.gif", save_all=True, append_images=frames[1:], duration=333, loop=0, optimize=True)

print("Created four SVG illustrations, three GIF animations, and branding assets.")
