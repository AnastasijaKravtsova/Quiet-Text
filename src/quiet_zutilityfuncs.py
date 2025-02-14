import yaml


settings_path = 'config/settings.yaml'
default_settings_path = 'config/settings-default.yaml'
default_syntax_path = 'language_configs/default_syntax.yaml'

def load_settings_data(default=False):
	if not default:
		with open(settings_path, 'r') as settings_config:
			return yaml.load(settings_config, Loader=yaml.FullLoader)
	else:
		with open(default_settings_path, 'r') as settings_config:
			return yaml.load(settings_config, Loader=yaml.FullLoader)

def load_default_syntax():
	with open(default_syntax_path) as syntax_config:
		return yaml.load(syntax_config, Loader=yaml.FullLoader)

def store_settings_data(new_settings):
	with open(settings_path, 'w') as settings_config:
		yaml.dump(new_settings, settings_config)

