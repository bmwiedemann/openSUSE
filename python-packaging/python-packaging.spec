#
# spec file for package python-packaging
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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
Name:           python-packaging%{psuffix}
Version:        19.1
Release:        0
Summary:        Core utilities for Python packages
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/pypa/packaging
Source:         https://pypi.io/packages/source/p/packaging/packaging-%{version}.tar.gz
# FIXME: drop these patches on the next release after 19.1
Patch0:         0001-Fix-test-failures-test_linux_platforms_manylinux-for.patch
Patch1:         0002-Fix-check-for-64-bit-OS.patch
Patch2:         0003-Add-additional-test-to-get-100-branch-coverage.patch
Patch3:         0004-Fix-test_macos_version_detection-failure-on-32-bit-L.patch
Patch4:         0005-Drop-dependency-on-attrs.patch
BuildRequires:  %{python_module six}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-pyparsing >= 2.0.2
Requires:       python-six
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
%python_subpackages

%description
Core utilities for Python packages

%prep
%setup -q -n packaging-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
# sdist must provide a packaging.egg-info, used below in install phase
test -d packaging.egg-info

# FIXME: drop this on the next release after 19.1
sed -i '/^attrs/d' packaging.egg-info/requires.txt

%build
%python_build

%if %{with test}
%check
%pytest
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
