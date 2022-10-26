# Unilm
## 简介
UniLM模型既可以应用于自然语言理解（NLU）任务，又可以应用于自然语言生成（NLG）任务。[论文](https://arxiv.org/abs/1905.03197)来自微软研究院。

## 预训练模型
来自云问开源的预训练unilm_base模型 https://github.com/YunwenTechnology/Unilm
预训练模型在网盘，需要自行下载

## 数据集
一份weibo新闻数据集，另一份是自制的CCTV新闻数据集

## 如何使用该模型进行NLG任务？
* fine-tuning
~~~
nohup python3 -u run_seq2seq.py --data_dir /data/unilm/data_file/ --src_file train_data.json --model_type unilm --model_name_or_path /data/unilm/yunwen_unilm/ --output_dir /data/unilm/output_dir/ --max_seq_length 512 --max_position_embeddings 512 --do_train --do_lower_case --train_batch_size 32 --learning_rate 1e-5 --num_train_epochs 3 > log.log 2>&1 &
~~~
* test
~~~
python3 -u decode_seq2seq.py --model_type unilm --model_name_or_path /data/unilm/yunwen_unilm/ --model_recover_path /data/unilm/output_dir/model.bin --max_seq_length 512 --input_file /data/unilm/data_file/test.json --output_file /data/unilm/data_file/predict_.json --do_lower_case --batch_size 32 --beam_szie 5 --max_tgt_length 128
~~~

# 训练环境
* torch 1.4.0
* transformers 2.6.0
