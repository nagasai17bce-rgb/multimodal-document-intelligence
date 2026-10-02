import re

class Service:
    def run(self, value: str):
        chunks = [x.strip() for x in re.split(r"\n{2,}", value) if x.strip()]
        return {
            "pages": 1,
            "blocks": len(chunks),
            "chunks": [
                {"id": f"chunk-{i+1}", "text": x, "citation": f"page:1#block:{i+1}"}
                for i, x in enumerate(chunks)
            ],
        }
