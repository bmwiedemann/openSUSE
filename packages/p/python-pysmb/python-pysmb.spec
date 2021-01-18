#
# spec file for package python-pysmb
#
# Copyright (c) 2021 SUSE LLC
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


Name:           python-pysmb
Version:        1.2.6
Release:        0
Summary:        SMB/CIFS library to support file sharing between Windows and Linux machines
License:        Zlib
Group:          Development/Languages/Python
URL:            https://miketeo.net/projects/pysmb
Source:         https://files.pythonhosted.org/packages/source/p/pysmb/pysmb-%{version}.zip
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  unzip
Requires:       python-pyasn1
BuildArch:      noarch
# SECTION test requirements
# nose packages still imported despite pytest
BuildRequires:  %{python_module nose}
BuildRequires:  %{python_module pyasn1}
BuildRequires:  %{python_module pytest}
%if 0%{?suse_version} < 1550
BuildRequires:  python-twisted
%endif
# /SECTION
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
%{python_expand # Run only the tests that can work without network (and only from the right python[2,3] dir)
# (the trick here is that $python_ is expanded early by the pytest and python_expand macros, not by the shell)
 $python_testdir=${python_flavor:0:7}
}
%pytest ${$python_testdir} -k 'not SMB and not test_broadcast'

%files %{python_files}
%doc CHANGELOG README.txt
%license LICENSE
%{python_sitelib}/*

%changelog
