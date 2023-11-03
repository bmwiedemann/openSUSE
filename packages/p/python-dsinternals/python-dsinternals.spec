#
# spec file for package python-dsinternals
#
# Copyright (c) 2023, Martin Hauke <mardnh@gmx.de>
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


Name:           python-dsinternals
Version:        1.2.4
Release:        0
Summary:        Directory Services Internals Library
License:        GPL-2.0
URL:            http://github.com/p0dalirius/pydsinternals
Source:         https://files.pythonhosted.org/packages/source/d/dsinternals/dsinternals-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  %{python_module pycryptodomex}
BuildRequires:  %{python_module pyOpenSSL}
BuildRequires:  fdupes
BuildArch:      noarch
%python_subpackages

%description
A Python native library containing necessary classes, functions and
structures to interact with Windows Active Directory.

%prep
%autosetup -p1 -n dsinternals-%{version}
# drop shebang
find dsinternals -name "*.py" -exec sed -i '/^#!\//, 1d' {} \;
# fix spurious exec permission on various files
chmod -x LICENSE README.md dsinternals.egg-info/top_level.txt

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%python_expand rm -rf %{buildroot}%{$python_sitelib}/tests

%check
%pyunittest -v

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/dsinternals
%{python_sitelib}/dsinternals-%{version}.dist-info

%changelog
