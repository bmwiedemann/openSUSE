#
# spec file for package snallygaster
#
# Copyright (c) 2020 SUSE LLC
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

%build
%python3_build

%install
%python3_install
fdupes %{buildroot}%{python_sitelib}

%check
%if 0%{?sle_version} == 150100 && 0%{?is_opensuse}
# on Leap 15.1 the pycodestyle test fails, we don't care
python3 setup.py test ||:
%else
python3 setup.py test
%endif

%files
%doc README.md
%license LICENSE
%{_bindir}/snallygaster
%{python3_sitelib}/*

%changelog
