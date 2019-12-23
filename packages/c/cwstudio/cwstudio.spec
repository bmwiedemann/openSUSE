#
# spec file for package cwstudio
#
# Copyright (c) 2019 SUSE LLC
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


Name:           cwstudio
Version:        0.9.6
Release:        0
Summary:        Fast, portable and lightweight Morse code signals generator
License:        GPL-3.0-or-later
Group:          Productivity/Hamradio/Other
URL:            http://cwstudio.sourceforge.net/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
BuildRequires:  gcc-c++
BuildRequires:  ncurses-devel
BuildRequires:  wxWidgets-devel

%description
CWStudio is lightweight, portable, almost library-independent and computationally
efficient generator of CW signals for telegraphy training purposes. It can create
sound with maximum similarity to real air, simulating many difficulties.

%prep
%setup -q
sed -i 's/\r$//' AUTHORS ChangeLog README

%build
%configure
make %{?_smp_mflags}

%install
%make_install

%files
%license COPYING
%doc AUTHORS ChangeLog README
%{_bindir}/cwcli
%{_bindir}/cwcurses
%{_bindir}/cwwx
%{_mandir}/man1/cwstudio.1%{?ext_man}

%changelog
