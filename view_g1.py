
import mujoco
import mujoco.viewer

model = mujoco.MjModel.from_xml_path(r"C:\Users\rbpra\Downloads\unitree_mujoco-main\unitree_mujoco-main\unitree_robots\g1\scene_29dof.xml")
data = mujoco.MjData(model)
mujoco.viewer.launch(model, data)