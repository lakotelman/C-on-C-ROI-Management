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

    def test_control_edit_user_delete(self):
        a = AppControl()
        a.control_edit_user(t1, "delete")
        self.assertEqual(a.active_user, None)
        self.assertNotIn(t1, a.all_users)

    def test_control_edit_user_rename(self):
        a = AppControl()
        a.control_edit_user(t1, "rename", "billybob")
        self.assertEqual(t1.profile_name, "billybob")

    def test_control_add_property(self):
        a = AppControl()
        u = User("Bilbo Baggins")
        a.active_user = u
        p = Property("4242 Bag End", 1000, 800, 100)
        a.control_add_property(p)
        self.assertIn(p, u.portfolio.values())


    def test_control_edit_property(self):
        a = AppControl()
        p = Property("4242 Bag End Ln", 1000, 800, 10000)
        a.control_edit_property(
            p,
            "revise",
            upd_address="4243 Bag End Ln",
            upd_expenses="1000",
            upd_gross="1000",
            upd_investment="12000",
        )
        self.assertEqual(p.address, "4243 Bag End Ln")
        self.assertEqual(p.expenses, 1000)
        self.assertEqual(p.gross, 1000)
        self.assertEqual(p.investment, 12000)

    def test_control_edit_property_delete(self):
        u = User("Bilbo Baggins")
        a = AppControl()
        p = Property("4242 Bag End Ln", 1000, 800, 10000)
        a.control_add_property(p)
        a.control_edit_property(p, "delete")
        self.assertNotIn(p, u.portfolio)

class TestProperty(unittest.TestCase):
    def test_property_init(self):
        p = Property("3145 Bag End Ln", 1000, 800, 10000)
        self.assertEqual(p.net, 200)
        self.assertEqual(p.roi, 24)


if __name__ == "__main__":
    unittest.main()
