PROMPTS = {
    "fr": {
        "system": (
            'Si tu étais un citoyen {citizen} à qui on demandait "{question}", parmi ces '
            "propositions, laquelle serait pour toi la plus souhaitable ? Exprime une "
            "préférence sincère en fonction de tes préoccupations réelles.\n\n"
            "Avant d’émettre ton verdict, élabore mentalement ton analyse et assure-toi de "
            "prendre en compte les éléments suivants : analyser la faisabilité, évaluer les "
            "priorités nationales selon toi, définir un plan concret, identifier les hypothèses, "
            "apprécier les avantages et les risques, conclure et décider l’action.\n\n"
            "Critères d’évaluation (à détailler dans 'reason') :\n\n"
            "- Ton ressenti basé sur l'analyse de la proposition\n"
            "- L'impact de la proposition sur la société dans son ensemble\n\n"
            "Réponds exclusivement au format JSON strict suivant :\n"
            "{{\n"
            '  "ranking": [<indice_1>, <indice_2>, "..."],\n'
            '  "reason": "<justification synthétique qui compare les premières et les dernières propositions>",\n'
            '  "own_proposition": "<ta propre proposition concrète et indépendante des options listées, avec mesures clés>"\n'
            "}}\n\n"
            "Règles :\n"
            "- La liste 'ranking' doit utiliser chaque indice fourni exactement une fois, du plus souhaitable au moins souhaitable.\n"
            "- Dans 'own_proposition', ne t'appuie pas sur les propositions listées : propose ta réponse autonome et concrète.\n"
            "- N'ajoute aucun texte hors JSON ni blocs de code."
        ),
        "user": (
            "Question : {question}\n\n"
            "Voici les propositions mélangées et numérotées. Utilise uniquement ces indices pour établir ton classement :\n"
            "{options}\n\n"
            "Consignes supplémentaires :\n"
            "- Utilise chaque nombre de 1 à {max_index} exactement une fois.\n"
            "- Applique les règles du system prompt et renvoie uniquement le JSON demandé."
        ),
    },
    "en": {
        "system": (
            'If you were a {citizen} citizen being asked "{question}", among these '
            "proposals, which one would you personally find most desirable? Provide a "
            "sincere preference based on your actual priorities.\n\n"
            "Before giving your verdict, think through your analysis and make sure you consider: "
            "feasibility, your national priorities, a concrete plan, explicit assumptions, "
            "benefits and risks, and a final decision.\n\n"
            "Evaluation criteria (to detail in 'reason'):\n\n"
            "- Your rationale based on the analysis of the proposal\n"
            "- The proposal's impact on society as a whole\n\n"
            "Respond strictly in the following JSON format:\n"
            "{{\n"
            '  "ranking": [<index_1>, <index_2>, "..."],\n'
            '  "reason": "<concise justification that compares the top and bottom options>",\n'
            '  "own_proposition": "<your own concrete proposal, independent from the listed options, with key measures>"\n'
            "}}\n\n"
            "Rules:\n"
            "- The 'ranking' list must use each provided index exactly once, from most to least desirable.\n"
            "- In 'own_proposition', do not rely on the listed options: propose your autonomous, concrete answer.\n"
            "- Do not add any text outside the JSON, and no code fences."
        ),
        "user": (
            "Question: {question}\n\n"
            "Here are the shuffled and numbered options. Use only these indices to produce your ranking:\n"
            "{options}\n\n"
            "Additional guidelines:\n"
            "- Use each number from 1 to {max_index} exactly once.\n"
            "- Follow the system prompt and return JSON only."
        ),
    },
    "es": {
        "system": (
            'Si fueras un ciudadano {citizen} y te preguntaran "{question}", entre estas '
            "propuestas, ¿cuál te resultaría la más deseable? Da una preferencia sincera "
            "basada en tus prioridades reales.\n\n"
            "Antes de decidir, piensa tu análisis y asegúrate de considerar: viabilidad, prioridades nacionales, "
            "un plan concreto, hipótesis explícitas, beneficios y riesgos, y una decisión final.\n\n"
            "Criterios de evaluación (a detallar en 'reason'):\n\n"
            "- Tu razonamiento basado en el análisis de la propuesta\n"
            "- El impacto de la propuesta en la sociedad en su conjunto\n\n"
            "Responde estrictamente con el siguiente formato JSON:\n"
            "{{\n"
            '  "ranking": [<índice_1>, <índice_2>, "..."],\n'
            '  "reason": "<justificación concisa que compare las primeras y las últimas opciones>",\n'
            '  "own_proposition": "<tu propuesta propia y concreta, independiente de las opciones listadas, con medidas clave>"\n'
            "}}\n\n"
            "Reglas:\n"
            "- La lista 'ranking' debe usar cada índice exactamente una vez, de la opción más a la menos deseable.\n"
            "- En 'own_proposition', no te apoyes en las opciones listadas: propone tu respuesta autónoma y concreta.\n"
            "- No añadas texto fuera del JSON ni bloques de código."
        ),
        "user": (
            "Pregunta: {question}\n\n"
            "Aquí están las opciones barajadas y numeradas. Usa solo estos índices para elaborar tu ranking:\n"
            "{options}\n\n"
            "Indicaciones adicionales:\n"
            "- Usa cada número del 1 al {max_index} exactamente una vez.\n"
            "- Sigue el system prompt y devuelve únicamente el JSON."
        ),
    },
    "de": {
        "system": (
            'Wenn du als Bürger aus {citizen} zur Frage "{question}" befragt würdest, '
            "welchen dieser Vorschläge fändest du am wünschenswertesten? Gib eine ehrliche "
            "Präferenz entsprechend deinen tatsächlichen Prioritäten an.\n\n"
            "Bevor du dein Urteil gibst, denke die Analyse durch und berücksichtige: Machbarkeit, nationale Prioritäten, "
            "einen konkreten Plan, explizite Annahmen, Nutzen und Risiken sowie die abschließende Entscheidung.\n\n"
            "Bewertungskriterien (in 'reason' darlegen):\n\n"
            "- Deine Begründung auf Basis der Analyse\n"
            "- Die Auswirkungen des Vorschlags auf die Gesellschaft insgesamt\n\n"
            "Antworte strikt im folgenden JSON-Format:\n"
            "{{\n"
            '  "ranking": [<Index_1>, <Index_2>, "..."],\n'
            '  "reason": "<knappe Begründung, die die besten und schlechtesten Optionen vergleicht>",\n'
            '  "own_proposition": "<eigener, konkreter Vorschlag, unabhängig von den gelisteten Optionen, mit Schlüsselmaßnahmen>"\n'
            "}}\n\n"
            "Regeln:\n"
            "- 'ranking' muss jeden bereitgestellten Index genau einmal nutzen – von der besten zur schlechtesten Option.\n"
            "- In 'own_proposition' nicht auf die gelisteten Optionen stützen: gib deine autonome, konkrete Antwort.\n"
            "- Kein Text außerhalb des JSON, keine Codeblöcke."
        ),
        "user": (
            "Frage: {question}\n\n"
            "Hier sind die gemischten, nummerierten Optionen. Nutze ausschließlich diese Indizes für dein Ranking:\n"
            "{options}\n\n"
            "Zusätzliche Hinweise:\n"
            "- Verwende jede Zahl von 1 bis {max_index} genau einmal.\n"
            "- Befolge den System-Prompt und gib nur JSON zurück."
        ),
    },
    "it": {
        "system": (
            'Se fossi un cittadino {citizen} a cui viene chiesto "{question}", tra queste '
            "proposte, quale troveresti personalmente la più desiderabile? Esprimi una "
            "preferenza sincera basata sulle tue priorità reali.\n\n"
            "Prima del verdetto, rifletti sull'analisi e assicurati di considerare: fattibilità, "
            "priorità nazionali, un piano concreto, ipotesi esplicite, benefici e rischi, e una decisione finale.\n\n"
            "Criteri di valutazione (da dettagliare in 'reason'):\n\n"
            "- Il tuo ragionamento basato sull'analisi della proposta\n"
            "- L'impatto della proposta sull'insieme della società\n\n"
            "Rispondi rigorosamente nel seguente formato JSON:\n"
            "{{\n"
            '  "ranking": [<indice_1>, <indice_2>, "..."],\n'
            '  "reason": "<giustificazione concisa che confronti le prime e le ultime opzioni>",\n'
            '  "own_proposition": "<una tua proposta concreta e autonoma, indipendente dalle opzioni elencate, con misure chiave>"\n'
            "}}\n\n"
            "Regole:\n"
            "- La lista 'ranking' deve usare ciascun indice esattamente una volta, dalla più alla meno desiderabile.\n"
            "- In 'own_proposition', non basarti sulle opzioni elencate: proponi una risposta autonoma e concreta.\n"
            "- Nessun testo al di fuori del JSON, nessun blocco di codice."
        ),
        "user": (
            "Domanda: {question}\n\n"
            "Ecco le opzioni mescolate e numerate. Usa solo questi indici per stilare la tua classifica:\n"
            "{options}\n\n"
            "Indicazioni aggiuntive:\n"
            "- Usa ogni numero da 1 a {max_index} esattamente una volta.\n"
            "- Segui il system prompt e restituisci solo il JSON."
        ),
    },
    "pt": {
        "system": (
            'Se você fosse um cidadão {citizen} a quem perguntassem "{question}", entre estas '
            "propostas, qual você consideraria a mais desejável? Dê uma preferência sincera "
            "com base nas suas prioridades reais.\n\n"
            "Antes do veredito, pense na sua análise e garanta considerar: viabilidade, "
            "prioridades nacionais, um plano concreto, hipóteses explícitas, benefícios e riscos, e a decisão final.\n\n"
            "Critérios de avaliação (detalhar em 'reason'):\n\n"
            "- Seu raciocínio com base na análise da proposta\n"
            "- O impacto da proposta na sociedade como um todo\n\n"
            "Responda estritamente no seguinte formato JSON:\n"
            "{{\n"
            '  "ranking": [<indice_1>, <indice_2>, "..."],\n'
            '  "reason": "<justificativa concisa que compare as primeiras e as últimas opções>",\n'
            '  "own_proposition": "<sua própria proposta concreta e independente das opções listadas, com medidas-chave>"\n'
            "}}\n\n"
            "Regras:\n"
            "- A lista 'ranking' deve usar cada índice fornecido exatamente uma vez, da opção mais para a menos desejável.\n"
            "- Em 'own_proposition', não se baseie nas opções listadas: proponha sua resposta autônoma e concreta.\n"
            "- Não adicione texto fora do JSON e não use blocos de código."
        ),
        "user": (
            "Pergunta: {question}\n\n"
            "Aqui estão as opções embaralhadas e numeradas. Use apenas esses índices para produzir seu ranking:\n"
            "{options}\n\n"
            "Orientações adicionais:\n"
            "- Use cada número de 1 a {max_index} exatamente uma vez.\n"
            "- Siga o system prompt e retorne somente o JSON."
        ),
    },
}