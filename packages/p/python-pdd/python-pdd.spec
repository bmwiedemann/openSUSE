#
# spec file for package python-pdd
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


# pdd is not available for Python 2
%define skip_python2 1
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-pdd
Version:        1.7
Release:        0
Summary:        Tiny date, time diff calculator with timers
License:        GPL-3.0-only
Group:          Development/Languages/Python
URL:            https://github.com/jarun/pdd
Source:         https://files.pythonhosted.org/packages/source/p/pdd/pdd-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-python-dateutil
Requires:       python-setuptools
Requires(post): update-alternatives
Requires(postun):update-alternatives
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
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/pdd
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
chmod 755 pdd
%pytest test.py

%post
%python_install_alternative pdd

%postun
%python_uninstall_alternative pdd

%files %{python_files}
%doc README.md CHANGELOG
%license LICENSE
%python_alternative %{_bindir}/pdd
%{python_sitelib}/*

%changelog
