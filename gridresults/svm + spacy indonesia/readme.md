Apa itu SVM
=============
Pada dasarnya, Support Vector Machine merupakan sebuah algoritma klasifikasi untuk data linear dan non-linear. SVM menggunakan mapping non-linear untuk mentransformasikan training data awal ke dimensi yang lebih tinggi.

Tujuan training model
=============
dataset di training menjadi sebuah model agar kita dapat melihat kualitas dari dataset tersebut. Pada kasus ini saya melakukan training data dengan memperhitungkan beberapa faktor yaitu :
- Confusion matrix dan histogram dari DIET classifier
- Confusion matrix dan histogram dari intent 

Work on
=============
- Rasa framework 2.8.6
- Conda 4.10.1

Depedencies
-------------
- Spacy 3.1.2

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

Setelah itu bukan Conda promt dan jalankan syntax berikut untuk melakukan benchmark terhadap dataset
        
    rasa test nlu --config config.yml --cross-validation --runs 1 --folds 2 --out gridresults/SVM_and_Spacy
    
File output dari syntax tersebut akan disimpan pada folder gridresults/SVM_and_Spacy

Output
=============

DIET Classifier bencmark
-------------

![](https://github.com/rsf-project/chatbot-rasa/blob/main/gridresults/svm%20%2B%20spacy%20indonesia/DIETClassifier_confusion_matrix.png)
![](https://github.com/rsf-project/chatbot-rasa/blob/main/gridresults/svm%20%2B%20spacy%20indonesia/DIETClassifier_histogram.png)

Dapat dilihat pada hasil output bahwa tingkat akurasi masih tidak merata untuk keseluruhan nilai confidence. Ini disebabkan karena memang dataset hanya mengandung sedikit elemen/entity, untuk menutupi kekurangan tersebut dapat dilakukan dengan cara memperbanyak data agar perhitungan dapat menghasilkan nilai yang lebih akurat.

Intent benchmark
-------------

![](https://github.com/rsf-project/chatbot-rasa/blob/main/gridresults/svm%20%2B%20spacy%20indonesia/intent_confusion_matrix.png)
![](https://github.com/rsf-project/chatbot-rasa/blob/main/gridresults/svm%20%2B%20spacy%20indonesia/intent_histogram.png)

Dapat dilihat pada hasil output bahwa masih ada tingkat error yang tinggi jika nilai confidence kurang dari 0.7 hal ini disebabkan oleh adanya kalimat yang masih ambigu ataupun yang mengarah pada lebih dari satu intent. Hal ini dapat diantisipasi dengan cara memperbanyak lagi intent dan memastikan bahwa setiap kalimat pada intent itu memiliki kemiripan text yang minim agar tidak menimbulkan ambiguitas.
