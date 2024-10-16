#
# spec file for package python-sshtunnel
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
Name:           python-sshtunnel
Version:        0.4.0
Release:        0
Summary:        SSH tunnels to remote server
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/pahaz/sshtunnel/
Source:         https://files.pythonhosted.org/packages/source/s/sshtunnel/sshtunnel-%{version}.tar.gz
BuildRequires:  %{python_module paramiko >= 2.7.2}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
# for the tests to validate some things
BuildRequires:  fdupes
BuildRequires:  openssh
BuildRequires:  python-rpm-macros
Requires:       openssh
Requires:       python-paramiko >= 2.7.2
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
%python_subpackages

%description
The sshtunnel package allows one to create SSH tunnels using local
or remote port forwarding. Thus, it provides a Python wrapper to
the same functionality provided by the SSH command using the -L
and -R parameters.

%prep
%setup -q -n sshtunnel-%{version}
# Remove shebang line
sed -i '1{\,^#!%{_bindir}/env python,d}' sshtunnel.py

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/sshtunnel
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# https://github.com/pahaz/sshtunnel/issues/259
sed -i 's:import mock:from unittest import mock:' tests/test_forwarder.py
%pytest

%post
%python_install_alternative sshtunnel

%postun
%python_uninstall_alternative sshtunnel

%files %{python_files}
%license LICENSE
%doc *.rst
%python_alternative %{_bindir}/sshtunnel
%pycache_only %{python_sitelib}/__pycache__/sshtunnel*pyc
%{python_sitelib}/sshtunnel.py
%{python_sitelib}/sshtunnel-{%version}.dist-info

%changelog
