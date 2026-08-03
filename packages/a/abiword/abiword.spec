#
# spec file for package abiword
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


Name:           abiword
Version:        3.0.8
Release:        0
Summary:        A Multiplatform Word Processor
License:        GPL-2.0-or-later
Group:          Productivity/Office/Word Processor
URL:            https://gitlab.gnome.org/World/AbiWord/
Source0:        %{name}-%{version}.tar.xz

BuildRequires:  autoconf-archive
BuildRequires:  bison
BuildRequires:  dbus-1-glib-devel
BuildRequires:  fdupes
BuildRequires:  flex
BuildRequires:  gcc-c++
BuildRequires:  libboost_headers-devel
BuildRequires:  libgcrypt-devel
BuildRequires:  librsvg-devel
BuildRequires:  libsoup-devel
BuildRequires:  libtool
BuildRequires:  libwmf-devel
BuildRequires:  link-grammar-devel
BuildRequires:  pkgconfig
BuildRequires:  readline-devel
BuildRequires:  pkgconfig(asio)
BuildRequires:  pkgconfig(cairo) >= 1.10
BuildRequires:  pkgconfig(enchant) >= 1.2.0
BuildRequires:  pkgconfig(fribidi) >= 0.10.4
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.0.8
BuildRequires:  pkgconfig(libgoffice-0.10) >= 0.10.0
BuildRequires:  pkgconfig(libgsf-1) >= 1.14.18
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(librevenge-0.0)
BuildRequires:  pkgconfig(libwpd-0.10)
BuildRequires:  pkgconfig(libwpg-0.3)
BuildRequires:  pkgconfig(libwps-0.4)
BuildRequires:  pkgconfig(libxslt)
BuildRequires:  pkgconfig(wv-1.0) >= 1.2.0
Conflicts:      abiword-unstable
Recommends:     gnome-icon-theme

%description
AbiWord is a multiplatform word processor with a GTK+ interface on the
UNIX platform.

%package -n libabiword-3_0
Summary:        A Multiplatform Word Processor - Library files
Group:          System/Libraries

%description -n libabiword-3_0
AbiWord is a multiplatform word processor with a GTK+ interface on the
UNIX platform.

%package -n libabiword-3_0-devel
Summary:        A Multiplatform Word Processor - Development files
Group:          Development/Libraries/GNOME
Requires:       cairo-devel
Requires:       enchant-devel
Requires:       fribidi-devel
Requires:       glib2-devel
Requires:       goffice-devel
Requires:       gtk3-devel
Requires:       libabiword-3_0 = %{version}
Requires:       libgsf-devel
Requires:       librsvg-devel
Requires:       pango-devel
Requires:       wv-devel
Provides:       %{name}-devel = %{version}
Obsoletes:      %{name}-devel < %{version}

%description -n libabiword-3_0-devel
AbiWord is a multiplatform word processor with a GTK+ interface on the
UNIX platform.

%prep
%autosetup -p1

%build
NOCONFIGURE=1 ./autogen.sh
%configure \
        --disable-static \
        --enable-plugins \
        --enable-clipart \
        --enable-templates \
        --enable-collab-backend-xmpp \
        --enable-collab-backend-tcp \
        --enable-collab-backend-sugar \
        --enable-collab-backend-service \
        --enable-emacs-keybinding \
        --enable-vi-keybinding \
        %{nil}
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
%fdupes %{buildroot}%{_prefix}

%ldconfig_scriptlets -n libabiword-3_0

%files
%license COPYING
%doc AUTHORS COPYRIGHT.TXT
%{_bindir}/abiword
%dir %{_datadir}/appdata
%{_datadir}/appdata/abiword.appdata.xml
%{_datadir}/applications/abiword.desktop
%{_datadir}/icons/hicolor/*/apps/abiword.*
%{_mandir}/man?/abiword.*

%files -n libabiword-3_0
%{_libdir}/libabiword-*.so
%{_libdir}/abiword-3.0/
%{_datadir}/abiword-3.0/

%files -n libabiword-3_0-devel
%{_includedir}/abiword-3.0/
%{_libdir}/pkgconfig/abiword-3.0.pc

%changelog
