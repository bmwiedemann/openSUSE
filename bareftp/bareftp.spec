#
# spec file for package bareftp
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2011 Packman project
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


Name:           bareftp
Version:        0.3.12
Release:        0
Summary:        A file transfer client for FTP/FTPS/SFTP
License:        GPL-2.0
Group:          Productivity/Networking/Ftp/Clients
Url:            http://www.bareftp.org/
Source:         http://www.bareftp.org/release/%{name}-%{version}.tar.gz
# PATCH-FIX-OPENSUSE- bareftp-mono-4.5.patch dimstar@opensuse.org -- Build for .Net 4.5 target. Upstream is 'dead' (busy porting to python) and mono 4.4 no longer has /usr/lib/mono/2.0 (but there would be /usr/lib/mono/2.0-api)
Patch0:         bareftp-mono-4.5.patch
BuildRequires:  gconf-sharp2
BuildRequires:  glib2-devel
BuildRequires:  gnome-keyring-sharp-devel
BuildRequires:  gnome-sharp2
BuildRequires:  gnome-vfs-sharp2
BuildRequires:  gtk-sharp2
BuildRequires:  hicolor-icon-theme
BuildRequires:  intltool
BuildRequires:  libtool
BuildRequires:  mono-data
BuildRequires:  mono-devel
BuildRequires:  mono-web
BuildRequires:  perl-XML-Parser
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Requires:       gconf-sharp2
Requires:       gnome-keyring-sharp
Requires:       gtk-sharp2
Requires:       mono-core

%description
bareFTP is a file transfer client supporting the FTP, FTP over SSL/TLS (FTPS)
and SSH File Transfer Protocol (SFTP). It is written in C#, targeting the
Mono framework and the GNOME desktop environment. bareFTP is released under
the terms of the GPL. 


%prep
%setup -q
%if 0%{?suse_version} > 1110
# Do not apply the mono 4.5 patch on SLE 11
%patch0 -p1
%endif

%build
%if 0%{?suse_version} > 1110
# SLE 11 can't bootstrap, but as we don't apply the patch, there is also no need
autoreconf -fiv
%endif
%configure --disable-static
%__make %{?jobs:-j%{jobs}}

%install
%makeinstall
find %{buildroot}%{_libdir} -type f -name '*.la' -delete -print
%__install -D -m 644 data/%{name}.png %{buildroot}/%{_datadir}/pixmaps/%{name}.png
%suse_update_desktop_file %{name} Network FileTransfer
%find_lang %{name}

%post
%desktop_database_post
%icon_theme_cache_post

%postun
%desktop_database_postun
%icon_theme_cache_postun

%files -f %{name}.lang
%defattr(-,root,root,-)
%doc COPYING README ChangeLog AUTHORS
%{_bindir}/%{name}
%{_libdir}/%{name}/
%{_libexecdir}/%{name}/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/pixmaps/%{name}.png
%{_mandir}/man1/%{name}.1.gz

%changelog
