from transformers import AutoProcessor, BarkModel
from scipy.io.wavfile import write as write_wav
import uuid
from pathlib import Path 
import os



processor = AutoProcessor.from_pretrained("suno/bark")
model = BarkModel.from_pretrained("suno/bark")

def gen_text(text):

  voice_preset = "v2/en_speaker_6"
  inputs = processor(text, voice_preset=voice_preset, return_tensors="pt")

  attention_mask = inputs["attention_mask"]

  outputs = model.generate(
    input_ids=inputs["input_ids"], 
    attention_mask=attention_mask,
    pad_token_id=processor.tokenizer.pad_token_id
  )

  path = os.path.dirname(
    os.path.dirname(
      os.path.dirname(
        os.path.abspath(__file__)
      )  
    )
  )

  filename = str(uuid.uuid4()) + ".wav"
  filepath = path + "/app/app/static/voice/" + filename
  audio_array = model.generate(**inputs)
  audio_array = audio_array.cpu().numpy().squeeze()
  sample_rate = model.generation_config.sample_rate
  write_wav(filepath, sample_rate, audio_array)
  pathflask = "/static/voice/" + filename

  return pathflask

