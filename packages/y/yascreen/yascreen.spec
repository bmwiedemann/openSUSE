#
# spec file for package yascreen
#
# Copyright (c) 2023 SUSE LLC
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


%define sover 0
Name:           yascreen
Version:        1.97
Release:        0
Summary:        A terminal control library (ncurses alternative)
License:        LGPL-3.0-or-later
URL:            https://github.com/bbonev/yascreen/
Source:         %{url}releases/download/v%{version}/yascreen-%{version}.tar.xz
Source2:        %{url}releases/download/v%{version}/yascreen-%{version}.tar.xz.asc
Source3:        https://raw.githubusercontent.com/bbonev/yascreen/v%{version}/debian/upstream/signing-key.asc#/%{name}.keyring
%if %{?suse_version} < 1599
BuildRequires:  gcc12
%endif

%description
yascreen is a lib(n)curses alternative, oriented towards modern terminals.

 * allows both internal and external event loop
 * allows stdin/stdout or external input/output (can work over socket)
 * supports basic set of telnet sequences, making it suitable for built-in
   terminal interfaces for daemons
 * supports a limited set of input keystroke sequences
 * fully Unicode compatible (parts of this depend on wcwidth in libc)
 * supports utf8 verification of input
 * relies only on a limited subset of ANSI/xterm ESC sequences, making it
   compatible with mostly all modern terminals (inspired by linenoise)
 * there is no curses API and ancient terminal compatibility

%package -n libyascreen%{sover}
Summary:        Yet Another Screen Library (lib(n)curses alternative)

%description -n libyascreen%{sover}
yascreen is a lib(n)curses alternative, oriented towards modern terminals.

%package devel
Summary:        Development files for yascreen
Requires:       libyascreen%{sover} = %{version}

%description devel
This package contains the header files and libraries needed to
compile applications or shared objects that use yascreen.

%prep
%autosetup -p1

%build
export CFLAGS="%{optflags}"
%if %{?suse_version} < 1599
export CC=gcc-12
%endif
%make_build

%install
%make_install PREFIX=%{_prefix} LIBDIR=/%{_lib}/
chmod +x %{buildroot}%{_libdir}/libyascreen.so.%{sover}
find %{buildroot}%{_libdir} -type f -name "*.a" -print -delete

%ldconfig_scriptlets -n libyascreen%{sover}

%files -n libyascreen0
%license LICENSE
%{_libdir}/libyascreen.so.%{sover}
%{_libdir}/libyascreen.so.%{sover}.*

%files devel
%license LICENSE
%doc README.md
%{_libdir}/libyascreen.so
%{_libdir}/pkgconfig/yascreen.pc
%{_mandir}/man3/yascreen.3%{?ext_man}
%{_includedir}/yascreen.h

%changelog
