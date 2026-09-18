[app]
title = Nazz Fiber Internet
package.name = nazzfiber
package.domain = org.nazz
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3, kivy==2.3.0, pillow
orientation = portrait
osx.kivy_version = 2.3.0
fullscreen = 0
icon.filename = logo.png.png
android.permissions = INTERNET
android.api = 33
android.ndk = 25b
android.accept_sdk_license = True
android.minapi = 21
android.ndk_api = 21
android.private_storage = True

[buildozer]
log_level = 1
warn_on_root = 1
