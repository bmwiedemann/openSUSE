#
# spec file for package patterns-devel-python
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           patterns-devel-python
Version:        20180125
Release:        0
Summary:        Patterns for Installation (Python devel)
License:        MIT
Group:          Metapackages
Url:            https://github.com/openSUSE/patterns
Source0:        %{name}-rpmlintrc
BuildRequires:  patterns-rpm-macros

%description
This is an internal package that is used to create the patterns as part
of the installation source setup.  Installation of this package does
not make sense.

This particular package contains all the python patterns.

%package devel_python3
%pattern_development
Summary:        Python 3 Developement
Group:          Metapackages
Provides:       pattern() = devel_python3
Provides:       pattern-icon() = pattern-python-devel
Provides:       pattern-order() = 3359
Provides:       pattern-visible()
Recommends:     python3
Recommends:     python3-devel
Recommends:     python3-flake8
Recommends:     python3-pip
Recommends:     python3-pytest
Recommends:     python3-requests
Recommends:     python3-setuptools
Recommends:     python3-tox
Recommends:     python3-virtualenv

%description devel_python3

%files devel_python3
%dir %{_docdir}/patterns
%{_docdir}/patterns/devel_python3.txt

%prep
:

%build
:

%install
mkdir -p %{buildroot}%{_docdir}/patterns/
echo 'This file marks the pattern devel_python3 to be installed.' > %{buildroot}%{_docdir}/patterns/devel_python3.txt

%changelog
