Apa itu Fuzzy
=============
Fuzzy atau lebih sering dikenal Logika samar adalah peningkatan dari logika Boolean yang berhadapan dengan konsep kebenaran sebagian. Saat logika klasik menyatakan bahwa segala hal dapat diekspresikan dalam istilah biner (0 atau 1, hitam atau putih, ya atau tidak), logika kabur menggantikan kebenaran boolean dengan tingkat kebenaran.

Logika kabur memungkinkan nilai keanggotaan antara 0 dan 1, tingkat keabuan dan juga hitam dan putih, dan dalam bentuk linguistik, konsep tidak pasti seperti "sedikit", "lumayan", dan "sangat". Logika ini berhubungan dengan set kabur dan teori kemungkinan. Logika kabur diperkenalkan oleh Dr. Lotfi Zadeh dari Universitas California, Berkeley pada 1965.

Tujuan Fuzzy Matchung
=============
Fuzzy Matching pada riset ini digunakan untuk melakukan  koreksi otomatis pada kesalahan penulisan user.

Work on
=============
- Rasa framework 2.8.6
- Conda 4.10.1
- Conda Powershell Promt

Depedencies
-------------
- fuzzywuzzy 0.18.0
- Levenshtein 0.13.2

Langkah Pengerjaan
=============

Set pipeline
-------------
Pada file config.ynl, copy pipeline berikut:

     - name: WhitespaceTokenizer
     - name: RegexFeaturizer
     - name: LexicalSyntacticFeaturizer
     - name: CountVectorsFeaturizer
       analyzer: char_wb
       min_ngram: 1
       max_ngram: 4
     - name: DIETClassifier
       epochs: 100
       constrain_similarities: true
     - name: RegexEntityExtractor
     - name: EntitySynonymMapper
     - name: ResponseSelector
       epochs: 100
       constrain_similarities: true
     - name: FallbackClassifier
       threshold: 0.3
       ambiguity_threshold: 0.1

Set Synonyms
-------------
Set synonims untuk seluruh entity pada file nlu.yml, berikut adalah code nya:

    - synonym: semester
      examples: |
        - 1
        - 2
        - 3
        - 4
        - 5
        - 6
        - 7
        - 8
        - ini
        - pendek
    - synonym: mk
      examples: |
        - kalkulus
        - algoritma pemrogramman 1
        - algoritma pemrogramman 2
        - struktur data 1
        - struktur data 2
    - synonym: nilai
      examples: |
        - nilai A
        - nilai B
        - nilai C
        - nilai D
        - nilai E

