#
# spec file for package python-agate-stats
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


Name:           python-agate-stats
Version:        0.4.0
Release:        0
License:        MIT
Summary:        Additional statistical methods for agate
URL:            http://agate-stats.readthedocs.org/
Group:          Development/Languages/Python
Source:         https://github.com/wireservice/agate-stats/archive/refs/tags/%{version}.tar.gz#/agate-stats-%{version}.tar.gz
# https://github.com/wireservice/agate-stats/compare/0.4.0...master.diff
Patch0:         python-agate-stats-remove-mysterious-line.patch
# https://github.com/wireservice/agate-stats/issues/18
Patch1:         python-agate-stats-no-six.patch
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module agate >= 1.5.0}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module six >= 1.6.1}
# /SECTION
Requires:       python-agate >= 1.5.0
Requires:       python-six >= 1.6.1
BuildArch:      noarch

%python_subpackages

%description
Agate-stats adds statistical methods to agate.

%prep
%setup -q -n agate-stats-%{version}
%autopatch -p1
sed -i -e '/^#!\//, 1d' agatestats/*.py

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%defattr(-,root,root,-)
%doc README.rst
%license COPYING
%{python_sitelib}/agate_stats*
%{python_sitelib}/agatestats*

%changelog
