# -*- coding: utf-8 -*-
import os
from kivymd.app import MDApp
from kaki.app import App
from kivy.factory import Factory


class Live(MDApp, App):
    DEBUG = 1

    CLASSES = {
        "MainScreenManager": "screens.screenmanager",
        "LoginScreen": "screens.login_screen.loginscreen"
    }

    KV_FILES = [
        os.path.join(os.getcwd(), "screens/screenmanager.kv"),
        os.path.join(os.getcwd(), "screens/login_screen/loginscreen.kv")
    ]

    AUTORELOADER_PATHS = [
        (".", {"recursive": True}),
    ]

    def build_app(self):
        self.theme_cls.primary_palette = "Green"
        return Factory.MainScreenManager()


if __name__ == "__main__":
    Live().run()