from pydantic import BaseModel

class UserSentiment(BaseModel):
    user: str
    total_posts: int
    positive_posts: int
    negative_posts: int
    satisfaction_percentage: float
    complaints_percentage: float
