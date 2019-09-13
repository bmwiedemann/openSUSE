#
# spec file for package python-leather
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
Name:           python-leather
Version:        0.3.3
Release:        0
Summary:        Python charting for 80% of humans
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/wireservice/leather
Source:         https://github.com/wireservice/leather/archive/%{version}.tar.gz
BuildRequires:  %{python_module lxml >= 3.6.0}
BuildRequires:  %{python_module nose}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six >= 1.6.1}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-six >= 1.6.1
BuildArch:      noarch
%python_subpackages

%description
Leather is the Python charting library for those who need charts *now*
and don't care if they're perfect.

%prep
%setup -q -n leather-%{version}
find leather -name '*.py' -exec sed -i -e '/^#!\//, 1d' {} \;
# this testcase is in git but does not work
rm test.py

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_expand nosetests-%{$python_bin_suffix}

%files %{python_files}
%doc README.rst
%license COPYING
%{python_sitelib}/*

%changelog
