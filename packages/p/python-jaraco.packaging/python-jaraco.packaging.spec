#
# spec file for package python-jaraco.packaging
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


Name:           python-jaraco.packaging
Version:        9.1.2
Release:        0
Summary:        Supplement packaging Python releases
License:        MIT
URL:            https://github.com/jaraco/jaraco.packaging
Source:         https://files.pythonhosted.org/packages/source/j/jaraco.packaging/jaraco.packaging-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.7}
BuildRequires:  %{python_module build}
BuildRequires:  %{python_module importlib-metadata if %python-version < 3.8}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools >= 56}
BuildRequires:  %{python_module setuptools_scm >= 3.4.1}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# SECTION test and docs
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module Sphinx}
BuildRequires:  %{python_module rst.linker >= 1.9}
# /SECTION
Requires:       python-build
%if 0%{?python_version_nodots} < 38
Requires:       python-importlib-metadata
%endif
BuildArch:      noarch
%python_subpackages

%description
Tools to supplement packaging Python releases.

%prep
%setup -q -n jaraco.packaging-%{version}
rm -rf jaraco.packaging.egg-info

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

#%%check
# Upstream removed their test suite from the repository, only checking for correct typing and lint

%files %{python_files}
%license LICENSE
%doc docs/*.rst CHANGES.rst README.rst
%{python_sitelib}/jaraco.packaging-%{version}*-info
%dir %{python_sitelib}/jaraco
%{python_sitelib}/jaraco/packaging/

%changelog
