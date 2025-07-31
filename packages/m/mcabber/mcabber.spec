#
# spec file for package mcabber
#
# Copyright (c) 2025 SUSE LINUX GmbH, Nuernberg, Germany.
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           mcabber
Version:        1.1.2
Release:        0
Summary:        Modular XMPP client on ncurses
License:        GPL-2.0-or-later
Group:          Productivity/Networking/Instant Messenger
URL:            https://mcabber.com/
Source:         https://mcabber.com/files/%{name}-%{version}.tar.bz2
Source1:        https://mcabber.com/files/%{name}-%{version}.tar.bz2.asc
Source2:        %{name}.keyring
# PATCH-FEATURE-OPENSUSE up_one_line_message_length.patch
Patch0:         up_one_line_message_length.patch
Patch1:         mcabber-1.1.2-gcc15.patch
Patch2:         mcabber-1.1.2-enchant-2.patch
# for mcabber-1.1.2-enchant-2.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  fdupes
BuildRequires:  libtool
BuildRequires:  pkgconfig >= 0.16
BuildRequires:  pkgconfig(enchant-2)
BuildRequires:  pkgconfig(glib-2.0) >= 2.14.0
BuildRequires:  pkgconfig(gpgme) >= 1.0.0
BuildRequires:  pkgconfig(libotr) >= 4.0.0
BuildRequires:  pkgconfig(loudmouth-1.0)
BuildRequires:  pkgconfig(ncursesw)

%description
mcabber is a small XMPP console client on ncurses. It features
SSL support, history logging, external actions, OTR support,
conferences (MUC) support.

%package devel
Summary:        Headers for modular XMPP client on ncurses
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}

%description devel
mcabber is a small XMPP console client on ncurses. It features
SSL support, history logging, external actions, OTR support,
conferences (MUC) support.

%prep
%autosetup -p1
mv -f %{name}rc.example %{name}rc

%build
# for mcabber-1.1.2-enchant-2.patch
autoreconf -fiv
%configure \
  --enable-enchant \
  --enable-hgcset \
  --enable-otr \
  %{nil}
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
%fdupes %{buildroot}%{_datadir}

%check
%make_build check

%files
%license COPYING
%doc AUTHORS ChangeLog NEWS README TODO
%doc %{name}rc doc/%{name}.?.* doc/manpage.css
%{_bindir}/%{name}
%{_libdir}/%{name}/
%{_datadir}/%{name}/
%{_mandir}/man?/%{name}.?%{?ext_man}

%files devel
%license COPYING
%{_includedir}/%{name}/
%{_libdir}/pkgconfig/%{name}.pc

%changelog
