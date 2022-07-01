from main import User, AppControl, t1, AppView, Property
import unittest


class TestControls(unittest.TestCase): 
    def test_control_create_user(self):
        a = AppControl()
        u = User("Sam Gamgee") 
        a.all_users[u.profile_name] = u
        self.assertIn(u.profile_name, a.all_users)

    def test_control_toggle_user(self): 
        a = AppControl()
        u = User("Bilbo Baggins")
        a.control_create_user(u)
        a.control_toggle_user(u)
        self.assertEqual(a.active_user, u)
    
    def test_control_add_property(self):
        pass


class TestProperty(unittest.TestCase):
    def test_property_init(self): 
        p = Property("3145 Bag End Ln", 1000, 800, 10000)
        self.assertEqual(p.net, 200)
        self.assertEqual(p.roi, 24)



if __name__ == "__main__": 
    unittest.main()


