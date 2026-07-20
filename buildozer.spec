[app]

title = Telegram Alarm

package.name = telegramalarm

package.domain = org.minhdao

source.dir = .

source.include_exts = py,png,jpg,kv,atlas,json,mp3

version = 1.0

requirements = python3,kivy,telethon,playsound

orientation = portrait

fullscreen = 0

android.api = 34

android.minapi = 24

android.archs = arm64-v8a

android.permissions = INTERNET,VIBRATE

[buildozer]

log_level = 2

warn_on_root = 1