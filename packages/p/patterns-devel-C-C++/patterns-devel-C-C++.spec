#
# spec file for package patterns-devel-C-C++
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


%bcond_with betatest

Name:           patterns-devel-C-C++
Version:        20170319
Release:        0
Summary:        Patterns for Installation (C/C++ devel pattern)
License:        MIT
Group:          Metapackages
URL:            https://github.com/openSUSE/patterns
Source0:        patterns-devel-C-C++-rpmlintrc

BuildRequires:  patterns-rpm-macros
BuildArch:      noarch

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

#
# Ensure openSUSE users will have a functional development environment.
# Hard require gcc-c++ and libstdc++-devel as they are only soft required by
# devel_basis Pattern.
#
Requires:       gcc-c++
Requires:       libstdc++-devel

Recommends:     boost-devel
Recommends:     boost-jam
Recommends:     glibc-info
Recommends:     ltrace
Recommends:     posix_cc
Recommends:     swig
Recommends:     valgrind
# 403368
Suggests:       dejagnu
Suggests:       expect

%description devel_C_C++
Tools and libraries for software development using C/C++ and other derivative
of the C programming language.

%files devel_C_C++
%dir %{_defaultdocdir}/patterns/
%{_defaultdocdir}/patterns/devel_C_C++.txt

################################################################################

%prep

%build

%install
mkdir -p %{buildroot}%{_defaultdocdir}/patterns
echo 'This file marks the pattern devel_C_C++ to be installed.' \
    > %{buildroot}%{_defaultdocdir}/patterns/devel_C_C++.txt

%changelog
