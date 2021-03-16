from aiorobot import run_robot
from aiorobot.fake_driver import Client

async def main(robot):
    await robot.marker.down()
    for i in range(4):
        await robot.motor.drive(150)
        await robot.motor.rotate(900)
    await robot.marker.up()
    await robot.disconnect()

await run_robot(started=main, client_cls=Client)