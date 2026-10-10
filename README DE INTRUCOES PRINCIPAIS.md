# 🏛️ README DE INSTRUÇÕES PRINCIPAIS — Techdim Debian Hardening Framework

**Repositório Oficial:** `https://github.com/Techdimbr/techdim-debian-hardening-framework`  
**Classificação:** Projeto de Referência Técnica Corporativa (Padrão Open-Core)  
**Doutrina de Engenharia:** Kether_1 · Central de Tecnologia TECHDIM  
**Status Atual:** Base Canônica Homologada — Pronto para Expansão de Funções  
**Website Institucional:** https://techdimbr.github.io/techdimbr/  
**Licença:** MIT Corporate  

---

## 1. Identificação e Propósito do Projeto
- **Nome Comercial:** Techdim Debian Hardening Framework
- **Identificador (Slug):** `techdim-debian-hardening-framework`
- **Categoria:** Infraestrutura como Código (IaC) & Blue Team
- **Stack Tecnológica:** Ansible Core 2.16+, Bash nativo, Debian 13 (Trixie/Sid), nftables, AppArmor, USBGuard, sysctl
- **Objetivo Central:** Fornecer playbooks idempotentes em Ansible e ferramentas de auditoria em Python/Bash para aplicar e validar o baseline de segurança CIS Benchmark Level 2 Server e STIG em frotas de servidores Debian 13.

### Casos de Uso Reais
1. **Implantação de Servidores Críticos:** Aplicação do hardening logo após a instalação do SO via PXE/Cloud-Init.
2. **Auditoria de Conformidade:** Execução de varredura contínua (`check-mode`) para detectar desvios de configuração (*configuration drift*).
3. **Proteção de Estações Físicas:** Bloqueio de portas USB contra ataques de BadUSB através do daemon USBGuard.

---

## 2. Arquitetura dos Componentes a Desenvolver em `03_APLICACAO/`

```text
03_APLICACAO/
├── requirements.txt                   # Dependências Python (ansible-core, etc.)
├── src/
│   ├── compliance_checker.py          # Script CLI de auditoria de conformidade (Python puro)
│   ├── site.yml                       # Playbook principal do Ansible
│   ├── inventory.ini.example          # Exemplo de inventário de hosts
│   └── roles/
│       ├── 01_sysctl_kernel/          # Hardening de memória, ASLR e redes
│       ├── 02_nftables_firewall/      # Políticas de firewall stateful
│       ├── 03_ssh_pam/                # Configuração segura de SSH e autenticação
│       └── 04_apparmor_usbguard/      # Confinamento de processos e mídia física
└── tests/
    ├── test_compliance.py             # Teste automatizado do verificador
    └── test_ansible_syntax.py         # Teste de sintaxe dos playbooks
```

---

## 3. Guia Operacional para o Desenvolvedor

1. **Bootstrap do Ambiente:**
   ```bash
   ./iniciar.sh
   ```
2. **Executar Testes Unitários:**
   ```bash
   python3 -m unittest discover 03_APLICACAO/tests
   ```
3. **Auditar Integridade Criptográfica dos Arquivos:**
   ```bash
   ./00_AUDITORIA/verificar_integridade.sh --gerar
   ```

---

## 4. Diretrizes e Regras de Negócio da Função (Para Preenchimento)
<!-- ÁREA DESTINADA À ESPECIFICAÇÃO DE NOVAS REGRAS DE HARDENING -->
- [x] Baseline de Kernel sysctl (`fs.protected_hardlinks=1`, `kernel.randomize_va_space=2`, `net.ipv4.conf.all.rp_filter=1`);
- [x] Regras de nftables com drop por padrão na cadeia input;
- [ ] Implementação de perfis AppArmor customizados para daemons de banco de dados e web;
- [ ] Integração com relatórios em formato JSON/HTML para entrega a equipes de compliance.
