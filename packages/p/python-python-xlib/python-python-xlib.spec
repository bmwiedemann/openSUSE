#
# spec file for package python-python-xlib
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
%define         oldpython python
Name:           python-python-xlib
Version:        0.29
Release:        0
Summary:        Python X11 interface
License:        LGPL-2.1-or-later
Group:          Development/Libraries/Python
URL:            https://github.com/python-xlib/python-xlib
Source:         https://files.pythonhosted.org/packages/source/p/python-xlib/python-xlib-%{version}.tar.gz
# PATCH-FEATURE-UPSTREAM remove-mock.patch -- gh#python-xlib/python-xlib#186
Patch0:         remove-mock.patch
BuildRequires:  %{python_module pytest-xvfb}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six >= 1.10.0}
%if 0%{suse_version} < 1550
BuildRequires:  python-mock
%endif
BuildRequires:  dos2unix
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-six >= 1.10.0
BuildArch:      noarch
Provides:       python-xlib = %{version}
Obsoletes:      python-xlib < %{version}
%ifpython2
Provides:       %{oldpython}-xlib = %{version}
Obsoletes:      %{oldpython}-xlib < %{version}
%endif
%python_subpackages

%description
The Python X Library is intended to be a fully functional X client
library for Python programs.

%prep
%setup -q -n python-xlib-%{version}
dos2unix CHANGELOG.md README.rst TODO dev-requirements.txt test/*
# patch only applies to unix endings
%patch0 -p1

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest -rs

%files %{python_files}
%license LICENSE
%doc CHANGELOG.md README.rst TODO
%{python_sitelib}/Xlib/
%{python_sitelib}/python_xlib-*

%changelog
