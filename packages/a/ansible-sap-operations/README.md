# suse.sap_operations Ansible Collection

## Description
This Ansible Collection executes various day-to-day operation tasks for SAP Systems.


## Requirements

### Control Nodes
Operating system:
- Any operating system with required Python and Ansible versions.

Python: 3.11 or higher

Ansible-core: 2.18 or higher

### Managed Nodes
Operating system:
- SUSE Linux Enterprise Server for SAP applications 15 SP5+ (SLE4SAP)
- Red Hat Enterprise Linux for SAP Solutions 8.x 9.x (RHEL4SAP)
**NOTE: Operating system needs to have access to required package repositories either directly or via subscription registration.**

Python: 3.11 or higher


## Use Cases

### Example Scenarios
- Operate `sapcontrol` functions like starting whole SAP System, stopping, etc.
- Update SAP profile files

### Ansible Roles
| Name | Summary |
| :--- | :--- |
| [sap_control](/roles/sap_control) | Operate sapcontrol tool (e.g. start, stop, etc.) |
| [sap_profile_update](/roles/sap_profile_update) | Update SAP System profiles (default or instance) |


## Testing
This Ansible Collection was tested across different Operating Systems, SAP products and scenarios. You can find examples of some of them below.

Operating systems:
- SUSE Linux Enterprise Server for SAP applications 15 SP5+ (SLE4SAP)
- Red Hat Enterprise Linux for SAP Solutions 8.x 9.x (RHEL4SAP)


## Contributing
You can find more information about ways you can contribute at [sap-linuxlab website](https://sap-linuxlab.github.io/initiative_contributions/).


## Support
You can report any issues using [Issues](https://github.com/SUSE/community.sap_operations/issues) section.


## Release Notes and Roadmap
You can find the release notes of this collection in [Changelog file](https://github.com/SUSE/community.sap_operations/blob/main/CHANGELOG.rst)


## Further Information

### Variable Precedence Rules
Please follow [Ansible Precedence guidelines](https://docs.ansible.com/ansible/latest/playbook_guide/playbooks_variables.html#variable-precedence-where-should-i-put-a-variable) on how to pass variables when using this collection.


## License
[Apache 2.0](https://github.com/SUSE/community.sap_operations/blob/main/LICENSE) 