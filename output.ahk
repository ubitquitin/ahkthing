T95_Spec()
{
SendInput {Home down}
Sleep, % ran(1,2)
SendInput {Home up}
Sleep, % ran(1,2)
}

Range2h()
{
SendInput {b down}
Sleep, % ran(1,2)
SendInput {b up}
Sleep, % ran(1,2)
}

Melee2h()
{
SendInput {Shift down}
Sleep, % ran(1,2)
SendInput {c down}
Sleep, % ran(1,2)
SendInput {c up}
Sleep, % ran(1,2)
SendInput {Shift up}
Sleep, % ran(1,2)
}
