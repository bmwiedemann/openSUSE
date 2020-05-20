#
# spec file for package python-pycha
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
Name:           python-pycha
Version:        0.8.1
Release:        0
Summary:        A library for making charts with Python
License:        LGPL-3.0-or-later
Group:          Development/Languages/Python
URL:            https://bitbucket.org/lgs/pycha/
Source:         https://files.pythonhosted.org/packages/source/p/pycha/pycha-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-cairocffi
Requires:       python-six
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module cairocffi}
BuildRequires:  %{python_module six}
# /SECTION
%python_subpackages

%description
Pycha is a Python package for drawing charts using the Cairo library.
It will not try to draw any possible chart on Earth, but draw the
most common ones nicely. Pycha is based on the Plotr which is based on
PlotKit, both of which are written in JavaScript and are for client
web programming. Pycha was developed for the server side.

%prep
%setup -q -n pycha-%{version}

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/chavier
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%post
%python_install_alternative chavier

%postun
%python_uninstall_alternative chavier

%files %{python_files}
%doc README.txt CHANGES.txt AUTHORS
%license COPYING
%{python_sitelib}/*
%python_alternative %{_bindir}/chavier

%changelog
