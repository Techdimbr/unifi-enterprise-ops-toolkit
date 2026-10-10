# 🏛️ README DE INSTRUÇÕES PRINCIPAIS — UniFi Enterprise Ops Toolkit

**Repositório Oficial:** `https://github.com/Techdimbr/unifi-enterprise-ops-toolkit`  
**Classificação:** Projeto de Referência Técnica Corporativa (Padrão Open-Core)  
**Doutrina de Engenharia:** Kether_1 · Central de Tecnologia TECHDIM  
**Status Atual:** Base Canônica Homologada — Pronto para Expansão de Funções  
**Website Institucional:** https://techdimbr.github.io/techdimbr/  
**Licença:** MIT Corporate  

---

## 1. Identificação e Propósito do Projeto
- **Nome Comercial:** UniFi Enterprise Ops Toolkit
- **Identificador (Slug):** `unifi-enterprise-ops-toolkit`
- **Categoria:** Automação & Operação de Redes Corporativas
- **Stack Tecnológica:** Python 3.10+, UniFi Network API / UniFi OS v3+, REST, SQLite/JSON
- **Objetivo Central:** Fornecer um kit corporativo de automação para controladoras UniFi Network, gerenciando rotinas de backup, provisionamento de redes/VLANs, diagnóstico de portas de switches e geração de relatórios de saúde de infraestrutura.

### Casos de Uso Reais
1. **Rotina Noturna de Backup Externo:** Download automatizado de backup `.unf` via API da UDM-Pro com retenção de 30 dias.
2. **Auditoria de Isolamento de Convidados:** Validação de que a VLAN de visitantes não tem rota para sub-redes corporativas.
3. **Detecção de Port Flapping e Erros de Cabo:** Leitura contínua dos contadores de erro das portas de switch.

---

## 2. Estrutura dos Módulos em `03_APLICACAO/src/`

```text
03_APLICACAO/src/
├── unifi_ops.py                       # Cliente principal de API, autenticação e despacho de comandos
├── backup_manager.py                  # Gerenciador de download, verificação de hash e rotação de backups
├── vlan_provisioner.py                # Mapeamento e criação declarativa de VLANs
└── health_monitor.py                  # Coleta de telemetria de switches, APs e clientes conectados
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
<!-- ÁREA DESTINADA À ESPECIFICAÇÃO DE NOVOS RECURSOS UNIFI -->
- [x] Autenticação com sessão cookie baseada em credenciais locais de admin;
- [x] Inventário estruturado de dispositivos com status de conectividade;
- [ ] Suporte a tokens de API da versão UniFi OS v3.2+;
- [ ] Exportação de topologia de rede em formato JSON e grafo Mermaid.
