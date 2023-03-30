import engine.engine as enginem
import constants

resolution = constants.WINDOW_RESOLUTION
snowflakes_number = constants.SNOWFLAKES_NUMBER

engine = enginem.SnowflakesEngine(resolution, snowflakes_number)
engine.run()
