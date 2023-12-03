
from lowkit.objects import globalconfig
from lowkit.ops.wd import get_cwd
from lowkit.infosources.distribution import info
from lowkit.settings import VERSION, PROJECT_NAME
from lowkit.ops.scaffolding import set_global_bracket_data, get_global_bracket_data
from lowkit.ops.scaffolding import get_hydrated_scaffolding_paths, build_scaffolding, test_scaffolding, get_scaffolding_style, scaffolding_styles
from lowkit.infosources.distribution import (
	get_distribution_name,
	get_distribution_version, 
	distribution_install_editable,
	caller_info, 
	call_order, 
	get_distribution_files, 
	get_distribution_filepaths,
	get_distribution_source,
	get_distribution_asset_filepath_by_ext,
	)


from lowkit.infosources.config import find_config


def cli():
    print("#####")
    print("name ==")
    name = get_distribution_name()
    print(name)
    print("#####")
    print("get_distribution_version")
    print(get_distribution_version(name))
    print("#####")
    print("distribution_install_editable")
    print(distribution_install_editable(name))
    print("#####")
    print("call_order")
    print(call_order())
    print("#####")
    print("get_distribution_files")
    print(get_distribution_files(name))
    print("#####")
    print("get_distribution_filepaths")
    print(get_distribution_filepaths(name))
    print("#####")
    print("get_distribution_source")
    print(get_distribution_source())
    print(get_distribution_asset_filepath_by_ext("txt"))
    print(get_cwd())
    print(find_config(name))