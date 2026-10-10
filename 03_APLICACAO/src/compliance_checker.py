#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Techdim Debian Hardening Framework - Verificador de Conformidade CIS
Verifica parâmetros de segurança no kernel Linux (/proc/sys) e serviços.
"""

import sys
import os
from typing import Dict, Tuple

REGRAS_SYSCTL = {
    "kernel.randomize_va_space": "2",
    "fs.protected_hardlinks": "1",
    "fs.protected_symlinks": "1",
    "fs.suid_dumpable": "0",
    "net.ipv4.ip_forward": "0",
    "net.ipv4.conf.all.send_redirects": "0",
    "net.ipv4.conf.all.accept_redirects": "0",
    "net.ipv4.conf.all.rp_filter": "1",
    "net.ipv4.tcp_syncookies": "1",
}

def ler_sysctl(chave: str) -> str:
    """Lê o valor de um parâmetro sysctl através do sistema de arquivos /proc/sys."""
    caminho = "/proc/sys/" + chave.replace(".", "/")
    try:
        with open(caminho, "r", encoding="utf-8") as f:
            return f.read().strip()
    except (FileNotFoundError, PermissionError):
        return "INDISPONIVEL"

def avaliar_conformidade(regras: Dict[str, str] = REGRAS_SYSCTL) -> Tuple[int, int, Dict[str, Dict[str, str]]]:
    """Avalia o status de conformidade das regras."""
    aprovados = 0
    reprovados = 0
    resultados = {}
    
    for chave, esperado in regras.items():
        atual = ler_sysctl(chave)
        status = "CONFORME" if atual == esperado else "NAO_CONFORME"
        if status == "CONFORME":
            aprovados += 1
        else:
            reprovados += 1
            
        resultados[chave] = {
            "esperado": esperado,
            "atual": atual,
            "status": status
        }
        
    return aprovados, reprovados, resultados

def main():
    print("=" * 65)
    print("🛡️  TECHDIM DEBIAN HARDENING - AUDITORIA DE CONFORMIDADE CIS")
    print("=" * 65)
    
    aprovados, reprovados, resultados = avaliar_conformidade()
    
    for chave, dados in resultados.items():
        icone = "✅" if dados["status"] == "CONFORME" else "❌"
        print(f"{icone} {chave:<35} | Esperado: {dados['esperado']} | Atual: {dados['atual']}")
        
    total = aprovados + reprovados
    pontuacao = (aprovados / total * 100) if total > 0 else 0
    
    print("-" * 65)
    print(f"📊 Pontuação de Conformidade: {pontuacao:.1f}% ({aprovados}/{total} regras aprovadas)")
    print("=" * 65)
    
    if reprovados > 0:
        sys.exit(1)
    sys.exit(0)

if __name__ == "__main__":
    main()
