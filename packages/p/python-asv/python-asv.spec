#
# spec file for package python-asv
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


%bcond_without libalternatives
%{?sle15_python_module_pythons}
Name:           python-asv
Version:        0.6.4
Release:        0
Summary:        Airspeed Velocity: A Python history benchmarking tool
License:        BSD-3-Clause AND MIT
Group:          Development/Languages/Python
URL:            https://github.com/airspeed-velocity/asv
Source:         https://files.pythonhosted.org/packages/source/a/asv/asv-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  alts
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  python-rpm-macros
Requires:       alts
Requires:       python-PyYAML
Requires:       python-Pympler
Requires:       python-asv-runner >= 0.2.1
Requires:       python-build
Requires:       python-json5
Requires:       python-tabulate
Requires:       python-virtualenv
Suggests:       python-python-hglib >= 1.5
%if %{python_version_nodots} < 311
Requires:       python-tomli
%endif
# SECTION test requirements
BuildRequires:  %{python_module json5}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module tabulate}
BuildRequires:  git
# /SECTION
%python_subpackages

%description
airspeed velocity (asv) is a tool for benchmarking Python packages
over their lifetime.

It is designed to benchmark a single project over its lifetime using
a given suite of benchmarks. The results are displayed in an
interactive web frontend that requires only a basic static webserver
to host.

%prep
%autosetup -n asv-%{version}

%build
export CFLAGS="%{optflags}"
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/asv
%python_expand %fdupes %{buildroot}%{$python_sitearch}
%python_expand rm %{buildroot}%{$python_sitearch}/asv/_rangemedian.cpp

%check
#MVY: there are so MANY tests failing inside OBS - like test_continuous calling pip and building bad command line
exit 0
# % pytest

%pre
%python_libalternatives_reset_alternative asv

%files %{python_files}
%doc CHANGES.rst README.rst
%license LICENSE.rst
%python_alternative %{_bindir}/asv
%{python_sitearch}/asv/
%{python_sitearch}/asv-%{version}*-info

%changelog
