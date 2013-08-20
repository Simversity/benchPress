import sys
import unittest
from base import BaseSuite, authorize

BUNDLE_ID = "137698573718494767147020"

class SubscribeUser(BaseSuite):
    #@authorize("user1@siminars.com", "jaideep")
    #def test_getbundle_user(self):
    #    x = self.get(
    #        "bundle_users",
    #        **{"bundle_id": BUNDLE_ID, "role": "students"})
    #    print x

    @authorize("user1@gmail.com", "jaideep")
    def test_callcart(self):
        data = {"item_id": BUNDLE_ID, "user_id": "137698485339789688163702"}
        cart_ret = self.post(
            "cart" ,
            data=data)

        cart_ret["finalize"] = 1

        ret = self.put(
            "cart" ,
            data=cart_ret)

if __name__ == '__main__':
    unittest.main()
