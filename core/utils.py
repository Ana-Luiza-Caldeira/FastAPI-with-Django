def get_first_name(self):
	if isinstance(self, bool):
		pass
	else:
		names = self.split()
		return names[0]


def get_last_name(self):
    if isinstance(self, bool):
        pass
    else:
        names = self.split()
        return names[-1]