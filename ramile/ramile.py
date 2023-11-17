#! python
import fire

from ramile.project import Project
from ramile.processors import FileProcessor


def extract(project_root, lines_to_extract=3000):
    project = Project(project_root, lines_to_extract)
    project.run()
    return

def main():
    fire.Fire(extract)


if __name__ == '__main__':
    main()
