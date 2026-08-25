#!/usr/bin/env python3
"""Marion's guardrail, 2026-08-24: no instructional text, internal notes, warnings,
slot labels or photo numbers on any visual draft delivered for review. Those live in
markdown or messages, never on the draft. This pass strips them from published review
pages. It is part of publishing, not optional."""
import re, sys, glob

CSS = """<style id="clean-draft">
/* Guardrail (Marion, 2026-08-24): a visual draft carries zero internal noise. */
.stamp,.notes,.slotmark,.grain ~ .notes{display:none!important}
.seg span.slot,.chip.slot,.bx.slotbx,.roles span.slot{display:none!important}
.sv .ph.phslot{border-block-end:1px solid var(--line)!important}
.bx .slot{display:none!important}
/* Marion rule 2 (2026-08-24): section numbering and numbered labels go too. */
.no,.idx{display:none!important}
.door .tag,.tag{display:none!important}
.sv .ph.phslot,.card .ph.phslot,.svc .ph.phslot{border-style:solid!important}
</style>
"""
def clean(path):
    s=open(path).read()
    n=0
    # remove the internal notes section entirely (nesting-safe: it is the last <section>)
    m=re.search(r'<section class="notes"[\s\S]*?</section>\s*', s)
    if m: s=s.replace(m.group(0),""); n+=1
    # unverified address lines: the note lives in markdown, the draft shows the city only
    s3=re.sub(r'<p class="addr">[^<]*TO VERIFY[^<]*</p>\s*','',s)
    if s3!=s: n+=1; s=s3
    # remove the INTERNAL DRAFT stamp node
    s2=re.sub(r'<(div|span|p)[^>]*class="stamp"[^>]*>[\s\S]*?</\1>\s*','',s)
    if s2!=s: n+=1; s=s2
    if 'id="clean-draft"' not in s:
        s=s.replace("</head>", CSS+"</head>"); n+=1
    RULE2 = '<style id="clean-draft-2">.no,.idx,.door .tag,p.tag{display:none!important}</style>'
    if 'clean-draft-2' not in s:
        s=s.replace("</head>", RULE2+"\n</head>"); n+=1
    open(path,"w").write(s)
    return n

if __name__=="__main__":
    targets = sys.argv[1:] or (glob.glob("gate-*.html")+["D1-signal.html","D2-gate.html","D3-live-yard.html","V7-deployable.html"])
    for t in targets:
        try: print(f"{t}: {clean(t)} cleanups")
        except FileNotFoundError: pass
    # verify nothing instructional remains visible
    bad=[]
    PATTERNS=["INTERNAL DRAFT","PHOTO TO SOURCE","TO CONFIRM","TO VERIFY","awaiting","PHOTO PENDING"]
    # rule 2 note: numbered labels are hidden by css; empty phslot panels are a publish failure per the mandatory-photograph rule
    for t in targets:
        try: s=open(t).read()
        except FileNotFoundError: continue
        low=s
        # only flag text OUTSIDE the clean-draft-hidden classes is hard statically;
        # flag any pattern not inside a display:none-managed class attribute line
        for p in PATTERNS:
            for mm in re.finditer(re.escape(p), low, re.I):
                ctx=low[max(0,mm.start()-160):mm.start()]
                if not re.search(r'class="[^"]*(slot|stamp|notes|slotmark|slotbx)', ctx):
                    bad.append((t,p)); break
    if bad:
        print("STILL VISIBLE:", bad); sys.exit(1)
    print("clean: no instructional text visible on any review draft")
