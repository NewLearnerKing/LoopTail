# Snake Game

A modern implementation of the classic Snake game with enhanced graphics, smooth gameplay, a beautiful menu system, special power-ups, and fully customizable settings.

## 🎮 Features

### Core Gameplay
- **Wall Wrapping**: Snake wraps around the screen instead of dying when hitting walls
- **Smooth Animations**: Food items animate with easing effects (growing/fading)
- **Progressive Difficulty**: Game speed increases every 5 points (respects settings)
- **Special Food**: Golden power-up food that appears randomly and gives bonus points

### Visual Enhancements
- **Modern UI**: Clean menu system with interactive buttons and hover effects
- **Animated Food**: Food items pulse and grow with smooth animations
- **Special Food Effects**: Golden food with sparkles and pulsing animation
- **Status Bar**: Real-time score, high score, and special food timer display
- **Debug Information**: Shows special food spawn chance and next check timing
- **Pause System**: In-game pause functionality
- **Consistent Color Scheme**: All buttons use the same color palette across all menus

### User Interface
- **Main Menu**: Beautiful start screen with Play, Settings, and Quit buttons
- **Colorful Buttons**: Green play button, blue settings button, red quit button with hover effects
- **Pause Menu**: In-game pause with Resume and Main Menu options
- **Game Over Screen**: Displays final score and high score with Restart and Main Menu options
- **Settings Menu**: Fully functional settings with interactive sliders
- **Interactive Buttons**: Hover effects and click animations
- **Mouse Support**: Full mouse navigation with keyboard shortcuts

### Settings System
- **Game Speed**: Adjustable from 5 to 20 FPS (affects snake movement speed)
- **Special Food Chance**: Control spawn rate from 5% to 25% (every 3 points)
- **Special Food Duration**: Set duration from 15 to 60 seconds
- **Interactive Sliders**: Drag to adjust settings in real-time
- **Immediate Application**: Settings are applied to new games and current gameplay
- **New Game Behavior**: Returning to main menu and pressing play starts a fresh game with current settings

### Special Food System
- **Golden Power-ups**: Special food appears randomly every 3 points based on configured chance
- **Single Spawn**: Only one special food can exist at a time
- **Time Limited**: Special food disappears after configurable duration
- **Bonus Points**: Gives 5 points instead of 1
- **Extra Growth**: Adds 3 segments to the snake instead of 1
- **Visual Effects**: Larger size, golden color, sparkles, and flashing when about to disappear
- **Timer Display**: Shows remaining time in status bar
- **Fully Controllable**: Player can set exact spawn chance and duration
- **Debug Information**: Status bar shows next check timing and current spawn chance
- **Console Logging**: Detailed console output for special food spawning events

### Technical Features
- **State Management**: Proper game state handling (menu, playing, paused, game over, settings)
- **Responsive Design**: Clean, modern UI that works well
- **High Score System**: Automatically saves and loads high scores
- **Reliable Quit**: Properly handles window close events
- **Dynamic Settings**: Game adapts to user preferences in real-time
- **Fresh Start**: Main menu always starts a new game with current settings
- **Debug Features**: Console logging and status bar debug information

## 🚀 Installation

1. Install Python 3.7+ and pygame:
```bash
pip install -r requirements.txt
```

2. Run the game:
```bash
python main.py
```

## 🎯 Controls

### In-Game
- **Arrow Keys**: Move snake
- **ESC**: Pause/Resume game
- **Mouse**: Click menu buttons

### Menu Navigation
- **Mouse**: Click any button to navigate
- **SPACE**: Start new game from main menu
- **ESC**: Resume from pause menu
- **SPACE**: Restart game from game over screen

### Settings
- **Mouse**: Drag sliders to adjust values
- **Real-time**: Changes apply immediately to new games
- **Back Button**: Return to main menu

### Quitting
- **Close Window**: Click the X button to quit (works properly!)
- **Quit Button**: Click the red "QUIT" button in main menu
- **Alt+F4**: Force quit (Windows)

## 🏆 Scoring

- **1 point** per normal food eaten
- **5 points** per special food eaten
- **Speed increase** every 5 points (respects settings)
- **High score** is automatically saved

## 🍎 Food Types

### Normal Food (Red)
- Standard red food
- Gives 1 point
- Adds 1 segment to snake
- Always available

### Special Food (Golden)
- Golden color with sparkles
- 1.5x larger than normal food
- Gives 5 points
- Adds 3 segments to snake
- Appears randomly every 3 points (based on settings)
- Only one special food can exist at a time
- Disappears after configurable duration
- Flashes purple when about to disappear
- **Fully Controllable**: Player sets exact spawn chance and duration
- **Debug Info**: Status bar shows "Next check: X | Chance: Y%"
- **Console Logging**: Shows spawn attempts and results

## ⚙️ Settings

### Game Speed (5-20 FPS)
- Controls how fast the snake moves
- Higher values = faster gameplay
- Default: 10 FPS
- **Effect**: Changes snake movement speed and game responsiveness

