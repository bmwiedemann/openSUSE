#
# spec file for package python-bugzilla
#
# Copyright (c) 2025 SUSE LLC
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


%define oldpython python
%bcond_without libalternatives
%{?sle15_python_module_pythons}
Name:           python-bugzilla
Version:        3.3.0
Release:        0
Summary:        Python library for Bugzilla
License:        GPL-2.0-or-later
Group:          Development/Libraries/Python
URL:            https://github.com/python-bugzilla/python-bugzilla
Source:         python-bugzilla-%{version}.tar
# PATCH-FIX-UPSTREAM 106-basic-auth.diff bsc#1098219 mcepl@suse.com
# Fix basic authentication on bugzilla.suse.com
Patch0:         106-basic-auth.diff
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module responses}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  alts
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       alts
Requires:       python-requests
Suggests:       osc
Conflicts:      %{oldpython}-bugzillatools
Obsoletes:      python2-bugzilla
Obsoletes:      python3-bugzilla
BuildArch:      noarch
%python_subpackages

%description
This is a Python module that provides a Python-ish interface to
Bugzilla over XMLRPC. It supports the Web Services provided by
upstream Bugzilla 3.0 and 3.2.

It also includes a 'bugzilla' commandline client which can be used for quick,
ad-hoc bugzilla jiggery-pokery.

%prep
%autosetup -p1

%build
sed -i -e '1{/^#!\/usr\/bin\/env python/d}' bugzilla/_cli.py

export CFLAGS="%{optflags}"
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/bugzilla
%python_clone -a %{buildroot}%{_mandir}/man1/bugzilla.1
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%pre
%python_libalternatives_reset_alternative bugzilla

%check
%pytest

%files %{python_files}
%doc NEWS.md
%python_alternative %{_bindir}/bugzilla
%python_alternative %{_mandir}/man1/bugzilla.1%{ext_man}
%{python_sitelib}/bugzilla
%{python_sitelib}/python_bugzilla-3.3.0*-info

%changelog
