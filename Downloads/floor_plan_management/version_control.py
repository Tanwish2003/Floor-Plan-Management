

class VersionControlSystem:
    def __init__(self):
        self.history = []
        self.current_version = 0s

    def commit(self, changes):
        # Commit changes to the floor plan
        self.current_version += 1
        self.history.append({'version': self.current_version, 'changes': changes})
        print(f"Committed changes to version {self.current_version}")

    def rollback(self, version):
        # Rollback to a specific version of the floor plan
        if version <= self.current_version and version > 0:
            self.current_version = version
            print(f"Rolled back to version {self.current_version}")
        else:
            print("Invalid version specified for rollback")

    def get_floor_plan_at_version(self, version):
        # Retrieve the floor plan at a specific version
        if version <= self.current_version and version > 0:
            floor_plan = {}
            for change in self.history[:version]:
                # Apply changes up to the specified version
                floor_plan.update(change['changes'])
            return floor_plan
        else:
            print("Invalid version specified for retrieval")

