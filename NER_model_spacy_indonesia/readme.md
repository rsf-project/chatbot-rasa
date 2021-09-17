Apa itu Spacy
=============
Spacy merupakan library natural language processing (NLP) yang sangat powerful, terutama untuk pemrosesan bahasa Inggris. Tidak hanya fungsi-fungsi dasar seperti tokenizer, library ini juga mendukung fungsi NLP yang bergantung pada solusi berbasis machine learning seperti part-of-speech (POS) tagging, Named entity recognition (NER), dan dependency parsing.

Tujuan training model
=============
Tujuan dari training model ini adalah untuk melakukan pemodelan Spacy NLP berbahasa indonesia.

Work on
=============
- Rasa framework 2.8.6
- Jupyter Notebook Conda 4.10.1

Depedencies
-------------
- Spacy 3.1.2

Dataset untuk training NER
-------------
- https://raw.githubusercontent.com/yusufsyaifudin/indonesia-ner/master/resources/ner/data_train.txt
- https://raw.githubusercontent.com/yohanesgultom/nlp-experiments/master/data/ner/training_data.txt

Referensi Syntax
-------------
- https://yudanta.github.io/posts/train-an-indonesian-ner-from-a-blank-spacy-model/

Perlu dicatat bahwa referensi diatas adalah training model bahasa indonesia untuk Spacy 2.x sedangkan saya menggunakan Spacy 3.1.2. Oleh karena itu akan ada beberapa syntax yang berbeda

Langkah pengerjaan
=============
Atur pipeline rasa yang ada pada file config.yml untuk mengintegrasikan Spacy bahasa indonesia

    language: en
    pipeline:
      - name: SpacyNLP
        model: "NER_model_spacy_indonesia"
      - name: SpacyTokenizer
      - name: SpacyFeaturizer
        pooling: mean
      - name: CountVectorsFeaturizer
        analyzer: char_wb
        min_ngram: 1
        max_ngram: 4
      - name: DIETClassifier
        epochs: 100
        constrain_similarities: true
      - name: EntitySynonymMapper
      - name: ResponseSelector
        epochs: 100
        constrain_similarities: true
      - name: FallbackClassifier
        threshold: 0.3
        ambiguity_threshold: 0.1
        
Syntax
-------------
Buka Jupyter Notebook, dan execute syntax dibawah secara berurutan setiap cell nya
```javascript
    import pickle
    import spacy
    import random
    from spacy.util import minibatch, compounding
    from spacy import load, displacy
    from spacy.training.example import Example
    
    with open('ner_spacy_fmt_datasets.pickle', 'rb') as f:
    ner_spacy_fmt_datasets = pickle.load(f)
    
    nlp=spacy.blank("id")
    
    nlp.add_pipe("ner")
    
    nlp.begin_training()
    
    import random
    from spacy.util import minibatch, compounding
    
    ner=nlp.get_pipe("ner")
    
    for _, annotations in ner_spacy_fmt_datasets:
      for ent in annotations.get("entities"):
        ner.add_label(ent[2])
        break
        
    pipe_exceptions = ["ner", "trf_wordpiecer", "trf_tok2vec"]
    unaffected_pipes = [pipe for pipe in nlp.pipe_names if pipe not in pipe_exceptions]
    
    //TRAINING THE MODEL
    with nlp.disable_pipes(*unaffected_pipes):
    //Training for 30 iterations
    for iteration in range(30):
      //shuufling examples  before every iteration
      random.shuffle(ner_spacy_fmt_datasets)
      losses = {}
      //batch up the examples using spaCy's minibatch
      batches = minibatch(ner_spacy_fmt_datasets, size=compounding(4.0, 32.0, 1.001))
      for batch in batches:
        for text, annotations in batch:
            //create Example
            doc = nlp.make_doc(text)
            example = Example.from_dict(doc, annotations)
            //Update the model
            nlp.update([example], losses=losses, drop=0.3)
        print("Losses at iteration {}".format(iteration), losses)
        
    //test 
    doc = nlp("SELUBUNG yang menyelimuti kasus penembakan yang menewaskan Pendeta Yeremia Zanambani di Kabupaten Intan Jaya, Papua kian terkuak. Hasil investigasi Tim Gabungan Pencari Fakta (TGPF) kasus tersebut menyatakan bahwa penembakan di Intan Jaya diduga dilakukan oleh aparat keamanan.")
    print(doc.ents)
    print("Entities", [(ent.text, ent.label_) for ent in doc.ents])
    
    //save model 
    from pathlib import Path
    output_dir = Path('NER_model_spacy_indonesia')
    nlp.to_disk(output_dir)
    print("Saved model to", output_dir)
    
    //load existing model 
    output_dir = 'NER_model_spacy_indonesia'
    print("Loading from", output_dir)
    nlp_updated = spacy.load(output_dir)
    
    doc = nlp_updated("Kementerian Perhubungan tidak mewajibkan rapid test COVID-19 untuk perjalanan darat lintas daerah, kecuali untuk tujuan Bali. Termasuk, dalam periode cuti bersama." )
    print("Entities", [(ent.text, ent.label_) for ent in doc.ents])
    
    displacy.render(doc, style="ent")
    
    doc = nlp_updated("Empat saksi terkait korupsi proyek infrastruktur fiktif yang dikerjakan PT Waskita Karya (Persero) Tbk absen dari panggilan KPK hari ini. Seorang di antaranya mantan Bupati Wakatobi, Hugua." )
    print("Entities", [(ent.text, ent.label_) for ent in doc.ents])
    
    displacy.render(doc, style="ent")
```
