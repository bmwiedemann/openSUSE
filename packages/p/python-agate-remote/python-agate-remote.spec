#
# spec file for package python-agate-remote
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
Name:           python-agate-remote
Version:        0.2.1
Release:        0
License:        MIT
Summary:        Read support for remote files for agate
URL:            http://agate-remote.readthedocs.org/
Group:          Development/Languages/Python
Source:         https://github.com/wireservice/agate-remote/archive/refs/tags/%{version}.tar.gz#/agate-remote-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module agate >= 1.5.0}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests >= 2.9.1}
Requires:       python-agate >= 1.5.0
Requires:       python-requests >= 2.9.1
BuildArch:      noarch

%python_subpackages

%description
Agate-remote adds read support for remote files to agate.

%prep
%setup -q -n agate-remote-%{version}
sed -i -e '/^#!\//, 1d' agateremote/*.py

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# online tests only
#%%pytest

%files %{python_files}
%defattr(-,root,root,-)
%doc README.rst
%license COPYING
%{python_sitelib}/*

%changelog
