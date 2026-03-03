#
# spec file for package linode-cli
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%define cli_name    linode-cli

Name:           linode-cli
Version:        5.65.0
Release:        0
Summary:        The Linode command-line interface
License:        BSD-3-Clause
URL:            https://github.com/linode/linode-cli
Source:         https://github.com/linode/linode-cli/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        openapi.json
# PATCH-FIX-OPENSUSE 0001-Remove-shebang-from-non-executable-files.patch
Patch0:         0001-Remove-shebang-from-non-executable-files.patch
BuildRequires:  %{python_module PyYAML}
BuildRequires:  %{python_module boto3}
BuildRequires:  %{python_module linode-metadata >= 0.3}
BuildRequires:  %{python_module openapi3}
BuildRequires:  %{python_module packaging}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest-mock}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module pytimeparse}
BuildRequires:  %{python_module requests-mock}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module rich}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-PyYAML
Requires:       python-linode-metadata >= 0.3
Requires:       python-openapi3
Requires:       python-packaging
Requires:       python-pytimeparse
Requires:       python-requests
Requires:       python-rich
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
%python_subpackages

%description
The Linode Command Line interface

%package -n %{name}-bash-completion
Summary:        Bash completion for linode-cli
Group:          System/Shells
Supplements:    %{python_module linode-cli and bash-completion}
BuildArch:      noarch

%description -n %{name}-bash-completion

Bash completion files for %{name}

%prep
%autosetup -p1

%build
LINODE_CLI_VERSION="%{version}" make create-version

# bake data file
python3 -m linodecli bake "%{SOURCE1}" --skip-config
cp data-3 linodecli/
# generate bash completion
python3 -m linodecli completion bash > completion.bash

# run the actual build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/%{cli_name}
%python_clone -a %{buildroot}%{_bindir}/lin
%python_clone -a %{buildroot}%{_bindir}/linode

# install generated bash completion to proper location
install -d %{buildroot}%{_datarootdir}/bash-completion/completions
mv completion.bash %{buildroot}%{_datarootdir}/bash-completion/completions/%{cli_name}

%python_expand %fdupes %{buildroot}%{$python_sitelib}

%post
%python_install_alternative %{cli_name}
%python_install_alternative lin
%python_install_alternative linode

%postun
%python_uninstall_alternative %{cli_name}
%python_uninstall_alternative lin
%python_uninstall_alternative linode

%check
export LINODE_CLI_TEST_MODE=1
# requires network
%pytest tests/unit -k 'not test_nonexisting_id'

%files %{python_files}
%python_alternative %{_bindir}/%{cli_name}
%python_alternative %{_bindir}/lin
%python_alternative %{_bindir}/linode
%{python_sitelib}/linodecli
%{python_sitelib}/linode_cli-%{version}.dist-info

%files -n %{name}-bash-completion
%dir %{_datarootdir}/bash-completion/completions/
%{_datarootdir}/bash-completion/completions/%{name}

%changelog
