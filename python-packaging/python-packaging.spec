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
%bcond_with test
Name:           python-packaging
Version:        19.0
Release:        0
Summary:        Core utilities for Python packages
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/pypa/packaging
Source:         https://pypi.io/packages/source/p/packaging/packaging-%{version}.tar.gz
BuildRequires:  %{python_module six}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# https://github.com/pypa/packaging/issues/91
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
# sdist must provide a packaging.egg-info, used below in install phase
test -d packaging.egg-info

%build
%python_build

%install
%python_install
# Replace distutils generated egg-info, which varies in metadata version and
# structure (single file vs directory) based on distutils, with the egg-info
# which is provided in the sdist and uses same metadata version as setuptools.
%{python_expand rm -r %{buildroot}%{$python_sitelib}/*.egg-info
cp -r packaging.egg-info %{buildroot}%{$python_sitelib}/packaging-%{version}-py%{$python_version}.egg-info
}
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%if %{with test}
%check
%python_exec %{_bindir}/py.test
%endif

%files %{python_files}
%license LICENSE LICENSE.APACHE LICENSE.BSD
%doc CHANGELOG.rst README.rst
%{python_sitelib}/packaging
%{python_sitelib}/packaging-%{version}-py*.egg-info/

%changelog
