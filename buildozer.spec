[app]
title = DR.tempo
package.name = drtempo
package.domain = br.com.ktsunii
source.main = login.py
source.include_exts = py,kv,png,jpg,env,ini,txt,md
requirements = python3,kivy,requests,python-dotenv
icon.filename = assets/icon.png
presplash.filename = assets/presplash.png

[buildozer]
log_level = 2

[android]
android.api = 35
android.minapi = 21
android.ndk = 26b
android.sdk = 35
android.archs = arm64-v8a, armeabi-v7a
