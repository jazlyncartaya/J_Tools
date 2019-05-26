# J_RemoveAllTransformKeys Button v.1.0.1
# Copyright (c) 2019 Jazlyn Cartaya.  All Rights Reserved.
# Add to menu.py
#import nuke

    # Creates button that removes keys in all knobs in "Transform":

def remove_all_transform_keys():
    """This function removes all of the keys in all knobs
    in the Transform node. """

    this_node = nuke.thisNode()

    # "Transform" Knob: Translate

    frame = nuke.frame()
    translate_knob = this_node['translate']
    translate_knob.removeKeyAt(frame)

    # "Transform" Knob: Rotate

    frame = nuke.frame()
    rotate_knob = this_node['rotate']
    rotate_knob.removeKeyAt(frame)

    # "Transform" Knob: Scale

    frame = nuke.frame()
    scale_knob = this_node['scale']
    scale_knob.removeKeyAt(frame)

    # "Transform" Knob: Skew X

    frame = nuke.frame()
    skew_x_knob = this_node['skewX']
    skew_x_knob.removeKeyAt(frame)

    # "Transform" Knob: Skew Y

    frame = nuke.frame()
    skew_y_knob = this_node['skewY']
    skew_y_knob.removeKeyAt(frame)

    # "Transform" Knob: Center

    frame = nuke.frame()
    center_knob = this_node['center']
    center_knob.removeKeyAt(frame)

def transform_tab():
    """This function creates a tab/button in Transform node
    which executes the remove_all_transform_keys() function."""

    node = nuke.thisNode()

    tab = nuke.Tab_Knob('Remove Keys')
    node.addKnob(tab)

    pyknob = nuke.PyScript_Knob('remove_all_transform_keys',
                                'remove all keys',
                                'remove_all_transform_keys()')
    node.addKnob(pyknob)

nuke.addOnCreate(lambda: transform_tab(), nodeClass='Transform')
