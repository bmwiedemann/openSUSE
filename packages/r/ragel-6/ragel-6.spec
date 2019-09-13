#
# spec file for package ragel
#
# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           ragel-6
Version:        6.10
Release:        0
Summary:        Finite state machine compiler
License:        GPL-2.0+
Group:          Development/Tools/Other
Url:            http://complang.org/ragel/

#Git-Clone:	git://git.colm.net/ragel.git
Source:         http://www.colm.net/files/ragel/ragel-%version.tar.gz
Source1:        http://www.colm.net/files/ragel/ragel-%version.tar.gz.asc
Source2:        %name.keyring
BuildRequires:  gcc-c++
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Conflicts:      ragel

%description
Ragel compiles finite state machines from regular languages into
executable C, C++, Objective-C, or D code. Ragel state machines can
not only recognize byte sequences as regular expression machines do,
but can also execute code at arbitrary points in the recognition of a
regular language. Code embedding is done using inline operators that
do not disrupt the regular language syntax.

%prep
%setup -qn ragel-%version

%build
%configure --docdir="%_docdir/%name"
make %{?_smp_mflags}

%check
make check

%install
b="%buildroot"
make install DESTDIR="$b"
c="$b/%_datadir/vim/site/syntax"
mkdir -p "$c"
install -pm0644 ragel*.vim "$c/"
cp -a COPYING doc/ragel-guide.pdf "$b/%_defaultdocdir/%name/"

%files
%defattr(-,root,root)
%_bindir/ragel
%_mandir/man1/ragel.1*
%_datadir/vim
%_defaultdocdir/%name/

%changelog
