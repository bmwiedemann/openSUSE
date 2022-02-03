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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define skip_python2 1
Name:           python-flufl.lock
Version:        7.0
Release:        0
Summary:        NFS-safe file locking with timeouts for POSIX and Windows
License:        Apache-2.0
URL:            https://gitlab.com/warsaw/flufl.lock
Source:         https://files.pythonhosted.org/packages/source/f/flufl.lock/flufl.lock-%{version}.tar.gz
BuildRequires:  %{python_module pdm}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module typing_extensions}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-atpublic
Requires:       python-psutil
Requires:       python-typing_extensions
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module atpublic}
BuildRequires:  %{python_module importlib-metadata}
BuildRequires:  %{python_module psutil}
BuildRequires:  %{python_module pytest-cov}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module six}
BuildRequires:  %{python_module sybil}
# /SECTION
%python_subpackages

%description
NFS-safe file locking with timeouts for POSIX and Windows.

%prep
%autosetup -p1 -n flufl.lock-%{version}

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
%{python_sitelib}/flufl/lock*
%{python_sitelib}/flufl.lock-%{version}*info

%changelog
