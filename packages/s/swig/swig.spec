#
# spec file for package swig
#
# Copyright (c) 2026 SUSE LLC and contributors
# Copyright (c) 2025 Andreas Stieger <Andreas.Stieger@gmx.de>
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


%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
# This flavour packages nothing -- it exists only to run the test suite --
# so do not leave a swig-test-debugsource behind either.
%global debug_package %{nil}
%else
%define psuffix %{nil}
%bcond_with test
%endif
# %%{name} carries the flavour suffix, so everything naming the upstream
# project -- sources, docdir, the unpacked tree -- goes through %%{origname}.
%define origname swig

%if 0%{?fedora} + 0%{?rhel_version} + 0%{?centos_version} > 0
%define docpath %{_docdir}/%{origname}-%{version}
BuildRequires:  perl-Test-Simple
BuildRequires:  perl-devel
%if 0%{?centos_version} < 800
BuildRequires:  ruby
%endif
%endif
%if 0%{?suse_version} > 0
%define docpath %{_docdir}/%{origname}
%if %{with test}
BuildRequires:  ruby-devel
%endif
%endif
Name:           %{origname}%{psuffix}
Version:        4.5.1
Release:        0
Summary:        Simplified Wrapper and Interface Generator
License:        BSD-3-Clause AND GPL-3.0-or-later
Group:          Development/Languages/C and C++
URL:            https://www.swig.org/
Source:         https://prdownloads.sourceforge.net/%{origname}/%{origname}-%{version}.tar.gz
Source1:        %{origname}.rpmlintrc
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  bison >= 3.5
BuildRequires:  fdupes
BuildRequires:  libtool
BuildRequires:  pcre2-devel
BuildRequires:  perl
BuildRequires:  pkgconfig
%if 0%{?suse_version} < 1600
BuildRequires:  gcc12
BuildRequires:  gcc12-c++
%else
BuildRequires:  gcc
BuildRequires:  gcc-c++
%endif
# Python, Ruby and Boost are needed ONLY to compile and run the generated
# bindings in the test suite -- swig itself is a C++ program that emits source
# code and links nothing but pcre2 (Debian builds it with none of these).
# Keeping them out of the default flavour also stops swig being rebuilt every
# time the python, ruby or boost stacks move.
%if %{with test}
%if 0%{?centos_version} >= 800
BuildRequires:  boost-devel
BuildRequires:  python3-devel
BuildRequires:  python3-tools
%else
%if 0%{?suse_version} >= 1500
BuildRequires:  libboost_headers-devel
BuildRequires:  python3-devel
BuildRequires:  python3-tools
%else
BuildRequires:  boost-devel
BuildRequires:  python-devel > 2.6
%endif
%endif
%endif

%description
SWIG is a compiler that attempts to make it easy to integrate C, C++,
or Objective-C code with scripting languages including Perl, Tcl, and
Python.  In a nutshell, you give it a bunch of ANSI C/C++ declarations
and it generates an interface between C and your favorite scripting
language.  However, this is only scratching the surface of what SWIG
can do--some of its more advanced features include automatic
documentation generation, module and library management, extensive
customization options, and more.

%if %{without test}
%package doc
Summary:        SWIG Manual
License:        BSD-3-Clause
Group:          Documentation/Man
Requires:       swig
BuildArch:      noarch

%description doc
SWIG is a compiler that attempts to make it easy to integrate C, C++,
or Objective-C code with scripting languages including Perl, Tcl, and
Python.  In a nutshell, you give it a bunch of ANSI C/C++ declarations
and it generates an interface between C and your favorite scripting
language.  However, this is only scratching the surface of what SWIG
can do--some of its more advanced features include automatic
documentation generation, module and library management, extensive
customization options, and more.

This package contains the SWIG manual.

%package examples
Summary:        SWIG example files
License:        BSD-3-Clause
Group:          Documentation/Howto
Requires:       swig
BuildArch:      noarch

%description examples
SWIG is a compiler that attempts to make it easy to integrate C, C++,
or Objective-C code with scripting languages including Perl, Tcl, and
Python.  In a nutshell, you give it a bunch of ANSI C/C++ declarations
and it generates an interface between C and your favorite scripting
language.  However, this is only scratching the surface of what SWIG
can do--some of its more advanced features include automatic
documentation generation, module and library management, extensive
customization options, and more.

This package contains SWIG examples, useful both for testing and
understanding SWIG usage.
%endif

%prep
%autosetup -p1 -n %{origname}-%{version}

%build
%if 0%{?suse_version} < 1600
export CC=gcc-12
export CXX=g++-12
%endif
%ifarch s390 s390x
export CCSHARED="-fPIC"
%endif
./autogen.sh
%configure \
	--without-ocaml \
	--disable-ccache
%make_build

%check
%if %{with test}
%if 0%{?suse_version} >= 1500 || 0%{?centos_version} >= 800
export PY3=true
%endif
%if 0%{?suse_version} < 1600
export CC=gcc-12
export CXX=g++-12
%endif
%make_build check EXTRA_CXXFLAGS="-fexcess-precision=fast"
%endif

%install
%if %{without test}
%make_install

install -d %{buildroot}%{docpath}
cp -a TODO ANNOUNCE CHANGES* README Doc/{Devel,Manual} \
	%{buildroot}%{docpath}
install -d %{buildroot}%{_datadir}/swig
cp -a Examples %{buildroot}%{_datadir}/swig/examples
rm -rf %{buildroot}%{_datadir}/swig/examples/test-suite

# rm files that are not needed for running or rebuilding the examples
find %{buildroot}%{_datadir}/swig \
	-name '*.dsp' -o -name '*.vcproj' -o -name '*.sln' -o \
	-name '*.o' -o -name '*_wrap.c' -print0 | xargs --no-run-if-empty -0 rm

# fix perms
chmod -x %{buildroot}%{docpath}/Manual/*
find %{buildroot}%{_datadir}/swig -name '*.h' -perm /111 | \
	xargs --no-run-if-empty chmod -x
ln -s %{_datadir}/swig/examples %{buildroot}%{docpath}/Examples

%fdupes %{buildroot}
%endif

%if %{without test}
%files
%license LICENSE
%dir %{docpath}
%{docpath}/[A-Z][A-Z]*
%{_datadir}/swig
%exclude %{_datadir}/swig/examples
%attr(755,root,root) %{_bindir}/swig

%files doc
%license LICENSE
%{docpath}/Devel
%{docpath}/Manual

%files examples
%license LICENSE
%{docpath}/Examples
%{_datadir}/swig/examples
%endif

%changelog
