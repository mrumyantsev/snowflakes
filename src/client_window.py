import engine.engine as E
import constants as C

resolution = C.WINDOW_RESOLUTION
snowflakes_number = C.SNOWFLAKES_NUMBER

engine = E.Engine(resolution, snowflakes_number)
engine.run()
