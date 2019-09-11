#
# spec file for package cdecl
#
# Copyright (c) 2011 SUSE LINUX Products GmbH, Nuernberg, Germany.
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



Name:           cdecl
Version:        2.5
Release:        1
Group:          Development/Languages/C and C++
Summary:        C/C++ function declaration translator
Url:            ftp://ftp.oss.cc.gatech.edu/pub/linux/devel/lang/c/cdecl-2.5.tar.gz
License:        SUSE-Public-Domain

Source:         %name-%version.tar.xz
Patch1:         %name-2.5-deb11.diff
Patch2:         keyword-identifier.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  bison flex readline-devel xz

%description
Turn English phrases to C or C++ declarations Cdecl is a program
which will turn English-like phrases such as "declare foo as array 5
of pointer to function returning int" into C declarations such as
"int (*foo[5])()". It can also translate the C into the
pseudo-English. And it handles typecasts, too. Plus C++. And in this
version it has command line editing and history with the GNU readline
library.

%prep
%setup
%patch -P 1 -P 2 -p1

%build
make CFLAGS="%optflags -DUSE_READLINE -DOLD_READLINE" %{?_smp_mflags};

%install
b="%buildroot";
install -dm0755 "$b/%_bindir";
install -dm0755 "$b/%_mandir/man1";
make install BINDIR="$b/%_bindir" MANDIR="$b/%_mandir/man1";

%files
%defattr(-,root,root)
%_bindir/*
%_mandir/*/*

%changelog
