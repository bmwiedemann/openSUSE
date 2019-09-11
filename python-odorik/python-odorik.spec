#
# spec file for package python-odorik
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-odorik
Version:        0.5
Release:        0
Summary:        Python module for Odorik API
License:        GPL-3.0-or-later
Group:          Development/Languages/Python
URL:            http://cihar.com/software/odorik/
Source:         https://files.pythonhosted.org/packages/source/o/odorik/odorik-%{version}.tar.bz2
BuildRequires:  %{python_module Sphinx}
BuildRequires:  %{python_module httpretty}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module python-dateutil}
BuildRequires:  %{python_module pyxdg}
BuildRequires:  fdupes
BuildRequires:  python
BuildRequires:  python-rpm-macros
Requires:       python-python-dateutil
Requires:       python-xdg
BuildArch:      noarch
%python_subpackages

%description
Python module to work with Odorik API.

%prep
%setup -q -n odorik-%{version}

%build
%python_build
make %{?_smp_mflags} -C docs man

%install
%python_install
install -d %{buildroot}%{_mandir}/man1
install -m 644 docs/_build/man/odorik.1 %{buildroot}%{_mandir}/man1
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_expand py.test-%{$python_version} odorik

%files %{python_files}
%license LICENSE
%doc NEWS.rst README.rst
%{python_sitelib}/*
%python3_only %{_mandir}/man1/*
%python3_only %{_bindir}/*

%changelog
