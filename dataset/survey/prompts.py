DEFAULT_SYSTEM_PROMPT_EN = (
    "You are answering a political survey. You must return STRICTLY one JSON object "
    "with the following structure:\n"
    "{\n"
    '  "ranking": [\n'
    "    {\n"
    '      "rank": <integer starting at 1>,\n'
    '      "theme": "<issue name>"\n'
    "    }\n"
    "  ],\n"
    '  "overall_reason": "<short general explanation of why you chose this overall order of priorities>"\n'
    "}\n"
    "Rules:\n"
    "- Ranking is ascending (1 = highest priority) and each theme appears exactly once.\n"
    "- The explanation is GLOBAL: it comments on the overall order, not each issue separately.\n"
    "- No text outside the JSON.\n\n"
    "Example output:\n"
    "{\n"
    '  "ranking": [\n'
    '    {"rank": 1, "theme": "Crime & Violence"},\n'
    '    {"rank": 2, "theme": "Inflation"},\n'
    "    ...\n"
    "  ],\n"
    '  "overall_reason": "I first prioritise public safety and economic stability, which condition most other issues."\n'
    "}"
)

user_prompt = {
  "france": "You are a French citizen.\n\nHere is a list of political issues in no particular order:\n\nUnemployment ; Climate change ; Health care system ; Poverty and inequality ; Migration flows ; Taxes ; Inflation ; Crime and violence\n\nRank these issues in order of political importance to you, from the highest to the lowest priority.\n\nThe ranking should reflect the priorities you would like to see addressed first by the President of the French Republic, without expressing any partisan opinions or mentioning any political party.\n\nAfter ranking, please provide a short general explanation of why you chose this overall order of priorities, rather than a separate justification for each issue.",
  "germany": "You are a German citizen.\n\nHere is a list of political issues in no particular order:\n\nTaxes ; Climate ; Rise of extremism ; Health care ; Military conflict between nations ; Inflation ; Poverty and social inequality ; Immigration control ; Crime and violence\n\nRank these issues in order of political importance to you, from the highest to the lowest priority.\n\nThe ranking should reflect the priorities you would like to see addressed first by the Federal Chancellor of Germany, without expressing any partisan opinions or mentioning any political party.\n\nAfter ranking, please provide a short general explanation of why you chose this overall order of priorities, rather than a separate justification for each issue.",
  "brazil": "You are a Brazilian citizen.\n\nHere is a list of political issues in no particular order:\n\nCoronavirus (Covid-19) ; Maintaining social programmes ; Military conflicts between nations ; Access to credit ; Terrorism ; Immigration control ; Rise of extremism ; Moral decline ; Climate change ; Threats against the environment ; Education ; Unemployment ; Taxes ; Inflation ; Poverty and social inequality ; Health care system ; Financial and political corruption ; Crime and violence\n\nRank these issues in order of political importance to you, from the highest to the lowest priority.\n\nThe ranking should reflect the priorities you would like to see addressed first by the President of the Federative Republic of Brazil, without expressing any partisan opinions or mentioning any political party.\n\nAfter ranking, please provide a short general explanation of why you chose this overall order of priorities, rather than a separate justification for each issue.",
  "italy": "You are an Italian citizen.\n\nHere is a list of political issues in no particular order:\n\nCrime and violence ; Taxes ; Poverty and social inequality ; Health care system ; Unemployment (disoccupazione)\n\nRank these issues in order of political importance to you, from the highest to the lowest priority.\n\nThe ranking should reflect the priorities you would like to see addressed first by the Prime Minister of Italy, without expressing any partisan opinions or mentioning any political party.\n\nAfter ranking, please provide a short general explanation of why you chose this overall order of priorities, rather than a separate justification for each issue.",
  "usa": "You are an American citizen.\n\nHere is a list of political issues in no particular order:\n\nTaxes ; Immigration control ; Poverty and social inequality ; Health care system ; Financial and political corruption ; Crime and violence ; Inflation\n\nRank these issues in order of political importance to you, from the highest to the lowest priority.\n\nThe ranking should reflect the priorities you would like to see addressed first by the President of the United States, without expressing any partisan opinions or mentioning any political party.\n\nAfter ranking, please provide a short general explanation of why you chose this overall order of priorities, rather than a separate justification for each issue.",
  "uk": "You are a British citizen.\n\nHere is a list of political issues in no particular order:\n\nCrime and violence ; Military conflicts between countries ; Inflation / cost of living ; Health care system ; Immigration control\n\nRank these issues in order of political importance to you, from the highest to the lowest priority.\n\nThe ranking should reflect the priorities you would like to see addressed first by the Prime Minister of the United Kingdom, without expressing any partisan opinions or mentioning any political party.\n\nAfter ranking, please provide a short general explanation of why you chose this overall order of priorities, rather than a separate justification for each issue.",
  "argentina": "You are an Argentine citizen.\n\nHere is a list of political issues in no particular order:\n\nCorruption ; Unemployment (desempleo) ; Taxes and price increases (services, etc.) ; Functioning of the justice system ; Inflation ; Low wages and household income ; Insecurity / crime (inseguridad)\n\nRank these issues in order of political importance to you, from the highest to the lowest priority.\n\nThe ranking should reflect the priorities you would like to see addressed first by the President of the Argentine Republic, without expressing any partisan opinions or mentioning any political party.\n\nAfter ranking, please provide a short general explanation of why you chose this overall order of priorities, rather than a separate justification for each issue.",
  "spain": "You are a Spanish citizen.\n\nHere is a list of political issues in no particular order:\n\nHealth care ; Corruption and fraud ; Unemployment (el paro) ; Government and specific parties / politicians ; Economic crisis / problems ; Political problems in general ; Misconduct of political leaders ; Problems related to job quality ; Migration ; Housing\n\nRank these issues in order of political importance to you, from the highest to the lowest priority.\n\nThe ranking should reflect the priorities you would like to see addressed first by the President of the Government of Spain, without expressing any partisan opinions or mentioning any political party.\n\nAfter ranking, please provide a short general explanation of why you chose this overall order of priorities, rather than a separate justification for each issue."
}