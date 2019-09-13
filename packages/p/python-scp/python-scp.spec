#
# spec file for package python-scp
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2017, Martin Hauke <mardnh@gmx.de>
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
Name:           python-scp
Version:        0.13.2
Release:        0
Summary:        SSH scp module for paramiko
License:        LGPL-2.1-or-later
Group:          Development/Languages/Python
URL:            https://github.com/jbardin/scp.py
Source:         https://files.pythonhosted.org/packages/source/s/scp/scp-%{version}.tar.gz
BuildRequires:  %{python_module paramiko}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-paramiko
BuildArch:      noarch
%python_subpackages

%description
The scp.py module uses a paramiko transport to send and receive files via the
scp protocol. This is the protocol as referenced from the openssh scp program,
and has only been tested with this implementation.

%prep
%setup -q -n scp-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# tests require running ssh server
#%%python_exec -m unittest discover

%files %{python_files}
%license LICENSE.txt
%doc README.rst
%{python_sitelib}/*

%changelog
