bl_info = {
    "name": "source bone operator",
    "author": "jerry_harm",
    "blender": (4,0,0),
    "category": "Armature",
    "location": "Armature > Source Bone Operator",
    "description": "addon for auto process the bone imported from source",
}

from boneoperator import register, unregister

if __name__ == "__main__":
    register()