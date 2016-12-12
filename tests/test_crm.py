# coding: utf-8
from .suite import BaseSuite


class TestCrm(BaseSuite):
    def test_action(self):
        rv = self.client.get('/crm/action')
        assert rv.status_code == 200
