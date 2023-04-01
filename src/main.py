import lib.lib as L
import config.config as C
import engine.engine as E


def main() -> None:
    cfg_path = L.get_app_dir(__file__) + 'config.yml'
    cfg = C.load_config(cfg_path)

    engine = E.Engine(cfg)
    engine.run()


if __name__ == "__main__":
    main()
