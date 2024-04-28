## Install
1. install `ffmpeg`
```
# ubuntu
apt install ffmpeg -y

# MacOS
brew update
brew upgrade
brew install ffmpeg
```

2. install requirements
```
pip install -r dry_requirements.txt
```

The Gradio app can work under `4.27.0`.

3. download checkpoint
> 
| Video Enc.  | Text Enc.  | Pretraining            | Fine-tuning   |  Checkpoints |
| ------------------ |  ------------------ | ------------------ | ------- | ---- |
| CLIP-B/16 | CLIP-B/16 | 4M      | -      |   [Google Drive](https://drive.google.com/drive/folders/1-eGata6ZPV0A1BBsZpYyIooos9yjMx2f?usp=sharing)  |
| CLIP-B/16 | CLIP-B/16 | 4M | QVHL + Charades + NLQ + TACoS + ActivityNet + DiDeMo      |  [Google Drive](https://drive.google.com/drive/folders/1l6RyjGuqkzfZryCC6xwTZsvjWaIMVxIO?usp=sharing)  

Download checkpoint and put it in the dir `results/omni`.

Download the example videos from [here](https://drive.google.com/drive/folders/1TpMYRmdAx5yx-lQu4ivCnAX67voUfBcL?usp=sharing) and put it under `examples/`

## Run
Run `python main_gradio.py --resume ./results/omni/model_best.ckpt`