### Special Food Chance (5-25%)
- Controls how often special food appears every 3 points
- Higher values = more frequent special food
- Default: 10%
- **Effect**: 25% chance means special food appears roughly once every 12 points on average
- **Player Control**: You can set this to any value between 5% and 25%
- **Debug Display**: Status bar shows current chance and next check timing

### Special Food Duration (15-60 seconds)
- Controls how long special food stays on screen
- Higher values = more time to reach special food
- Default: 30 seconds
- **Effect**: Longer duration gives more time to strategize and reach the special food
- **Player Control**: You can set this to any value between 15 and 60 seconds

## 🔧 Technical Details

### Game States
- `MENU`: Main menu screen with navigation
- `PLAYING`: Active gameplay
- `PAUSED`: Paused game with overlay
- `GAME_OVER`: Game over screen with results
- `SETTINGS`: Settings menu with interactive sliders

### File Structure
```
snake-game/
├── main.py              # Entry point
├── game.py              # Main game logic with menu integration
├── menu.py              # Menu system with buttons, sliders, and states
├── snake.py             # Snake class with wall wrapping
├── food.py              # Food class with animations and special food
├── utils.py             # Utilities and constants
├── requirements.txt     # Dependencies
├── highscore.txt        # High score storage
├── .gitignore           # Git ignore file
├── LICENSE              # MIT License
└── README.md           # This file
```

### Dependencies
- `pygame>=2.5.0`: Game engine and multimedia support

## 🎨 Design Philosophy

The game follows modern design principles:
- **Simplicity**: Clean, intuitive interface
- **Responsiveness**: Smooth animations and immediate feedback
- **Accessibility**: Clear visual hierarchy and readable fonts
- **Reliability**: Robust quit and restart functionality
- **Interactivity**: Hover effects and visual feedback
- **Excitement**: Special food adds unpredictability and rewards
- **Customization**: Settings allow personalization of gameplay
- **Fresh Start**: Always start new games with current settings
- **Transparency**: Debug information helps understand game mechanics

## 🐛 Troubleshooting

### Game Won't Start
- Ensure pygame is installed: `pip install pygame`
- Check Python version (3.7+ required)

### Can't Quit Game
- **Fixed!** Use the X button on the window - it now works properly
- Click the red "QUIT" button in the main menu
- Press Alt+F4 (Windows) or Cmd+Q (Mac) as backup

### Menu Not Working
- Use mouse to click buttons
- All buttons have hover effects for visual feedback
- Keyboard shortcuts still work (SPACE, ESC)

### Settings Not Working
- Drag sliders with mouse to adjust values
- Settings apply to new games immediately
- Use the red "BACK" button to return to main menu
- **New Game**: Returning to main menu and pressing play starts a fresh game with current settings

### Restart Not Working
- In game over screen, click the green "RESTART" button
- Or press SPACE to restart
- The restart functionality is fully implemented

### Special Food Not Appearing
- Check settings for special food chance
- Special food appears randomly every 3 points based on configured percentage
- Only one special food can exist at a time
- Will disappear after configured duration if not eaten
- Look for the golden food with sparkles!
- **Player Control**: You can adjust the spawn chance in settings (5-25%)
- **Debug Info**: Status bar shows "Next check: X | Chance: Y%"
- **Console Logging**: Check console for spawn attempt messages
- **Improved Frequency**: Now checks every 3 points instead of 5 for better odds

### Game Too Fast/Slow
- Adjust Game Speed setting in the Settings menu
- Lower values = slower gameplay
- Higher values = faster gameplay
- Settings apply to new games

### Game Resumes Instead of Starting New
- When you return to main menu and press play, it now starts a completely new game
- The game will use your current settings for the new game
- Previous game state is not preserved when returning to main menu

## 🚀 Future Enhancements

The game is designed to be easily extensible. Future features could include:
- **More Settings**: Visual options, sound settings, difficulty modes
- **Custom Sprites**: Snake and food images
- **Sound Effects**: Eating sounds, game over sounds, special food sounds
- **Background Music**: Looping game music
- **More Power-ups**: Different types of special food with unique effects
- **Different Game Modes**: Time attack, maze mode, multiplayer
- **Settings Persistence**: Save settings between game sessions

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📝 Changelog

### Version 1.2.0
- **Improved Special Food Spawning**: Now checks every 3 points instead of 5 for better frequency
- **Added Debug Information**: Status bar shows next check timing and spawn chance
- **Console Logging**: Detailed output for special food spawning events
- **Better Odds**: 66% more chances to spawn special food

### Version 1.1.0
- **Settings Menu**: Fully functional settings with interactive sliders
- **Special Food System**: Golden power-ups with configurable spawn chance and duration
- **New Game Behavior**: Main menu always starts fresh games with current settings
- **Consistent UI**: All buttons use the same color scheme

### Version 1.0.0
- **Core Gameplay**: Wall wrapping, smooth animations, progressive difficulty
- **Menu System**: Main menu, pause menu, game over screen
- **High Score System**: Automatic save/load functionality
- **Reliable Quit**: Proper window close handling 