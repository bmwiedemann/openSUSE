#
# spec file for package python-PyCondor
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
Name:           python-PyCondor
Version:        0.6.0
Release:        0
Summary:        Python utility for HTCondor
License:        MIT
URL:            https://github.com/jrbourbeau/pycondor
Source:         https://files.pythonhosted.org/packages/source/P/PyCondor/PyCondor-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  alts
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       alts
Requires:       python-click >= 7.0
BuildArch:      noarch
# SECTION For tests
BuildRequires:  %{python_module click >= 7.0}
BuildRequires:  %{python_module pytest}
# /SECTION
%python_subpackages

%description
PyCondor (Python HTCondor) is a tool to help build and submit workflows to HTCondor in a straight-forward manner with minimal hassle.

%prep
%setup -q -n PyCondor-%{version}
sed -Ei "1{/^#!\/usr\/bin\/env python/d}" pycondor/tests/example_script.py

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%python_clone -a %{buildroot}%{_bindir}/pycondor

%pre
# Removing old update-alternatives entries.
%python_libalternatives_reset_alternative pycondor

%check
# We cannot actually submit jobs, so disable these tests
%pytest -k 'not (test_monitor_file_raises or test_submit_file_raises)'

%files %{python_files}
%license LICENSE
%doc README.md
%python_alternative %{_bindir}/pycondor
%{python_sitelib}/pycondor/
%{python_sitelib}/[Pp]y[Cc]ondor-%{version}*-info/

%changelog
