#
# spec file for package python-pygal
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
Name:           python-pygal
Version:        2.4.0
Release:        0
Summary:        A python svg graph plotting library
License:        LGPL-3.0-or-later
Group:          Development/Languages/Python
URL:            http://pygal.org/
Source:         https://files.pythonhosted.org/packages/source/p/pygal/pygal-%{version}.tar.gz
Source10:       https://raw.githubusercontent.com/Kozea/pygal/%{version}/COPYING
Patch0:         python38.patch
# PATCH-FIX-UPSTREAM pytest4.patch gh#Kozea/pygal#340 mcepl@suse.com
# yes, THIS is what makes this test suite pytest4+ compatible!
Patch1:         pytest4.patch
BuildRequires:  %{python_module Flask}
BuildRequires:  %{python_module lxml}
BuildRequires:  %{python_module pyquery}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  python3-CairoSVG
Requires:       python-lxml
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
%ifpython3
Recommends:     python-CairoSVG
%endif
# SECTION test requirements
BuildRequires:  %{python_module pytest-runner}
BuildRequires:  %{python_module pytest}
# /SECTION
%python_subpackages

%description
Pygal is a dynamic SVG charting library written in python.
It supports various chart types and CSS styling.

%prep
%setup -q -n pygal-%{version}
%autopatch -p1

cp %{SOURCE10} .

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

mv %{buildroot}%{_bindir}/pygal_gen.py %{buildroot}%{_bindir}/pygal_gen
%python_clone -a %{buildroot}%{_bindir}/pygal_gen

%check
%python_exec setup.py test

%post
%python_install_alternative pygal_gen

%postun
%python_uninstall_alternative pygal_gen

%files %{python_files}
%doc README
%license COPYING
%python_alternative %{_bindir}/pygal_gen
%{python_sitelib}/*

%changelog
