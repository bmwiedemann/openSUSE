#
# spec file for package python-leather
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


Name:           python-leather
Version:        0.3.4
Release:        0
Summary:        Python charting for 80% of humans
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/wireservice/leather
Source:         https://github.com/wireservice/leather/archive/%{version}.tar.gz#/leather-0.3.4-gh.tar.gz
# https://github.com/wireservice/leather/commit/9238eb5f4603496b61fc1c1dabad805ca5380b71
Patch0:         python-leather-no-python2.patch
BuildRequires:  %{python_module lxml >= 3.6.0}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
Leather is the Python charting library for those who need charts *now*
and don't care if they're perfect.

%prep
%autosetup -p1 -n leather-%{version}

%build
find leather -name '*.py' -exec sed -i -e '/^#!\//, 1d' {} \;
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# this testcase is in git but does not work
rm test.py
%pytest

%files %{python_files}
%doc README.rst
%license COPYING
%{python_sitelib}/leather
%{python_sitelib}/leather-%{version}*-info

%changelog
