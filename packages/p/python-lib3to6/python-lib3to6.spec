#
# spec file for package python-lib3to6
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
Name:           python-lib3to6
Version:        202009.1044
Release:        0
Summary:        Module to compile Python 3.6+ code to Python 2.7+
License:        MIT
URL:            https://gitlab.com/mbarkhau/lib3to6
Source:         https://files.pythonhosted.org/packages/source/l/lib3to6/lib3to6-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-astor
Requires:       python-click
Requires:       python-pathlib2
Requires:       python-typing
Requires:       python-wheel
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module astor}
BuildRequires:  %{python_module click}
BuildRequires:  %{python_module pathlib2}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module typing}
# /SECTION
%python_subpackages

%description
A module to compile Python 3.6+ code to Python 2.7+.

%prep
%setup -q -n lib3to6-%{version}
sed -i '/typing/d' requirements/*
sed -i '1{/^#!/d}' src/lib3to6/__main__.py

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/lib3to6
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# Avoid Python 3.8 specific test cases to support Leap 15.x
%pytest -k 'not (fixture7 or fixture17 or fixture53 or fixture54 or fixture55 or fixture56 or fixture57)'

%post
%python_install_alternative lib3to6

%postun
%python_uninstall_alternative lib3to6

%files %{python_files}
%doc CHANGELOG.md README.md
%license LICENSE
%python_alternative %{_bindir}/lib3to6
%{python_sitelib}/*

%changelog
