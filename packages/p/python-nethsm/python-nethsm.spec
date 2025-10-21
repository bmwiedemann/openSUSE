#
# spec file for package python-nethsm
#
# Copyright (c) 2025 SUSE LLC and contributors
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


%{?sle15_python_module_pythons}
Name:           python-nethsm
Version:        2.0.0
Release:        0
Summary:        Python Library to manage NetHSM(s)
License:        Apache-2.0
URL:            https://github.com/Nitrokey/nethsm-sdk-py
Source:         https://github.com/Nitrokey/nethsm-sdk-py/archive/v%{version}.tar.gz#/nethsm-%{version}.tar.gz
BuildRequires:  %{python_module certifi}
BuildRequires:  %{python_module cryptography >= 41.0}
BuildRequires:  %{python_module flit >= 3.2}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module python-dateutil}
BuildRequires:  %{python_module typing_extensions >= 4.3.0}
BuildRequires:  %{python_module urllib3 >= 2.0 with %python-urllib3 < 3}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module docker}
BuildRequires:  %{python_module podman}
BuildRequires:  %{python_module pycryptodome}
# /SECTION
BuildRequires:  fdupes
Requires:       python-certifi
Requires:       python-cryptography >= 41.0
Requires:       python-python-dateutil
Requires:       python-typing_extensions >= 4.3.0
Requires:       (python-urllib3 >= 2.0 with python-urllib3 < 3)
Suggests:       python-black >= 22.1.0
Suggests:       python-flake8
Suggests:       python-flit >= 3.2
Suggests:       python-ipython
Suggests:       python-isort
Suggests:       python-mypy >= 1.4
Suggests:       python-pytest
Suggests:       python-pytest-reporter-html1
Suggests:       python-docker
Suggests:       python-pycryptodome
Suggests:       python-requests
Suggests:       python-types-python-dateutil
Suggests:       python-types-requests
Suggests:       python-pytest-cov
Suggests:       python-cryptography
Suggests:       python-pyyaml
BuildArch:      noarch
%python_subpackages

%description
# nethsm-sdk-py

