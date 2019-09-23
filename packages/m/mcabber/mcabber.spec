#
# spec file for package mcabber
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


Name:           mcabber
Version:        1.1.0
Release:        0
Summary:        Modular XMPP client on ncurses
License:        GPL-2.0+
Group:          Productivity/Networking/Instant Messenger
Url:            https://mcabber.com/
Source:         https://mcabber.com/files/%{name}-%{version}.tar.bz2
Source1:        https://mcabber.com/files/%{name}-%{version}.tar.bz2.asc
Source2:        %{name}.keyring
# PATCH-FEATURE-OPENSUSE up_one_line_message_length.patch
Patch0:         up_one_line_message_length.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  fdupes
BuildRequires:  libgpgme-devel
BuildRequires:  libotr-devel
BuildRequires:  libtool
BuildRequires:  ncurses-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(enchant)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(loudmouth-1.0)

%description
mcabber is a small XMPP console client on ncurses. It features
SSL support, history logging, external actions, OTR support,
conferences (MUC) support.

%package devel
Summary:        Headers for modular XMPP client on ncurses
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}
Requires:       pkgconfig(glib-2.0)
Requires:       pkgconfig(gmodule-2.0)
Requires:       pkgconfig(loudmouth-1.0)

%description devel
mcabber is a small XMPP console client on ncurses. It features
SSL support, history logging, external actions, OTR support,
conferences (MUC) support.

%prep
%setup -q
%patch0
mv -f %{name}rc.example %{name}rc

%build
NOCONFIGURE=1 ./autogen.sh
%configure \
  --enable-enchant \
  --enable-hgcset \
  --enable-otr
make %{?_smp_mflags} V=1

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
%fdupes %{buildroot}%{_datadir}

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog COPYING NEWS README TODO
%doc %{name}rc doc/%{name}.?.* doc/manpage.css
%{_bindir}/%{name}
%{_libdir}/%{name}/
%{_datadir}/%{name}/
%{_mandir}/man?/%{name}.?%{?ext_man}

%files devel
%defattr(-,root,root)
%{_includedir}/%{name}/
%{_libdir}/pkgconfig/%{name}.pc

%changelog
