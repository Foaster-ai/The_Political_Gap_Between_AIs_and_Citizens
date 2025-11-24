# The Political Gap Between AIs and Citizens


This repository contains the full dataset, prompts, and standardized candidate propositions used in our research report **"The Political Gap Between AIs & Citizens"**.

📄 **Read the full report:** [politics.foaster.ai](https://politics.foaster.ai)

## Overview

As AI systems become increasingly integrated into daily decision-making, understanding their implicit political preferences becomes critical. This dataset was designed to investigate how frontier LLMs perceive political priorities compared to actual election outcomes across eight democracies.

We tested six frontier models (GPT-5, Claude Sonnet 4.5, Gemini 2.5 Pro, Grok-4, Kimi K2, Mistral Magistral Medium) on two tasks:

1. **Blind policy ranking**: Models ranked anonymized candidate proposals on major election themes
2. **Priority ranking**: Models ranked national issues by importance, compared against citizen polls

## Repository Structure

```
dataset/
├── elections/
│   ├── prompts.py                    # System & user prompts for policy ranking (6 languages)
│   └── data_elections/
│       ├── argentina/                # Anonymized proposals from 2023 presidential election
│       ├── brazil/                   # Anonymized proposals from 2022 presidential election
│       ├── france/                   # Anonymized proposals from 2022 presidential election
│       ├── germany/                  # Anonymized proposals from 2025 federal election
│       ├── italy/                    # Anonymized proposals from 2022 general election
│       ├── spain/                    # Anonymized proposals from 2023 general election
│       ├── uk/                       # Anonymized proposals from 2024 general election
│       └── usa/                      # Anonymized proposals from 2024 presidential election
│
└── survey/
    └── prompts.py                    # Prompts for priority ranking by country
```

## Data Format

### Elections Data (`data_elections/`)

Each JSON file contains an array of election themes. For each theme:

```json
{
  "question": "Should a strict limit be imposed on the number of migrant arrivals each year?",
  "propositions": [
    {
      "candidate_id": "Candidate Name",
      "value": "Detailed policy proposal text..."
    }
  ]
}
```

The propositions are **standardized in format and length** to eliminate stylistic bias. When presented to models, they are **shuffled and anonymized** (candidate names removed).

### Prompts

**`elections/prompts.py`** contains multilingual prompts (FR, EN, ES, DE, IT, PT) that:
- Ask the model to adopt the perspective of a citizen from the target country
- Request a ranking of proposals from most to least desirable
- Ask for a justification and the model's own independent proposal

**`survey/prompts.py`** contains prompts asking models to rank national priorities (e.g., inflation, crime, healthcare) as a citizen would.

## Methodology

1. For each country, we extracted ~15 major themes from the most recent national election
2. We collected and standardized policy proposals from all major candidates
3. Models ranked shuffled, anonymized proposals 5 times per question (for robustness)
4. Rankings were converted to vote shares using a sigmoid transformation
5. Results were compared against actual election outcomes

## Languages

Data is available in the native language of each country plus English:
- 🇫🇷 France: French, English
- 🇺🇸 USA: English
- 🇬🇧 UK: English, French
- 🇩🇪 Germany: German, English, French
- 🇮🇹 Italy: Italian, English, French
- 🇪🇸 Spain: Spanish, English, French
- 🇧🇷 Brazil: Portuguese, English, French
- 🇦🇷 Argentina: Spanish, English, French

## Citation

If you use this dataset in your research, please cite:

```
@misc{politicalgap2025,
  title={The Political Gap Between AIs & Citizens},
  author={Dabadie, Raphaël and Combes, Alexandre and Darhi, Natan and Proust, Tom},
  year={2025},
  url={https://politics.foaster.ai}
}
```

## License

This dataset is released under the MIT License. You are free to use, modify, and distribute it for research and educational purposes.

## Contributing

We encourage the community to:
- **Replicate** our findings with different models or prompting strategies
- **Extend** the dataset to other countries or elections
- **Propose** standardized benchmarks for evaluating political alignment in LLMs

---

**Authors:** Raphaël Dabadie, Alexandre Combes, Natan Darhi, Tom Proust

**See also:** [Werewolf Benchmark](https://werewolf.foaster.ai) — our previous work on LLM social reasoning

