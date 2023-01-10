#
# spec file for package python-scikit-hep-testdata
#
# Copyright (c) 2023 SUSE LLC
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


%define srcname scikit-hep-testdata
%define modname %( echo %{srcname} | tr '-' '_' )
Name:           python-scikit-hep-testdata
Version:        0.4.26
Release:        0
Summary:        Example HEP files for testing and demonstrating
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/scikit-hep/scikit-hep-testdata
Source:         https://github.com/scikit-hep/scikit-hep-testdata/archive/v%{version}.tar.gz#/%{srcname}-%{version}.tar.gz
# PATCH-FEATURE-OPENSUSE scikit-hep-testdata-datadir.patch -- change the install location of the datadir code@bnavigator.de
Patch1:         scikit-hep-testdata-datadir.patch
BuildRequires:  %{python_module PyYAML}
BuildRequires:  %{python_module importlib-resources >= 1.3 if %python-base < 3.9}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module toml}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# SECTION Test requirements
BuildRequires:  %{python_module pytest}
# /SECTION
Requires:       python-PyYAML
Requires:       python-requests
%if %python_version_nodots < 39
Requires:       python-importlib-resources >= 1.3
%endif
Requires:       scikit-hep-testdata-files = %{version}
Requires(post): update-alternatives
Requires(postun):update-alternatives
BuildArch:      noarch
%python_subpackages

%description
A common package to provide example files (*e.g*. ROOT) for testing and
developing packages against.  The sample of files is representative of typical
files found "in the wild".

In addition to including some root files directly, this package adds some
simple helper methods to get larger files from common open-access data
repositories.

%package -n scikit-hep-testdata-files
Summary:        Example HEP files for testing and demonstrating - common file package

%description -n scikit-hep-testdata-files
A common package to provide example files (*e.g*. ROOT) for testing and
developing packages against.  The sample of files is representative of typical
files found "in the wild".

In addition to including some root files directly, this package adds some
simple helper methods to get larger files from common open-access data
repositories.

This subpackage contains the data files for all python flavors.

%prep
%autosetup -p1 -n %{srcname}-%{version}

%build
# GH source doesn't allow proper detection of version: https://github.com/scikit-hep/scikit-hep-testdata/issues/40
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%python_build

%install
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%python_clone -a %{buildroot}%{_bindir}/scikit-hep-testdata
%python_clone -a %{buildroot}%{_bindir}/skhep-testdata
install -D -m 644 -t %{buildroot}%{_datadir}/scikit-hep-testdata/data src/skhep_testdata/data/*
%fdupes %{buildroot}%{_datadir}/scikit-hep-testdata

%check
export SKHEP_DATA_DIR=%{buildroot}%{_datadir}/scikit-hep-testdata
%pytest

%post
%python_install_alternative scikit-hep-testdata
%python_install_alternative skhep-testdata

%postun
%python_uninstall_alternative scikit-hep-testdata
%python_uninstall_alternative skhep-testdata

%files %{python_files}
%license LICENSE
%doc README.md
%python_alternative %{_bindir}/scikit-hep-testdata
%python_alternative %{_bindir}/skhep-testdata
%{python_sitelib}/skhep_testdata/
%{python_sitelib}/%{modname}-%{version}-py%{python_version}.egg-info/

%files -n scikit-hep-testdata-files
%license LICENSE
%{_datadir}/scikit-hep-testdata

%changelog
