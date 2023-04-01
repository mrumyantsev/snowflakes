import lib.lib as L
import config.config as C
import engine.engine as E

cfg_path = L.get_app_dir(__file__) + 'config.yml'
cfg = C.load_config(cfg_path)

resolution = (
    cfg['r_windowResolutionWidth'],
    cfg['r_windowResolutionHeight']
)

engine = E.Engine(resolution, cfg)
engine.run()
