import unittest
from pydsr import *
import numpy as np

class Test(unittest.TestCase):

    def test_create_attribute(self):

        a = Node(12, "world", "elmundo")

        #int32
        a.attrs["vehicle_id"] = Attribute(10, 1)
        a.attrs["vehicle_id"].value = 11
        a.attrs["vehicle_id"].value = int(24)
        a.attrs["vehicle_id"].value = int(12.45)
        with self.assertRaises(RuntimeError):
            a.attrs["vehicle_id"] = Attribute(10.0, 1)
        with self.assertRaises(RuntimeError):
            a.attrs["vehicle_id"] = Attribute("10.0", 1)
        with self.assertRaises(RuntimeError):
            a.attrs["vehicle_id"] = Attribute(True, 1)
        with self.assertRaises(RuntimeError):
            a.attrs["vehicle_id"] = Attribute([10], 1)
        with self.assertRaises(RuntimeError):
            a.attrs["vehicle_id"] = Attribute([10.0], 1)
        with self.assertRaises(RuntimeError):
            a.attrs["vehicle_id"] = Attribute([10, 12,22], 1)
        with self.assertRaises(RuntimeError):
            a.attrs["vehicle_id"] = Attribute([10.0, 11.2], 1)
        with self.assertRaises(RuntimeError):
            a.attrs["vehicle_id"] = Attribute(22222222222222222222222222222222222222222222222, 1)
        with self.assertRaises(RuntimeError):
            a.attrs["vehicle_id"].value = "string"
        with self.assertRaises(RuntimeError):
            a.attrs["vehicle_id"].value = 10.0
        with self.assertRaises(RuntimeError):
            a.attrs["vehicle_id"].value = [10]
        with self.assertRaises(RuntimeError):
            a.attrs["vehicle_id"].value = [10.0]
        with self.assertRaises(RuntimeError):
            a.attrs["vehicle_id"].value = 22222222222222222222222222222222222222222222222222222
        with self.assertRaises(RuntimeError):
            a.attrs["vehicle_id"].value = np.array([1.2, 4.4], dtype=np.float)
        with self.assertRaises(RuntimeError):
            a.attrs["vehicle_id"].value = (10,)

        #bool
        a.attrs["vehicle_occupancy"] = Attribute(True, 1)
        a.attrs["vehicle_occupancy"].value = False
        a.attrs["vehicle_occupancy"].value = True
        with self.assertRaises(RuntimeError):
            a.attrs["vehicle_occupancy"] = Attribute(10.0, 1)
        with self.assertRaises(RuntimeError):
            a.attrs["vehicle_occupancy"] = Attribute("10.0", 1)
        with self.assertRaises(RuntimeError):
            a.attrs["vehicle_occupancy"] = Attribute(1, 1)
        with self.assertRaises(RuntimeError):
            a.attrs["vehicle_occupancy"] = Attribute(0, 1)
        with self.assertRaises(RuntimeError):
            a.attrs["vehicle_occupancy"] = Attribute(1110, 1)
        with self.assertRaises(RuntimeError):
            a.attrs["vehicle_occupancy"] = Attribute([10], 1)
        with self.assertRaises(RuntimeError):
            a.attrs["vehicle_occupancy"] = Attribute([10.0], 1)
        with self.assertRaises(RuntimeError):
            a.attrs["vehicle_occupancy"] = Attribute([10, 12,22], 1)
        with self.assertRaises(RuntimeError):
            a.attrs["vehicle_occupancy"] = Attribute([10.0, 11.2], 1)
        with self.assertRaises(RuntimeError):
            a.attrs["vehicle_occupancy"] = Attribute(22222222222222222222222222222222222222222222222, 1)
        with self.assertRaises(RuntimeError):
            a.attrs["vehicle_occupancy"].value = 1
        with self.assertRaises(RuntimeError):
            a.attrs["vehicle_occupancy"].value = 1.0
        with self.assertRaises(RuntimeError):
            a.attrs["vehicle_occupancy"].value = "True"
        with self.assertRaises(RuntimeError):
            a.attrs["vehicle_occupancy"].value = [True]



        #float
        a.attrs["vehicle_steer"] = Attribute(1.0, 1)
        a.attrs["vehicle_steer"].value = 1.0
        a.attrs["vehicle_steer"].value = float(12)
        with self.assertRaises(RuntimeError):
            a.attrs["vehicle_steer"] = Attribute(True, 1)
        with self.assertRaises(RuntimeError):
            a.attrs["vehicle_steer"] = Attribute("10.0", 1)
        with self.assertRaises(RuntimeError):
            a.attrs["vehicle_steer"] = Attribute(1, 1)
        with self.assertRaises(RuntimeError):
            a.attrs["vehicle_steer"] = Attribute(0, 1)
        with self.assertRaises(RuntimeError):
            a.attrs["vehicle_steer"] = Attribute(1110, 1)
        with self.assertRaises(RuntimeError):
            a.attrs["vehicle_steer"] = Attribute([10], 1)
        with self.assertRaises(RuntimeError):
            a.attrs["vehicle_steer"] = Attribute([10.0], 1)
        with self.assertRaises(RuntimeError):
            a.attrs["vehicle_steer"] = Attribute([10, 12,22], 1)
        with self.assertRaises(RuntimeError):
            a.attrs["vehicle_steer"] = Attribute([10.0, 11.2], 1)
        with self.assertRaises(RuntimeError):
            a.attrs["vehicle_steer"] = Attribute(22222222222222222222222222222222222222222222222, 1)
        with self.assertRaises(RuntimeError):
            a.attrs["vehicle_steer"].value = 1
        with self.assertRaises(RuntimeError):
            a.attrs["vehicle_steer"].value = "1.0"
        with self.assertRaises(RuntimeError):
            a.attrs["vehicle_steer"].value = [1.0]
        with self.assertRaises(RuntimeError):
            a.attrs["vehicle_steer"].value = np.array([1.2], dtype=np.float)
        with self.assertRaises(RuntimeError):
            a.attrs["vehicle_steer"].value = 0.0000000000000000000000000000000000000000000000123

        #double
        a.attrs["test_double_type"] = Attribute(1.0, 1)
        a.attrs["test_double_type"] = Attribute(1.132432543543645646703, 1)
        a.attrs["test_double_type"].value = 1.0
        a.attrs["test_double_type"].value = 1.132432543543645646703
        with self.assertRaises(RuntimeError):
            a.attrs["test_double_type"] = Attribute(True, 1)
        with self.assertRaises(RuntimeError):
            a.attrs["test_double_type"] = Attribute("10.0", 1)
        with self.assertRaises(RuntimeError):
            a.attrs["test_double_type"] = Attribute(1, 1)
        with self.assertRaises(RuntimeError):
            a.attrs["test_double_type"] = Attribute(0, 1)
        with self.assertRaises(RuntimeError):
            a.attrs["test_double_type"] = Attribute(1110, 1)
        with self.assertRaises(RuntimeError):
            a.attrs["test_double_type"] = Attribute([10], 1)
        with self.assertRaises(RuntimeError):
            a.attrs["test_double_type"] = Attribute([10.0], 1)
        with self.assertRaises(RuntimeError):
            a.attrs["test_double_type"] = Attribute([10, 12,22], 1)
        with self.assertRaises(RuntimeError):
            a.attrs["test_double_type"] = Attribute([10.0, 11.2], 1)
        with self.assertRaises(RuntimeError):
            a.attrs["test_double_type"] = Attribute(22222222222222222222222222222222222222222222222, 1)
        with self.assertRaises(RuntimeError):
            a.attrs["test_double_type"].value = 1
        with self.assertRaises(RuntimeError):
            a.attrs["test_double_type"].value = "1.0"
        with self.assertRaises(RuntimeError):
            a.attrs["test_double_type"].value = np.array([1.2], dtype=np.float)
        with self.assertRaises(RuntimeError):
            a.attrs["test_double_type"].value = [10.0]

        #string
        a.attrs["name"] = Attribute("Prueba", 1)
        a.attrs["name"].value = "Prueba"
        with self.assertRaises(RuntimeError):
            a.attrs["name"] = Attribute(True, 1)
        with self.assertRaises(RuntimeError):
            a.attrs["name"] = Attribute(10.0, 1)
        with self.assertRaises(RuntimeError):
            a.attrs["name"] = Attribute(1, 1)
        with self.assertRaises(RuntimeError):
            a.attrs["name"] = Attribute(0, 1)
        with self.assertRaises(RuntimeError):
            a.attrs["name"] = Attribute(1110, 1)
        with self.assertRaises(RuntimeError):
            a.attrs["name"] = Attribute([10], 1)
        with self.assertRaises(RuntimeError):
            a.attrs["name"] = Attribute([10.0], 1)
        with self.assertRaises(RuntimeError):
            a.attrs["name"] = Attribute([10, 12,22], 1)
        with self.assertRaises(RuntimeError):
            a.attrs["name"] = Attribute([10.0, 11.2], 1)
        with self.assertRaises(RuntimeError):
            a.attrs["name"] = Attribute(22222222222222222222222222222222222222222222222, 1)
        with self.assertRaises(RuntimeError):
            a.attrs["name"].value = 1
        with self.assertRaises(RuntimeError):
            a.attrs["name"].value = np.array([1.2], dtype=np.float)
        with self.assertRaises(RuntimeError):
            a.attrs["name"].value = [10.0]
        with self.assertRaises(RuntimeError):
            a.attrs["name"].value = True

        #vec float
        a.attrs["rt_translation"] = Attribute([10.0], 1)
        a.attrs["rt_translation"] = Attribute([10.0, 11.2], 1)
        a.attrs["rt_translation"] = Attribute(np.array([1.2, 4.4], dtype=np.float), 1)
        a.attrs["rt_translation"].value = [10.0, 11.2]
        a.attrs["rt_translation"].value = np.array([1.2, 4.4], dtype=np.float)
        with self.assertRaises(RuntimeError):
            a.attrs["rt_translation"] = Attribute(True, 1)
        with self.assertRaises(RuntimeError):
            a.attrs["rt_translation"] = Attribute(10.0, 1)
        with self.assertRaises(RuntimeError):
            a.attrs["rt_translation"] = Attribute(1, 1)
        with self.assertRaises(RuntimeError):
            a.attrs["rt_translation"] = Attribute(0, 1)
        with self.assertRaises(RuntimeError):
            a.attrs["rt_translation"] = Attribute(1110, 1)
        with self.assertRaises(RuntimeError):
            a.attrs["rt_translation"] = Attribute([10], 1)
        with self.assertRaises(RuntimeError):
            a.attrs["rt_translation"] = Attribute("[10.0]", 1)
        with self.assertRaises(RuntimeError):
            a.attrs["rt_translation"] = Attribute([10, 12,22], 1)
        with self.assertRaises(RuntimeError):
            a.attrs["rt_translation"] = Attribute(np.array([12, 44], dtype=np.uint8), 1)
        with self.assertRaises(RuntimeError):
            a.attrs["rt_translation"] = Attribute(22222222222222222222222222222222222222222222222, 1)
        with self.assertRaises(RuntimeError):
            a.attrs["rt_translation"] = Attribute(np.array([12, 44], dtype=np.uint64), 1)
        with self.assertRaises(RuntimeError):
            a.attrs["rt_translation"].value = [10, 11]
        with self.assertRaises(RuntimeError):
            a.attrs["rt_translation"].value = np.array([1, 4], dtype=np.uint8)
        with self.assertRaises(RuntimeError):
            a.attrs["rt_translation"].value = 11.0
        with self.assertRaises(RuntimeError):
            a.attrs["rt_translation"].value = (10.0, 11.1)
        with self.assertRaises(RuntimeError):
            a.attrs["rt_translation"].value = [10.0, True, 1]
        with self.assertRaises(RuntimeError):
            a.attrs["rt_translation"].value = [[11.0, 0.0, 1.1]]



        #vec bytes
        a.attrs["cam_image"] = Attribute([100], 1)
        a.attrs["cam_image"] = Attribute([100, 112], 1)
        a.attrs["cam_image"] = Attribute(np.array([12, 44], dtype=np.uint8), 1)
        a.attrs["cam_image"].value = [100, 112]
        a.attrs["cam_image"].value = np.array([12, 44], dtype=np.uint8)
        with self.assertRaises(RuntimeError):
            a.attrs["cam_image"] = Attribute(True, 1)
        with self.assertRaises(RuntimeError):
            a.attrs["cam_image"] = Attribute(10.0, 1)
        with self.assertRaises(RuntimeError):
            a.attrs["cam_image"] = Attribute(1, 1)
        with self.assertRaises(RuntimeError):
            a.attrs["cam_image"] = Attribute(0, 1)
        with self.assertRaises(RuntimeError):
            a.attrs["cam_image"] = Attribute(1110, 1)
        with self.assertRaises(RuntimeError):
            a.attrs["cam_image"] = Attribute([10, "a"], 1)
        with self.assertRaises(RuntimeError):
            a.attrs["cam_image"] = Attribute("[10.0]", 1)
        with self.assertRaises(RuntimeError):
            a.attrs["cam_image"] = Attribute([10.0, 12.,22], 1)
        with self.assertRaises(RuntimeError):
            a.attrs["cam_image"] = Attribute(np.array([12.5, 44.2, 1], dtype=np.float), 1)
        with self.assertRaises(RuntimeError):
            a.attrs["cam_image"] = Attribute(22222222222222222222222222222222222222222222222, 1)
        with self.assertRaises(RuntimeError):
            a.attrs["cam_image"].value = np.array([12456, 41233544], dtype=np.uint32)
        with self.assertRaises(RuntimeError):
            a.attrs["cam_image"].value = np.array([12456, 41233544], dtype=np.uint64)
        with self.assertRaises(RuntimeError):
            a.attrs["cam_image"].value = [12456, 41233544]
        with self.assertRaises(RuntimeError):
            a.attrs["cam_image"].value = [1.0, 244.0]
        with self.assertRaises(RuntimeError):
            a.attrs["cam_image"].value = [10, True, 1]
        with self.assertRaises(RuntimeError):
            a.attrs["cam_image"].value = [10, 1.0]
        with self.assertRaises(RuntimeError):
            a.attrs["cam_image"].value = [[11, 0, 1]]

        #uint32
        a.attrs["test_uint32_type"] = Attribute(100, 1)
        a.attrs["test_uint32_type"].value = 100
        a.attrs["test_uint32_type"].value = int(100)
        a.attrs["test_uint32_type"].value = int(100.0)
        with self.assertRaises(RuntimeError):
            a.attrs["test_uint32_type"] = Attribute(True, 1)
        with self.assertRaises(RuntimeError):
            a.attrs["test_uint32_type"] = Attribute(10.0, 1)
        with self.assertRaises(RuntimeError):
            a.attrs["test_uint32_type"] = Attribute(1, 1)
        with self.assertRaises(RuntimeError):
            a.attrs["test_uint32_type"] = Attribute(0, 1)
        with self.assertRaises(RuntimeError):
            a.attrs["test_uint32_type"] = Attribute(1110, 1)
        with self.assertRaises(RuntimeError):
            a.attrs["test_uint32_type"] = Attribute([10, "a"], 1)
        with self.assertRaises(RuntimeError):
            a.attrs["test_uint32_type"] = Attribute("[10.0]", 1)
        with self.assertRaises(RuntimeError):
            a.attrs["test_uint32_type"] = Attribute([10.0, 12.,22], 1)
        with self.assertRaises(RuntimeError):
            a.attrs["test_uint32_type"] = Attribute([10, 11], 1)
        with self.assertRaises(RuntimeError):
            a.attrs["test_uint32_type"] = Attribute(np.array([12.5, 44.2, 1], dtype=np.float), 1)
        with self.assertRaises(RuntimeError):
            a.attrs["test_uint32_type"] = Attribute(22222222222222222222222222222222222222222222222, 1)
        with self.assertRaises(RuntimeError):
            a.attrs["test_uint32_type"] = Attribute(-12, 1)
        with self.assertRaises(RuntimeError):
            a.attrs["test_uint32_type"].value = 100.0
        with self.assertRaises(RuntimeError):
            a.attrs["test_uint32_type"].value = "100"
        with self.assertRaises(RuntimeError):
            a.attrs["test_uint32_type"].value = 22222222222222222222222222222222222222222222222
        with self.assertRaises(RuntimeError):
            a.attrs["test_uint32_type"].value = True

        #uint64
        a.attrs["parent"] = Attribute(100, 1)
        a.attrs["parent"] = Attribute(3689348814741910323, 1)
        a.attrs["parent"].value = 100
        a.attrs["parent"].value = 3689348814741910323
        with self.assertRaises(RuntimeError):
            a.attrs["parent"] = Attribute(True, 1)
        with self.assertRaises(RuntimeError):
            a.attrs["parent"] = Attribute(10.0, 1)
        with self.assertRaises(RuntimeError):
            a.attrs["parent"] = Attribute(1, 1)
        with self.assertRaises(RuntimeError):
            a.attrs["parent"] = Attribute(0, 1)
        with self.assertRaises(RuntimeError):
            a.attrs["parent"] = Attribute(1110, 1)
        with self.assertRaises(RuntimeError):
            a.attrs["parent"] = Attribute([10, "a"], 1)
        with self.assertRaises(RuntimeError):
            a.attrs["parent"] = Attribute("[10.0]", 1)
        with self.assertRaises(RuntimeError):
            a.attrs["parent"] = Attribute([10.0, 12.,22], 1)
        with self.assertRaises(RuntimeError):
            a.attrs["parent"] = Attribute([10, 11], 1)
        with self.assertRaises(RuntimeError):
            a.attrs["parent"] = Attribute(np.array([12.5, 44.2, 1], dtype=np.float), 1)
        with self.assertRaises(RuntimeError):
            a.attrs["parent"] = Attribute(-12, 1)
        with self.assertRaises(RuntimeError):
            a.attrs["parent"].value = -12
        with self.assertRaises(RuntimeError):
            a.attrs["parent"].value = True
        with self.assertRaises(RuntimeError):
            a.attrs["parent"].value = 1.0


        #double
        a.attrs["test_double_type"] = Attribute(100.0, 1)
        a.attrs["test_double_type"] = Attribute(3689348814741910323.0, 1)
        a.attrs["test_double_type"].value = 100.0
        a.attrs["test_double_type"].value = 3689348814741910323.0
        a.attrs["test_double_type"].value = 368934.13434254222233213576564
        with self.assertRaises(RuntimeError):
            a.attrs["test_double_type"] = Attribute(True, 1)
        with self.assertRaises(RuntimeError):
            a.attrs["test_double_type"] = Attribute(10, 1)
        with self.assertRaises(RuntimeError):
            a.attrs["test_double_type"] = Attribute(0, 1)
        with self.assertRaises(RuntimeError):
            a.attrs["test_double_type"] = Attribute(1110, 1)
        with self.assertRaises(RuntimeError):
            a.attrs["test_double_type"] = Attribute([10, "a"], 1)
        with self.assertRaises(RuntimeError):
            a.attrs["test_double_type"] = Attribute("[10.0]", 1)
        with self.assertRaises(RuntimeError):
            a.attrs["test_double_type"] = Attribute([10.0, 12.,22], 1)
        with self.assertRaises(RuntimeError):
            a.attrs["test_double_type"] = Attribute([10, 11], 1)
        with self.assertRaises(RuntimeError):
            a.attrs["test_double_type"] = Attribute(np.array([12.5, 44.2, 1], dtype=np.float), 1)
        with self.assertRaises(RuntimeError):
            a.attrs["test_double_type"] = Attribute(-12, 1)
        with self.assertRaises(RuntimeError):
            a.attrs["test_double_type"].value = -12
        with self.assertRaises(RuntimeError):
            a.attrs["test_double_type"].value = True
        with self.assertRaises(RuntimeError):
            a.attrs["test_double_type"].value = 1

        #u64_vec
        a.attrs["test_uint64_vec_type"] = Attribute([256], 1)
        a.attrs["test_uint64_vec_type"] = Attribute([100], 1)
        a.attrs["test_uint64_vec_type"] = Attribute([100, 112], 1)
        a.attrs["test_uint64_vec_type"] = Attribute(np.array([12, 44], dtype=np.uint64), 1)
        a.attrs["test_uint64_vec_type"].value = [100, 112]
        a.attrs["test_uint64_vec_type"].value = np.array([12, 44], dtype=np.uint64)
        with self.assertRaises(RuntimeError):
            a.attrs["test_uint64_vec_type"] = Attribute(True, 1)
        with self.assertRaises(RuntimeError):
            a.attrs["test_uint64_vec_type"] = Attribute(10.0, 1)
        with self.assertRaises(RuntimeError):
            a.attrs["test_uint64_vec_type"] = Attribute(1, 1)
        with self.assertRaises(RuntimeError):
            a.attrs["test_uint64_vec_type"] = Attribute(0, 1)
        with self.assertRaises(RuntimeError):
            a.attrs["test_uint64_vec_type"] = Attribute(1110, 1)
        with self.assertRaises(RuntimeError):
            a.attrs["test_uint64_vec_type"] = Attribute([10, "a"], 1)
        with self.assertRaises(RuntimeError):
            a.attrs["test_uint64_vec_type"] = Attribute("[10.0]", 1)
        with self.assertRaises(RuntimeError):
            a.attrs["test_uint64_vec_type"] = Attribute([10.0, 12.,22], 1)
        with self.assertRaises(RuntimeError):
            a.attrs["test_uint64_vec_type"] = Attribute(np.array([12.5, 44.2, 1], dtype=np.float), 1)
        with self.assertRaises(RuntimeError):
            a.attrs["test_uint64_vec_type"] = Attribute(22222222222222222222222222222222222222222222222, 1)
        with self.assertRaises(RuntimeError):
            a.attrs["test_uint64_vec_type"].value = np.array([12456, 41233544], dtype=np.uint32)
        with self.assertRaises(RuntimeError):
            a.attrs["test_uint64_vec_type"].value = np.array([1245.0, 0.41233544], dtype=np.float)
        with self.assertRaises(RuntimeError):
            a.attrs["test_uint64_vec_type"].value = np.array([12, 41], dtype=np.uint8)
        with self.assertRaises(RuntimeError):
            a.attrs["test_uint64_vec_type"].value = [1.0, 244.0]
        with self.assertRaises(RuntimeError):
            a.attrs["test_uint64_vec_type"].value = [10, True, 1]
        with self.assertRaises(RuntimeError):
            a.attrs["test_uint64_vec_type"].value = [10, 1.0]
        with self.assertRaises(RuntimeError):
            a.attrs["test_uint64_vec_type"].value = [[11, 0, 1]]

        #vec2
        a.attrs["test_vec2_type"] = Attribute([10.0, 1.0], 1)
        a.attrs["test_vec2_type"] = Attribute([10.0, 11.2], 1)
        a.attrs["test_vec2_type"] = Attribute(np.array([1.2, 4.4], dtype=np.float), 1)
        a.attrs["test_vec2_type"].value = [10.0, 11.2]
        a.attrs["test_vec2_type"].value = np.array([1.2, 4.4], dtype=np.float)
        with self.assertRaises(RuntimeError):
            a.attrs["test_vec2_type"] = Attribute(True, 1)
        with self.assertRaises(RuntimeError):
            a.attrs["test_vec2_type"] = Attribute(10.0, 1)
        with self.assertRaises(RuntimeError):
            a.attrs["test_vec2_type"] = Attribute(1, 1)
        with self.assertRaises(RuntimeError):
            a.attrs["test_vec2_type"] = Attribute(0, 1)
        with self.assertRaises(RuntimeError):
            a.attrs["test_vec2_type"] = Attribute(1110, 1)
        with self.assertRaises(RuntimeError):
            a.attrs["test_vec2_type"] = Attribute([10], 1)
        with self.assertRaises(RuntimeError):
            a.attrs["test_vec2_type"] = Attribute("[10.0]", 1)
        with self.assertRaises(RuntimeError):
            a.attrs["test_vec2_type"] = Attribute([10, 12,22], 1)
        with self.assertRaises(RuntimeError):
            a.attrs["test_vec2_type"] = Attribute(np.array([12, 44], dtype=np.uint8), 1)
        with self.assertRaises(RuntimeError):
            a.attrs["test_vec2_type"] = Attribute(22222222222222222222222222222222222222222222222, 1)
        with self.assertRaises(RuntimeError):
            a.attrs["test_vec2_type"] = Attribute(np.array([12, 44], dtype=np.uint64), 1)
        with self.assertRaises(RuntimeError):
            a.attrs["test_vec2_type"].value = [10, 11]
        with self.assertRaises(RuntimeError):
            a.attrs["test_vec2_type"].value = np.array([1, 4], dtype=np.uint8)
        with self.assertRaises(RuntimeError):
            a.attrs["test_vec2_type"].value = 11.0
        with self.assertRaises(RuntimeError):
            a.attrs["test_vec2_type"].value = (10.0, 11.1)
        with self.assertRaises(RuntimeError):
            a.attrs["test_vec2_type"].value = [10.0, True]
        with self.assertRaises(RuntimeError):
            a.attrs["test_vec2_type"].value = [[11.0, 0.0]]
        with self.assertRaises(RuntimeError):
            a.attrs["test_vec2_type"].value = np.array([1.2, 4.4, 1.0], dtype=np.float)
        with self.assertRaises(RuntimeError):
            a.attrs["test_vec2_type"].value = np.array([1.2], dtype=np.float)

        #vec3
        a.attrs["test_vec3_type"] = Attribute([10.0, 1.0, 0.0], 1)
        a.attrs["test_vec3_type"] = Attribute([10.0, 11.2, 0.0], 1)
        a.attrs["test_vec3_type"] = Attribute(np.array([1.2, 4.4, 0.0], dtype=np.float), 1)
        a.attrs["test_vec3_type"].value = [10.0, 11.2, 0.0]
        a.attrs["test_vec3_type"].value = np.array([1.2, 4.4, 0.0], dtype=np.float)
        with self.assertRaises(RuntimeError):
            a.attrs["test_vec3_type"] = Attribute(True, 1)
        with self.assertRaises(RuntimeError):
            a.attrs["test_vec3_type"] = Attribute(10.0, 1)
        with self.assertRaises(RuntimeError):
            a.attrs["test_vec3_type"] = Attribute(1, 1)
        with self.assertRaises(RuntimeError):
            a.attrs["test_vec3_type"] = Attribute(0, 1)
        with self.assertRaises(RuntimeError):
            a.attrs["test_vec3_type"] = Attribute(1110, 1)
        with self.assertRaises(RuntimeError):
            a.attrs["test_vec3_type"] = Attribute([10], 1)
        with self.assertRaises(RuntimeError):
            a.attrs["test_vec3_type"] = Attribute("[10.0]", 1)
        with self.assertRaises(RuntimeError):
            a.attrs["test_vec3_type"] = Attribute([10, 12,22], 1)
        with self.assertRaises(RuntimeError):
            a.attrs["test_vec3_type"] = Attribute(np.array([12, 44, 0], dtype=np.uint8), 1)
        with self.assertRaises(RuntimeError):
            a.attrs["test_vec3_type"] = Attribute(22222222222222222222222222222222222222222222222, 1)
        with self.assertRaises(RuntimeError):
            a.attrs["test_vec3_type"] = Attribute(np.array([12, 44, 0], dtype=np.uint64), 1)
        with self.assertRaises(RuntimeError):
            a.attrs["test_vec3_type"].value = [10, 11]
        with self.assertRaises(RuntimeError):
            a.attrs["test_vec3_type"].value = np.array([1, 4, 3], dtype=np.uint8)
        with self.assertRaises(RuntimeError):
            a.attrs["test_vec3_type"].value = 11.0
        with self.assertRaises(RuntimeError):
            a.attrs["test_vec3_type"].value = (10.0, 11.1)
        with self.assertRaises(RuntimeError):
            a.attrs["test_vec3_type"].value = [10.0, True, 1.0]
        with self.assertRaises(RuntimeError):
            a.attrs["test_vec3_type"].value = [[11.0, 0.0, 0.0]]
        with self.assertRaises(RuntimeError):
            a.attrs["test_vec3_type"].value = np.array([1.2, 4.4, 1.0, 0.0], dtype=np.float)
        with self.assertRaises(RuntimeError):
            a.attrs["test_vec3_type"].value = np.array([1.2], dtype=np.float)


        #vec4
        a.attrs["test_vec4_type"] = Attribute([10.0, 1.0, 0.0, 1.0], 1)
        a.attrs["test_vec4_type"] = Attribute([10.0, 11.2, 0.0, 1.0], 1)
        a.attrs["test_vec4_type"] = Attribute(np.array([1.2, 4.4, 1.0, 0.0], dtype=np.float), 1)
        a.attrs["test_vec4_type"].value = [10.0, 11.2, 0.0, 1.0]
        a.attrs["test_vec4_type"].value = np.array([1.2, 4.4, 6.3, 0.0], dtype=np.float)
        with self.assertRaises(RuntimeError):
            a.attrs["test_vec4_type"] = Attribute(True, 1)
        with self.assertRaises(RuntimeError):
            a.attrs["test_vec4_type"] = Attribute(10.0, 1)
        with self.assertRaises(RuntimeError):
            a.attrs["test_vec4_type"] = Attribute(1, 1)
        with self.assertRaises(RuntimeError):
            a.attrs["test_vec4_type"] = Attribute(0, 1)
        with self.assertRaises(RuntimeError):
            a.attrs["test_vec4_type"] = Attribute(1110, 1)
        with self.assertRaises(RuntimeError):
            a.attrs["test_vec4_type"] = Attribute([10], 1)
        with self.assertRaises(RuntimeError):
            a.attrs["test_vec4_type"] = Attribute("[10.0]", 1)
        with self.assertRaises(RuntimeError):
            a.attrs["test_vec4_type"] = Attribute([10, 12,22, 1], 1)
        with self.assertRaises(RuntimeError):
            a.attrs["test_vec4_type"] = Attribute(np.array([12, 44, 0, 2], dtype=np.uint8), 1)
        with self.assertRaises(RuntimeError):
            a.attrs["test_vec4_type"] = Attribute(22222222222222222222222222222222222222222222222, 1)
        with self.assertRaises(RuntimeError):
            a.attrs["test_vec4_type"] = Attribute(np.array([12, 44, 0, 3], dtype=np.uint64), 1)
        with self.assertRaises(RuntimeError):
            a.attrs["test_vec4_type"].value = [10, 11]
        with self.assertRaises(RuntimeError):
            a.attrs["test_vec4_type"].value = np.array([1, 4, 3, 5], dtype=np.uint8)
        with self.assertRaises(RuntimeError):
            a.attrs["test_vec4_type"].value = 11.0
        with self.assertRaises(RuntimeError):
            a.attrs["test_vec4_type"].value = (10.0, 11.1, 11.0, 11.0)
        with self.assertRaises(RuntimeError):
            a.attrs["test_vec4_type"].value = [10.0, True, 1.0, 1.0]
        with self.assertRaises(RuntimeError):
            a.attrs["test_vec4_type"].value = [[11.0, 0.0, 0.0, 1.0]]
        with self.assertRaises(RuntimeError):
            a.attrs["test_vec4_type"].value = np.array([1.2, 4.4, 1.0, 0.0, 0.0], dtype=np.float)
        with self.assertRaises(RuntimeError):
            a.attrs["test_vec4_type"].value = np.array([1.2], dtype=np.float)


        #vec6
        a.attrs["test_vec6_type"] = Attribute([10.0, 1.0, 0.0, 1.2, 4.4, 0.0], 1)
        a.attrs["test_vec6_type"] = Attribute([10.0, 11.2, 0.0, 1.2, 4.4, 0.0], 1)
        a.attrs["test_vec6_type"] = Attribute(np.array([1.2, 4.4, 0.0, 1.2, 4.4, 0.0], dtype=np.float), 1)
        a.attrs["test_vec6_type"].value = [10.0, 11.2, 0.0, 1.2, 4.4, 0.0]
        a.attrs["test_vec6_type"].value = np.array([1.2, 4.4, 0.0, 1.2, 4.4, 0.0], dtype=np.float)
        with self.assertRaises(RuntimeError):
            a.attrs["test_vec6_type"] = Attribute(True, 1)
        with self.assertRaises(RuntimeError):
            a.attrs["test_vec6_type"] = Attribute(10.0, 1)
        with self.assertRaises(RuntimeError):
            a.attrs["test_vec6_type"] = Attribute(1, 1)
        with self.assertRaises(RuntimeError):
            a.attrs["test_vec6_type"] = Attribute(0, 1)
        with self.assertRaises(RuntimeError):
            a.attrs["test_vec6_type"] = Attribute(1110, 1)
        with self.assertRaises(RuntimeError):
            a.attrs["test_vec6_type"] = Attribute([10], 1)
        with self.assertRaises(RuntimeError):
            a.attrs["test_vec6_type"] = Attribute("[10.0]", 1)
        with self.assertRaises(RuntimeError):
            a.attrs["test_vec6_type"] = Attribute([10, 12,22,1, 4, 3], 1)
        with self.assertRaises(RuntimeError):
            a.attrs["test_vec6_type"] = Attribute(np.array([12, 44, 0,1, 4, 3], dtype=np.uint8), 1)
        with self.assertRaises(RuntimeError):
            a.attrs["test_vec6_type"] = Attribute(22222222222222222222222222222222222222222222222, 1)
        with self.assertRaises(RuntimeError):
            a.attrs["test_vec6_type"] = Attribute(np.array([12, 44, 0,1, 4, 3], dtype=np.uint64), 1)
        with self.assertRaises(RuntimeError):
            a.attrs["test_vec6_type"].value = [10, 11]
        with self.assertRaises(RuntimeError):
            a.attrs["test_vec6_type"].value = np.array([1, 4, 3,1, 4, 3], dtype=np.uint8)
        with self.assertRaises(RuntimeError):
            a.attrs["test_vec6_type"].value = 11.0
        with self.assertRaises(RuntimeError):
            a.attrs["test_vec6_type"].value = (10.0, 11.1)
        with self.assertRaises(RuntimeError):
            a.attrs["test_vec6_type"].value = [10.0, True, 1.0,11.0, 0.0, 0.0]
        with self.assertRaises(RuntimeError):
            a.attrs["test_vec6_type"].value = [[11.0, 0.0, 0.0,11.0, 0.0, 0.0]]
        with self.assertRaises(RuntimeError):
            a.attrs["test_vec6_type"].value = np.array([1.2, 4.4, 1.0, 0.0, 1.0, 0.0, 1.0, 0.0], dtype=np.float)
        with self.assertRaises(RuntimeError):
            a.attrs["test_vec6_type"].value = np.array([1.2], dtype=np.float)
#print(a)
    #    print(a.attrs["cam_image"].value)


if __name__ == '__main__':
    #import psutil
    #if psutil.Process(os.getpid()).parent().name() == 'sh':
    #    unittest.main()
    #else:
    #    print("You probably want to execute test with the runTest.sh script.")
    unittest.main()