#
# spec file for package patterns-devel-C-C++
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


%bcond_with betatest

Name:           patterns-devel-C-C++
Version:        20170319
Release:        0
Summary:        Patterns for Installation (C/C++ devel pattern)
License:        MIT
Group:          Metapackages
Url:            https://github.com/openSUSE/patterns
Source0:        %{name}-rpmlintrc
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  patterns-rpm-macros

%description
This is an internal package that is used to create the patterns as part
of the installation source setup.  Installation of this package does
not make sense.

This particular package contains the C and C++ development patterns.

################################################################################

%package devel_C_C++
%pattern_development
Summary:        C/C++ Development
Group:          Metapackages
Provides:       pattern() = devel_C_C++
Provides:       pattern-icon() = pattern-c-devel
Provides:       pattern-order() = 3240
Provides:       pattern-visible()
Requires:       pattern() = devel_basis

Recommends:     glibc-info
Recommends:     boost-devel
Recommends:     boost-jam
Recommends:     posix_cc
Recommends:     swig
Recommends:     valgrind
Recommends:     ltrace
# 403368
Suggests:       dejagnu
Suggests:       expect

%description devel_C_C++
Tools and libraries for software development using C/C++ and other derivative of the C programming language.

%files devel_C_C++
%dir /usr/share/doc/packages/patterns
/usr/share/doc/packages/patterns/devel_C_C++.txt

################################################################################

%prep

%build

%install
mkdir -p $RPM_BUILD_ROOT/usr/share/doc/packages/patterns
echo 'This file marks the pattern devel_C_C++ to be installed.' > $RPM_BUILD_ROOT/usr/share/doc/packages/patterns/devel_C_C++.txt

%changelog
