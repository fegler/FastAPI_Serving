from transformers.onnx import export
from transformers.onnx.features import FeaturesManager
from transformers import LayoutLMv3ForTokenClassification, LayoutLMv3Processor
from pathlib import Path
import torch

model_id = "nielsr/layoutlmv3-finetuned-funsd"
model = LayoutLMv3ForTokenClassification.from_pretrained(model_id)
processor = LayoutLMv3Processor.from_pretrained("microsoft/layoutlmv3-base", apply_ocr=False)

onnx_path = Path("layoutlmv3_onnx")
onnx_path.mkdir(exist_ok=True)

# 올바른 ONNX config 인스턴스 생성
feature = "token-classification"
model_onnx_config_cls = FeaturesManager.get_supported_features_for_model_type("layoutlmv3")[feature]
onnx_config = model_onnx_config_cls(model.config)

# export 실행
export(
    preprocessor=processor,
    model=model,
    config=onnx_config,
    opset=14,
    output=onnx_path / "model.onnx"
)