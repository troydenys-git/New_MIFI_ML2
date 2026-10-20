"""Download GTZAN dataset to ./data via KaggleHub."""

from __future__ import annotations

import os
from pathlib import Path

from dotenv import load_dotenv

DATASET_HANDLE = "andradaolteanu/gtzan-dataset-music-genre-classification"
PROJECT_ROOT = Path(__file__).resolve().parent
DATA_DIR = PROJECT_ROOT / "data"


def configure_kaggle_credentials() -> None:
    token = os.getenv("KAGGLE_API_TOKEN")
    if not token:
        return

    from kagglehub import config as kaggle_config

    kaggle_config.set_kaggle_api_token(token.strip())


def download_dataset(
    output_dir: Path | str = DATA_DIR,
    *,
    force_download: bool = False,
) -> Path:
    import kagglehub

    load_dotenv(PROJECT_ROOT / ".env")
    configure_kaggle_credentials()

    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    path = kagglehub.dataset_download(
        DATASET_HANDLE,
        output_dir=str(output_dir),
        force_download=force_download,
    )
    return Path(path)


def main() -> None:
    path = download_dataset()
    print(f"Path to dataset files: {path}")


if __name__ == "__main__":
    main()
