#
# spec file for package gnudos
#
# Copyright (c) 2024 Andreas Stieger <Andreas.Stieger@gmx.de>
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


%define sover 2
Name:           gnudos
Version:        2.0
Release:        0
Summary:        Library and utilities for DOS look-and-feel
License:        GPL-3.0-or-later
URL:            https://www.gnu.org/software/gnudos/
Source:         https://ftp.gnu.org/pub/gnu/gnudos/%{name}-2.0.tar.gz
Source2:        https://ftp.gnu.org/pub/gnu/gnudos/%{name}-2.0.tar.gz.sig
Source3:        https://savannah.gnu.org/people/viewgpg.php?user_id=94484#/%{name}.keyring
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(ncursesw)

%description
GnuDOS is a library designed to help new users of the GNU system, who are
coming from a DOS background, fit into the picture and start using the GNU
system with ease. It also addresses the console programmers of such programs
that have the look and feel of old DOS system.

%package -n libgnudos%{sover}
Summary:        Library for DOS look-and-feel

%description -n libgnudos%{sover}
GnuDOS is a library designed to help new users of the GNU system, who are
coming from a DOS background, fit into the picture and start using the GNU
system with ease. It also addresses the console programmers of such programs
that have the look and feel of old DOS system.

This package contains the libgnudos%{sover} shared library.

%package devel
Summary:        Development files for GnuDOS
Requires:       libgnudos%{sover} = %{version}

%description devel
GnuDOS is a library designed to help new users of the GNU system, who are
coming from a DOS background, fit into the picture and start using the GNU
system with ease. It also addresses the console programmers of such programs
that have the look and feel of old DOS system.

This package contains files required for development with GnuDOS.

%prep
%autosetup -p1

%build
%configure \
	--enable-static=no \
	%{nil}
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
# does not honor --docdir
mkdir -p %{buildroot}%{_docdir}/%{name}/
mv -v %{buildroot}%{_datadir}/doc/%{name}/* %{buildroot}%{_docdir}/%{name}/
rmdir -v %{buildroot}%{_datadir}/doc/%{name}
rm %{buildroot}%{_docdir}/%{name}/COPYING

%check
%make_build check

%ldconfig_scriptlets -n libgnudos%{sover}

%files
%license COPYING
%doc ChangeLog README AUTHORS NEWS
%{_bindir}/mino
%{_bindir}/prime
%{_mandir}/man1/mino.1%{?ext_man}
%{_mandir}/man1/prime.1%{?ext_man}
%{_docdir}/gnudos/mino
%{_docdir}/gnudos/prime

%files -n libgnudos%{sover}
%license COPYING
%{_libdir}/libgnudos.so.%{sover}
%{_libdir}/libgnudos.so.%{sover}.*
%dir %{_docdir}/gnudos

%files devel
%license COPYING
%doc ChangeLog README AUTHORS NEWS
%{_includedir}/console/
%{_libdir}/libgnudos.so
%{_mandir}/man1/gnudos.1%{?ext_man}
%{_docdir}/gnudos/*.c
%{_docdir}/gnudos/keybindings

%changelog
