# Final Project (TCC)

---

## ⚙️ Requirements

### Using Docker (recommended)

- Docker  
- Docker Compose

### Running Locally

- Python 3.8+  
- Java 8 (required to run `evomaster.jar`)  
  → [Compatibility details](https://github.com/WebFuzzing/EvoMaster/blob/master/docs/jdks.md)  
- (Recommended) Virtual environment using `venv`

---

## 📥 Cloning the Project

```bash
git clone https://github.com/Wanderson-Valentim/tcc.git
cd tcc
```

---

## 🐳 Using Docker

### 1. Copy EvoMaster base configuration

```bash
cp tool/configs/em.yaml.example tool/configs/em.yaml
```

You can edit this file to customize the tool’s behavior.  
Check the official documentation to understand each available option:  
🔗 https://github.com/WebFuzzing/EvoMaster/blob/master/docs/options.md

### 2. (Optional) Edit the experiment setup

The file `tool/configs/setup_experiment.json` defines how many times the experiment will run and which algorithms will be used. It comes with default values but can be modified.

### 3. Run the experiment with Docker

```bash
docker compose up --build
```

> The `--build` flag is required whenever source code changes are made.

### 📁 Generated Data

Results of each experiment will be saved in:

```
tool/data_generated/<experiment_name>/
```

---

## 💻 Running Locally

### 1. Check Java 8

Make sure Java 8 is properly installed and configured:

```bash
java -version
```

> The version should start with `1.8`.

### 2. Create a virtual environment and install dependencies

```bash
python -m venv venv
source venv/bin/activate  # on Windows: venv\Scripts\activate
pip install -r tool/requirements.txt
```

### 3. Copy and configure `em.yaml`

```bash
cp tool/configs/em.yaml.example tool/configs/em.yaml
```

### 4. (Optional) Adjust `setup_experiment.json`

### 5. Run the experiment

```bash
python tool/main.py
```

Results will also be saved in `tool/data_generated/<experiment_name>/`.

---

## 📊 Generate CSV with Statistics

After running an experiment, you can generate a `.csv` file with the data:

```bash
python tool/run_get_statistics_csv.py -n <experiment_name>
```

Example:

```bash
python tool/run_get_statistics_csv.py -n experiment-date-<DD-MM-YY>-time-<HH-MM-SS-mmm>
```

The CSV file will be saved in:

```
tool/statistics/
```

This script processes the generated data and extracts statistics such as the number of tests and coverage metrics.