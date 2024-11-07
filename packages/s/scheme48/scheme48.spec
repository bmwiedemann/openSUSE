#
# spec file for package scheme48
#
# Copyright (c) 2024 SUSE LLC
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


#!BuildIgnore:  scheme48-vm
Name:           scheme48
Version:        1.9.3
Release:        0
Summary:        An implementation of Scheme written by Richard Kelsey and Jonathan Rees
License:        BSD-3-Clause
Group:          Development/Languages/Scheme
URL:            https://www.s48.org/
Source0:        https://www.s48.org/1.9.3/scheme48-1.9.3.tgz
Source1:        scheme48-rpmlintrc
Patch0:         noreturn.patch
Patch1:         no-env-trampoline.diff
Patch2:         debian-user-name.diff
Patch3:         man-properly-escape-minuses.diff
Patch4:         security-tmpfile.patch
#Patch5:         scheme48-1.9.2-gcc14.patch
BuildRequires:  emacs-nox
Requires:       %{name}-vm = %{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%define add_optflags(a:f:t:p:w:W:d:g:O:A:C:D:E:H:i:M:n:P:U:u:l:s:X:B:I:L:b:V:m:x:c:S:E:o:v:) \
%global optflags %{optflags} %{**}

%description
Scheme 48 is an implementation of the Scheme programming language as described
in the Revised5 Report on the Algorithmic Language Scheme. It is based on a
compiler and interpreter for a virtual Scheme machine. Scheme 48 tries to be
faithful to the Revised5 Scheme Report, providing neither more nor less in
the initial user environment.

%package vm
Summary:        Virtual Machine for Scheme48
Group:          System/Libraries

%description vm
Core files of Scheme48 without development environment.

%package devel
Summary:        Virtual Machine for Scheme48
Group:          Development/Languages/Scheme
Requires:       %name = %version

%description devel
A devel files for %{name} and %{name}-prescheme. This includes a header files,
libprescheme.so and %{name}-config.

%package doc
Summary:        Documentation for Scheme48
Group:          Development/Languages/Scheme

%description doc
Documentation for Scheme48 VM and interpreter

%package prescheme
Summary:        PreScheme compiler
Group:          Development/Languages/Scheme
Requires:       %name = %version

%description prescheme
Pre-Scheme is a low-level dialect of Scheme, designed for systems programming
with higher-level abstractions. For example, the Scheme48 virtual machine is
written in Pre-Scheme. Pre-Scheme is a particularly interesting alternative to
C for many systems programming tasks, because not only does it operate at about
the same level as C, but it also may be run in a regular high-level Scheme
development with no changes to the source, without resorting to low-level stack
munging with tools such as gdb. Pre-Scheme also supports two extremely
important high-level abstractions of Scheme: macros and higher-order, anonymous
functions. Richard Kelsey's Pre-Scheme compiler, based on his PhD research on
transformational compilation, compiles Pre-Scheme to efficient C, applying
numerous intermediate source transformations in the process.

%package -n emacs-scheme48
Summary:        CMUScheme48 emacs mode
Group:          Productivity/Text/Editors
Requires:       %name = %version
Recommends:     emacs

%description -n emacs-scheme48
Scheme process in a buffer.  Adapted from cmuscheme.el

%prep
%autosetup -p1

%build
%global _lto_cflags %{_lto_cflags} -ffat-lto-objects
%add_optflags -Wall -Wno-return-type -fPIC -D_DEFAULT_SOURCE -D_XOPEN_SOURCE=500

%configure --docdir=%{_datadir}/doc/packages/%{name}
touch c/scheme48.h
# Please to not use option -j here as this may break build
make
rm -vf c/scheme48.h
# Redo the image, also do not use -j here
make RUNNABLE=$PWD/go

pushd ps-compiler
    ../go -h 20000000 -a batch <<- 'EOF'
	,config ,load ../scheme/prescheme/interface.scm
	,config ,load ../scheme/prescheme/package-defs.scm
	,exec ,load load-ps-compiler.scm
	,in prescheme-compiler prescheme-compiler
	,user (define prescheme-compiler ##)
	,dump ../ps-compiler.image "(Pre-Scheme)"
	,exit
	EOF
popd

#ld -O2 -Bsymbolic-functions -shared -as-needed -soname=libprescheme.so.%{version} \
#    -o libprescheme.so c/unix/misc.o c/unix/fd-io.o c/unix/io.o -lc
ar cru libprescheme.a c/unix/misc.o c/unix/fd-io.o c/unix/io.o
ranlib libprescheme.a

emacs -q -no-site-file -batch -eval "(byte-compile-file \"emacs/cmuscheme48.el\")"

# It's now 2019, no latin text anymore
for f in README COPYING
do
    iconv -f latin1 -t utf-8 -o $f.new $f
    touch -r $f $f.new
    mv $f.new $f
done

%install
make install-no-doc DESTDIR=%{?buildroot} INSTALL="install -p"
rm -vf %{buildroot}%{_docdir}/COPYING
rm -vf %{buildroot}%{_datadir}/doc/COPYING
rm -vf %{buildroot}%{_datadir}/doc/%{name}/COPYING
rm -vf %{buildroot}%{_datadir}/doc/packages/%{name}/COPYING

cat > %{buildroot}%{_bindir}/prescheme <<- 'EOF'
	#!/bin/sh
	LIB=%{_libdir}/%{name}-%{version}
	exec $LIB/scheme48vm -i $LIB/ps-compiler.image -h 20000000 "$@"
	EOF
chmod a+x %{buildroot}%{_bindir}/prescheme

install -m644 ps-compiler.image	    %{buildroot}%{_libdir}/%{name}-%{version}/
install -m644 c/{prescheme,io}.h    %{buildroot}/%{_includedir}/
#install -m644 libprescheme.so	    %{buildroot}/%{_libdir}/libprescheme.so.%{version}
#ln -sf libprescheme.so.%{version}   %{buildroot}/%{_libdir}/libprescheme.so
install -m644 libprescheme.a	    %{buildroot}/%{_libdir}/
PATH=/sbin:/usr/sbin:$PATH ldconfig -C $PWD/mycache %{buildroot}%{_libdir}/
rm -vf mycache*
mkdir -p %{buildroot}%{_datadir}/emacs/site-lisp
install -m644 emacs/cmuscheme48.el* %{buildroot}%{_datadir}/emacs/site-lisp/
ln -sf %{_libdir}/%{name}-%{version}/%{name}vm %{buildroot}%{_bindir}/%{name}vm

%files
%defattr(-,root,root)
%license COPYING
%doc README
%defattr(-,root,root,0755)
%{_bindir}/*
%exclude %{_bindir}/%{name}-config
%exclude %{_bindir}/prescheme
%exclude %{_bindir}/%{name}vm
%{_libdir}/%{name}-%{version}
%exclude %{_libdir}/%{name}-%{version}/ps-compiler.image
%exclude %{_libdir}/%{name}-%{version}/%{name}vm
%{_datadir}/%{name}-%{version}
%{_mandir}/man1/%{name}.1.gz

%files vm
%defattr(-,root,root,0755)
%{_bindir}/%{name}vm
%{_libdir}/%{name}-%{version}/%{name}vm

%files doc
%defattr(-,root,root,0755)
%doc doc/*.txt doc/html/ doc/*.pdf doc/*.ps

%files devel
%defattr(-,root,root,0755)
%{_includedir}/*.h
%{_includedir}/%{name}-external.exp
%{_includedir}/%{name}.def
%{_includedir}/%{name}.exp
%{_bindir}/%{name}-config
%{_libdir}/libprescheme.a

%files prescheme
%defattr(-,root,root,0755)
%{_bindir}/prescheme
%{_libdir}/%{name}-%{version}/ps-compiler.image

%files -n emacs-scheme48
%defattr(-,root,root,0755)
%dir %{_datadir}/emacs/site-lisp
%{_datadir}/emacs/site-lisp/*

%changelog
