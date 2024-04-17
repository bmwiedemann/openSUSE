#
# spec file for package filezilla
#
# Copyright (c) 2024 SUSE LLC
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


%define libversion 3.67.0
%define libfilezillaversion 0.47.0

Name:           filezilla
Version:        3.67.0
Release:        0
Summary:        A GUI FTP and SFTP Client
License:        GPL-2.0-or-later
Group:          Productivity/Networking/Ftp/Clients
URL:            https://filezilla-project.org/
Source0:        https://download.filezilla-project.org/client/FileZilla_%{version}_src.tar.xz
Patch0:         %{name}-welcome_dialog.patch
Patch1:         disable-avx-on-i586.patch
Patch2:         %{name}-verifyhostkeydialog.patch
Patch3:         %{name}-sftp_crypt_info_dlg.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
%if 0%{?suse_version} > 1500
BuildRequires:  libboost_regex-devel >= 1.76.0
%else
BuildRequires:  libboost_regex-devel-impl >= 1.76.0
%endif
BuildRequires:  libtool
BuildRequires:  pkgconfig
# needs long long support in pugixml
BuildRequires:  pugixml-devel >= 1.7
BuildRequires:  update-desktop-files
BuildRequires:  wxWidgets-3_2-devel >= 3.2.1
BuildRequires:  xdg-utils
BuildRequires:  pkgconfig(cppunit)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(libfilezilla) >= %{libfilezillaversion}
BuildRequires:  pkgconfig(libidn)
BuildRequires:  pkgconfig(nettle) >= 3.1
BuildRequires:  pkgconfig(sqlite3) >= 3.7.0
# See boo#966384 filezilla fails to start
Requires:       libpugixml1 >= 1.7
Recommends:     %{name}-lang
# upstream use gnutls 3.8.0
%if 0%{?suse_version} > 1500
BuildRequires:  pkgconfig(gnutls) >= 3.7.9
%else
BuildRequires:  pkgconfig(gnutls) >= 3.7.3
%endif

%description
FileZilla is a modern and powerful FTP client.
FileZilla development focuses on high usability while also
supporting as many useful features as possible.

Some of the main features are:
 * Continuing interrupted up-/downloads.
 * Managing different FTP sites.
 * Modifiable Commands.
 * Keep-Alive-System.
 * Timeout detection.
 * Firewall support.
 * SOCKS4/5 and HTTP 1.1 proxy support.
 * SSL support (secure connections).
 * SFTP support.
 * Upload/Download queue.
 * Drag&Drop support.

%package devel
Summary:        Development files for filezilla
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}

%description devel
This are development files for filezilla.

%lang_package

%prep
%autosetup -p1

%build
autoreconf -fi
%configure \
  --disable-static            \
  --disable-manualupdatecheck \
  --disable-autoupdatecheck   \
  --with-dbus
%make_build

%install
%make_install
%suse_update_desktop_file %{name}
%fdupes %{buildroot}%{_datadir}/
%find_lang %{name}

%check
%make_build check

%post -p /sbin/ldconfig
%desktop_database_post
%icon_theme_cache_post

%postun -p /sbin/ldconfig
%desktop_database_postun
%icon_theme_cache_postun

%files
%license COPYING
%doc README NEWS
%{_bindir}/%{name}
%{_bindir}/fzsftp
%{_bindir}/fzputtygen
%{_datadir}/%{name}/
%{_datadir}/applications/%{name}.desktop
%dir %{_datadir}/icons/hicolor/480x480
%dir %{_datadir}/icons/hicolor/480x480/apps
%{_datadir}/icons/hicolor/*/apps/%{name}.*
%{_datadir}/pixmaps/%{name}.png
%dir %{_datadir}/appdata/
%{_datadir}/appdata/%{name}.appdata.xml
%{_libdir}/libfzclient-commonui-private-%{libversion}.so
%{_libdir}/libfzclient-private-%{libversion}.so
%{_mandir}/man1/filezilla.1%{?ext_man}
%{_mandir}/man1/fzputtygen.1%{?ext_man}
%{_mandir}/man1/fzsftp.1%{?ext_man}
%{_mandir}/man5/fzdefaults.xml.5%{?ext_man}

%files devel
%{_libdir}/libfzclient-commonui-private.la
%{_libdir}/libfzclient-commonui-private.so
%{_libdir}/libfzclient-private.la
%{_libdir}/libfzclient-private.so

%files lang -f %{name}.lang

%changelog
