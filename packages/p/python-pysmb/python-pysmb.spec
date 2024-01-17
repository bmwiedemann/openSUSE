#
# spec file for package python-pysmb
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


Name:           python-pysmb
Version:        1.2.9.1
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
%if 0%{?sle_version} && 0%{?sle_version} <= 150400
BuildRequires:  python-nose
BuildRequires:  python-twisted
%endif
BuildRequires:  %{python_module nose2}
BuildRequires:  %{python_module pyasn1}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module tqdm}
# /SECTION
%python_subpackages

%description
pysmb is an experimental SMB/CIFS library written in Python. It implements the client-side SMB/CIFS protocol which allows your Python application to access and transfer files to/from SMB/CIFS shared folders like your Windows file sharing and Samba folders.

%prep
%autosetup -p1 -n pysmb-%{version}

sed -Ei "1{/^#!\/usr\/bin\/python/d}" python*/smb/*/sha256.py

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
rm python3/tests/SMBConnectionTests/test_SMBHandler.py
%{python_expand # Run only the tests that can work without network (and only from the right python[2,3] dir)
python_testdir_str=$python
python_testdir=${python_testdir_str:0:7}
export PYTHONPATH=%{$python_sitelib} PYTHONDONTWRITEBYTECODE=1
find . -name \*.pyc\* -delete
pytest-%{$python_bin_suffix} ${python_testdir} -k 'not (SMB or test_broadcast)'
}

%files %{python_files}
%doc CHANGELOG README.txt
%license LICENSE
%{python_sitelib}/smb/
%{python_sitelib}/nmb/
%{python_sitelib}/pysmb-%{version}-py%{python_version}.egg-info/

%changelog
