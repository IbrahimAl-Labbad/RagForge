# RagForge 

A powerful Document Q&A application that lets you interact with your documents using AI.

---

## Requirements

- Python 3.8
- MiniConda

---
## Installation

### 1. Install System Dependencies

```bash
sudo apt update
sudo apt install libpq-dev gcc python3-dev
```

### 2. Install Python using MiniConda

Download and install MiniConda from [here](https://docs.conda.io/en/latest/miniconda.html).

### 3. Create a new environment

```bash
conda create -n RAGFORGE python=3.8
```

### 4. Activate the environment

```bash
conda activate RAGFORGE
```

---

### Install the required packages

```bash
$ pip install -r requirements.txt
```

### Setup the environment variables

```bash
$ cp .env.example .env
```

Set your environment variables in the `.env` file. Like `OPENAI_API_KEY` value.


## License

This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.