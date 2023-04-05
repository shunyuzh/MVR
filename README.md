# MVR

Code for Paper [Multi-View Document Representation Learning for Open-Domain Dense Retrieval](https://arxiv.org/abs/2203.08372). 
ACL2022 Main Conference, Long Paper. 

MVR is to address the multi-view problem in which the single vector representation of a document is hard to match with multi-view potential queries.  It presents a Multi-View document Representation (MVR) learning framework, aiming to produce multi-view embeddings to represent documents and enforce them to align with different queries. 



##  Environment and Data Downloading

Installation from the source. Python's virtual or Conda environments are recommended. Experimentally we use python==3.8. And one needs to download the train data.

```
cd MVR
conda create -n mvr python=3.8
pip install . --user

bash scripts/download_data.sh
```



## Fine-tuning Stage 1

Example for retriever training.
```shell
python -m torch.distributed.launch --nproc_per_node=8 train_dense_encoder.py \
    train=biencoder_nq \
    train_datasets=[list of train datasets, comma separated without spaces] \
    dev_datasets=[list of dev datasets, comma separated without spaces] \
    encoder.pretrained_model_cfg={initial model dir, we use cocondenser for nq\tq, and bert for squad} \
    output_dir={path to checkpoints dir}
```



## Mining Hard Negatives

#### Encode 

Encode the corpus to generate  embeddings.

```shell
python generate_dense_embeddings.py \
	model_file={path to biencoder checkpoint} \
	ctx_src={name of the passages resource, set to dpr_wiki to use original wikipedia split} \
	shard_id={shard_num, 0-based} \
	num_shards={total number of shards} \
	out_file={result files location + name PREFX}	
```

#### Search

```shell
python dense_retriever.py \
	model_file={path to the best checkpoint} \
	qa_dataset={qa_train_dataset} \
	ctx_datatsets=[dpr_wiki] \
	encoded_ctx_files=[{list of encoded document files, comma separated without spaces}] \
	out_file={path to output json file with results} 
```

#### Build HN Train file

```
python scripts/mine_hn.py
```



## Fine-tuning Stage 2

Train with mined negatives and bm25 negatives. 

```shell
python -m torch.distributed.launch --nproc_per_node=8 train_dense_encoder.py \
    train=biencoder_nq \
    train_datasets=[list of train datasets, comma separated without spaces] \
    dev_datasets=[list of dev datasets, comma separated without spaces] \
    encoder.pretrained_model_cfg={initial model dir, we use cocondenser for nq\tq, and bert for squad} \
    output_dir={path to checkpoints dir}
```



## Encode and Search

Encode the corpus to generate  embeddings.

```shell
python generate_dense_embeddings.py \
	model_file={path to biencoder checkpoint} \
	ctx_src={name of the passages resource, set to dpr_wiki to use original wikipedia split} \
	shard_id={shard_num, 0-based} \
	num_shards={total number of shards} \
	out_file={result files location + name PREFX}	
```

Search and evaluate.

```shell
python dense_retriever.py \
	model_file={path to the best checkpoint} \
	qa_dataset={qa_dataset} \
	ctx_datatsets=[dpr_wiki] \
	encoded_ctx_files=[{list of encoded document files, comma separated without spaces}] \
	out_file={path to output json file with results}
```



##  Citation

If you find our work useful, please cite the following paper:

```
@inproceedings{zhang-etal-2022-multi,
    title = "Multi-View Document Representation Learning for Open-Domain Dense Retrieval",
    author = "Zhang, Shunyu  and Liang, Yaobo  and Gong, Ming  and Jiang, Daxin  and Duan, Nan",
    booktitle = "Proceedings of the 60th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2022.acl-long.414",
    doi = "10.18653/v1/2022.acl-long.414",
    pages = "5990--6000",
}
