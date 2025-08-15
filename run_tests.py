"""Run simple function-based tests (pytest-style) without external dependencies."""
import importlib
import pkgutil
import inspect
import sys

failed = 0
ran = 0

# Discover test modules in the tests package
for finder, name, ispkg in pkgutil.iter_modules(['tests']):
    module_name = f"tests.{name}"
    module = importlib.import_module(module_name)
    for obj_name, obj in inspect.getmembers(module, inspect.isfunction):
        if obj_name.startswith('test_'):
            ran += 1
            try:
                obj()
                print(f"PASS: {module_name}.{obj_name}")
            except AssertionError as e:
                failed += 1
                print(f"FAIL: {module_name}.{obj_name} - AssertionError: {e}")
            except Exception as e:
                failed += 1
                print(f"ERROR: {module_name}.{obj_name} - Exception: {e}")

print(f"\nRan {ran} tests, {failed} failures")
if failed:
    sys.exit(1)
else:
    sys.exit(0)
