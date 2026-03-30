# UTAddOn

Always wanted to speedrun the game (but not really)?  
Now you have to (kinda), because if you don't ...  
... you die!

---

## About

The idea of UTAddOn is in general a potential add-on for any (suitable) game, with the goal to add the well known UT-Sounds ('Double Kill', 'Multi Kill', ...) to the gameplay.

The specific add-on of this repository has been made for `Turok - Dinosaur Hunter` (avaliable on [Steam](https://store.steampowered.com/app/405820/Turok/)), which already supports mods written in AngelScript used by the Kex engine, which the game is built on.

### ‼️Important compatibility note‼️

The code of this mod is based on the Kex3 engine, but since the end of February 2025 the game has been upgraded to Kex4, to which the code is no longer compatible, leading to an error on startup!

Since to date no upgrade to Kex4 is planned, the game must be reverted to the latest Kex3 version (in **Steam** navigate to the **Properties** of the game and select **Game Version:** kex3 (Legacy Release, March 14, 2025)).

Feel free to create a Kex4 compatible version, if you are interested.

### ⚠️ Important note about sounds ⚠️

UTAddOn is supposed to play certain UnrealTournament sound files (that's the whole idea), but the sound files are not included in this repository and must be added manually! 

➡️ See [_Info.md](UTAddOn/sounds/waves/_Info.md) for more details.

### How to play the game with this mod

1. Buy the game on [Steam](https://store.steampowered.com/app/405820/Turok/)
2. Ensure to use the Kex3 Legacy Release version (see [Important compatiblity note](#️important-compatibility-note️))
3. Navigate to the [Workshop](https://steamcommunity.com/app/405820/workshop/) page of the game, find UTAddOn and subscribe it
4. Navigate to the Properties of the game in Steam and ensure the option `General->Selected Launch Option` is set to `Ask When starting game`
5. Start the game via PLAY button in Steam and you should get asked to either start the game normally or to launch the game editor -> select `Launch Game Editor` and start it
6. Navigate to the `Workshop Items` tab -> you should see UTAddOn there
7. Select UTAddOn in the list (and maybe other mods as well, but compatibility is not ensured!) and click the Play button (looks like: ▶️) to start the game with the selected mods

💡HINT: Ingame the console can usually be opened via `^` key (circumflex). There you can see status messages from UTAddOn and certain commands can be executed (see [Console Commands](#console-commands)).

## Quick start

Not a fan of reading long texts? Then just do the following:

- Start Turok with this mod enabled  
- Go to **Options** -> **Game Play** -> **Hud Options** and set **Show Hud** to **Off** 
- Go to **Options** -> **Game Play** -> **Head Bobbing Options** and set ALL options to **Off**  
- Start a new game and have fun  

Or watch [this video (YouTube)](https://www.youtube.com/watch?v=uCNFpQMSxpU)

## Demo

[Level 5 and 6 Demo (YouTube)](https://www.youtube.com/watch?v=V8UssdtAS7o)

---

## Description

Aside from several cool Unreal Tournament sounds being played (like "Double Kill", etc.), UTAddOn adds continuous damage to the player, such that your health/armor decreases every few seconds. But killing enemies will pause that damage infliction and will even heal, if you kill fast enough.

### Killing Streaks

If the time between kills do not exceed 2.5 seconds, you are on a killing streak! The remaining time until the streak ends is displayed as a red bar (that changes width) in the UTAddOn HUD (details see below) and can only be reset by further kills. If the time is up, damage infliction starts again immediately.

The higher the streak, the higher the healing rate, until the healing rate limit is reached (depends on difficulty setting, see below for details). The healing will always stop at the maximal health limit, depicted as orange bar in the UTAddOn HUD below the health value. This limit can be increased, if you reach high killing streaks (at least 7 kills in a row).

Note that in general, if your health/armor is above this limit (depicted as red bar in the HUD below the health/armor value), the damage that is inflicted is increased.

### Killing Sprees

Try not to get hit by enemies! If you manage to kill 5 enemies without getting hit, a small percentage of ammo is restored for the currently used weapon. This event is called a killing spree!

There are 6 levels of killing sprees, where each gives more ammo than the previous one. If you manage to reach the highest spree (30 kills without getting hit), you get full armor and ammo (for the current weapon) and the armor limit is increased by 5. So it's totally worth it! 

Note that any hit you get will reset the spree count to zero! Only a shield will protect you from that (but shields won't gonna last long).

### Boss fights

During boss fights, damage is still continuously taken! But if your health drops below 60, the bosses begin to spawn health items.

When that happens, be quick collecting them, because they only last for 10 seconds until they despawn again! Also note that health items are spawned close to the boss. But usually it's not a good idea to get within the melee range of a boss. So be careful.

### HUD

For the best experience, UTAddOn comes with an own ingame HUD. See section [About the HUD](#about-the-hud) for details about that.

### Damage infliction

The damage infliction on Turok's health/armor is set as follows:

- If health is 60 or smaller (yellow bar in HUD): 1 damage is taken every second (DPS = 1.0 (DPS = damage per second))
- If health is at the current limit or smaller (orange bar in HUD): 3 damage is taken every 2 seconds (DPS = 1.5)
- If health is above the current limit (red bar in HUD): 5 damage is taken every 2 seconds (DPS = 2.5)

- If armor is at the current limit or smaller (orange bar in HUD): 2 armor damage is taken every 2 seconds (DPS = 1.0)
- If armor is above the current limit (red bar in HUD): 2 armor damage is taken every second (DPS = 2.0)

---

## Compatibility to other mods

UTAddOn should be compatible with most mods. But it was not possible to avoid overriding the following scripts:

- `player.txt`  
- `enemy/enemy.txt`  
- `enemy/insect.txt`  
- `enemy/sentry.txt`  
- `enemy/turret.txt`  

If these files are not touched by another mod, things should work out.

Note that UTAddOn is not compatible with the Turok+ mod for the above reasons.

---

## Game alterations

UTAddOn swaps the 3D models for the big and small plasma ammo item (because that's actually wrong in the remaster version of the game).

---

## About the HUD

UTAddOn comes with an own HUD. Unfortunately, the "Turok script language" does not offer a possibility to implement an actual custom HUD. So instead, 3d objects are used and placed within the 3d world, such that it looks like a HUD. 

This leads to some unwanted side effects, which cannot be avoided (unfortunately):

- Parts of the HUD may clip into parts of the 3d world and some weapon models
- Bobbing and things like climbing alter the camera orientation, which cannot be accessed entirely from within the script language. Thus, when bobbing effects are enabled and/or Turok is climbing or standing on movable ground, the HUD will be displaced (sometimes in weird ways). This cannot be avoided and we have to live with that. But at least bobbing could be disabled (see [Recommended game settings](#recommended-game-settings)).

### How to enable the HUD

Since the default Turok HUD would interfere with the UTAddOn HUD, the UTAddOn HUD is automatically disabled, if the Turok HUD is enabled. Vice versa, the UTAddOn HUD is automatically enabled, if the Turok HUD is disabled.

To disable the Turok HUD, do the following:

- In the game go to **Options** -> **Game Play** -> **Hud Options**
- Set option **Show Hud** to **Off**

**Important note:**  

If the Turok HUD is disabled like that, this would lead to several ingame texts to be invisible (e.g. the "All keys found in this level" message, or the life counter in the top right corner). To avoid this, it is also possible to leave the "Show Hud" option "On" and decrease the "Hud opacity" to a value below 100.0 (or even 0.0) instead. This would also automatically enable the UTAddOn HUD, without the normal game texts to get invisible.

Note that the UTAddOn HUD is not automatically enabled, if you change the Turok settings during a game. You need to go back to the main menue and start a new game or just load a savegame or enter a new level.
If you want to enable the UTAddOn HUD manually and immediately, you can execute the following console command:

```call UTAddOn::Hud::Enable```

(a Disable command exists accordingly)

See the section [Console commands](#console-commands) below for more details on that.

### Recommended game settings

It is recommended to disable the Turok HUD entirely, because just reducing the opacity will not prevent the original hit-screens (red/yellow flash when getting hit) to appear, which leads to unpleasing visual effects. But that's personal taste only.

Aside from that, it is highly recommended to disable all bobbing effects, such that the HUD stays fixed on the screen in most situations.

To disable bobbing effects, do the following:

- In the game go to **Options** -> **Game Play** -> **Head Bobbing Options**
- Set everything to **Off**

---

## Console commands

The ingame console can usually be opened (and closed) by pressing the `^`-key (circumflex/caret -> the key left to the number 1 on most keyboards). You might find some useful information there, since UTAddOn prints some messages to the console. But more importantly, there are certain commands, which can be executed.

To see the list of available UTAddOn commands, type the following into the console and press enter:

```call UTAddOn::Help```

---

## Difficulties

As can bee seen in the console by executing the `Help` command, you can alter the gameplay settings of UTAddOn by setting a different UTAddOn difficulty level (by executing the corresponding command in the console; execute `call UTAddOn::Help` to see them). 
Do this in case the default setting doesn't satisfy you (especially when using UTAddOn together with other mods, it might happen that the default setting doesn't fit well enough and makes things too hard or too easy).

The following options are provided:

### Difficulty: Off

Select this, if you don't want UTAddOn to interfere with any of the default gameplay mechanics. Only sound effects and the HUD will still be enabled, but no damage, healing or achievements will happen.

### Difficulty: Normal (default)

This is the default setting and it should work fine for the original game.

- Streak duration (max. time between kills to count as a streak) is 2.5 seconds
- Maximum heal rate is 5 HP per second

### Difficulty: Baby

If you really don't know what you are doing, this setting may be for you.

- Continuous damage is OFF
- Healing is ON
- Armor is healed when health is maxxed
- Unlimited heal rate
- Streak duration is 3.5 seconds  

### Difficulty: Easy

If Baby is too easy, but Normal still too hard.

- Continuous damage is ON
- Healing is ON
- Armor is healed when health is maxxed
- Heal rate is limited to 10 HP per second
- Streak duration is 3.0 seconds

### Difficulty: Hard

If the normal difficulty is not hard enough.

- Killing enemies doesn't interrupt the continuous damage!
- Heal rate is limited to 3 health per second
- Streak duration is 2.5 seconds

### Difficulty: Hardcore

If you like the pain.

- Killing enemies doesn't interrupt the continuous damage!
- No healing
- No achievements
- Streak duration is 2.5 seconds

---

💡 If the difficulty is too high, don't be ashamed to lower it! The mod is supposed to be fun!

---

## Note for mod developers

Feel free to re-use any of the code.

Execute `pack_and_start.bat` to generate a new kpf-file and start the game (requires to put the repo in `<TurokGameDir>/mods/turok-ut-addon`).

---

## Credits

Special thanks to Smoke39 for the amazing and very useful online documentation ([Turok Ex Modding Guide](https://smoke39.github.io/turok/index.html)).