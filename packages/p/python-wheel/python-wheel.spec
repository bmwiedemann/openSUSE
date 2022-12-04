#
# spec file
#
# Copyright (c) 2022 SUSE LLC
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


%if 0%{?suse_version} > 1500
%bcond_without libalternatives
%else
%bcond_with libalternatives
%endif

%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif
Name:           python-wheel%{psuffix}
Version:        0.38.4
Release:        0
Summary:        A built-package format for Python
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/pypa/wheel
Source:         https://github.com/pypa/wheel/archive/%{version}.tar.gz#/wheel-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.7}
BuildRequires:  %{python_module setuptools >= 45.2.0}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros >= 20210929
Requires:       python-setuptools >= 45.2.0
%if %{with libalternatives}
Requires:       alts
BuildRequires:  alts
%else
Requires(post): update-alternatives
Requires(postun):update-alternatives
%endif
BuildArch:      noarch
%if %{with test}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pytest >= 3.0.0}
BuildRequires:  %{python_module wheel >= %{version}}
%endif
%python_subpackages

%description
A built-package format for Python.

A wheel is a ZIP-format archive with a specially formatted filename
and the .whl extension. It is designed to contain all the files for a
PEP 376 compatible install in a way that is very close to the on-disk
format. Many packages will be properly installed with only the "Unpack"
step (simply extracting the file onto sys.path), and the unpacked archive
preserves enough information to "Spread" (copy data and scripts to their
final locations) at any later time.

%prep
%setup -q -n wheel-%{version}
# Remove addopts as it requires pytest-cov
sed -i '/addopts = /d' setup.cfg

%build
%python_build

%install
%if !%{with test}
%python_install
%python_clone -a %{buildroot}%{_bindir}/wheel
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%check
%if %{with test}
export LC_ALL=en_US.utf8
export PYTHONDONTWRITEBYTECODE=1
%pytest
%endif

%if !%{with test}

%pre
# If libalternatives is used: Removing old update-alternatives entries.
%python_libalternatives_reset_alternative wheel

%post
%python_install_alternative wheel

%postun
%python_uninstall_alternative wheel

%files %{python_files}
%doc docs/news.rst README.rst
%license LICENSE.txt
%python_alternative %{_bindir}/wheel
%{python_sitelib}/wheel-%{version}*-info
%{python_sitelib}/wheel/
%endif

%changelog
