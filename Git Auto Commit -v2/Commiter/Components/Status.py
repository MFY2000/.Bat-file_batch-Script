class Status:
  def __init__(self, repo):
    self.repo = repo
    self.changes = []
    Status.status(self)

  def status(self):

    untrack = [ item for item in self.repo.untracked_files ]
    modified = [ item.a_path for item in self.repo.index.diff(None) ]
    
    self.changes = untrack + modified

  def isStatus(repo):
    result = repo.untracked_files != [] or repo.index.diff(None) != []
    return (result)

