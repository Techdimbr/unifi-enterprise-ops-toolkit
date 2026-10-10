#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Testes unitários para o UniFi Enterprise Ops Toolkit.
"""

import unittest
import sys
from pathlib import Path

SRC_DIR = Path(__file__).resolve().parent.parent / "src"
sys.path.insert(0, str(SRC_DIR))

from unifi_ops import UniFiOpsClient

class TestUniFiOpsClient(unittest.TestCase):
    def setUp(self):
        self.client = UniFiOpsClient()

    def test_auditoria_dispositivos_online(self):
        dispositivos = [
            {"type": "ugw", "state": 1},
            {"type": "usw", "state": 1},
            {"type": "uap", "state": 1}
        ]
        self.client.carregar_dispositivos(dispositivos)
        resultado = self.client.auditar_topologia()
        self.assertEqual(resultado["online"], 3)
        self.assertEqual(resultado["offline"], 0)
        self.assertEqual(resultado["conformidade"], "100%")

    def test_auditoria_dispositivos_com_queda(self):
        dispositivos = [
            {"type": "uap", "state": 1},
            {"type": "uap", "state": 0}
        ]
        self.client.carregar_dispositivos(dispositivos)
        resultado = self.client.auditar_topologia()
        self.assertEqual(resultado["online"], 1)
        self.assertEqual(resultado["offline"], 1)
        self.assertEqual(resultado["conformidade"], "50.0%")

if __name__ == "__main__":
    unittest.main()
