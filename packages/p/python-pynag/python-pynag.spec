#
# spec file for package python-pynag
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


Name:           python-pynag
Version:        1.1.2
Release:        0
Summary:        Python modules for Nagios plugins and configuration
License:        GPL-2.0-or-later
Group:          Development/Languages/Python
URL:            http://pynag.org/
Source:         https://github.com/pynag/pynag/archive/pynag-%{version}-1.tar.gz
BuildRequires:  fdupes
BuildRequires:  git-core
BuildRequires:  python2-chardet
BuildRequires:  python2-mock
BuildRequires:  python2-pytest
BuildRequires:  python2-rpm-macros
BuildRequires:  python2-setuptools
BuildRequires:  python2-unittest2
BuildArch:      noarch

%description
Python modules and utilities for pragmatically handling Nagios configuration
file maintenance, status information, log file parsing and plug-in development.

%prep
%setup -q -n pynag-pynag-%{version}-1
sed -i -e '/^#!\//, 1d' pynag/Utils/importer.py

%build
%python2_build

%install
%python2_install
%fdupes %{buildroot}%{python_sitelib}

%check
# Fix deprecation warnings
sed -i 's|self.assertEquals|self.assertEqual|g' tests/*.py
# Init git
git config --global user.email "pynag-obs-tester@localhost"
git config --global user.name "pynag OBS tester"
# Don't run tests that have dependencies like a running live Nagios system
# that cannot satisfied in an OBS chroot environment
rm -f tests/test_utils.py
rm -f tests/test_model.py
rm -f tests/test_command.py
rm -f tests/test_parsers.py
rm -f tests/test_other.py
# Run tests
pytest tests

%files
%license LICENSE
%doc AUTHORS CHANGES README.md
%{_bindir}/pynag
%{python_sitelib}/*
%{_mandir}/man1/pynag.1%{?ext_man}

%changelog
