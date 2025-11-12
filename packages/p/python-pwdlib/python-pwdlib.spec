#
# spec file for package python-pwdlib
#
# Copyright (c) 2025 SUSE LLC
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


Name:           python-pwdlib
Version:        0.3.0
Release:        0
Summary:        Modern password hashing for Python
License:        MIT
URL:            https://github.com/frankie567/pwdlib
Source:         https://files.pythonhosted.org/packages/source/p/pwdlib/pwdlib-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module argon2-cffi}
BuildRequires:  %{python_module bcrypt}
BuildRequires:  fdupes
Suggests:       python-argon2-cffi >= 23.1.0
Suggests:       python-bcrypt >= 4.1.2
BuildArch:      noarch
%python_subpackages

%description
Modern password hashing for Python

**Documentation**: <a href="https://frankie567.github.io/pwdlib/" target="_blank">https://frankie567.github.io/pwdlib/</a>

**Source Code**: <a href="https://github.com/frankie567/pwdlib" target="_blank">https://github.com/frankie567/pwdlib</a>

%prep
%autosetup -p1 -n pwdlib-%{version}
sed -i '/addopts/d' pyproject.toml

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.md
%license LICENSE LICENSE
%{python_sitelib}/pwdlib
%{python_sitelib}/pwdlib-%{version}.dist-info

%changelog
