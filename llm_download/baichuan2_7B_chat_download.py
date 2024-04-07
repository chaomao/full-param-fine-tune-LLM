from modelscope.hub.snapshot_download import snapshot_download
model_dir = snapshot_download('baichuan-inc/Baichuan2-7B-Base', cache_dir='/root/autodl-tmp/chaomao/base_model/', revision='v1.0.2')
