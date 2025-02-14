#
# spec file for package cwstudio
#
# Copyright (c) 2019 SUSE LLC
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


%bcond_without  gui
Name:           cwstudio
Version:        0.9.7
Release:        0
Summary:        Fast, portable and lightweight Morse code signals generator
License:        GPL-3.0-or-later
URL:            https://cwstudio.sourceforge.net/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Patch0:         cwstudio-0.9.7-nonvoid-return.patch
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(ncurses)
BuildRequires:  pkgconfig(libpulse)
%if %{with gui}
BuildRequires:  c++_compiler
BuildRequires:  wxWidgets-devel >= 2.8.0
%endif

%description
CWStudio is lightweight, portable, almost library-independent and computationally
efficient generator of CW signals for telegraphy training purposes. It can create
sound with maximum similarity to real air, simulating many difficulties.

%if %{with gui}
%package gui
Summary:        Fast, portable and lightweight Morse code signals generator - GUI version

%description gui
CWStudio is lightweight, portable, almost library-independent and computationally
efficient generator of CW signals for telegraphy training purposes. It can create
sound with maximum similarity to real air, simulating many difficulties.

This package contains the wxWidgets based GUI version.
%endif

%prep
%autosetup -p1
sed -i 's/\r$//' AUTHORS ChangeLog README

%build
%configure \
	--with-ncurses \
	%{nil}
%make_build

%install
%make_install

%check
%make_build check

%files
%license COPYING
%doc AUTHORS ChangeLog README
%{_bindir}/cwcli
%{_bindir}/cwcurses
%{_mandir}/man1/cwstudio.1%{?ext_man}

%if %{with gui}
%files gui
%license COPYING
%doc AUTHORS ChangeLog README
%{_bindir}/cwwx
%endif

%changelog
