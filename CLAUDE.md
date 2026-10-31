# 공부방 — regras do projeto

App de estudo de coreano 세종한국어 2A (preparação do 성취도 평가 do 세종학당). Texto da app e respostas em **português de Portugal** (nunca PT-BR).

## Onde vive a app
- **Fonte única:** `src/gongbubang.html` — é o ficheiro publicado como artefacto no claude.ai.
- **Artefacto (com Claude):** https://claude.ai/artifact/JDnF1drQVmF4YGE2whP9f3 — capability `sample`.
- **App instalável (GitHub Pages):** https://antropologiadoiscte-arch.github.io/gongbubang/ — gerada por `tools/build.py` (`index.html`, `sw.js`, `manifest.json`, ícones).

## Regra: atualizar o artefacto = fazer commit
Sempre que o artefacto for alterado, no mesmo pedido:
1. Editar `src/gongbubang.html`.
2. Publicar o artefacto a partir desse ficheiro, mantendo o URL acima (passar `url` se for outra conversa).
3. `python3 tools/build.py` (gera `index.html` e muda a versão da cache do `sw.js`).
4. `git add -A && git commit` com uma mensagem curta em português sobre a mudança, e `git push origin main`.
5. Dizer à utilizadora que a app instalada atualiza cerca de 1 minuto depois (fechar e reabrir).

Nunca publicar o artefacto sem o commit, nem fazer commit sem publicar o artefacto.
