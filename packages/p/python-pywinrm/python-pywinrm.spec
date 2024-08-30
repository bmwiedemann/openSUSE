#
# spec file for package python-pywinrm
#
# Copyright (c) 2024 SUSE LLC
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
Name:           python-pywinrm
Version:        0.5.0
Release:        0
Summary:        Python library for Windows Remote Management
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/diyan/pywinrm/
Source:         https://github.com/diyan/pywinrm/archive/refs/tags/v%{version}.tar.gz#/pywinrm-%{version}.tar.gz
BuildRequires:  %{python_module kerberos}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests >= 2.9.1}
BuildRequires:  %{python_module requests_ntlm >= 1.1.0}
BuildRequires:  %{python_module wheel}
BuildRequires:  %{python_module xmltodict}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-requests >= 2.9.1
Requires:       python-requests_ntlm >= 1.1.0
Requires:       python-xmltodict
Suggests:       python-requests-credssp >= 0.0.1
Suggests:       python-requests-kerberos >= 0.10.0
BuildArch:      noarch
%python_subpackages

%description
pywinrm is a Python client for Windows Remote Management (WinRM). This
allows you to invoke commands on target Windows machines from any
machine that can run Python.

WinRM allows you to call native objects in Windows. This includes, but
is not limited to, running batch scripts, powershell scripts and
fetching WMI variables. For more information on WinRM, please visit
Microsoft's WinRM http://msdn.microsoft.com/en-us/library/aa384426.aspx

%prep
%setup -q -n pywinrm-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%python_expand rm -Rv  %{buildroot}%{$python_sitelib}/winrm/tests

%check
# https://github.com/diyan/pywinrm/issues/345
sed -i 's:import mock:from unittest import mock:' winrm/tests/test_transport.py
%pyunittest discover -v

%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitelib}/winrm
%{python_sitelib}/pywinrm-%{version}.dist-info

%changelog
