#
# spec file for package snallygaster
#
# Copyright (c) 2021 SUSE LLC
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


Name:           snallygaster
Version:        0.0.9
Release:        0
Summary:        Tool to scan for hidden files on HTTP servers
License:        CC0-1.0
Group:          Development/Languages/Python
URL:            https://github.com/hannob/snallygaster
Source:         https://files.pythonhosted.org/packages/source/s/snallygaster/snallygaster-%{version}.tar.gz
Source1:        https://github.com/hannob/snallygaster-testdata/archive/refs/heads/master.tar.gz#/testdata.tar.gz
# PATCH-FIX-UPSTREAM fix-codestyle.patch -- fixes codestyle to pass pylint testcase
Patch0:         https://github.com/hannob/snallygaster/pull/58.patch#/fix-codestyle.patch
BuildRequires:  python-rpm-macros
BuildRequires:  python3-setuptools
# SECTION test requirements
BuildRequires:  python3-beautifulsoup4
BuildRequires:  python3-dnspython
BuildRequires:  python3-flake8
BuildRequires:  python3-pycodestyle
BuildRequires:  python3-pyflakes
BuildRequires:  python3-pylint
BuildRequires:  python3-pyupgrade
BuildRequires:  python3-urllib3
# /SECTION
BuildRequires:  fdupes
Requires:       python3-beautifulsoup4
Requires:       python3-dnspython
Requires:       python3-urllib3
BuildArch:      noarch

%description
A tool that looks for files accessible on web servers that shouldn't be public
and can pose a security risk.

Typical examples include publicly accessible git repositories, backup files
potentially containing passwords or database dumps. In addition, it contains
a few checks for other security vulnerabilities.

%prep
%setup -q -n snallygaster-%{version}
%setup -T -D -a 1
# -n snallygaster-testdata-master
mkdir snallygaster-testdata-master/.git/
echo '[core]' > snallygaster-testdata-master/.git/config
%patch0 -p1

%build
%python3_build

%install
%python3_install
fdupes %{buildroot}%{python_sitelib}

%check
rm tests/test_codingstyle.py
TESTDATA_REPOSITORY=$(pwd)/snallygaster-testdata-master/ RUN_ONLINETESTS=1 python3 setup.py test

%files
%doc README.md
%license LICENSE
%{_bindir}/snallygaster
%{python3_sitelib}/*

%changelog
