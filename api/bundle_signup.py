import unittest
import settings
from base import BaseSuite, authorize

class SubscribeUser(BaseSuite):
    @authorize(settings.STUDENT_EMAIL, settings.STUDENT_PASSWORD)
    def test_callcart(self):
        data = {"item_id": settings.BUNDLE_ID, "user_id": self.current_user_id}
        cart_ret = self.post("cart" , data=data)

        cart_ret["finalize"] = 1

        ret = self.put(
            "cart" ,
            data=cart_ret)

if __name__ == '__main__':
    unittest.main()
