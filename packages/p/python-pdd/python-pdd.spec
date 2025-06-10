#
# spec file for package python-pdd
#
# Copyright (c) 2025 SUSE LLC
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


%bcond_without libalternatives
# pdd is not available for Python 2
Name:           python-pdd
Version:        1.7
Release:        0
Summary:        Tiny date, time diff calculator with timers
License:        GPL-3.0-only
Group:          Development/Languages/Python
URL:            https://github.com/jarun/pdd
Source:         https://files.pythonhosted.org/packages/source/p/pdd/pdd-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  alts
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       alts
Requires:       python-python-dateutil
Requires:       python-setuptools
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module python-dateutil}
# /SECTION
%python_subpackages

%description
pdd (Python3 Date Diff) is a small cmdline utility to calculate date and time difference. It can also be used as a timer

%prep
%setup -q -n pdd-%{version}

%build
# this seems to be fixed in github (there is pdd instead of pdd.py,
# what setup.py expects, if I have not missed anything)
mv pdd.py pdd
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/pdd
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
chmod 755 pdd
%pytest test.py

%pre
%python_libalternatives_reset_alternative pdd

%files %{python_files}
%doc README.md CHANGELOG
%license LICENSE
%python_alternative %{_bindir}/pdd
%{python_sitelib}/pdd.py
%{python_sitelib}/pdd-%{version}*-info
%pycache_only %{python_sitelib}/__pycache__/pdd*

%changelog
