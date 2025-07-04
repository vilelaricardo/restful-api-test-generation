# Projeto

---

## ⚙️ Requisitos

### Usando Docker (recomendado)

- Docker
- Docker Compose

### Usando Localmente

- Python 3.8+
- Java 8 (obrigatório para rodar o `evomaster.jar`)  
  → [Detalhes sobre compatibilidade](https://github.com/WebFuzzing/EvoMaster/blob/master/docs/jdks.md)
- (Recomendado) Ambiente virtual com `venv`

---

## 📥 Clonando o Projeto

```bash
git clone https://github.com/Wanderson-Valentim/tcc.git
cd tcc
```

---

## 🐳 Usando com Docker

### 1. Copiar a configuração base do EvoMaster

```bash
cp tool/configs/em.yaml.example tool/configs/em.yaml
```

Você pode editar esse arquivo para ajustar o comportamento da ferramenta.  
Consulte a documentação para entender cada opção disponível:  
🔗 https://github.com/WebFuzzing/EvoMaster/blob/master/docs/options.md

### 2. (Opcional) Editar o experimento

O arquivo `tool/configs/setup_experiment.json` define quantas vezes o experimento será executado e os algoritmos. Já vem com valores padrão, mas pode ser ajustado.

### 3. Rodar o experimento com Docker

```bash
docker compose up --build
```

> O `--build` é necessário sempre que houver mudanças no código fonte.

### 📁 Dados gerados

Os resultados de cada experimento serão salvos em:

```
tool/data_generated/<nome_experimento>/
```

---

## 💻 Usando Localmente

### 1. Verificar Java 8

Certifique-se de que o Java 8 está instalado e configurado corretamente:

```bash
java -version
```

> A versão deve começar com `1.8`.

### 2. Criar ambiente virtual e instalar dependências

```bash
python -m venv venv
source venv/bin/activate  # no Windows: venv\Scripts\activate
pip install -r tool/requirements.txt
```

### 3. Copiar e configurar `em.yaml`

```bash
cp tool/configs/em.yaml.example tool/configs/em.yaml
```


### 4. (Opcional) Ajustar o `setup_experiment.json`


### 5. Rodar o experimento

```bash
python tool/main.py
```

Os resultados também serão salvos em `tool/data_generated/<nome_experimento>/`.

---

## 📊 Gerar CSV com Estatísticas

Após a execução de um experimento, você pode gerar um arquivo `.csv` com os dados:

```bash
python tool/run_get_statistics_csv.py -n <nome_do_experimento>
```

Exemplo:

```bash
python tool/run_get_statistics_csv.py -n experiment-date-<DD-MM-YY>-time-<HH-MM-SS-mmm>
```

O arquivo será salvo em:

```
tool/statistics/
```

Esse script busca os dados gerados e extrai estatísticas como quantidade de testes e cobertura de critérios.
