#
# spec file for package swig
#
# Copyright (c) 2024 SUSE LLC
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


%bcond_with  swig_ocaml
%if 0%{?fedora} + 0%{?rhel_version} + 0%{?centos_version} > 0
%define docpath %{_docdir}/%{name}-%{version}
BuildRequires:  perl-Test-Simple
BuildRequires:  perl-devel
%if 0%{?centos_version} < 800
BuildRequires:  ruby
%endif
%endif
%if 0%{?suse_version} > 0
%define docpath %{_docdir}/%{name}
BuildRequires:  ruby-devel
%endif
Name:           swig
Version:        4.3.1
Release:        0
Summary:        Simplified Wrapper and Interface Generator
License:        BSD-3-Clause AND GPL-3.0-or-later
Group:          Development/Languages/C and C++
URL:            https://www.swig.org/
Source:         https://prdownloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Source1:        %{name}.rpmlintrc
BuildRequires:  fdupes
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
%if %{with swig_ocaml}
BuildRequires:  ncurses-devel
BuildRequires:  ocaml >= 3.12.0
BuildRequires:  ocaml-camlp4-devel
BuildRequires:  ocaml-findlib
%endif

# for swig-4.3.0-Fix-precedence-of-casts.patch
BuildRequires:  bison

%description
SWIG is a compiler that attempts to make it easy to integrate C, C++,
or Objective-C code with scripting languages including Perl, Tcl, and
Python.  In a nutshell, you give it a bunch of ANSI C/C++ declarations
and it generates an interface between C and your favorite scripting
language.  However, this is only scratching the surface of what SWIG
can do--some of its more advanced features include automatic
documentation generation, module and library management, extensive
customization options, and more.

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
understandig SWIG usage.

%prep
%autosetup -p1 -n %{name}-%{version}

%build
%if 0%{?suse_version} < 1600
export CC=gcc-12
export CXX=g++-12
%endif
%ifarch s390 s390x
export CCSHARED="-fPIC"
%endif
%configure \
%if %{without swig_ocaml}
	--without-ocaml \
%endif
	--disable-ccache
%make_build

%check
%if 0%{?suse_version} >= 1500 || 0%{?centos_version} >= 800
export PY3=true
%endif
%if 0%{?suse_version} < 1600
export CC=gcc-12
export CXX=g++-12
%endif
%make_build check EXTRA_CXXFLAGS="-fexcess-precision=fast"

%install
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
	-name '*.o' -o -name '*_wrap.c' | xargs rm

# fix perms
chmod -x %{buildroot}%{docpath}/Manual/*
find %{buildroot}%{_datadir}/swig -name '*.h' -perm /111 | \
	xargs --no-run-if-empty chmod -x
ln -s %{_datadir}/swig/examples %{buildroot}%{docpath}/Examples

%fdupes %{buildroot}

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

%changelog
