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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif
# in order to avoid rewriting for subpackage generator
%define mypython python
%global skip_python2 1
Name:           python-packaging%{psuffix}
Version:        21.3
Release:        0
Summary:        Core utilities for Python packages
License:        Apache-2.0
URL:            https://github.com/pypa/packaging
Source:         https://files.pythonhosted.org/packages/source/p/packaging/packaging-%{version}.tar.gz
# Restore compatibility with 20.4 for setuptools
Patch1:         no-legacyversion-warning.patch
# Fix testsuite on big-endian systems
# see: https://github.com/pypa/packaging/pull/538
Patch2:         fix-big-endian-build.patch
BuildRequires:  %{python_module devel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
#!BuildIgnore:  post-build-checks-malwarescan
Requires:       python-pyparsing >= 2.0.2
BuildArch:      noarch
# do not add setuptools dependency, this is now a dependency
# of setuptools. Ensure that all dependencies also don't depend
# on setuptools
# (at the moment, six and pyparsing are ok)
%if %{with test}
BuildRequires:  %{python_module pretend}
BuildRequires:  %{python_module pyparsing >= 2.0.2}
BuildRequires:  %{python_module pytest}
%endif
# work around boo#1186870
Provides:       %{mypython}%{python_version}dist(packaging) = %{version}-%{release}
%if "%{python_flavor}" == "python3" || "%{python_provides}" == "python3"
Provides:       %{mypython}3dist(packaging) = %{version}-%{release}
%endif
%python_subpackages

%description
Core utilities for Python packages

%prep
%autosetup -p1 -n packaging-%{version}
# sdist must provide a packaging.egg-info, used below in install phase
test -d packaging.egg-info

%build
%python_build

%if %{with test}
%check
%if "%{python_flavor}" >= "python362"
# no-legacyversion-warning.patch causes these to fail
%pytest -k "not (test_legacy_specifier_is_deprecated or test_legacy_version_is_deprecated)"
%endif
%endif # %%{with_test}

%if !%{with test}
%install
%python_install
# Replace distutils generated egg-info, which varies in metadata version and
# structure (single file vs directory) based on distutils, with the egg-info
# which is provided in the sdist and uses same metadata version as setuptools.
%{python_expand rm -r %{buildroot}%{$python_sitelib}/*.egg-info
cp -r packaging.egg-info %{buildroot}%{$python_sitelib}/packaging-%{version}-py%{$python_version}.egg-info
}
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%license LICENSE LICENSE.APACHE LICENSE.BSD
%doc CHANGELOG.rst README.rst
%{python_sitelib}/packaging
%{python_sitelib}/packaging-%{version}-py*.egg-info/

%endif # !%%{with_test}

%changelog
