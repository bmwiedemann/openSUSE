#
# spec file for package python-flufl.lock
#
# Copyright (c) 2022 SUSE LLC
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


Name:           python-flufl.lock
Version:        7.1.1
Release:        0
Summary:        NFS-safe file locking with timeouts for POSIX and Windows
License:        Apache-2.0
URL:            https://gitlab.com/warsaw/flufl.lock
Source:         https://files.pythonhosted.org/packages/source/f/flufl.lock/flufl.lock-%{version}.tar.gz
BuildRequires:  %{python_module atpublic >= 2.3}
BuildRequires:  %{python_module base >= 3.7}
BuildRequires:  %{python_module pdm-pep517}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module psutil >= 5.9}
BuildRequires:  %{python_module typing_extensions if %python-base < 3.8}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-atpublic >= 2.3
Requires:       python-psutil >= 5.9
Requires:       (python-typing_extensions if python-base < 3.8)
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module sybil}
# /SECTION
%python_subpackages

%description
NFS-safe file locking with timeouts for POSIX and Windows.

%prep
%autosetup -p1 -n flufl.lock-%{version}
sed -i 's/--cov=flufl --cov-report=term --cov-report=xml//' pyproject.toml

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.rst docs/NEWS.rst
%license LICENSE
%dir %{python_sitelib}/flufl
%{python_sitelib}/flufl/lock
%{python_sitelib}/flufl.lock-%{version}*info

%changelog
