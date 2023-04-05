
# Downloading train data
mkdir -p data/retriever/
cd data/retriever/

wget https://dl.fbaipublicfiles.com/dpr/data/retriever/biencoder-nq-train.json.gz
gunzip biencoder-nq-train.json.gz

wget https://dl.fbaipublicfiles.com/dpr/data/retriever/biencoder-nq-dev.json.gz
gunzip biencoder-nq-dev.json.gz

wget https://dl.fbaipublicfiles.com/dpr/data/retriever/biencoder-trivia-train.json.gz
gunzip biencoder-trivia-train.json.gz

wget https://dl.fbaipublicfiles.com/dpr/data/retriever/biencoder-trivia-dev.json.gz
gunzip biencoder-trivia-dev.json.gz

wget https://dl.fbaipublicfiles.com/dpr/data/retriever/biencoder-squad1-train.json.gz
gunzip biencoder-squad1-train.json.gz

wget https://dl.fbaipublicfiles.com/dpr/data/retriever/biencoder-squad1-dev.json.gz
gunzip biencoder-squad1-dev.json.gz


# Downloading wiki passage data.
wget https://dl.fbaipublicfiles.com/dpr/wikipedia_split/psgs_w100.tsv.gz
gunzip psgs_w100.tsv.gz


# Downloading subset for validation. (Query, Answer)
mkdir -p qas
cd ./qas

wget https://dl.fbaipublicfiles.com/dpr/data/retriever/nq-train.qa.csv
wget https://dl.fbaipublicfiles.com/dpr/data/retriever/nq-dev.qa.csv
wget https://dl.fbaipublicfiles.com/dpr/data/retriever/nq-test.qa.csv

wget https://dl.fbaipublicfiles.com/dpr/data/retriever/trivia-train.qa.csv.gz
wget https://dl.fbaipublicfiles.com/dpr/data/retriever/trivia-dev.qa.csv.gz
wget https://dl.fbaipublicfiles.com/dpr/data/retriever/trivia-test.qa.csv.gz

