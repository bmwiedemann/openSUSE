#
# spec file for package python-gprof2dot
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
Name:           python-gprof2dot
Version:        2024.6.6
Release:        0
Summary:        Script to generate a dot graph from the output of several profilers
License:        LGPL-3.0-or-later
URL:            https://github.com/jrfonseca/gprof2dot
Source:         https://files.pythonhosted.org/packages/source/g/gprof2dot/gprof2dot-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.8}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
%python_subpackages

%description
GProf2Dot.py is a Python script to convert the output from many
profilers into a dot graph.

%prep
%setup -q -n gprof2dot-%{version}
sed -i -e '/^#!\//, 1d' gprof2dot.py

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/gprof2dot
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%post
%python_install_alternative gprof2dot

%postun
%python_uninstall_alternative gprof2dot

%files %{python_files}
%license LICENSE.txt
%doc README.md
%python_alternative %{_bindir}/gprof2dot
%{python_sitelib}/gprof2dot.py
%pycache_only %{python_sitelib}/__pycache__/gprof2dot*
%{python_sitelib}/gprof2dot-%{version}.dist-info

%changelog
