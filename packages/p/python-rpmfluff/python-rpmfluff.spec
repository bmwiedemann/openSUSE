#
# spec file for package python-rpmfluff
#
# Copyright (c) 2020 SUSE LLC
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
Name:           python-rpmfluff
Version:        0.6.1
Release:        0
Summary:        Lightweight way of building RPMs, and sabotaging them
License:        GPL-2.0-or-later
URL:            https://pagure.io/rpmfluff
Source:         https://files.pythonhosted.org/packages/source/r/rpmfluff/rpmfluff-%{version}.tar.gz
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module rpm}
BuildRequires:  %{python_module setuptools}
BuildRequires:  createrepo_c
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-rpm
Suggests:       createrepo_c
BuildArch:      noarch
%python_subpackages

%description
Lightweight way of building RPMs, and sabotaging them.

%prep
%setup -q -n rpmfluff-%{version}
rm rpmfluff/.*.py.swp

%build
export LANG=en_US.UTF-8
%python_build

%install
export LANG=en_US.UTF-8
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export LANG=en_US.UTF-8
%pytest -rs rpmfluff/test.py


%files %{python_files}
%doc README-releng README.md
%license LICENSE
%{python_sitelib}/*

%changelog
