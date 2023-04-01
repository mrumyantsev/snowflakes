import engine.engine as E
import constants

resolution = constants.WINDOW_RESOLUTION
snowflakes_number = constants.SNOWFLAKES_NUMBER

engine = E.Engine(resolution, snowflakes_number)
engine.run()
