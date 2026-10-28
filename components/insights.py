"""Blocs de récit décisionnel (À retenir · Point d'attention · Analyse · Implication · Recommandation) et badges.

Les textes sont toujours construits à partir des données (voir utils/story.py) : aucun chiffre n'est écrit à la main dans les vues.
"""
from __future__ import annotations

import html

import streamlit as st

ICONS = {"retenir": "fa-lightbulb", "attention": "fa-triangle-exclamation", "analyse": "fa-chart-simple", "implication": "fa-compass", "recommandation": "fa-bullseye"}
TAGS = {"retenir": "À retenir", "attention": "Point d'attention", "analyse": "Analyse", "implication": "Implication", "recommandation": "Recommandation"}
FLAG_TXT = {"HIGH": "Comparable", "MEDIUM": "Prudence", "LOW": "Non comparable"}
PRIO_CLS = {"Très haute": "p-tres-haute", "Haute": "p-haute", "Moyenne": "p-moyenne", "Faible": "p-faible"}


def story_html(kind: str, text: str) -> str:
    """HTML d'un bloc de récit ; `text` peut contenir des balises <b> (valeurs mises en gras)."""
    return (f'<div class="story {kind}"><div class="s-ico"><i class="fa-solid {ICONS[kind]}"></i></div>'
            f'<div><div class="s-tag">{TAGS[kind]}</div><div class="s-txt">{text}</div></div></div>')


def story(kind: str, text: str) -> None:
    st.markdown(story_html(kind, text), unsafe_allow_html=True)


def story_grid(items: list[tuple[str, str]]) -> None:
    """Plusieurs blocs côte à côte (grille responsive)."""
    st.markdown('<div class="story-grid">' + "".join(story_html(k, t) for k, t in items) + "</div>", unsafe_allow_html=True)


def badge(text: str, cls: str = "stat") -> str:
    return f'<span class="bdg {cls}">{html.escape(str(text))}</span>'


def flag_badge(flag: str | None) -> str:
    if not flag or flag != flag:
        return badge("N/D", "nd")
    return badge(f"{flag} · {FLAG_TXT.get(flag, '')}", flag.lower())


def priority_badge(classe: str | None) -> str:
    return badge(classe, PRIO_CLS.get(classe, "nd")) if classe else badge("N/D", "nd")


def stat_badge(label: str) -> str:
    """Étiquette de nature de la donnée : OBSERVATION · CALCUL · PROXY · ESTIMATION · HYPOTHÈSE."""
    return badge(label, "stat")


def empty_state(message: str = "Aucune donnée disponible pour cette sélection.") -> None:
    st.markdown(f'<div style="color:#4f6270;padding:26px 0;text-align:center"><i class="fa-solid fa-circle-info" style="margin-right:8px"></i>{html.escape(message)} '
                f'Élargissez la sélection ou utilisez « Réinitialiser ».</div>', unsafe_allow_html=True)


def nd_note(text: str) -> None:
    """Note discrète sous un graphique : explique une absence de donnée (N/D) ou une limite de lecture."""
    st.markdown(f'<div class="note">{text}</div>', unsafe_allow_html=True)
