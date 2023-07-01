```python
import unittest
from src import deployer

class TestDeployer(unittest.TestCase):

    def setUp(self):
        self.deployer = deployer.Deployer()

    def test_deploy(self):
        result = self.deployer.deploy()
        self.assertTrue(result, "Deployment failed")

    def test_rollback(self):
        result = self.deployer.rollback()
        self.assertTrue(result, "Rollback failed")

    def test_update(self):
        result = self.deployer.update()
        self.assertTrue(result, "Update failed")

    def test_health_check(self):
        result = self.deployer.health_check()
        self.assertTrue(result, "Health check failed")

if __name__ == '__main__':
    unittest.main()
```