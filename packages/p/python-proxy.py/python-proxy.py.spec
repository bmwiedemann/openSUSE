#
# spec file for package python-proxy.py
#
# Copyright (c) 2023 SUSE LLC
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


%{?!python_module:%define python_module() python3-%{**}}
%define skip_python2 1
%{?sle15_python_module_pythons}
Name:           python-proxy.py
Version:        2.3.1
Release:        0
Summary:        TLS interception capable proxy server
License:        BSD-3-Clause
URL:            https://github.com/abhinavsingh/proxy.py
# PyPI sdist does not have tests, use Github source
Source:         https://github.com/abhinavsingh/proxy.py/archive/refs/tags/v%{version}.tar.gz#/proxy.py-%{version}-gh.tar.gz
# PATCH-FIX-OPENSUSE proxy.py-command.patch -- deconflict with libproxy, code@bnavigator.de
Patch0:         proxy.py-command.patch
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-typing-extensions >= 3.7.4.3
Requires(post): update-alternatives
Requires(postun):update-alternatives
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module typing-extensions >= 3.7.4.3}
BuildRequires:  openssl
# /SECTION
%python_subpackages

%description
Fast, Lightweight, Pluggable, TLS interception capable proxy server
focused on Network monitoring, controls & Application development, testing, debugging.

Note: On SUSE distributions, the command is installed as proxy-py not as proxy.

%prep
%autosetup -p1 -n proxy.py-%{version}

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/proxy-py
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%post
%python_install_alternative proxy-py

%postun
%python_uninstall_alternative proxy-py

%files %{python_files}
%doc README.md
%license LICENSE
%python_alternative %{_bindir}/proxy-py
%{python_sitelib}/proxy
%{python_sitelib}/proxy.py-%{version}*-info

%changelog
