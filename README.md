# ICRA 2026 Fabric vs BTGenBot comparison

## Setup

Create a python virtual environment

```bash 
python3 -m venv .venv
source .venv/bin/activate
```

Install Dependencies

```bash
pip install -r requirements.txt
```

## Running ICRA2026 related evaluations

Activate the venv
```bash
source .venv/bin/activate
```
Following commands will run the code for each of the tasks available in the tasks folder and write the corresponding plan to workspace/src/bt_client/bt_xml folder with filename format of `<model>-<zero>-<original_filename>-<iteration>.xml`

### BT

To run the BT generation with llamachat
```bash
export HF_TOKEN="your_hugging_face_token_here"
python3 BTGenBot/inference-llamachat.py
```

To run the BT generation with codellama
```bash
export HF_TOKEN="your_hugging_face_token_here"
python3 BTGenBot/inference-codellama.py
```

To run the BT generation with openai models select the correct file
```bash
export OPENAI_API_KEY="your_openai_key_here"
python3 BTGenBot/inference-openai-4o.py
python3 BTGenBot/inference-openai-4.1.py
python3 BTGenBot/inference-openai-5.py
```

### Fabric

To run the generation with llamachat
```bash
export HF_TOKEN="your_hugging_face_token_here"
python3 Fabric/inference-llamachat.py
```

To run the generation with codellama
```bash
export HF_TOKEN="your_hugging_face_token_here"
python3 Fabric/inference-codellama.py
```

To run the generation with openai
```bash
export OPENAI_API_KEY="your_openai_key_here"
python3 Fabric/inference-openai-4o.py
python3 Fabric/inference-openai-4.1.py
python3 Fabric/inference-openai-5.0.py
```

Prompts and results will be printed onto the terminal.

Data used for evaluation will be available on output-eval and logs-eval folders
