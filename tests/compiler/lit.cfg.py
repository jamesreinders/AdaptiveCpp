import lit.formats
import os

config.name = 'AdaptiveCpp Plugin'
config.test_format = lit.formats.ShTest(True)

config.suffixes = ['.c', '.cpp', '.cc']

config.test_source_root = os.path.dirname(__file__)
config.test_exec_root = os.path.join(config.my_obj_root, 'test')

config.substitutions.append(('%acpp', config.acpp_compiler))

if "ACPP_DEBUG_LEVEL" in os.environ:
  config.environment["ACPP_DEBUG_LEVEL"] = os.environ["ACPP_DEBUG_LEVEL"]
if "ACPP_VISIBILITY_MASK" in os.environ:
  config.environment["ACPP_VISIBILITY_MASK"] = os.environ["ACPP_VISIBILITY_MASK"]
