#
# spec file for package python-semver
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


%bcond_without test
Name:           python-semver
Version:        3.0.0~dev.4
Release:        0
Summary:        Python helper for Semantic Versioning
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/python-semver/python-semver
Source:         https://github.com/python-semver/python-semver/archive/refs/tags/3.0.0-dev.4.tar.gz#/%{name}-3.0.0-dev.4-gh.tar.gz
# PATCH-FIX-UPSTREAM - setup-remove-asterisk.patch
Patch0:         https://github.com/python-semver/python-semver/pull/398.patch#/setup-remove-asterisk.patch
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires(post): update-alternatives
Requires(postun):update-alternatives
# See https://github.com/k-bx/python-semver/issues/67 for why conflicts is needed
Conflicts:      python-node-semver
BuildArch:      noarch
%python_subpackages

%description
A Python module for semantic versioning. Simplifies comparing versions.
See also http://semver.org/

%prep
%setup -q -n python-semver-3.0.0-dev.4
%patch0 -p1
sed -i '/-cov/d' setup.cfg

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/pysemver

%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%post
%python_install_alternative pysemver

%postun
%python_uninstall_alternative pysemver

%files %{python_files}
%doc README.rst
%{python_sitelib}/semver*
%python_alternative %{_bindir}/pysemver

%changelog