Tambahkan logika fuzzy pada Component EntitySynonimMapper
-------------
Buka directory EntitySynonimMapper yang ada pada instalasi RASA anda (tergantung komputer masing masing). Pada kasus ini direktory RASA saya adalah "C:\Users\airlab2\anaconda3\envs\installingrasa\Lib\site-packages\rasa\rasa\nlu\extractors\entity_synonyms.py". Lalu copy code berikut:
```javascript
import os
from typing import Any, Dict, List, Optional, Text, Type

from rasa.nlu.components import Component
from rasa.shared.constants import DOCS_URL_TRAINING_DATA
from rasa.shared.nlu.constants import ENTITIES, TEXT
from rasa.nlu.config import RasaNLUModelConfig
from rasa.nlu.extractors.extractor import EntityExtractor
from rasa.nlu.model import Metadata
from rasa.shared.nlu.training_data.training_data import TrainingData
from rasa.shared.nlu.training_data.message import Message
from rasa.nlu.utils import write_json_to_file
import rasa.utils.io
import rasa.shared.utils.io
from fuzzywuzzy import process


class EntitySynonymMapper(EntityExtractor):
    @classmethod
    def required_components(cls) -> List[Type[Component]]:
        return [EntityExtractor]

    def __init__(
        self,
        component_config: Optional[Dict[Text, Any]] = None,
        synonyms: Optional[Dict[Text, Any]] = None,
    ) -> None:

        super().__init__(component_config)

        self.synonyms = synonyms if synonyms else {}

    def train(
        self,
        training_data: TrainingData,
        config: Optional[RasaNLUModelConfig] = None,
        **kwargs: Any,
    ) -> None:

        for key, value in list(training_data.entity_synonyms.items()):
            self.add_entities_if_synonyms(key, value)

        for example in training_data.entity_examples:
            for entity in example.get(ENTITIES, []):
                entity_val = example.get(TEXT)[entity["start"] : entity["end"]]
                self.add_entities_if_synonyms(entity_val, str(entity.get("value")))

    def process(self, message: Message, **kwargs: Any) -> None:

        updated_entities = message.get(ENTITIES, [])[:]
        self.replace_synonyms(updated_entities)
        message.set(ENTITIES, updated_entities, add_to_output=True)

    def persist(self, file_name: Text, model_dir: Text) -> Optional[Dict[Text, Any]]:

        if self.synonyms:
            file_name = file_name + ".json"
            entity_synonyms_file = os.path.join(model_dir, file_name)
            write_json_to_file(
                entity_synonyms_file, self.synonyms, separators=(",", ": ")
            )
            return {"file": file_name}
        else:
            return {"file": None}

    @classmethod
    def load(
        cls,
        meta: Dict[Text, Any],
        model_dir: Text,
        model_metadata: Optional[Metadata] = None,
        cached_component: Optional["EntitySynonymMapper"] = None,
        **kwargs: Any,
    ) -> "EntitySynonymMapper":
        """Loads trained component (see parent class for full docstring)."""
        file_name = meta.get("file")
        if not file_name:
            synonyms = None
            return cls(meta, synonyms)

        entity_synonyms_file = os.path.join(model_dir, file_name)
        if os.path.isfile(entity_synonyms_file):
            synonyms = rasa.shared.utils.io.read_json_file(entity_synonyms_file)
        else:
            synonyms = None
            rasa.shared.utils.io.raise_warning(
                f"Failed to load synonyms file from '{entity_synonyms_file}'.",
                docs=DOCS_URL_TRAINING_DATA + "#synonyms",
            )
        return cls(meta, synonyms)

    def replace_synonyms(self, entities: List[Dict[Text, Any]]) -> None:
        for entity in entities:
            # need to wrap in `str` to handle e.g. entity values of type int
            entity_value = str(entity["value"])
            # if entity_value.lower() in self.synonyms:
            #     entity["value"] = self.synonyms[entity_value.lower()]
            #     self.add_processor_name(entity)
            fuzzy_matched_value = process.extractOne(entity_value, self.synonyms.keys(), score_cutoff=90)
            if fuzzy_matched_value:
                entity["value"] = self.synonyms[fuzzy_matched_value[0]]
                self.add_processor_name(entity)
                entities.append({
                    "value": entity["value"],
                    "auto_correct":fuzzy_matched_value[0],
                    "fuzzy_value": fuzzy_matched_value[1]
                })

    def add_entities_if_synonyms(
        self, entity_a: Text, entity_b: Optional[Text]
    ) -> None:
        if entity_b is not None:
            original = str(entity_a)
            replacement = str(entity_b)

            if original != replacement:
                original = original.lower()
                if original in self.synonyms and self.synonyms[original] != replacement:
                    rasa.shared.utils.io.raise_warning(
                        f"Found conflicting synonym definitions "
                        f"for {repr(original)}. Overwriting target "
                        f"{repr(self.synonyms[original])} with "
                        f"{repr(replacement)}. "
                        f"Check your training data and remove "
                        f"conflicting synonym definitions to "
                        f"prevent this from happening.",
                        docs=DOCS_URL_TRAINING_DATA + "#synonyms",
                    )

                self.synonyms[original] = replacement

```

Training RASA nlu
-------------
Jalankan kode berikut pada Conda Powrshell Promt:

    rasa train nlu --config config.yml
    
Lalu untuk menjalankan hasil training, jalankan kode berikut:
  
    rasa shell
    
Training Fuzzy Matching
-------------
Berikut adalah hasil Fuzzy Matching

![](https://github.com/rsf-project/chatbot-rasa/blob/main/Fuzzy%20Matching/Example%20run.png)

Perhitungan presentase perubahan perhitungan fuzzy pada riset
-------------
Perhitungan detail terkait fuzzy mathing dapat dilihat pada link berikut:
- https://github.com/rsf-project/chatbot-rasa/blob/main/Fuzzy%20Matching/presentase%20fuzzy%20matching.xlsx
