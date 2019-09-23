#
# spec file for package pcmanx-gtk2
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           pcmanx-gtk2
Version:        1.3
Release:        0
Summary:        User-friendly telnet client designed for BBS browsing
License:        GPL-2.0+
Group:          Productivity/Networking/Other
Url:            https://github.com/pcman-bbs/pcmanx
Source:         %{name}-%{version}.tar.xz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  gcc-c++
BuildRequires:  gtk2-devel
BuildRequires:  intltool
BuildRequires:  libnotify-devel
BuildRequires:  libtool
BuildRequires:  update-desktop-files
BuildRequires:  xz
Requires(post):   desktop-file-utils
Requires(postun): desktop-file-utils

%description
An easy-to-use telnet client mainly targets BBS users.
PCManX is a newly developed GPL'd version of PCMan, a full-featured famous BBS
client formerly designed for MS Windows only. It aimed to be an easy-to-use yet
full-featured telnet client facilitating BBS browsing with the ability to
process double-byte characters.

%prep
%setup -q

%build
%configure --enable-iplookup --enable-proxy --enable-libnotify \
	--enable-debug \
;
make %{?_smp_mflags} V=1

%install
%makeinstall
%suse_update_desktop_file pcmanx GTK Network News Chat InstantMessaging

%find_lang pcmanx

%post
%desktop_database_post

%postun
%desktop_database_postun

%files -f pcmanx.lang
%defattr(-,root,root)
%doc AUTHORS COPYING NEWS README TODO
%dir %{_datadir}/pcmanx/
%dir %{_datadir}/pcmanx/nancy_bot/
%{_bindir}/pcmanx
%{_datadir}/applications/pcmanx.desktop
%{_datadir}/pcmanx/emoticons
%{_datadir}/pcmanx/sitelist
%{_datadir}/pcmanx/nancy_bot/default.conf
%{_datadir}/pcmanx/nancy_bot/default_msg.data
%{_datadir}/pcmanx/nancy_bot/example_msg.data
%{_datadir}/pcmanx/nancy_bot/example_usages.data
%{_datadir}/pcmanx/nancy_bot/example.conf
%{_datadir}/pcmanx/nancy_bot/default_usages.data
%{_datadir}/pixmaps/pcmanx.svg
%{_mandir}/man1/pcmanx.1*

%changelog
