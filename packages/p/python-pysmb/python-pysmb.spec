#
# spec file for package python-pysmb
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-pysmb
Version:        1.1.25
Release:        0
License:        Zlib
Summary:        SMB/CIFS library to support file sharing between Windows and Linux machines
Url:            https://miketeo.net/projects/pysmb
Group:          Development/Languages/Python
Source:         https://files.pythonhosted.org/packages/source/p/pysmb/pysmb-%{version}.zip
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module setuptools}
# SECTION test requirements
BuildRequires:  %{python_module pyasn1}
# /SECTION
BuildRequires:  unzip
BuildRequires:  fdupes
Requires:       python-pyasn1
BuildArch:      noarch

%python_subpackages

%description
pysmb is an experimental SMB/CIFS library written in Python. It implements the client-side SMB/CIFS protocol which allows your Python application to access and transfer files to/from SMB/CIFS shared folders like your Windows file sharing and Samba folders.

%prep
%setup -q -n pysmb-%{version}

%build
%python_build

%install
%python_install

%{python_expand # Remove hashbangs from a non-exec file
sed -Ei "1{/^#!\/usr\/bin\/python/d}" %{buildroot}%{$python_sitelib}/smb/utils/sha256.py
}

%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec setup.py test

%files %{python_files}
%doc CHANGELOG README.txt
%license LICENSE
%{python_sitelib}/*

%changelog
