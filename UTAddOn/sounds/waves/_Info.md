# UT Sounds

Sound files of the original UnrealTournament games are not included!
The intended sound files to use are the "female voice" from "Unreal Tournament 2003/2004" and sounds from "Unreal Tournament 3". The names of all currently implemented sound files are listed in [Original UT Sound files](#original-ut-sound-files).
But in general, any other sound files can be used. See [WAV Compatibility](#wav-compatibility) to learn how to prepare sound files for usage.



## WAV Compatibility

Even if provided files are already in WAV format, they might not work for the Kex engine! Thus, all sound files should be converted in the following way:

What always seems to work:
* Use foobar2000
* Add desired files to a playlist
* Select all of them
* Rightclick->Convert->[default]

WAVs converted using WavePad don't work for some reason! Probably because some Info block is added to the header, which is too large.



## Original UT Sound Files

The following sound files are currently used by UT-AddOn (target storage location: `<root>/UTAddOn/sounds/waves/`):

UT2003/2004 sounds:

```
1_minute_remains.wav
20_seconds.wav
30_seconds_remain.wav
AmmoPack.wav
ArmorHit.wav
Averted.wav
Booster.wav
Denied.wav
Dominating.wav
Double_Kill.wav
GodLike.wav
HolyShit.wav
Humiliating_defeat.wav
Killing_Spree.wav
Last_Second_Save.wav
LudicrousKill.wav
MegaKill.wav
MonsterKill.wav
MultiKill.wav
Ownage.wav
Rampage.wav
Retribution.wav
ShieldPack.wav
UltraKill.wav
Unstoppable.wav
WhickedSick.wav
eight.wav
first_blood.wav
five.wav
four.wav
nine.wav
one.wav
seven.wav
six.wav
ten.wav
three.wav
two.wav
```

UT3 sounds:

```
bloodbath.wav
eradication.wav
excellent.wav
extermination.wav
impressive.wav
massacre.wav
termination.wav
unreal.wav
```

You may want to look at `<root>\UTAddOn\_tools_python\wav_durations.txt` to cross-check audio durations of these (and other) files.