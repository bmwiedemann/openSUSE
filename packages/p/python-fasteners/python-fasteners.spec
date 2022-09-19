#
# spec file for package python-fasteners
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
%bcond_without python2
Name:           python-fasteners
Version:        0.17.3
Release:        0
Summary:        A python package that provides useful locks
License:        Apache-2.0
URL:            https://github.com/harlowja/fasteners
Source:         https://github.com/harlowja/fasteners/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}-gh.tar.gz
BuildRequires:  %{python_module diskcache}
BuildRequires:  %{python_module more-itertools}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module testtools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-more-itertools
Requires:       python-six
BuildArch:      noarch
%if %{with python2}
BuildRequires:  python-futures
%endif
%python_subpackages

%description
A python package that provides useful locks
It includes the following.
 * Locking decorator
 * Reader-writer locks
 * Inter-process locks
 * Generic helpers

%prep
%setup -q -n fasteners-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license LICENSE
%doc CHANGELOG README.md
%{python_sitelib}/*

%changelog
