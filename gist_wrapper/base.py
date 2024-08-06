from typing import Dict
from os import getenv

from gist_wrapper.star import StarGist
from gist_wrapper.get_gist import GetGist
from gist_wrapper.fork import ForkGist
from gist_wrapper.create import CreateGist
from gist_wrapper.delete import DeleteGist
from gist_wrapper.users import GetUser
from dotenv import load_dotenv
from os import getenv


load_dotenv()

GITHUB_API_KEY = getenv("GITHUB_API_KEY")


class Gist():
    def __init__(self):
        
        self.gist_token = GITHUB_API_KEY
        
        header: Dict[str, str] = {
            "Accept": "application/vnd.github+json",
            "Authorization": f"Bearer {self.gist_token}",
            "X-GitHub-Api-Version": "2022-11-28",
        }
        self.headers = header
        
        self.identity = {}

        self.gist_token = None

        self.rate = StarGist(self.headers)
        self.get = GetGist(self.headers)
        self.fork = ForkGist(self.headers)
        self.create = CreateGist(self.headers)
        self.delete = DeleteGist(self.headers)
        self.user = GetUser(self.headers)
        
if __name__ == "__main__":
    gist = Gist()

    # TEST DELETE
    # delete_gist = gist.delete.removeGist(gist_id="21e5d319c5c2b2f2323815aee90c876a")
    # print(delete_gist)

    # TEST CREATE
    # files = {"README.md": {"content": "Hello World"}}
    # create_gist = gist.create.newGist(description="A sample readme file", public=False, files=files)

    # print(create_gist)

    # TEST FORK
    # forks = gist.fork.getForks(gist_id="54b4995bd68275691a23")
    # print(forks)

    # fork_gist = gist.fork.createFork(gist_id="2cd39deefde8c8926b1127c9029165ab")
    # print(fork_gist)

    # TEST STAR
    # status = gist.star.check_if_starred(gist_id="4582cb1902a626231c7a2746082f7ee4")
    # print(status)

    # status = gist.star.star(gist_id="4582cb1902a626231c7a2746082f7ee4")
    # print(status)

    # status = gist.star.unstar(gist_id="4582cb1902a626231c7a2746082f7ee4")
    # print(status)

    # TEST FETCH GISTS
    # gists = gist.get.Gist(category="")
    # print(gists[0])

    # gist_by_id = gist.get.by_id(gist_id="b9893bd47dd9b00e4fc4aa7bc20fb553")
    # print(gist_by_id)

    # TEST GET COMMITS
    # gist_commits = gist.get.commits(gist_id="b9893bd47dd9b00e4fc4aa7bc20fb553")
    # print(gist_commits[0])
