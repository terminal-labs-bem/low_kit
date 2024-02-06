
from lowkit.objects import globalconfig
from lowkit.ops.wd import get_cwd
from lowkit.initialization.workingset import setup_workingset
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
	setup_workingset()
