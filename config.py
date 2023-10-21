from __future__ import annotations
from typing import Final

import os
from dotenv import load_dotenv

load_dotenv()

TOKEN: Final = os.getenv("TOKEN")
