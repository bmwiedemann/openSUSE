#
# spec file for package jikes
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


Name:           jikes
Version:        1.22
Release:        0
Summary:        IBM Java Compiler
License:        IPL-1.0
Group:          Development/Languages/Java
Url:            http://jikes.sourceforge.net/
Source0:        %{name}-%{version}.tar.bz2
Patch0:         %{name}-%{version}-uninitialized-variables.patch
Patch1:         %{name}-%{version}-strict_aliasing.patch
BuildRequires:  automake
BuildRequires:  gcc-c++
Requires:       jre >= 1.1

%description
Jikes(TM) is a compiler that translates Java(TM) source files as
defined in "The Java Language Specification" into the byte code
instruction set and binary format defined in "The Java Virtual Machine
Specification."

You may wonder why the world needs another Java compiler, considering
that Sun provides javac free with its SDK. Jikes has four advantages
that make it a valuable contribution to the Java community:

* Open source. Jikes is OSI Certified Open Source Software. OSI
   Certified is a certification mark of the Open Source Initiative.

* Strictly Java compatible. Jikes strives to adhere to both "The
   Java Language Specification" and "The Java Virtual Machine
   Specification" as tightly as possible and does not support
   subsets, supersets, or other variations of the language. The FAQ
   describes some of the side effects of this strict language
   conformance.

* High performance. Jikes is a high performance compiler, making it
   ideal for use with larger projects.

* Dependency analysis. Jikes performs a dependency analysis on your
   code that provides two very useful features: Incremental builds
   and makefile generation.

Note that you must set CLASSPATH correctly to use jikes.

%prep
%setup -q
%patch0
%patch1
cp -v  doc/license.htm license.html

%build
autoreconf -I src/m4 --force --install
CFLAGS="%{optflags}" \
CXXFLAGS="%{optflags}" \
%configure --mandir=%{_mandir} \
           --prefix=%{_prefix} \
           --infodir=%{_infodir} \
           --sysconfdir=%{_sysconfdir}
make %{?_smp_mflags}

%install
%make_install
#
rm %{buildroot}/%{_datadir}/doc/%{name}-%{version}/license.htm

%files
%doc AUTHORS COPYING ChangeLog NEWS README TODO doc/license.htm
%{_mandir}/man1/jikes.1%{ext_man}
%{_includedir}/*
%{_bindir}/jikes

%changelog
