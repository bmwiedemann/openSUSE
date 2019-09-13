#
# spec file for package python-agate-dbf
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
Name:           python-agate-dbf
Version:        0.2.1
Release:        0
Summary:        Read support for dbf files for agate
License:        MIT
Group:          Development/Languages/Python
Url:            http://agate-dbf.readthedocs.org/
# https://github.com/wireservice/agate-dbf/issues/4
Source:         https://github.com/wireservice/agate-dbf/archive/%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module agate >= 1.5.0}
BuildRequires:  %{python_module dbfread >= 2.0.5}
BuildRequires:  %{python_module nose}
# /SECTION
Requires:       python-agate >= 1.5.0
Requires:       python-dbfread >= 2.0.5
BuildArch:      noarch

%python_subpackages

%description
Agate-dbf adds read support for dbf files to agate.

%prep
%setup -q -n agate-dbf-%{version}
sed -i -e '/^#!\//, 1d' agatedbf/*.py

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_expand nosetests-%{$python_bin_suffix}

%files %{python_files}
%defattr(-,root,root,-)
%doc CHANGELOG.rst README.rst
%license COPYING
%{python_sitelib}/*

%changelog
