#
# spec file for package python-rpmlb
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
Name:           python-rpmlb
Version:        1.1.1
Release:        0
Summary:        RPM List Builder
License:        GPL-2.0+
URL:            https://github.com/sclorg/rpm-list-builder
Source:         https://files.pythonhosted.org/packages/source/r/rpmlb/rpmlb-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module setuptools_scm}
# SECTION test requirements
BuildRequires:  %{python_module click}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module pytest-helpers-namespace}
BuildRequires:  %{python_module PyYAML}
BuildRequires:  %{python_module retry}
# /SECTION
BuildRequires:  fdupes
Requires:       python-click
Requires:       python-PyYAML
Requires:       python-retry
Suggests:       python-typing
BuildArch:      noarch
%python_subpackages

%description
RPM List Builder.

%prep
%setup -q -n rpmlb-%{version}
sed -i '/pytest-runner/d' setup.py

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/rpmlb
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# test_make_srpm_creates_srpm uses macros only works on CentOS/Fedora
# test_custom_build_hooks depends on executable
export LANG=en_US.UTF-8
%pytest -k 'not (test_make_srpm_creates_srpm or test_custom_build_hooks)'

%post
%python_install_alternative rpmlb

%postun
%python_uninstall_alternative rpmlb

%files %{python_files}
%doc README.rst
%license LICENSE
%python_alternative %{_bindir}/rpmlb
%{python_sitelib}/*

%changelog
