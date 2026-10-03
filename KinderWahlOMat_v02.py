# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 22:45:04 2026

@author: zora
"""
# -*- coding: utf-8 -*-
"""
KINDER WAHLOMAT

Streamlit-Version
"""

import streamlit as st


# =========================================================
# 1. PARTEI-GEWICHTE
# =========================================================

#### Hier werden für die spätere Ergebnisberechnung die Werte pro Partei für die Gewichtung hinterlegt.
#### Die ergeben sich aus den Manifesto-Daten (Codings der Parteiprogramme Bundestagswahl 2025) und sind in dieser Datei zu finden
####### "C:\Users\zorah\Documents\Wissen, Spass und mehr\Politik, Wirtschaft, Geo\Politik\Manifesto Daten\MPDataset_MPDS2026a_Auszug_bearbeitet_v2.xlsx"


parteien = {

    "Bündnis90 / Die Grünen": {
        "per104": 2.36088684,
        "per106": 1.51577657,
        "per107": 3.55842105,
        "per108": 2.64259026,
        "per201": 5.32054078,
        "per202": 7.68142761,
        "per303": 3.20599710,
        "per401": 0.42314447,
        "per402": 1.79747999,
        "per403": 4.96811683,
        "per410": 2.57186973,
        "per411": 8.63261866,
        "per414": 0.28170342,
        "per501": 10.00695420,
        "per502": 1.48041631,
        "per503": 13.88361760,
        "per504": 11.13494650,
        "per506": 2.14990394,
        "per601": 0.52804658,
        "per603": 0.10608079,
        "per605": 6.62415577,
        "per606": 2.57186973,
        "per607": 1.86702184,
        "per701": 3.03037447,
        "per703": 1.65603894
    },

    "DIE LINKE": {
        "per104": 0.11319638,
        "per106": 2.49032042,
        "per107": 2.82990957,
        "per108": 0.90557106,
        "per201": 4.58445351,
        "per202": 3.90527521,
        "per303": 0.22639277,
        "per401": 0.05659819,
        "per402": 0.16979457,
        "per403": 13.63887780,
        "per410": 0.33958915,
        "per411": 7.80926409,
        "per414": 0,
        "per501": 6.11131835,
        "per502": 1.47155298,
        "per503": 22.18391840,
        "per504": 14.31805610,
        "per506": 3.90527521,
        "per601": 0,
        "per603": 0,
        "per605": 2.32052585,
        "per606": 0.90557106,
        "per607": 1.41495479,
        "per701": 9.45061165,
        "per703": 0.84897287
    },

    "SPD": {
        "per104": 3.70966238,
        "per106": 1.57386682,
        "per107": 4.27159112,
        "per108": 3.76562209,
        "per201": 2.75484984,
        "per202": 4.60968103,
        "per303": 3.26081888,
        "per401": 1.12385749,
        "per402": 2.19175527,
        "per403": 4.38467637,
        "per410": 3.37273830,
        "per411": 9.55628614,
        "per414": 0.28096437,
        "per501": 2.36080022,
        "per502": 3.09177392,
        "per503": 13.49095320,
        "per504": 14.27788660,
        "per506": 2.64176460,
        "per601": 0.73097370,
        "per603": 0.67501399,
        "per605": 6.74547659,
        "per606": 2.30484051,
        "per607": 1.29290244,
        "per701": 6.63239134,
        "per703": 0.89885283
    },

    "FDP": {
        "per104": 3.77647578,
        "per106": 0.60060796,
        "per107": 2.06045303,
        "per108": 1.97465189,
        "per201": 5.23632085,
        "per202": 4.20548147,
        "per303": 13.47568150,
        "per401": 10.12821140,
        "per402": 3.77647578,
        "per403": 3.26166895,
        "per410": 2.83266327,
        "per411": 10.98744850,
        "per414": 2.91846440,
        "per501": 2.23205530,
        "per502": 1.71724848,
        "per503": 6.00853108,
        "per504": 6.09433222,
        "per506": 5.15051971,
        "per601": 2.57525985,
        "per603": 0.17160227,
        "per605": 4.20548147,
        "per606": 1.71724848,
        "per607": 0.51480682,
        "per701": 2.23205530,
        "per703": 2.14625417
    },

    "CDU/CSU": {
        "per104": 7.14294076,
        "per106": 0.51388905,
        "per107": 2.51793929,
        "per108": 2.51793929,
        "per201": 3.13484027,
        "per202": 2.72396315,
        "per303": 6.57754574,
        "per401": 4.72801339,
        "per402": 4.93286666,
        "per403": 3.13484027,
        "per410": 3.03182834,
        "per411": 11.86978360,
        "per414": 1.74769101,
        "per501": 3.08333431,
        "per502": 2.92881642,
        "per503": 4.26563030,
        "per504": 6.78356960,
        "per506": 3.95659452,
        "per601": 5.34374378,
        "per603": 1.79802639,
        "per605": 7.75984174,
        "per606": 2.00405024,
        "per607": 0.46238309,
        "per701": 4.11111241,
        "per703": 2.92881642
    },

    "BSW": {
        "per104": 0.18831692,
        "per106": 3.29306820,
        "per107": 1.50529641,
        "per108": 0.28247538,
        "per201": 7.71356006,
        "per202": 6.96153131,
        "per303": 4.79712569,
        "per401": 3.19890974,
        "per402": 1.03450412,
        "per403": 8.84222264,
        "per410": 1.69361333,
        "per411": 11.28910360,
        "per414": 0.18831692,
        "per501": 1.78777179,
        "per502": 1.22282104,
        "per503": 10.06628260,
        "per504": 13.26395340,
        "per506": 5.83286874,
        "per601": 3.38598773,
        "per603": 1.12866258,
        "per605": 4.79712569,
        "per606": 1.22282104,
        "per607": 0.28247538,
        "per701": 3.29306820,
        "per703": 2.72811745
    },

    "AfD": {
        "per104": 1.35686749,
        "per106": 0.81386852,
        "per107": 1.49293219,
        "per108": 0.20409706,
        "per201": 11.19384180,
        "per202": 5.76637186,
        "per303": 2.57767027,
        "per401": 7.73427067,
        "per402": 2.30680072,
        "per403": 1.62773704,
        "per410": 2.03593116,
        "per411": 9.56610477,
        "per414": 2.98460453,
        "per501": 4.40950437,
        "per502": 0.54299897,
        "per503": 2.17073601,
        "per504": 7.05520699,
        "per506": 2.50963792,
        "per601": 12.34787210,
        "per603": 8.82026860,
        "per605": 6.37740318,
        "per606": 0.33890191,
        "per607": 0,
        "per701": 1.83183410,
        "per703": 3.93453776
    }
}


# =========================================================
# 2. FRAGEN
# =========================================================

fragen = [

    # -----------------------------------------------------
    # AUSSENPOLITIK
    # -----------------------------------------------------

    {
        "id": "per104",
        "thema": "AUSSENPOLITIK",
        "frage": "1. Wie findest du hauen und schlagen und beißen?",
        "option1": "gut",
        "option2": "blöd"
    },

    {
        "id": "per106",
        "thema": "AUSSENPOLITIK",
        "frage": "2. Ein Kind aus der Kita ärgert dich oft und ist richtig gemein zu dir. Gerade hat es eine tolle große Sandburg gebaut und ist weggegangen. Was tust du?",
        "option1": "nichts",
        "option2": "Ich gehe zur Sandburg und zerstöre sie."
    },

    {
        "id": "per107",
        "thema": "AUSSENPOLITIK",
        "frage": "3. Spielst du lieber mit anderen Kindern zusammen oder lieber allein?",
        "option1": "mit anderen Kindern",
        "option2": "allein"
    },

    {
        "id": "per108",
        "thema": "AUSSENPOLITIK",
        "frage": "4. Wer soll entscheiden, wo du und deine Eltern Urlaub machen?",
        "option1": "Ich und meine Eltern - ich finde es gut, wenn meine Eltern und ich einfach in ein anderes Land reisen können.",
        "option2": "Das andere Land - Die Leute im anderen Land sollen selber sagen, wer dort Urlaub machen darf."
    },


    # -----------------------------------------------------
    # FREIHEIT UND DEMOKRATIE
    # -----------------------------------------------------

    {
        "id": "per201",
        "thema": "FREIHEIT UND DEMOKRATIE",
        "frage": "5. Willst du selbst entscheiden, was du machst?",
        "option1": "ja",
        "option2": "nein"
    },

    {
        "id": "per202",
        "thema": "FREIHEIT UND DEMOKRATIE",
        "frage": "6. Willst du ganz allein über alles entscheiden oder dürfen andere mitmachen?",
        "option1": "auch andere",
        "option2": "ich allein"
    },


    # -----------------------------------------------------
    # POLITISCHES SYSTEM
    # -----------------------------------------------------

    {
        "id": "per303",
        "thema": "POLITISCHES SYSTEM",
        "frage": "7. Wie findest du Papier mit ganz vielen Buchstaben darauf?",
        "option1": "langweilig",
        "option2": "spannend"
    },


    # -----------------------------------------------------
    # WIRTSCHAFT
    # -----------------------------------------------------

    {
        "id": "per401",
        "thema": "WIRTSCHAFT",
        "frage": "8. Du willst Schokolade kaufen. Bei Rewe kostet sie mehr Geld als bei Kaufland. Wie findest du das?",
        "option1": "Total okay. Jeder Laden darf selber entscheiden, wie viel Geld die Schokolade kostet.",
        "option2": "Gemein. Gleiche Schokolade sollte überall gleich viel Geld kosten."
    },

    {
        "id": "per402",
        "thema": "WIRTSCHAFT",
        "frage": "9. Eis ist sehr teuer. Soll jemand anders dein Eis bezahlen, damit deine Eltern weniger Geld dafür ausgeben?",
        "option1": "Jemand anders, dann haben meine Eltern mehr Geld für anderes und alle haben Eis.",
        "option2": "Nö, meine Eltern sollen mein Eis bezahlen."
    },

    {
        "id": "per403",
        "thema": "WIRTSCHAFT",
        "frage": "10. Die Eisdiele verkauft leckeres Eis und ekliges Eis. Wie findest du das?",
        "option1": "Finde ich doof. Es soll verboten sein, ekliges Eis zu verkaufen.",
        "option2": "Mir egal, ich suche mir einfach leckeres Eis aus."
    },

    {
        "id": "per410",
        "thema": "WIRTSCHAFT",
        "frage": "11. Man soll immer mehr Geld verdienen und immer mehr kaufen können und es soll ganz viel verkauft werden.",
        "option1": "ja",
        "option2": "nein"
    },

    {
        "id": "per411",
        "thema": "WIRTSCHAFT",
        "frage": "12. Was magst du lieber?",
        "option1": "Tablet und Handy",
        "option2": "Bücher und Papier zum Basteln"
    },

    {
        "id": "per414",
        "thema": "WIRTSCHAFT",
        "frage": "13. Stell dir vor, du möchtest unbedingt ein neues Kuscheltier haben. Aber es dauert noch ewig bis zu deinem Geburtstag!",
        "option1": "Damit ich glücklich bin, kaufen meine Eltern mir das einfach so.",
        "option2": "Blöd für mich. Ich muss bis zum Geburtstag warten."
    },


    # -----------------------------------------------------
    # WOHLSTAND UND LEBENSQUALITÄT
    # -----------------------------------------------------

    {
        "id": "per501",
        "thema": "WOHLSTAND UND LEBENSQUALITÄT",
        "frage": "14. Was magst du lieber?",
        "option1": "Tiere und Blumen und Pilze",
        "option2": "Autos und Lastwagen und Flugzeuge"
    },

    {
        "id": "per502",
        "thema": "WOHLSTAND UND LEBENSQUALITÄT",
        "frage": "15. Wie findest du die Bibliothek?",
        "option1": "mag ich, gehe ich gerne hin",
        "option2": "mir egal, brauche ich nicht"
    },

    {
        "id": "per503",
        "thema": "WOHLSTAND UND LEBENSQUALITÄT",
        "frage": "16. Du hast gerade eine große Portion Spaghetti bekommen und deine Schwester nur eine kleine. Wie findest du das?",
        "option1": "komisch, warum ist ihre Portion so klein?",
        "option2": "super, mehr für mich!"
    },

    {
        "id": "per504",
        "thema": "WOHLSTAND UND LEBENSQUALITÄT",
        "frage": "17. Gehst du gerne in die Kita?",
        "option1": "ja",
        "option2": "nein"
    },

    {
        "id": "per506",
        "thema": "WOHLSTAND UND LEBENSQUALITÄT",
        "frage": "18. Was würde dir in der Kita gut gefallen?",
        "option1": "mehr Spielsachen & mehr Räume & mehr Erzieherinnen",
        "option2": "weniger Spielsachen & weniger Räume & weniger Erzieherinnen"
    },


    # -----------------------------------------------------
    # GESELLSCHAFT
    # -----------------------------------------------------

    {
        "id": "per601",
        "thema": "GESELLSCHAFT",
        "frage": "19. Das Land in dem du lebst, ist Deutschland. Findest du das gut?",
        "option1": "Ja, ich lebe gern in Deutschland.",
        "option2": "Okay, aber ich würde lieber woanders leben. / Es ist mir egal, wie das Land heißt."
    },

    {
        "id": "per603",
        "thema": "GESELLSCHAFT",
        "frage": "20. Manche Kinder haben keinen Papa, sondern nur eine Mama oder zwei Mamas. Wie findest du das?",
        "option1": "Jedes Kind sollte einen Papa und eine Mama haben.",
        "option2": "Cool, ich hätte auch lieber 2 Mamas oder keinen Papa."
    },

    {
        "id": "per605",
        "thema": "GESELLSCHAFT",
        "frage": "21. Wie findest du die Polizei?",
        "option1": "Toll, es sollte viel mehr Polizei geben.",
        "option2": "Toll, aber es gibt schon genug."
    },

    {
        "id": "per606",
        "thema": "GESELLSCHAFT",
        "frage": "22. Hilfst du gerne anderen Kindern?",
        "option1": "ja",
        "option2": "nein"
    },

    {
        "id": "per607",
        "thema": "GESELLSCHAFT",
        "frage": "23. Wie findest du es, dass Kinder mehrere Sprachen sprechen und verschieden aussehen?",
        "option1": "Gut. Ich mag, wenn alle verschieden sind.",
        "option2": "Blöd. Ich finde es besser, wenn alle sind wie ich."
    },


    # -----------------------------------------------------
    # SOZIALE GRUPPEN
    # -----------------------------------------------------

    {
        "id": "per701",
        "thema": "SOZIALE GRUPPEN",
        "frage": "24. Wie findest du es, wenn Erwachsene arbeiten?",
        "option1": "Gut. Aber sie sollen auch zuhause sein und Zeit für ihr Kind haben.",
        "option2": "Gut. Erwachsene sollen ganz viel und lange arbeiten."
    },

    {
        "id": "per703",
        "thema": "SOZIALE GRUPPEN",
        "frage": "25. Magst du Bauernhöfe?",
        "option1": "Ja, und Tiere ganz besonders.",
        "option2": "Ja, aber lieber mag ich Computer."
    }
]


# =========================================================
# 3. THEMEN / SEITEN ERMITTELN
# =========================================================

# Die Reihenfolge der Themen wird automatisch aus der
# Reihenfolge der Fragen übernommen.

themen = []

for frage in fragen:

    if frage["thema"] not in themen:
        themen.append(frage["thema"])


# =========================================================
# 4. FRAGEN NACH THEMEN GRUPPIEREN
# =========================================================

fragen_nach_thema = {}

for thema in themen:

    fragen_nach_thema[thema] = []

    for frage in fragen:

        if frage["thema"] == thema:
            fragen_nach_thema[thema].append(frage)


# =========================================================
# 5. BERECHNUNGSFUNKTION
# =========================================================

def berechne_ergebnis(antworten):

    rohwerte = {}

    # Für jede Partei
    for partei, gewichte in parteien.items():

        summe = 0

        # Für jede beantwortete Frage
        for frage_id, antwort in antworten.items():

            # Antwortoption 1:
            # Das Gewicht der Partei wird addiert.
            if antwort == 1:

                summe += gewichte[frage_id]

            # Antwortoption 2:
            # Es werden 0 Punkte addiert.
            elif antwort == 2:

                summe += 0

        rohwerte[partei] = summe


    # -----------------------------------------------------
    # Normierung auf 0–100 Punkte
    # -----------------------------------------------------

    maximum = max(rohwerte.values())
    minimum = min(rohwerte.values())

    normierte_werte = {}

    for partei, wert in rohwerte.items():

        if maximum == minimum:

            # Sonderfall:
            # Alle Parteien haben exakt denselben Wert.
            normierter_wert = 100

        else:

            normierter_wert = (
                (wert - minimum)
                / (maximum - minimum)
                * 100
            )

        normierte_werte[partei] = normierter_wert


    return rohwerte, normierte_werte


# =========================================================
# 6. SESSION STATE INITIALISIEREN
# =========================================================

if "seite" not in st.session_state:

    st.session_state.seite = 1


if "antworten" not in st.session_state:

    st.session_state.antworten = {}


# =========================================================
# 7. TITEL
# =========================================================

st.title("Der Wahl-O-Mat für Kinder")


# =========================================================
# 8. FRAGEBOGEN
# =========================================================

# Anzahl der Themenseiten
anzahl_themen = len(themen)


if st.session_state.seite <= anzahl_themen:

    # -----------------------------------------------------
    # Aktuelles Thema bestimmen
    # -----------------------------------------------------

    aktuelles_thema = themen[
        st.session_state.seite - 1
    ]


    # -----------------------------------------------------
    # Fragen dieses Themas bestimmen
    # -----------------------------------------------------

    aktuelle_fragen = fragen_nach_thema[
        aktuelles_thema
    ]


    # -----------------------------------------------------
    # Überschrift
    # -----------------------------------------------------

    st.header(
        "THEMA " + aktuelles_thema
    )


    # -----------------------------------------------------
    # Fortschrittsanzeige
    # -----------------------------------------------------

    st.progress(
        st.session_state.seite / anzahl_themen
    )

    st.write(
        f"Thema {st.session_state.seite} "
        f"von {anzahl_themen}"
    )


    # -----------------------------------------------------
    # Fragen anzeigen
    # -----------------------------------------------------

    for frage in aktuelle_fragen:

        st.radio(

            frage["frage"],

            [
                frage["option1"],
                frage["option2"]
            ],

            key=frage["id"]
        )


    st.write("")


    # -----------------------------------------------------
    # Button
    # -----------------------------------------------------

    if st.session_state.seite < anzahl_themen:

        button_text = "Weiter →"

    else:

        button_text = "Auswertung →"


    if st.button(button_text):

        # -------------------------------------------------
        # Antworten speichern
        # -------------------------------------------------

        for frage in aktuelle_fragen:

            antwort = st.session_state[
                frage["id"]
            ]


            if antwort == frage["option1"]:

                st.session_state.antworten[
                    frage["id"]
                ] = 1

            else:

                st.session_state.antworten[
                    frage["id"]
                ] = 2


        # -------------------------------------------------
        # Nächste Themenseite
        # -------------------------------------------------

        st.session_state.seite += 1

        st.rerun()


# =========================================================
# 9. ERGEBNISSE
# =========================================================

else:

    st.header("Dein Ergebnis")

    st.write(
        "Vielen Dank! Du hast alle Fragen beantwortet."
    )


    # -----------------------------------------------------
    # Berechnung durchführen
    # -----------------------------------------------------

    rohwerte, ergebnis = berechne_ergebnis(
        st.session_state.antworten
    )


    # -----------------------------------------------------
    # Ergebnis sortieren
    # -----------------------------------------------------

    sortiertes_ergebnis = sorted(
        ergebnis.items(),
        key=lambda x: x[1],
        reverse=True
    )


    # -----------------------------------------------------
    # Ergebnis anzeigen
    # -----------------------------------------------------

    st.subheader("Deine Übereinstimmung")


    for partei, punkte in sortiertes_ergebnis:

        st.write(
            f"**{partei} – {punkte:.1f} Punkte**"
        )

        st.progress(
            int(round(punkte))
        )


    # -----------------------------------------------------
    # Antworten anzeigen
    # -----------------------------------------------------

    with st.expander(
        "Meine Antworten anzeigen"
    ):

        for frage in fragen:

            frage_id = frage["id"]


            if frage_id in st.session_state.antworten:

                antwort_nummer = (
                    st.session_state.antworten[
                        frage_id
                    ]
                )


                if antwort_nummer == 1:

                    antwort_text = frage["option1"]

                else:

                    antwort_text = frage["option2"]


                st.write(
                    f"**{frage['frage']}**  \n"
                    f"{antwort_text}"
                )


    # -----------------------------------------------------
    # Neustart
    # -----------------------------------------------------

    st.write("")


    if st.button("Nochmal starten"):

        st.session_state.clear()

        st.session_state.seite = 1

        st.session_state.antworten = {}

        st.rerun()

