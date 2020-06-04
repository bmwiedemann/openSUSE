#
# spec file for package swig
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


%bcond_with  swig_ocaml
%if 0%{?fedora} + 0%{?rhel_version} + 0%{?centos_version} > 0
%define docpath %{_docdir}/%{name}-%{version}
BuildRequires:  perl-Test-Simple
BuildRequires:  perl-devel
BuildRequires:  ruby
%endif
%if 0%{?suse_version} > 0
%define docpath %{_docdir}/%{name}
BuildRequires:  ruby-devel
%endif
Name:           swig
Version:        4.0.1
Release:        0
Summary:        Simplified Wrapper and Interface Generator
License:        GPL-3.0-or-later AND BSD-3-Clause
Group:          Development/Languages/C and C++
URL:            http://www.swig.org/
Source:         https://github.com/%{name}/%{name}/archive/rel-%{version}.tar.gz
Source1:        %{name}.rpmlintrc

# ruby 2.7 support (cherry-picked from 4.0.2~pre)
Patch1:         0001-Fix-code-generated-for-Ruby-global-variables.patch
Patch2:         0002-Add-support-for-Ruby-2.7.patch
Patch3:         0003-Move-new-macros-for-Ruby-to-their-dedicated-namespac.patch
Patch4:         0004-Improve-description-of-cast-macros-for-Ruby.patch

Patch300:       ruby-std-wstring-byte-order.patch
Patch308:       swig308-isfinite.diff

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  bison
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  pcre-devel
BuildRequires:  perl
BuildRequires:  pkgconfig
%if 0%{?suse_version} >= 1500
BuildRequires:  libboost_headers-devel
BuildRequires:  python3-devel
BuildRequires:  python3-tools
%else
BuildRequires:  boost-devel
BuildRequires:  python-devel > 2.6
%endif
%if %{with swig_ocaml}
BuildRequires:  ncurses-devel
BuildRequires:  ocaml >= 3.12.0
BuildRequires:  ocaml-camlp4-devel
BuildRequires:  ocaml-findlib
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
%setup -q -n %{name}-rel-%{version}
%autopatch -p1

%build
%ifarch s390 s390x
export CCSHARED="-fPIC"
%endif
./autogen.sh
%configure \
%if %{without swig_ocaml}
	--without-ocaml \
%endif
	--disable-ccache
make %{?_smp_mflags}

%check
%if 0%{?suse_version} >= 1500
export PY3=true
%endif
make %{?_smp_mflags} check

%install
%make_install

install -d %{buildroot}%{docpath}
cp -a TODO ANNOUNCE CHANGES* LICENSE README Doc/{Devel,Manual} \
	%{buildroot}%{docpath}
install -d %{buildroot}%{_libdir}/swig
cp -a Examples %{buildroot}%{_libdir}/swig/examples
rm -rf %{buildroot}%{_libdir}/swig/examples/test-suite

# rm files that are not needed for running or rebuilding the examples
find %{buildroot}%{_libdir}/swig \
	-name '*.dsp' -o -name '*.vcproj' -o -name '*.sln' -o \
	-name '*.o' -o -name '*_wrap.c' | xargs rm

# fix perms
chmod -x %{buildroot}%{docpath}/Manual/*
find %{buildroot}%{_libdir}/swig -name '*.h' -perm /111 | \
	xargs --no-run-if-empty chmod -x
ln -s %{_libdir}/swig/examples %{buildroot}%{docpath}/Examples

%fdupes %{buildroot}

%files
%defattr(644,root,root,755)
%dir %{docpath}
%{docpath}/[A-Z][A-Z]*
%{_datadir}/swig
%attr(755,root,root) %{_bindir}/swig

%files doc
%{docpath}/Devel
%{docpath}/Manual

%files examples
%{docpath}/Examples
%{_libdir}/swig

%changelog
