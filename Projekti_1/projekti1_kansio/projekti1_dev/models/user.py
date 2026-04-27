class User:
    def __init__(self, id, username, created_at):
        self.id = int(id)
        self.username = username
        self.created_at = created_at
        
    @classmethod
    def from_row(cls, row):
        return cls(
            id = row["id"],
            username = row["username"],
            created_at = row["created_at"],
        )
    
    def __repr__(self):
        return print(f"[{self.id}] {self.username}")
    
    def __str__(self):
        return self.username