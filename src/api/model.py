from pydantic import BaseModel, Field 

class ImageRequest(BaseModel):
    image: str = Field(
        ...,
        title="utf-8 string from a base64 encoded image",
        example="AQIDBAUG"
    )
    height: int = Field(..., tilte="Image height", example=224)
    width: int = Field(..., title="image width", example=224)

class PredictionResponse(BaseModel):
    ## TODO 
    pass