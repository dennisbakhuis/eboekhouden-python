"""Simple test script for local testing."""
import eboekhouden_python as eb
from eboekhouden_python.models import MutatieFilter

client = eb.EboekhoudenClient()

# mutaties = client.get_mutaties()

print(MutatieFilter().export())
