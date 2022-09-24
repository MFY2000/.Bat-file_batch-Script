class Status:
  def __init__(self, repo):
    self.repo = repo
    self.changes = []
    Status.status(self)

  def status(self):
    untrack = [ item for item in self.repo.untracked_files ]
    modified = [ item.a_path for item in self.repo.index.diff(None) ]
    
    self.changes = untrack + modified

  def isStatus(self):
    result = self.repo.untracked_files != [] or self.repo.index.diff(None) != []
    return (result)

