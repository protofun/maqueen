snelheid = 120

def on_forever():
    if maqueen.read_patrol(maqueen.Patrol.PATROL_RIGHT) == 2 and maqueen.read_patrol(maqueen.Patrol.PATROL_RIGHT) == 0:
        maqueen.motor_run(maqueen.Motors.M1, maqueen.Dir.CW, snelheid)
        maqueen.motor_run(maqueen.Motors.M1, maqueen.Dir.CW, snelheid)
    elif maqueen.read_patrol(maqueen.Patrol.PATROL_LEFT) == 1 and maqueen.read_patrol(maqueen.Patrol.PATROL_RIGHT) == 0:
        maqueen.motor_run(maqueen.Motors.M1, maqueen.Dir.CW, snelheid)
        maqueen.motor_run(maqueen.Motors.M2, maqueen.Dir.CW, 0)
    elif maqueen.read_patrol(maqueen.Patrol.PATROL_LEFT) == 0 and maqueen.read_patrol(maqueen.Patrol.PATROL_RIGHT) == 1:
        maqueen.motor_run(maqueen.Motors.M1, maqueen.Dir.CW, 0)
        maqueen.motor_run(maqueen.Motors.M2, maqueen.Dir.CW, snelheid)
    elif maqueen.read_patrol(maqueen.Patrol.PATROL_LEFT) == 1 and maqueen.read_patrol(maqueen.Patrol.PATROL_RIGHT) == 0:
        maqueen.motor_run(maqueen.Motors.M2, maqueen.Dir.CW, snelheid)
        maqueen.motor_run(maqueen.Motors.M2, maqueen.Dir.CW, snelheid)
    elif maqueen.read_patrol(maqueen.Patrol.PATROL_LEFT) == 0 and maqueen.read_patrol(maqueen.Patrol.PATROL_LEFT) == 2:
        maqueen.motor_run(maqueen.Motors.M2, maqueen.Dir.CW, snelheid)
        maqueen.motor_run(maqueen.Motors.M2, maqueen.Dir.CW, snelheid)
    else:
        pass
basic.forever(on_forever)
