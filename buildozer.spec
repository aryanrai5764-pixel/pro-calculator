[app]

title = Pro Calculator

package.name = procalculator
package.domain = org.aryanrai

source.dir = .
source.include_exts = py,kv,png,jpg,jpeg,ttf,otf

version = 1.0

requirements = python3,kivy,kivymd

orientation = portrait

fullscreen = 0

icon.filename = icon.png

android.api = 33
android.minapi = 21
android.ndk_api = 21

android.permissions = INTERNET

[buildozer]

log_level = 2
warn_on_root = 1
