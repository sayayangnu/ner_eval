Evaluating NLTK's NER model on Emerging Entities
-------------------------------------------------

This project applies the default named entity recognition model in NLTK to the WNUT2017 Emerging Entities Task.

Data and links to task information and paper are available 
[on github](https://github.com/leondz/emerging_entities_17). NOTE: there are illegal tags in the test data.


Instructor repository at <https://github.com/emmerkhofer/ner_eval> . 

## Entity mapping

 | Nltk entity type | WNUT entity  |
 | ------------- | ------------- |
 |ORGANIZATION | -> corporation |
 |PERSON | -> person |
 |LOCATION | -> location |
 |DATE | None |
 |TIME | None |
 |MONEY | None |
 |PERCENT| None |
 |FACILITY| -> location |
 |GPE | -> location |


## Homework: `wnut_predict.py`

* Use `ne_chunk` in `nltk` to tag entities in WNUT.
* Use the mapping above to convert the entity types detected by NLTK to WNUT types.
* Write your results in a format that can be evaluated with `wnuteval.py`
* Evaluate your performance using `wnuteval.py`; report the metrics in the results section of the README.
* Do not alter `wnuteval.py`; debug how your output doesn't match expectations.
* Grading uses 
1) your `wnut_predict.py` code and 
2) your README.

This homework is submitted as a link to your Github repo on Canvas. You may submit the link early; 
we will grade the state of your repository at the deadline.


## wnuteval.py

Taken from the WNUT17 website. Slight modifications fix import error in Python 3 and stop crashing on 
illegal tags in test data. (This fix does NOT ensure test tags are valid.)

Use with a tab-separated submission in the form:
`<original word>  <gold standard tag>   <predicted tag>`

Example usage:

`python wnuteval.py my_predictions.tsv`

## lab.py

`lab.py` loads the WNUT data and makes predictions on a sentence using `nltk`'s `ne_chunk` NER model.

`python lab.py --data emerging.dev.conll`

## wnut_predict.py

TODO: Replace this section with a description of your code.
* Use `.md` filetype
* Describe what your script does.
* Include a usage example showing command line flags
* Describe your output.

## Results

TODO: paste your Entity Precision/Recall/F1 on dev here, *ONLY* for relevant entity classes.


