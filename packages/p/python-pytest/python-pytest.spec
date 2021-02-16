#
# spec file for package python
#
# Copyright (c) 2021 SUSE LLC
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
%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -%{flavor}
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif
%define skip_python2 1
Name:           python-pytest%{psuffix}
Version:        6.2.2
Release:        0
Summary:        Simple powerful testing with Python
License:        MIT
URL:            https://github.com/pytest-dev/pytest
Source:         https://files.pythonhosted.org/packages/source/p/pytest/pytest-%{version}.tar.gz
BuildRequires:  %{python_module setuptools >= 42.0}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module toml}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-attrs >= 19.2.0
Requires:       python-importlib-metadata >= 0.12
Requires:       python-iniconfig
Requires:       python-packaging
Requires:       python-pluggy >= 0.12
Requires:       python-py >= 1.8.2
Requires:       python-setuptools
Requires:       python-toml
Requires:       python-wcwidth
Requires(post): update-alternatives
Requires(postun): update-alternatives
Obsoletes:      python-pytest-doc
BuildArch:      noarch
%if %{with test}
BuildRequires:  %{python_module Jinja2}
BuildRequires:  %{python_module Twisted}
BuildRequires:  %{python_module decorator}
BuildRequires:  %{python_module hypothesis >= 3.56}
# nose is really not REQUIRED, the test suite skips over particular
# tests, when the package is not available.
# BuildRequires:  %%{python_module nose}
BuildRequires:  %{python_module numpy if (%python-base without python36-base)}
BuildRequires:  %{python_module pexpect}
BuildRequires:  %{python_module pygments-pytest}
BuildRequires:  %{python_module pytest >= %{version}}
BuildRequires:  %{python_module pytest-xdist}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module xmlschema}
BuildRequires:  lsof
%endif
%if %{?python_version_nodots} < 36
Requires:       python-pathlib2 >= 2.2.0
%endif
%python_subpackages

%description
The pytest framework makes it easy to write small tests, yet scales to support
complex functional testing for applications and libraries.

%prep
%setup -q -n pytest-%{version}
# fix gh#pytest-dev/pytest#7891 still happening for Leap
sed -i '/^\[metadata\]/ a version = %{version}' setup.cfg

%build
%python_build

%install
%if ! %{with test}
%python_install
%python_clone -a %{buildroot}%{_bindir}/pytest
%python_clone -a %{buildroot}%{_bindir}/py.test
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%check
%if %{with test}
%pytest
%endif

%if ! %{with test}
%post
# py.test was the master until Oct 2020. boo#1178547
alternatives=$(update-alternatives --quiet --list py.test 2> /dev/null) && (
  update-alternatives --remove-all py.test
  # reinstall group with new master for all existing flavors except ourself
  for a in $alternatives; do
    if [ $a != %{_bindir}/py.test-%{python_bin_suffix} ]; then
      bin_suffix=${a##*-}
      prio=${bin_suffix/./}
      update-alternatives --quiet --install %{_bindir}/pytest pytest ${a/py.test/pytest} $prio \
         --slave %{_bindir}/py.test py.test $a
    fi
  done
) ||:
%python_install_alternative pytest py.test

%postun
%python_uninstall_alternative pytest

%files %{python_files}
%doc AUTHORS CHANGELOG.rst README.rst
%license LICENSE
%python_alternative %{_bindir}/pytest
%python_alternative %{_bindir}/py.test
%{python_sitelib}/_pytest
%{python_sitelib}/pytest
%{python_sitelib}/pytest-%{version}*-info
%endif

%changelog
