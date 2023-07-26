import sys
import pytest

from pathlib import Path, PosixPath
from typing import List

from dangerzone.document import SAFE_EXTENSION

sys.dangerzone_dev = True  # type: ignore[attr-defined]


SAMPLE_DIRECTORY = "test_docs"
SAMPLE_EXTERNAL_DIRECTORY = "test_docs_external"
BASIC_SAMPLE = "sample-pdf.pdf"
test_docs_dir = Path(__file__).parent.joinpath(SAMPLE_DIRECTORY)
test_docs = [
    p
    for p in test_docs_dir.rglob("*")
    if p.is_file()
    and not (p.name.endswith(SAFE_EXTENSION) or p.name.startswith("sample_bad"))
]

# Pytest parameter decorators
for_each_doc = pytest.mark.parametrize("doc", test_docs)


# External Docs - base64 docs encoded for externally sourced documents
# XXX to reduce the chance of accidentally opening them
test_docs_external_dir = Path(__file__).parent.joinpath(SAMPLE_EXTERNAL_DIRECTORY)


def get_docs_external(pattern: str = "*") -> List[PosixPath]:
    if not pattern.endswith("*"):
        pattern = f"{pattern}.b64"
    return [
        p
        for p in test_docs_external_dir.rglob(pattern)
        if p.is_file() and not (p.name.endswith(SAFE_EXTENSION))
    ]


# Pytest parameter decorators
def for_each_external_doc(glob_pattern: str = None):
    test_docs_external = get_docs_external(glob_pattern)
    return pytest.mark.parametrize(
        "doc",
        test_docs_external,
        ids=[str(doc.name).rstrip(".b64") for doc in test_docs_external],
    )


class TestBase:
    sample_doc = str(test_docs_dir.joinpath(BASIC_SAMPLE))


@pytest.fixture
def sample_doc() -> str:
    return str(test_docs_dir.joinpath(BASIC_SAMPLE))


@pytest.fixture
def unreadable_pdf(tmp_path: Path) -> str:
    file_path = tmp_path / "document.pdf"
    file_path.touch(mode=0o000)
    return str(file_path)
