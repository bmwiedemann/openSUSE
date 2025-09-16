#
# spec file for package snallygaster
#
# Copyright (c) 2025 SUSE LLC and contributors
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
Version:        0.0.14
Release:        0
Summary:        Tool to scan for hidden files on HTTP servers
License:        0BSD
Group:          Development/Languages/Python
URL:            https://github.com/hannob/snallygaster
Source:         https://files.pythonhosted.org/packages/source/s/snallygaster/snallygaster-%{version}.tar.gz
Source1:        https://github.com/hannob/snallygaster-testdata/archive/refs/heads/master.tar.gz#/testdata.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  python3-setuptools
# SECTION test requirements
BuildRequires:  python3-pytest
BuildRequires:  python3-base >= 3.9
BuildRequires:  python3-dnspython
BuildRequires:  python3-lxml
BuildRequires:  python3-urllib3
# /SECTION
BuildRequires:  fdupes
Requires:       python3-base >= 3.9
Requires:       python3-dnspython
Requires:       python3-lxml
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

%build
%python3_build

%install
%python3_install
fdupes %{buildroot}%{python_sitelib}

%check
# remove tests irrelevant for us
rm tests/test_codingstyle.py tests/test_docs.py
export TESTDATA_REPOSITORY=$(pwd)/snallygaster-testdata-master/
export RUN_ONLINETESTS=1
PYTHONPATH=${PYTHONPATH:+$PYTHONPATH:}%BUILDROOT%{python3_sitelib}/snallygaster/ PYTHONDONTWRITEBYTECODE=1 pytest -v tests/

%files
%doc README.md
%license LICENSE
%{_bindir}/snallygaster
%{python3_sitelib}/snallygaster-%{version}*-info

%changelog
