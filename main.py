from gist_wrapper import Gist


gist = Gist()

gist.create.create_new_gist(public=False, description="A new gist", files={"README.md":{"content":"Hello World"}})

