# LLM Instruct for OpenIE

LLM instruct for OpenIE task.

## Dependencies

```bash
# EasyInstruct
python -m pip install git+https://github.com/zjunlp/EasyInstruct@main
python -m pip install -e ./easyinstruct

# OpenAI
conda install openai
```

## Citation

I used codes and prompts from `easyinstruct`. Citation for `easyinstruct`

```bibtex
@misc{easyinstruct,
  author = {Yixin Ou and Ningyu Zhang and Honghao Gui and Zhen Bi and Yida Xue and Runnan Fang and Kangwei Liu and Lei Li and Shuofei Qiao and Huajun Chen},
  title = {EasyInstruct: An Easy-to-use Instruction Processing Framework for Large Language Models},
  year = {2023},
  url = {https://github.com/zjunlp/EasyInstruct},
}
```
