#!/usr/bin/env python3
"""Gera a versão instalável (index.html) a partir do artefacto em src/gongbubang.html.

O artefacto do claude.ai não tem <html>/<head>; aqui junta-se o esqueleto, o manifest
e o registo do service worker. O nome da cache do sw.js muda com o conteúdo, para a
app instalada ir buscar a versão nova depois de cada commit.
"""
import hashlib, pathlib, re

ROOT = pathlib.Path(__file__).resolve().parent.parent
app = (ROOT / "src" / "gongbubang.html").read_text(encoding="utf-8")

HEAD = """<!doctype html>
<html lang="pt-PT"><head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<link rel="manifest" href="manifest.json">
<meta name="theme-color" content="#6a2ee0">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-title" content="공부방">
<link rel="apple-touch-icon" href="icon-192.png">
<link rel="icon" href="icon-192.png">
<style>:root{padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px);color-scheme:light}body{margin:0;font:14px system-ui,sans-serif}img{max-width:100%}[hidden]{display:none!important}</style>
</head><body>
"""
TAIL = """
<script>if("serviceWorker" in navigator)addEventListener("load",()=>navigator.serviceWorker.register("sw.js").catch(()=>{}));</script>
</body></html>
"""
(ROOT / "index.html").write_text(HEAD + app + TAIL, encoding="utf-8")

h = hashlib.sha1(app.encode("utf-8"))
for f in ("manifest.json", "icon-192.png", "icon-512.png"):  # icon or manifest changes also count as a new version
    h.update((ROOT / f).read_bytes())
version = h.hexdigest()[:10]
sw = ROOT / "sw.js"
sw.write_text(re.sub(r'const C="gongbubang-[^"]*"', f'const C="gongbubang-{version}"', sw.read_text(encoding="utf-8")), encoding="utf-8")
print(f"index.html gerado · cache gongbubang-{version}")
