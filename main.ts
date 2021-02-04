let snelheid = 120
basic.forever(function () {
    if (maqueen.readPatrol(maqueen.Patrol.PatrolRight) == 2 && maqueen.readPatrol(maqueen.Patrol.PatrolRight) == 0) {
        maqueen.motorRun(maqueen.Motors.M1, maqueen.Dir.CW, snelheid)
        maqueen.motorRun(maqueen.Motors.M1, maqueen.Dir.CW, snelheid)
    } else if (maqueen.readPatrol(maqueen.Patrol.PatrolLeft) == 1 && maqueen.readPatrol(maqueen.Patrol.PatrolRight) == 0) {
        maqueen.motorRun(maqueen.Motors.M1, maqueen.Dir.CW, snelheid)
        maqueen.motorRun(maqueen.Motors.M2, maqueen.Dir.CW, 0)
    } else if (maqueen.readPatrol(maqueen.Patrol.PatrolLeft) == 0 && maqueen.readPatrol(maqueen.Patrol.PatrolRight) == 1) {
        maqueen.motorRun(maqueen.Motors.M1, maqueen.Dir.CW, 0)
        maqueen.motorRun(maqueen.Motors.M2, maqueen.Dir.CW, snelheid)
    } else if (maqueen.readPatrol(maqueen.Patrol.PatrolLeft) == 1 && maqueen.readPatrol(maqueen.Patrol.PatrolRight) == 0) {
        maqueen.motorRun(maqueen.Motors.M2, maqueen.Dir.CW, snelheid)
        maqueen.motorRun(maqueen.Motors.M2, maqueen.Dir.CW, snelheid)
    } else if (maqueen.readPatrol(maqueen.Patrol.PatrolLeft) == 0 && maqueen.readPatrol(maqueen.Patrol.PatrolLeft) == 2) {
        maqueen.motorRun(maqueen.Motors.M2, maqueen.Dir.CW, snelheid)
        maqueen.motorRun(maqueen.Motors.M2, maqueen.Dir.CW, snelheid)
    } else {
    	
    }
})
