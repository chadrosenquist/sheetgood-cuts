"""Provides APIs to best make cuts in sheetgoods."""

from sheetgoodcuts import Mixed


def sheetgoodcuts(desired_cuts,
                  sheets,
                  saw_blade_width="1/8"):
    saw_blade_width = Mixed(saw_blade_width)
    return desired_cuts