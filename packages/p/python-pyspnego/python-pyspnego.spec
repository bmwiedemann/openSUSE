#
# spec file for package python-pyspnego
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


%if 0%{?suse_version} > 1500
%bcond_without libalternatives
%else
%bcond_with libalternatives
%endif
%{?sle15_python_module_pythons}
Name:           python-pyspnego
Version:        0.11.2
Release:        0
Summary:        Python SPNEGO authentication library
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/jborean93/pyspnego
Source:         https://github.com/jborean93/pyspnego/archive/v%{version}.tar.gz#/pyspnego-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-cryptography
Suggests:       python-gssapi >= 1.5.0
Suggests:       python-ruamel.yaml
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module cryptography}
BuildRequires:  %{python_module dataclasses if %python-base < 3.7}
BuildRequires:  %{python_module pytest-mock}
BuildRequires:  %{python_module pytest}
# /SECTION
%if 0%{python_version_nodots} < 37
Requires:       python-dataclasses
%endif
%if %{with libalternatives}
BuildRequires:  alts
Requires:       alts
%else
Requires(post): update-alternatives
Requires(postun): update-alternatives
%endif
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

%pre
%python_libalternatives_reset_alternative pyspnego-parse

%check
%pytest

%files %{python_files}
%license LICENSE
%doc CHANGELOG.md README.md
%python_alternative %{_bindir}/pyspnego-parse
%{python_sitelib}/spnego
%{python_sitelib}/pyspnego-%{version}.dist-info

%changelog
