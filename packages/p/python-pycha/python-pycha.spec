#
# spec file for package python-pycha
#
# Copyright (c) 2024 SUSE LLC
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


%{?sle15_python_module_pythons}
Name:           python-pycha
Version:        0.8.1
Release:        0
Summary:        A library for making charts with Python
License:        LGPL-3.0-or-later
URL:            https://github.com/timesong/pycha
Source:         https://files.pythonhosted.org/packages/source/p/pycha/pycha-%{version}.tar.gz
# is safe_unicode() needed at all?
Patch0:         python-pycha-no-six.patch
# PATCH-FIX-OPENSUSE remove makeSuite calls
Patch1:         remove-makesuite.patch
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-cairocffi
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module cairocffi}
BuildRequires:  %{python_module pytest}
# /SECTION
%python_subpackages

%description
Pycha is a Python package for drawing charts using the Cairo library.
It will not try to draw any possible chart on Earth, but draw the
most common ones nicely. Pycha is based on the Plotr which is based on
PlotKit, both of which are written in JavaScript and are for client
web programming. Pycha was developed for the server side.

%prep
%autosetup -p1 -n pycha-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/chavier
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%post
%python_install_alternative chavier

%postun
%python_uninstall_alternative chavier

%check
%pytest tests/*.py

%files %{python_files}
%doc README.txt CHANGES.txt AUTHORS
%license COPYING
%{python_sitelib}/pycha
%{python_sitelib}/pycha-%{version}.dist-info
%{python_sitelib}/chavier
%python_alternative %{_bindir}/chavier

%changelog
