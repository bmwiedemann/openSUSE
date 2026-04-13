#
# spec file for package python-dsinternals
#
# Copyright (c) 2026 SUSE LLC and contributors
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
# Copyright (c) 2023-2026, Martin Hauke <mardnh@gmx.de>
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.


Name:           python-dsinternals
Version:        1.2.5
Release:        0
Summary:        Directory Services Internals Library
License:        GPL-2.0-only
URL:            http://github.com/p0dalirius/pydsinternals
Source:         https://github.com/p0dalirius/pydsinternals/archive/refs/tags/%{version}.tar.gz#/pydsinternals-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pyOpenSSL}
BuildRequires:  %{python_module pycryptodomex}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
A Python native library containing necessary classes, functions and
structures to interact with Windows Active Directory.

%prep
%autosetup -p1 -n pydsinternals-%{version}
# drop shebang
find dsinternals -name "*.py" -exec sed -i '/^#!\//, 1d' {} \;
# fix spurious exec permission on various files
chmod -x LICENSE README.md

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%python_expand rm -rf %{buildroot}%{$python_sitelib}/tests

%check
%pyunittest -v

%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitelib}/dsinternals
%{python_sitelib}/dsinternals-%{version}.dist-info

%changelog
