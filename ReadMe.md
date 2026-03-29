# UT-AddOn

Always wanted to speedrun the game (but not really)?  
Now you have to (kinda), because if you don't ...  
... you die!

---

## About

The idea of UT-AddOn is in general a potential add-on for any (suitable) game, with the goal to add the well known UT-Sounds ('Double Kill', 'Multi Kill', ...) to the gameplay.

The specific add-on of this repository has been made for `Turok - Dinosaur Hunter` (avaliable on [Steam](https://store.steampowered.com/app/405820/Turok/)), which already supports mods written in AngelScript used by the Kex engine, which the game is built on.

### ‼️Important compatibility note‼️

The code of this mod is based on the Kex3 engine, but since the end of February 2025 the game has been upgraded to Kex4, to which the code is no longer compatible, leading to an error on startup!

Since to date no upgrade to Kex4 is planned, the game must be reverted to the latest Kex3 version (in **Steam** navigate to the **Properties** of the game and select **Game Version:** kex3 (Legacy Release, March 14, 2025)).

Feel free to create a Kex4 compatible version, if you are interested.

### ⚠️ Important note about sounds ⚠️

UT-AddOn is supposed to play certain UnrealTournament sound files (that's the whole idea), but the sound files are not included in this repository and must be added manually! 

➡️ See [_Info.md](UTAddOn/sounds/waves/_Info.md) for more details.

### How to play the game with this mod

1. Buy the game on [Steam](https://store.steampowered.com/app/405820/Turok/)
2. Ensure to use the Kex3 Legacy Release version (see previous section)
3. Navigate to the [Workshop](https://steamcommunity.com/app/405820/workshop/) page of the game, find UT-AddOn and subscribe it
4. Navigate to the Properties of the game in Steam and ensure the option `General->Selected Launch Option` is set to `Ask When starting game`
5. Start the game via PLAY button in Steam and you should get asked to either start the game normally or to launch the game editor -> select `Launch Game Editor` and start it
6. Navigate to the `Workshop Items` tab -> you should see UT-AddOn there
7. Select UT-AddOn in the list (and maybe other mods as well, but compatibility is not ensured!) and click the Play button (looks like: ▶️) to start the game with the selected mods

💡HINT: Ingame the console can usually be opened via `^` key (circumflex). There you can see status messages from UT-AddOn and certain commands can be executed (see [Console Commands](#console-commands)).

## Quick start

Not a fan of reading long texts? Then just do the following:

- Start Turok with this mod enabled  
- Go to **Options** -> **Game Play** -> **Hud Options** and set **Show Hud** to **Off** 
- Go to **Options** -> **Game Play** -> **Head Bobbing Options** and set ALL options to **Off**  
- Start a new game and have fun  

Or watch [this video](https://www.youtube.com/watch?v=uCNFpQMSxpU)

## Demo

[Level 5 and 6 Demo (YouTube)](https://www.youtube.com/watch?v=V8UssdtAS7o)

---

## Description

Aside from several cool Unreal Tournament sounds being played (like "Double Kill", etc.), UT-AddOn adds continuous damage to the player, such that your health/armor decreases every few seconds. But killing enemies will pause that damage infliction and will even heal, if you kill fast enough.

### Killing Streaks

If the time between kills do not exceed 2.5 seconds, you are on a killing streak! The remaining time until the streak ends is displayed as a red bar (that changes width) in the UT-AddOn HUD (details see below) and can only be reset by further kills. If the time is up, damage infliction starts again immediately.  

The higher the streak, the higher the healing rate, until the healing rate limit is reached (depends on difficulty setting, see below for details). The healing will always stop at the maximal health limit, depicted as orange bar in the UT-AddOn hud below the health value. This limit can be increased, if you reach high killing streaks (at least 7 kills in a row).  

Note that in general, if your health/armor is above this limit (depicted as red bar in the hud below the health/armor value), the damage that is inflicted is increased.

### Killing Sprees

Try not to get hit by enemies! If you manage to kill 5 enemies without getting hit, a small percentage of ammo is restored for the currently used weapon. This event is called a killing spree!  

There are 6 levels of killing sprees, where each gives more ammo than the previous one. If you manage to reach the highest spree (30 kills without getting hit), you get full armor and ammo (for the current weapon) and the armor limit is increased by 5. So it's totally worth it!  

Note that any hit you get will reset the spree count to zero! Only a shield will protect you from that (but shields won't gonna last long).

### Boss fights

During boss fights, damage is still continuously taken! But if your health drops below 60, the bosses begin to spawn health items.  

When that happens, be quick collecting them, because they only last for 10 seconds until they despawn again! Also note that health items are spawned close to the boss. But usually it's not a good idea to get within the melee range of a boss. So be careful.

### HUD

For the best experience, UT-AddOn comes with an own ingame HUD. See the corresponding section further below for details about that.

### Damage infliction

The damage infliction on Turok's health/armor is set as follows:

- If health is 60 or smaller (yellow bar in hud): 1 damage every second (DPS = 1.0)  
- If health is at the current limit or smaller (orange bar): 3 damage every 2 seconds (DPS = 1.5)  
- If health is above the current limit (red bar): 5 damage every 2 seconds (DPS = 2.5)  

- If armor is at the current limit or smaller (orange bar): 2 damage every 2 seconds (DPS = 1.0)  
- If armor is above the current limit (red bar): 2 damage every second (DPS = 2.0)  

---

## Compatibility to other mods

UT-AddOn should be compatible with most mods. But it was not possible to avoid overriding the following scripts:

- `player.txt`  
- `enemy/enemy.txt`  
- `enemy/insect.txt`  
- `enemy/sentry.txt`  
- `enemy/turret.txt`  

If these files are not touched by another mod, things should work out.

Note that UT-AddOn is not compatible with the Turok+ mod for the above reasons.

---

## Game alterations

UT-AddOn swaps the 3D models for the big and small plasma ammo item (because that's actually wrong in the remaster version of the game).

---

## About the HUD

UT-AddOn comes with an own hud. Unfortunately, the "Turok script language" does not offer a possibility to implement an actual custom hud. So instead, 3D objects are used and placed within the 3D world, such that it looks like a hud.  

This leads to some unavoidable side effects:

- Parts of the hud may clip into parts of the 3D world and some weapon models  
- Bobbing and climbing effects alter the camera orientation → hud may shift or behave strangely  

### How to enable the HUD

Since the default Turok hud would interfere with the UT-AddOn hud:

- If Turok HUD is ON → UT-AddOn HUD is disabled  
- If Turok HUD is OFF → UT-AddOn HUD is enabled  

To disable the Turok HUD:

- Go to "Options" -> "Game Play" -> "Hud Options"  
- Set "Show Hud" to "Off"  

**Important note:**  
Disabling the HUD hides some game texts. Alternative:

- Keep "Show Hud" ON  
- Reduce "Hud opacity" below 100 (or 0)  

This keeps texts visible and enables UT-AddOn HUD.

Note:  
UT-AddOn HUD is not enabled immediately after changing settings. You must:

- Return to main menu and start/load a game  

Or use console:

```call UTAddOn::Hud::Enable```

(A disable command also exists.)

### Recommended game settings

- Disable Turok HUD completely (personal preference)  
- Disable ALL bobbing effects  

To disable bobbing:

- "Options" -> "Game Play" -> "Head Bobbing Options"  
- Set everything to "Off"  

---

## Console commands

Open console with `^` (left of 1 key).

To see available commands:

```call UTAddOn::Help```

---

## Difficulties

You can change UT-AddOn gameplay via console.

### Difficulty: Off

- No gameplay changes  
- Only sounds + HUD active  

### Difficulty: Normal (default)

- Streak duration: 2.5 seconds  
- Max heal rate: 5 HP/sec  

### Difficulty: Baby

- No damage  
- Healing ON  
- Armor heals with full health  
- Unlimited heal rate  
- Streak duration: 3.5 seconds  

### Difficulty: Easy

- Armor heals with full health  
- Heal rate ≤ 10 HP/sec  
- Streak duration: 3.0 seconds  

### Difficulty: Hard

- Kills do NOT stop damage  
- Heal rate ≤ 3 HP/sec  
- Healing starts with first kill  
- Streak duration: 2.5 seconds  

### Difficulty: Hardcore

- Like Hard  
- NO healing  
- NO achievements  

---

💡 If the difficulty is too high, don't be ashamed to lower it! The mod is supposed to be fun!

---

## Note for mod developers

Feel free to re-use any of the code.

Execute `pack_and_start.bat` to generate a new kpf-file and start the game (requires to put the repo in `<TurokGameDir>/mods/turok-ut-addon`).

---

## Credits

Special thanks to Smoke39 for the amazing and very useful online documentation ([Turok Ex Modding Guide](https://smoke39.github.io/turok/index.html)).