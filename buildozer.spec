[app]
title = Maya
package.name = maya
package.domain = org.maya.app
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0
requirements = python3,kivy
orientation = portrait
fullscreen = 0
android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE,CALL_PHONE,CAMERA,RECORD_AUDIO,VIBRATE
android.api = 33
android.minapi = 21
android.ndk = 25b
android.archs = arm64-v8a,armeabi-v7a
p4a.branch = master

[buildozer]
log_level = 2
warn_on_root = 1
