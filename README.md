# Multimodal Document Intelligence

A document-processing API that converts structured text into addressable chunks with page/block citations. It provides the contract for later OCR, layout, table, chart, and image extraction.

## Run
```bash
pip install -e '.[dev]'
uvicorn app.main:app --reload
```

POST document text as `{"value":"Title\\n\\nBody"}` to `/v1/run`.

## Production extensions
Add OCR, layout detection, table extraction, image understanding, page-level provenance, object storage, asynchronous ingestion, and multimodal embedding pipelines.
