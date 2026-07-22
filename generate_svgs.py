import os

with open('ascii-art.txt', 'r', encoding='utf-8') as f:
    ascii_lines = [line.rstrip('\r\n') for line in f if line.strip()]

print(f"Read {len(ascii_lines)} ascii lines.")

def generate_svg(is_dark=True):
    bg_glow_start = '#0B1120' if is_dark else '#F8FAFC'
    bg_glow_end = '#050816' if is_dark else '#E2E8F0'
    
    title_bg = '#0B1120' if is_dark else '#FFFFFF'
    title_bg_opacity = '0.85' if is_dark else '0.9'
    
    box_bg = '#0B1120' if is_dark else '#FFFFFF'
    box_bg_opacity = '0.35' if is_dark else '0.55'
    box_stroke_opacity = '0.35' if is_dark else '0.4'
    
    scan_line_color = '#7DD3FC' if is_dark else '#334155'
    scan_line_opacity = '0.05' if is_dark else '0.035'
    
    scan_grad_stop1 = '#22D3EE' if is_dark else '#0EA5E9'
    scan_grad_stop2 = '#A5F3FC' if is_dark else '#38BDF8'
    scan_grad_stop3 = '#7C3AED' if is_dark else '#7C3AED'
    scan_blend_mode = 'mix-blend-mode:screen' if is_dark else 'mix-blend-mode:multiply'
    
    ascii_stop1_start = '#22D3EE' if is_dark else '#4F46E5'
    ascii_stop1_vals = '#22D3EE;#7C3AED;#38BDF8;#22D3EE' if is_dark else '#4F46E5;#7C3AED;#0EA5E9;#4F46E5'
    ascii_stop2_start = '#7C3AED' if is_dark else '#7C3AED'
    ascii_stop2_vals = '#7C3AED;#38BDF8;#22D3EE;#7C3AED' if is_dark else '#7C3AED;#0EA5E9;#4F46E5;#7C3AED'
    
    key_color = '#22D3EE' if is_dark else '#0284C7'
    val_color = '#E5E7EB' if is_dark else '#1E293B'
    cc_color = '#475569' if is_dark else '#94A3B8'
    head_color = '#7C3AED' if is_dark else '#7C3AED'
    accent_color = '#10B981' if is_dark else '#059669'
    title_text_color = '#DBEAFE' if is_dark else '#1E293B'
    term_label_color = '#64748B'
    scan_label_color = '#F87171' if is_dark else '#DC2626'
    panel_title_color = '#38BDF8' if is_dark else '#0284C7'
    panel_title_opacity = '0.7' if is_dark else '0.75'

    # Build ASCII tspans
    ascii_tspans = []
    start_y = 64.0
    step_y = 10.4
    for i, line in enumerate(ascii_lines):
        y_pos = round(start_y + i * step_y, 2)
        ascii_tspans.append(f'<tspan x="30" y="{y_pos}" xml:space="preserve">{line}</tspan>')
    ascii_content = '\n'.join(ascii_tspans)

    def xml_esc(s):
        return s.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')

    # Info lines definition
    info_lines_def = [
        ('head', 'nblancs@devs', 'cc', ' -——————————————————————————————————————————-—-'),
        ('cc', '. ', 'key', 'Subject', 'cc', ': .......................... ', 'val', 'Noel Jhumel Blanco'),
        ('cc', '. ', 'key', 'Role', 'cc', ': ............................. ', 'val', 'Software Developer · IT Student'),
        ('cc', '. ', 'key', 'Origin', 'cc', ': ........................... ', 'val', 'Philippines'),
        ('cc', '. ', 'key', 'Education', 'cc', ': ......................... ', 'val', 'BS Information Technology · USTP'),
        ('cc', '. ', 'key', 'Status', 'cc', ': ............ ', 'val', xml_esc('Learning Neovim & Arch • Shipping')),
        ('cc', '. ', 'key', 'ToolChain', 'cc', ': ................. ', 'val', 'Neovim, Git, VS Code, Linux/Arch'),
        ('cc', '. '),
        ('cc', '. ', 'key', 'Core.Lang', 'cc', ': .......... ', 'val', 'Java, Python, C, JavaScript, PHP, Kotlin'),
        ('cc', '. ', 'key', 'Core.Frontend', 'cc', ': ...... ', 'val', 'React, Next.js, Vite, HTML5, CSS3'),
        ('cc', '. ', 'key', 'Core.Backend', 'cc', ': ....... ', 'val', 'Laravel, Node.js, REST APIs'),
        ('cc', '. ', 'key', 'Core.Database', 'cc', ': ...... ', 'val', 'MySQL, SQLite, Supabase, Firebase'),
        ('cc', '. ', 'key', 'Core.Mobile', 'cc', ': ........ ', 'val', 'Android Studio, Kotlin, Java'),
        ('cc', '. '),
        ('accent', '- Contact', 'cc', ' -————————————————————————————————————————————-—-'),
        ('cc', '. ', 'key', 'Grid.Mail', 'cc', ': ....................... ', 'val', 'blanco.noeljhumel1@gmail.com'),
        ('cc', '. ', 'key', 'Grid.Portfolio', 'cc', ': .................. ', 'val', 'https://nblancs.vercel.app/'),
        ('cc', '. ', 'key', 'Grid.ProfileCard', 'cc', ': ................. ', 'val', 'profile-card-opal-one.vercel.app'),
        ('cc', '. ', 'key', 'Grid.Monkeytype', 'cc', ': .................. ', 'val', 'monkeytype.com/profile/nblancs'),
        ('cc', '. ', 'key', 'Grid.Github', 'cc', ': ..................... ', 'val', 'NBlancs'),
    ]

    clip_paths = []
    info_groups = []
    line_css_rules = []
    
    y_positions = [
        42, 64, 86, 108, 130, 152, 174, 194,
        214, 236, 258, 280, 302, 322,
        342, 364, 386, 408, 430, 450, 470,
        490, 510
    ]
    
    begin_start = 0.75
    begin_step = 0.11

    for idx, item in enumerate(info_lines_def):
        begin_time = round(begin_start + idx * begin_step, 2)
        y_pos = y_positions[idx]
        
        clip_paths.append(
            f'<clipPath id="lc{idx}"><rect class="line-rect-{idx}" x="500" y="{y_pos - 16:.2f}" width="0" height="24">'
            f'<animate attributeName="width" from="0" to="690" dur="0.38s" begin="{begin_time}s" fill="freeze"/></rect></clipPath>'
        )
        
        line_css_rules.append(
            f'.line-rect-{idx} {{ animation: typeLine 0.38s ease-out {begin_time}s forwards; }}'
        )
        
        # Build line tspans
        if len(item) == 1 and item[0] == 'cc':
            tspans_str = f'<tspan x="520" y="{y_pos}" class="cc">. </tspan>'
        else:
            tspans_str = f'<tspan x="520" y="{y_pos}"'
            i = 0
            first = True
            while i < len(item):
                cls = item[i]
                txt = item[i+1]
                if first:
                    tspans_str += f' class="{cls}">{txt}</tspan>'
                    first = False
                else:
                    tspans_str += f'<tspan class="{cls}">{txt}</tspan>'
                i += 2
                
        group_str = f'<g clip-path="url(#lc{idx})"><text x="520" y="0" fill="{title_text_color}">{tspans_str}</text></g>'
        info_groups.append(group_str)

    clip_paths_str = '\n  '.join(clip_paths)
    info_groups_str = '\n  '.join(info_groups)
    line_css_str = '\n    '.join(line_css_rules)

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="1180" height="610" viewBox="0 0 1180 610">
<defs>
  <linearGradient id="asciiGrad" x1="0%" y1="0%" x2="100%" y2="100%">
    <stop offset="0%" stop-color="{ascii_stop1_start}">
      <animate attributeName="stop-color" values="{ascii_stop1_vals}" dur="9s" repeatCount="indefinite"/>
    </stop>
    <stop offset="100%" stop-color="{ascii_stop2_start}">
      <animate attributeName="stop-color" values="{ascii_stop2_vals}" dur="9s" repeatCount="indefinite"/>
    </stop>
  </linearGradient>
  <linearGradient id="borderGrad" x1="0%" y1="0%" x2="100%" y2="100%">
    <stop offset="0%" stop-color="#7C3AED"/>
    <stop offset="50%" stop-color="#22D3EE"/>
    <stop offset="100%" stop-color="#10B981"/>
  </linearGradient>
  <radialGradient id="bgGlow" cx="30%" cy="20%" r="80%">
    <stop offset="0%" stop-color="{bg_glow_start}"/>
    <stop offset="100%" stop-color="{bg_glow_end}"/>
  </radialGradient>
  <linearGradient id="scanGrad" x1="0%" y1="0%" x2="0%" y2="100%">
    <stop offset="0%" stop-color="{scan_grad_stop1}" stop-opacity="0"/>
    <stop offset="45%" stop-color="{scan_grad_stop1}" stop-opacity="0.05"/>
    <stop offset="50%" stop-color="{scan_grad_stop2}" stop-opacity="0.65"/>
    <stop offset="55%" stop-color="{scan_grad_stop1}" stop-opacity="0.05"/>
    <stop offset="100%" stop-color="{scan_grad_stop3}" stop-opacity="0"/>
  </linearGradient>
  <pattern id="scanlines" width="4" height="4" patternUnits="userSpaceOnUse">
    <rect width="4" height="1" fill="{scan_line_color}" opacity="{scan_line_opacity}"/>
  </pattern>
  <filter id="softGlow" x="-50%" y="-50%" width="200%" height="200%">
    <feGaussianBlur stdDeviation="4" result="blur"/>
    <feMerge>
      <feMergeNode in="blur"/>
      <feMergeNode in="SourceGraphic"/>
    </feMerge>
  </filter>
  <mask id="revealMask" maskUnits="userSpaceOnUse" x="0" y="0" width="1180" height="620">
    <rect class="mask-rect" x="0" y="0" width="1180" height="0" fill="#fff">
      <animate attributeName="height" from="0" to="560" dur="2.6s" begin="0.2s" fill="freeze" calcMode="spline" keySplines="0.25 0.1 0.25 1"/>
    </rect>
  </mask>
  {clip_paths_str}
  <style>
    @keyframes maskReveal {{
      from {{ height: 0px; }}
      to {{ height: 560px; }}
    }}
    @keyframes typeLine {{
      from {{ width: 0px; }}
      to {{ width: 690px; }}
    }}
    .mask-rect {{
      animation: maskReveal 2.6s cubic-bezier(0.25, 0.1, 0.25, 1) 0.2s forwards;
    }}
    {line_css_str}

    .ascii  {{ font-family: 'Courier New', Consolas, monospace; font-size: 6.6px; fill: url(#asciiGrad); letter-spacing: -0.2px; }}
    .key    {{ font-family: 'Courier New', Consolas, monospace; font-size: 14px; fill: {key_color}; font-weight: bold; }}
    .value  {{ font-family: 'Courier New', Consolas, monospace; font-size: 14px; fill: {val_color}; }}
    .cc     {{ font-family: 'Courier New', Consolas, monospace; font-size: 14px; fill: {cc_color}; }}
    .head   {{ font-family: 'Courier New', Consolas, monospace; font-size: 16px; fill: {head_color}; font-weight: bold; }}
    .accent {{ font-family: 'Courier New', Consolas, monospace; font-size: 14px; fill: {accent_color}; font-weight: bold; }}
    text, tspan {{ white-space: pre; }}
    
    .term-label {{ font-family: 'Courier New', Consolas, monospace; font-size: 12px; fill: {term_label_color}; letter-spacing: 0.5px; }}
    .scan-label {{ font-family: 'Courier New', Consolas, monospace; font-size: 10px; fill: {scan_label_color}; letter-spacing: 1px; }}
    .panel-title {{ font-family: 'Courier New', Consolas, monospace; font-size: 11px; fill: {panel_title_color}; letter-spacing: 2px; opacity: {panel_title_opacity}; }}
  </style>
</defs>

<rect width="1180" height="610" rx="18" fill="url(#bgGlow)"/>
<rect width="1180" height="610" rx="18" fill="url(#scanlines)"/>

<g id="titlebar">
  <rect x="3" y="3" width="1174" height="34" rx="16" fill="{title_bg}" fill-opacity="{title_bg_opacity}"/>
  <circle cx="24" cy="20" r="5" fill="#EF4444"><animate attributeName="opacity" values="1;0.55;1" dur="4s" repeatCount="indefinite"/></circle>
  <circle cx="42" cy="20" r="5" fill="#F59E0B"><animate attributeName="opacity" values="1;0.55;1" dur="4s" begin="0.3s" repeatCount="indefinite"/></circle>
  <circle cx="60" cy="20" r="5" fill="#10B981"><animate attributeName="opacity" values="1;0.55;1" dur="4s" begin="0.6s" repeatCount="indefinite"/></circle>
  <text x="590" y="25" text-anchor="middle" class="term-label">nblancs@devs ~ % ./profile.sh --live</text>
</g>

<g transform="translate(0,38)">
  <rect x="14" y="26" width="488" height="468" rx="14" fill="{box_bg}" fill-opacity="{box_bg_opacity}" stroke="url(#borderGrad)" stroke-width="1" opacity="{box_stroke_opacity}"/>
  <rect x="508" y="10" width="655" height="500" rx="14" fill="{box_bg}" fill-opacity="{box_bg_opacity}" stroke="url(#borderGrad)" stroke-width="1" opacity="{box_stroke_opacity}"/>
  <text x="524" y="24" class="panel-title">SYSTEM.INFO</text>

  <g mask="url(#revealMask)">
  <text x="30" y="0" class="ascii">
{ascii_content}
  </text>
  </g>

  {info_groups_str}
</g>

<rect x="0" y="-70" width="1180" height="70" fill="url(#scanGrad)" opacity="0.7" style="{scan_blend_mode}">
  <animateTransform attributeName="transform" type="translate" from="0 -70" to="0 680" dur="4.2s" repeatCount="indefinite"/>
</rect>

<rect x="3" y="3" width="1174" height="604" rx="16" fill="none" stroke="url(#borderGrad)" stroke-width="2" opacity="0.8">
  <animate attributeName="opacity" values="0.5;0.95;0.5" dur="3.2s" repeatCount="indefinite"/>
</rect>
</svg>
'''
    return svg

with open('dark.svg', 'w', encoding='utf-8') as f:
    f.write(generate_svg(is_dark=True))

with open('light.svg', 'w', encoding='utf-8') as f:
    f.write(generate_svg(is_dark=False))

print("Generated dark.svg and light.svg keeping typing effect but removing blinking cursor block!")
