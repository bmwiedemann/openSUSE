#
# spec file for package python-pycha
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2016 Dr. Axel Braun
# Copyright (c) 2017 Oliver Kurz
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

%define         mod_name pycha
Name:           python-pycha
Version:        0.7.0
Release:        0
Summary:        A library for making charts with Python
License:        LGPL-3.0+
Group:          Development/Languages/Python
Url:            http://bitbucket.org/lgs/%{mod_name}/
Source:         https://pypi.io/packages/source/p/%{mod_name}/%{mod_name}-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  python-rpm-macros
BuildRequires:  fdupes
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch
%python_subpackages

%description
Pycha is a Python package for drawing charts using the Cairo library.
It will not try to draw any possible chart on Earth, but draw the
most common ones nicely. Pycha is based on the Plotr which is based on
PlotKit, both of which are written in JavaScript and are for client
web programming. Pycha was developed for the server side.

%prep
%setup -q -n %{mod_name}-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%doc README.txt CHANGES.txt AUTHORS
%license COPYING
%{python_sitelib}/*
%python3_only %{_bindir}/chavier

%changelog
