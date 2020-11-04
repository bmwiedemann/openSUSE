#
# spec file for package codespell
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


Name:           codespell
Version:        1.17.1
Release:        0
Summary:        Source code checker for common misspellings
License:        GPL-2.0-only
Group:          Development/Tools/Other
URL:            https://github.com/codespell-project/codespell/
Source0:        https://github.com/codespell-project/codespell/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch1:         help2man-run-needs-utf8-locale.patch
BuildRequires:  fdupes
BuildRequires:  help2man
BuildRequires:  python-rpm-macros
BuildRequires:  python3-chardet
BuildRequires:  python3-pytest
BuildRequires:  python3-setuptools
Requires:       python3-chardet
Requires:       python3-setuptools
BuildArch:      noarch

%description
codespell fixes common misspellings in text files. It primarily checks
misspelled words in source code, but it can be used with other files as well.

%prep
%setup -q
%autopatch

# remove config that requires pulling more pytest stuff
rm -f setup.cfg

%build
make %{?_smp_mflags} codespell.1
%python3_build

%check
# disable command test; does not work in chroot
export PATH=$PATH:%{buildroot}%{_bindir}
make %{?_smp_mflags} check-dictionary
python3 -m pytest -k 'not test_command'

%install
%python3_install
install -D -m644 codespell.1 %{buildroot}/%{_mandir}/man1/codespell.1
%fdupes %{buildroot}%{python3_sitelib}

%files
%license COPYING
%doc README.rst
%{_mandir}/man1/codespell.1%{?ext_man}
%{_bindir}/codespell
%{python3_sitelib}/codespell_lib
%{python3_sitelib}/%{name}-%{version}-py%{py3_ver}.egg-info

%changelog
