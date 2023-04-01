import engine.engine as E
import constants as C

resolution = C.FULLSCREEN_RESOLUTION
snowflakes_number = C.SNOWFLAKES_NUMBER

engine = E.Engine(resolution, snowflakes_number)
engine.run()
