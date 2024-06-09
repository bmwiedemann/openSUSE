#
# spec file for package python-pyspnego
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
Name:           python-pyspnego
Version:        0.10.2
Release:        0
Summary:        Python SPNEGO authentication library
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/jborean93/pyspnego
Source:         https://github.com/jborean93/pyspnego/archive/v%{version}.tar.gz#/pyspnego-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module dataclasses if %python-base < 3.7}
BuildRequires:  %{python_module cryptography}
BuildRequires:  %{python_module pytest-mock}
BuildRequires:  %{python_module pytest}
# /SECTION
BuildRequires:  fdupes
Requires:       python-cryptography
%if 0%{python_version_nodots} < 37
Requires:       python-dataclasses
%endif
Requires(post): update-alternatives
Requires(postun): update-alternatives
Suggests:       python-gssapi >= 1.5.0
Suggests:       python-ruamel.yaml
BuildArch:      noarch
%python_subpackages

%description
Library to handle SPNEGO (Negotiate, NTLM, Kerberos) authentication.
Also includes a packet parser that can be used to decode raw
NTLM/SPNEGO/Kerberos tokens into a human readable format.

%prep
%setup -q -n pyspnego-%{version}
sed -i '1{/^#!/ d}' src/spnego/__main__.py

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/pyspnego-parse
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%post
%python_install_alternative pyspnego-parse

%postun
%python_uninstall_alternative pyspnego-parse

%check
%pytest

%files %{python_files}
%license LICENSE
%doc CHANGELOG.md README.md
%python_alternative %{_bindir}/pyspnego-parse
%{python_sitelib}/spnego
%{python_sitelib}/pyspnego-%{version}.dist-info

%changelog
