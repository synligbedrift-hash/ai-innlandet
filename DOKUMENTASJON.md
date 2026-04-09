# AI Innlandet – Prosjektdokumentasjon

**Sist oppdatert:** 9. april 2026
**Status:** 🟢 LIVE

---

## 1. Om prosjektet

**AI Innlandet** er en nettside som hjelper bedrifter i Innlandet med å forstå, velge og ta i bruk kunstig intelligens. Siden presenterer tjenester, AI-nyheter og har et lead-skjema for å bestille gratis AI-kartlegging.

---

## 2. Viktige lenker

| Hva | URL |
|---|---|
| **Live nettside** | https://aiinnlandet.netlify.app |
| **GitHub repo (kildekode)** | https://github.com/synligbedrift-hash/ai-innlandet |
| **Netlify dashboard** | https://app.netlify.com/projects/AIinnlandet |
| **Leads / skjemasvar** | https://app.netlify.com/projects/AIinnlandet/forms |
| **Kontakt-epost** | synligbedrift@gmail.com |

---

## 3. Teknisk arkitektur

```
Claude Code (her i chatten)
    ↓ redigerer filer lokalt
Lokal mappe: ai-innlandet/
    ↓ git push
GitHub (kildekode + backup)
    ↓ auto-trigger
Netlify (bygger og publiserer)
    ↓
https://aiinnlandet.netlify.app
```

### Teknologi
- **Frontend:** Statisk HTML/CSS (vanilla, ingen rammeverk)
- **Hosting:** Netlify (gratis plan)
- **Kildekode:** GitHub (public repo)
- **Leadskjema:** Netlify Forms (gratis, innebygd)
- **Deploy:** Automatisk ved hvert `git push` til main-branch

### Kostnader
- GitHub: 0 kr
- Netlify: 0 kr
- Domene (når kjøpt): ~150 kr/år
- **Totalt ved lansering: ~12 kr/mnd**

---

## 4. Filstruktur

```
ai-innlandet/
├── index.html           ← Hele nettsiden (HTML, CSS, innhold)
├── netlify.toml         ← Netlify-konfigurasjon
├── README.md            ← Kort beskrivelse
├── DOKUMENTASJON.md     ← Dette dokumentet
└── .gitignore           ← Filer som ikke skal til GitHub
```

---

## 5. Verktøy installert lokalt

| Verktøy | Versjon | Bruk |
|---|---|---|
| Homebrew | 5.1.5 | Pakkebehandler for Mac |
| Git | Innebygd | Versjonering |
| GitHub CLI (`gh`) | 2.89.0 | Snakker med GitHub fra Terminal |
| Node.js | v25.9.0 | Kreves av Netlify CLI |
| npm | 11.12.1 | Pakkebehandler for Node |
| Netlify CLI | 24.10.0 | Snakker med Netlify fra Terminal |

### Kontoer koblet
- **GitHub:** `synligbedrift-hash`
- **Netlify:** `synligbedrift@gmail.com` (team: `Synlig Bedrift`)

---

## 6. Hvordan gjøre endringer

### Enkleste vei – snakk med Claude Code
I chatten med Claude sier du f.eks.:
> *"Legg til en seksjon om AI for regnskapsbyråer"*
> *"Endre hovedoverskriften til X"*
> *"Oppdater nyhetene"*

Claude gjør automatisk:
1. Redigerer `index.html` lokalt
2. `git add` + `git commit` + `git push`
3. Netlify deployer live på ~30 sek

### Manuell vei (hvis nødvendig)
I Terminal, fra mappen `ai-innlandet/`:
```bash
# Etter endringer:
git add .
git commit -m "Beskrivelse av endringen"
git push

# Sjekk deploy-status:
netlify status

# Åpne siden:
netlify open:site
```

---

## 7. Lead-skjema

### Hvor havner lead-ene?
Alle innsendte skjemaer lagres i Netlify og er synlige her:
https://app.netlify.com/projects/AIinnlandet/forms

### E-postvarsling (ikke satt opp ennå)
For å få e-post til `synligbedrift@gmail.com` hver gang noen sender inn:
1. Gå til Netlify dashboard → Forms → Settings
2. Legg til notification → Email → `synligbedrift@gmail.com`

**Neste steg:** Sette opp dette automatisk.

---

## 8. Roadmap – fase for fase

### ✅ Fase 1 – Lansering (FERDIG 9. april 2026)
- [x] Sette opp utviklingsmiljø (Homebrew, gh, Node, Netlify CLI)
- [x] Opprette HTML-side med "AI Innlandet"-branding
- [x] Opprette GitHub-repo
- [x] Koble til Netlify med automatisk deploy
- [x] Publisere live

### 🔜 Fase 2 – Forbedringer (neste uker)
- [ ] E-postvarsling for lead-skjema
- [ ] Eget domene (`ai-innlandet.no` eller lignende)
- [ ] Logo og visuell profil
- [ ] Case-studier og referanser
- [ ] Om oss-seksjon
- [ ] Personvernerklæring (GDPR)

### 🎯 Fase 3 – Automatisering (senere)
- [ ] Automatisk oppdatering av AI-nyheter (GitHub Actions + Claude API)
- [ ] Ekte AI-chat med Claude via Netlify Functions
- [ ] Voice-chat med AI-ekspert (stemme-til-stemme)
- [ ] Analytics (besøk, konvertering)
- [ ] Blogg-seksjon

### 🚀 Fase 4 – Skalering (langsiktig)
- [ ] Nyhetsbrev-abonnement
- [ ] Bookingsystem for samtaler
- [ ] Kundeportal
- [ ] Flere språk

---

## 9. Støttende rutiner

### Daglig / ukentlig
- Sjekk nye leads i Netlify dashboard
- Oppdater nyhetsseksjon ved behov

### Månedlig
- Sjekk Netlify-statistikk (besøk, båndbredde)
- Gå gjennom roadmap og prioriter

### Ved feil
1. Sjekk Netlify deploy-logg: https://app.netlify.com/projects/AIinnlandet/deploys
2. Sjekk GitHub commit-historikk: https://github.com/synligbedrift-hash/ai-innlandet/commits/main
3. Ved kritisk feil: Rull tilbake via Netlify → Deploys → velg forrige deploy → "Publish deploy"

---

## 10. Sikkerhet

- Ingen sensitive data lagres i koden
- API-nøkler (når vi legger til Claude API) lagres som **miljøvariabler** i Netlify, aldri i koden
- GitHub-repoet er public, så alt som pushes er synlig for alle

---

## 11. Kontakt og ansvar

| Rolle | Navn | Kontakt |
|---|---|---|
| Eier | Roger Hjelmstadstuen | synligbedrift@gmail.com |
| Utvikler-agent | Claude Code | (via chat) |

---

## 12. Historikk

| Dato | Hva skjedde |
|---|---|
| 9. april 2026 | Prosjekt startet, verktøy installert, side live på Netlify |

---

*Dette dokumentet holdes oppdatert etter hvert som prosjektet utvikler seg.*
