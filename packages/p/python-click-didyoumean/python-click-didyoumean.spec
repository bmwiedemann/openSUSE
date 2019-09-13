#
# spec file for package python-click-didyoumean
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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
Name:           python-click-didyoumean
Version:        0.0.3
Release:        0
Summary:        Plugin to enable git-like did-you-mean feature in python-click
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/timofurrer/click-didyoumean
Source:         https://github.com/click-contrib/click-didyoumean/archive/v%{version}.tar.gz#/click-didyoumean-%{version}.tar.gz
# https://github.com/click-contrib/click-didyoumean/pull/4
Patch0:         update-tests.patch
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-click
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module click}
BuildRequires:  %{python_module pytest}
# /SECTION
%python_subpackages

%description
This package enables a git-like did-you-mean feature in click.

%prep
%setup -q -n click-didyoumean-%{version}
%patch0 -p1

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_expand PYTHONPATH=%{buildroot}%{$python_sitelib} $python -m pytest

%files %{python_files}
%doc README.rst
%{python_sitelib}/*

%changelog
