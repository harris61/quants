import sys
import os

print("=== Python Installation Info ===")
print(f"Python executable: {sys.executable}")
print(f"Python version: {sys.version}")
print(f"Install location: {os.path.dirname(sys.executable)}")

# Check if in virtual environment
print(f"\nIn virtual environment: {hasattr(sys, 'real_prefix') or sys.prefix != sys.base_prefix}")
if hasattr(sys, 'real_prefix') or sys.prefix != sys.base_prefix:
    print(f"Virtual env location: {sys.prefix}")

print(f"\nPATH contains:")
for path in sys.path[:5]:  # First 5 paths
    print(f"  {path}")