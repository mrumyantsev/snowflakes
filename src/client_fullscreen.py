import engine.engine as enginem
import constants

resolution = constants.FULLSCREEN_RESOLUTION
snowflakes_number = constants.SNOWFLAKES_NUMBER

engine = enginem.SnowflakesEngine(resolution, snowflakes_number)
engine.run()
