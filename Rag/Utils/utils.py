from omegaconf.omegaconf import OmegaConf


def get_config(config_path: str):
    """
    Load the configuration file.
    Args:
        config_path (str): Path to the configuration file.
    Returns:
        dict: Configuration settings.
    """
    config = OmegaConf.load(config_path)
    config_dict = OmegaConf.to_container(config, resolve=True)
    return config_dict