Python client for NetHSM. NetHSM documentation available here: [NetHSM documentation](https://docs.nitrokey.com/nethsm/)

%prep
%autosetup -p1 -n nethsm-sdk-py-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# Ignore all checks that require network connectivity
IGNORED_CHECKS="test_csr"
IGNORED_CHECKS="${IGNORED_CHECKS} or test_add_delete_list_operator_tags"
IGNORED_CHECKS="${IGNORED_CHECKS} or test_add_delete_user_administrator"
IGNORED_CHECKS="${IGNORED_CHECKS} or test_add_get_key_by_public_key"
IGNORED_CHECKS="${IGNORED_CHECKS} or test_add_key"
IGNORED_CHECKS="${IGNORED_CHECKS} or test_add_key_tag_get_key"
IGNORED_CHECKS="${IGNORED_CHECKS} or test_add_list_operator_tags"
IGNORED_CHECKS="${IGNORED_CHECKS} or test_add_operator_tags"
IGNORED_CHECKS="${IGNORED_CHECKS} or test_add_users_set_passphrases_connect"
IGNORED_CHECKS="${IGNORED_CHECKS} or test_decrypt"
IGNORED_CHECKS="${IGNORED_CHECKS} or test_delete_certificate"
IGNORED_CHECKS="${IGNORED_CHECKS} or test_delete_key"
IGNORED_CHECKS="${IGNORED_CHECKS} or test_delete_key_tag_get_key"
IGNORED_CHECKS="${IGNORED_CHECKS} or test_encrypt_decrypt"
IGNORED_CHECKS="${IGNORED_CHECKS} or test_factory_reset"
IGNORED_CHECKS="${IGNORED_CHECKS} or test_generate_get_key_by_id"
IGNORED_CHECKS="${IGNORED_CHECKS} or test_generate_key"
IGNORED_CHECKS="${IGNORED_CHECKS} or test_get_config_get_certificate"
IGNORED_CHECKS="${IGNORED_CHECKS} or test_get_config_get_public_key"
IGNORED_CHECKS="${IGNORED_CHECKS} or test_get_config_logging"
IGNORED_CHECKS="${IGNORED_CHECKS} or test_get_config_network"
IGNORED_CHECKS="${IGNORED_CHECKS} or test_get_config_time"
IGNORED_CHECKS="${IGNORED_CHECKS} or test_get_config_unattended_boot"
IGNORED_CHECKS="${IGNORED_CHECKS} or test_get_user_admin"
IGNORED_CHECKS="${IGNORED_CHECKS} or test_info"
IGNORED_CHECKS="${IGNORED_CHECKS} or test_key_csr"
IGNORED_CHECKS="${IGNORED_CHECKS} or test_list_get_delete_add_users"
IGNORED_CHECKS="${IGNORED_CHECKS} or test_list_get_keys"
IGNORED_CHECKS="${IGNORED_CHECKS} or test_passphrase_add_user_retrieve_backup"
IGNORED_CHECKS="${IGNORED_CHECKS} or test_provision_reboot"
IGNORED_CHECKS="${IGNORED_CHECKS} or test_provision_shutdown"
IGNORED_CHECKS="${IGNORED_CHECKS} or test_provision_system_info"
IGNORED_CHECKS="${IGNORED_CHECKS} or test_set_backup_passphrase"
IGNORED_CHECKS="${IGNORED_CHECKS} or test_set_certificate"
IGNORED_CHECKS="${IGNORED_CHECKS} or test_set_get_key_certificate"
IGNORED_CHECKS="${IGNORED_CHECKS} or test_set_get_logging_config"
IGNORED_CHECKS="${IGNORED_CHECKS} or test_set_get_network_config"
IGNORED_CHECKS="${IGNORED_CHECKS} or test_set_get_time"
IGNORED_CHECKS="${IGNORED_CHECKS} or test_set_get_unattended_boot"
IGNORED_CHECKS="${IGNORED_CHECKS} or test_set_unlock_passphrase_lock_unlock"
IGNORED_CHECKS="${IGNORED_CHECKS} or test_sign"
IGNORED_CHECKS="${IGNORED_CHECKS} or test_state"
IGNORED_CHECKS="${IGNORED_CHECKS} or test_state_no_auth"
IGNORED_CHECKS="${IGNORED_CHECKS} or test_state_provision"
IGNORED_CHECKS="${IGNORED_CHECKS} or test_state_provision_add_user_get_random_data"
IGNORED_CHECKS="${IGNORED_CHECKS} or test_state_provision_add_user_metrics_get_metrics"
IGNORED_CHECKS="${IGNORED_CHECKS} or test_state_provision_lock_unlock"
IGNORED_CHECKS="${IGNORED_CHECKS} or test_state_provision_unlock_lock"
IGNORED_CHECKS="${IGNORED_CHECKS} or test_state_provision_update"
IGNORED_CHECKS="${IGNORED_CHECKS} or test_state_provision_update_cancel_update"
IGNORED_CHECKS="${IGNORED_CHECKS} or test_state_restore"
IGNORED_CHECKS="${IGNORED_CHECKS} or test_update_commit_update"
# ignore checks that need docker
IGNORED_CHECKS="${IGNORED_CHECKS} or test_keys"
IGNORED_CHECKS="${IGNORED_CHECKS} or test_config"
IGNORED_CHECKS="${IGNORED_CHECKS} or test_add_user"
IGNORED_CHECKS="${IGNORED_CHECKS} or test_delete_self"
IGNORED_CHECKS="${IGNORED_CHECKS} or test_ca_certs_none"
IGNORED_CHECKS="${IGNORED_CHECKS} or test_ca_certs_empty"
IGNORED_CHECKS="${IGNORED_CHECKS} or test_ca_certs_valid"
IGNORED_CHECKS="${IGNORED_CHECKS} or test_move_key"
IGNORED_CHECKS="${IGNORED_CHECKS} or test_list_keys_prefix"
%pytest -k "not (${IGNORED_CHECKS})"

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/nethsm
%{python_sitelib}/nethsm-%{version}.dist-info

%changelog
