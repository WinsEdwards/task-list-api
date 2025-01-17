from app import db
from sqlalchemy.sql import false

class Task(db.Model):
    task_id = db.Column(db.Integer, primary_key=True, nullable=False)
    title = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    completed_at = db.Column(db.DateTime, nullable=True, server_default=None)
    goal_id = db.Column(db.Integer, db.ForeignKey('goal.goal_id'), nullable=True)
    goal = db.relationship("Goal", back_populates="tasks")

    def to_dict(self):
        return {
                "id": self.task_id,
                "title": self.title,
                "description": self.description,
                "is_complete": True if self.completed_at else False
                }