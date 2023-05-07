import importlib
import os

class BlueprintLoaders:
    def __init__(self):
        pass

    @staticmethod
    def discover_blueprints_by_pattern():
        package_blueprints = list()
        packages = os.listdir('apps')

        for package in packages:
            if ".py" in package:
                continue
            if "." in package:
                continue
            if "__" in package:
                continue

            package = ".{}.blueprints".format(package)
            try:
                spec = importlib.util.find_spec(package, 'apps')
                if spec is None:
                    continue
                else:
                    modules = importlib.util.module_from_spec(spec)
                    spec.loader.exec_module(modules)

                    package_attributes = dir(modules)
                    pmodules = [pm for pm in package_attributes if "_blueprint" in pm]
                    for pmodule in pmodules:
                        package_blueprints.append(getattr(modules, pmodule))
            except Exception as e:
                raise Exception(e)
                continue

        return package_blueprints
