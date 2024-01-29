# Prompts for OpenIE

Prompts for zero-shot OpenIE.

OpenIE gives a structural representation of the facts in a sentence as `<subject, predicate, object>`. It is helpful for relation extractions with limited or no training data. The tuples extracted by OpenIE may help knowledge graph schema design or factual question and answer.

Since the extracted relation tuples are under the Resource Description Framework (RDF) data model, I adopted the RDF extraction prompt for OpenIE and gave the solution.

An example prompt is written as follows:

```
You are a highly intelligent and accurate Resource Description Framework (RDF) data model. You take Passage as input and convert it into RDF triples.
A triple is a set of three entities that codifies a statement about semantic data in subject-predicate-object expressions.
Your output format is only [[ subject, predicate, object ], ...], nothing else.
Input: [Sentence]
Output: 
```

I analyzed ten extractions and found that the extractions produced by the above prompt are worse than the ones produced by the following prompt.

```
Please exhaustively express the information from the text in a list of
dictionaries following json format.
Each dictionary corresponds to a fact extracted from the text and should
consist of “subject”, “predicate”, “object”, “confidence” four keys.
The value of “subject” key is a string indicating the subject of a fact.
The value of “object” key is a string indicating the object of a fact.
The value of “predicate” key is a string indicating the relation between
the subject and the object.
The value of “confidence” key is an integer ranging from 0 to 100,
indicating how confident you are about the fact.
Copy words from the text. Remove duplicated dictionaries.
Note that your answer should only contain the json string.
Text: [Sentence].
```

More detailed instructions will lead to better extractions.

## Dependencies

```bash
# OpenAI
conda install openai
```

## References

I used codes and prompts from `easyinstruct`. Citation for `easyinstruct`

```bibtex
@misc{easyinstruct,
  author = {Yixin Ou and Ningyu Zhang and Honghao Gui and Zhen Bi and Yida Xue and Runnan Fang and Kangwei Liu and Lei Li and Shuofei Qiao and Huajun Chen},
  title = {EasyInstruct: An Easy-to-use Instruction Processing Framework for Large Language Models},
  year = {2023},
  url = {https://github.com/zjunlp/EasyInstruct},
}
```
