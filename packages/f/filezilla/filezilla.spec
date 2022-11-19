#
# spec file for package filezilla
#
# Copyright (c) 2022 SUSE LLC
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


Name:           filezilla
Version:        3.62.1
Release:        0
Summary:        A GUI FTP and SFTP Client
License:        GPL-2.0-or-later
Group:          Productivity/Networking/Ftp/Clients
URL:            https://filezilla-project.org/
Source0:        https://download.filezilla-project.org/client/FileZilla_%{version}_src.tar.bz2
Patch0:         %{name}-welcome_dialog.patch
Patch1:         disable-avx-on-i586.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  libtool
BuildRequires:  pkgconfig
# needs long long support in pugixml
BuildRequires:  pugixml-devel >= 1.7
BuildRequires:  update-desktop-files
BuildRequires:  wxWidgets-3_0-devel >= 3.0.4
BuildRequires:  xdg-utils
BuildRequires:  pkgconfig(cppunit)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(libfilezilla) >= 0.39.2
BuildRequires:  pkgconfig(libidn)
BuildRequires:  pkgconfig(nettle) >= 3.1
# filezilla-team use BuildRequires:  pkgconfig(sqlite3) >= 3.11.1
BuildRequires:  pkgconfig(sqlite3) >= 3.7.8
# See boo#966384 filezilla fails to start
Requires:       libpugixml1 >= 1.7
Recommends:     %{name}-lang
# upstream use gnutls 3.6.7
%if 0%{?suse_version} > 1500
BuildRequires:  pkgconfig(gnutls) >= 3.6.7
%else
BuildRequires:  pkgconfig(gnutls) >= 3.4.15
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
%setup -q
%patch0 -p1
%patch1 -p1

# Fix invalid translation locales:
cd locales
for LOC in\
    bg_BG\
    ca_ES@valencia\
    cs_CZ\
    fa_IR\
    fi_FI\
    gl_ES\
    he_IL\
    hu_HU\
    id_ID\
    ja_JP\
    km_KH\
    ko_KR\
    lo_LA\
    lt_LT\
    lv_LV\
    mk_MK\
    nb_NO\
    nn_NO\
    pl_PL\
    pt_BR\
    pt_PT\
    ro_RO\
    sk_SK\
    sl_SI\
    th_TH\
    uk_UA\
    vi_VN\
    zh_CN\
    zh_TW;
do
    mv -iv $LOC.po ${LOC/_??}.po
done

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
%{_libdir}/libfzclient-commonui-private-%{version}.so
%{_libdir}/libfzclient-private-%{version}.so
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
