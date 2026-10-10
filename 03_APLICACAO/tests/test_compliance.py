#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Testes unitários para o módulo de conformidade do Techdim Debian Hardening Framework.
"""

import unittest
from unittest.mock import patch
import sys
from pathlib import Path

# Adiciona o diretório src ao PATH
SRC_DIR = Path(__file__).resolve().parent.parent / "src"
sys.path.insert(0, str(SRC_DIR))

from compliance_checker import avaliar_conformidade

class TestComplianceChecker(unittest.TestCase):
    def test_todas_regras_conformes(self):
        regras_teste = {
            "kernel.randomize_va_space": "2",
            "fs.protected_hardlinks": "1"
        }
        with patch("compliance_checker.ler_sysctl", side_effect=lambda k: regras_teste[k]):
            aprovados, reprovados, resultados = avaliar_conformidade(regras_teste)
            self.assertEqual(aprovados, 2)
            self.assertEqual(reprovados, 0)
            self.assertEqual(resultados["kernel.randomize_va_space"]["status"], "CONFORME")

    def test_regras_nao_conformes(self):
        regras_teste = {
            "kernel.randomize_va_space": "2",
            "fs.suid_dumpable": "0"
        }
        with patch("compliance_checker.ler_sysctl", return_value="0"):
            aprovados, reprovados, resultados = avaliar_conformidade(regras_teste)
            self.assertEqual(aprovados, 1) # fs.suid_dumpable esperado "0", atual "0"
            self.assertEqual(reprovados, 1) # randomize esperado "2", atual "0"

if __name__ == "__main__":
    unittest.main()
