from pathlib import Path

import yaml


class TestGenerator(type):
    def __new__(
        cls,
        name,
        bases,
        attrs,
        # Directory to find test files (.yaml, .yml, .json)
        tests_dir: str = "",
        # Prefix for the generated test methods
        test_prefix: str = "testgen_",
        # Class method name to call for each test, must start with _ to avoid being run as a test
        test_method: str = "_test",
    ):
        test_suffixes = {".yaml", ".yml", ".json"}
        test_files = [f for f in Path(tests_dir).iterdir() if f.suffix in test_suffixes]

        def gen_test(test_name, test_file):
            def test(self):
                test_data = yaml.safe_load(test_file.open(encoding="utf-8").read())
                getattr(self, test_method)(test_name, test_data)

            return test

        # Loop them and create class methods
        for test_file in test_files:
            test_name = test_file.stem
            # Attach the method
            method_name = "{0}{1}".format(test_prefix, test_name)
            attrs[method_name] = gen_test(test_name, test_file)

        return type.__new__(cls, name, bases, attrs)
