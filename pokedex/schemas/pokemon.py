import pydantic

class Pokemon(pydantic.BaseModel):
    number: int
    name: str
    name_fr: str
    types: list[str]
    image_url: str
    height: int # en centimètres
    weight: int # en grammes
    evolves_from_number: int | None = None