#
# spec file for package python-sshtunnel
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-sshtunnel
Version:        0.1.5
Release:        0
Summary:        SSH tunnels to remote server
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/pahaz/sshtunnel/
Source:         https://files.pythonhosted.org/packages/source/s/sshtunnel/sshtunnel-%{version}.tar.gz
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module paramiko >= 1.15.2}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
# for the tests to validate some things
BuildRequires:  fdupes
BuildRequires:  openssh
BuildRequires:  python-rpm-macros
Requires:       openssh
Requires:       python-paramiko >= 1.15.2
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
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/sshtunnel
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%post
%python_install_alternative sshtunnel

%postun
%python_uninstall_alternative sshtunnel

%files %{python_files}
%license LICENSE
%doc *.rst
%python_alternative %{_bindir}/sshtunnel
%{python_sitelib}/*

%changelog
