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
Version:        3.0.5
Release:        0
Summary:        A Multiplatform Word Processor
# FIXME next version: check if the telepathy support still requires old version of empathy (with libempathy-gtk)
# FIXME: package aiksaurus, libots, mathview-frontend-libxml2
License:        GPL-2.0-or-later
Group:          Productivity/Office/Word Processor
URL:            http://www.abisource.com/
Source0:        http://abisource.com/downloads/abiword/%{version}/source/%{name}-%{version}.tar.gz
Source1:        abiword.appdata.xml
# PATCH-FIX-UPSTREAM abiword-librevenge.patch fstrba@suse.com -- Fix build against librevenge-based libraries (svn revs 34461, 34462, 34463, 34464 and 34468)
Patch5:         abiword-librevenge.patch
# PATCH-FIX-UPSTREAM abiword-libwps-0.4.patch dimstar@opensuse.org -- Port to libwps-0.4; patch taken from Fedora.
Patch6:         abiword-libwps-0.4.patch
# PATCH-FIX-UPSTREAM boost_asio.patch adam.majer@suse.de -- Add support for boost::asio
Patch7:         boost_asio.patch
# PATCH-FIX-UPSTREAM xml-inc.patch -- Add missing include
Patch8:         xml-inc.patch
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
# FIXME: requires libgda >= 1.2.0 libgnomedb >= 1.2.0 and we have
# libgda-[34].0.pc
#BuildRequires:  libgda-4_0-devel
#BuildRequires:  libgnomedb-devel
# FIXME: missing BuildRequires as of 05/12/2009:
# Aiksaurus.h not found
# libots-1 >= 0.5.0
# mathview-frontend-libxml2 >= 0.7.5
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
%autosetup -p0

%build
# We modified plugin configuration and thus we need to regenerate the whole build system
# The following script is lifted from upstream autogen-common.sh file that is not
# distributed in the release tarball.
rm -rf plugins/aiksaurus
find plugins -name Makefile.am | sed  's|.am$||g' > plugin-makefiles.m4
find plugins -maxdepth 1 -type d | grep -v -e '^\.$' -e '\./\.' | sed 's|plugins/||g' | xargs echo > plugin-list.m4
(for plugin in `cat plugin-list.m4`; do
        u=`echo $plugin | tr '[:lower:]' '[:upper:]'`
        echo 'AM_CONDITIONAL(['$u'_BUILTIN], test "$enable_'$plugin'_builtin" = "yes")'
done) > plugin-builtin.m4
find plugins -name plugin.m4 | xargs cat > plugin-configure.m4
for f in ` find ./plugins -name '*.m4' | grep -v 'plugin\.m4'`; do
    ln -sf $f
done
libtoolize --force --copy --install
autoreconf -fi

# -fno-strict-aliasing added 2009-04-12. Leave it in because we are
# not sure it is not needed any more and the performance cost of this
# option is cheaper then random undefined behaviours.
CFLAGS="%{optflags} -fno-strict-aliasing"
%if 0%{?suse_version} >= 1550
# Enforce std=c++14 as codebase is not c++17 (default for gcc 11) ready
CXXFLAGS="%{optflags} -std=c++14"
%endif
%configure \
        --disable-static \
        --enable-dynamic \
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
install -dm 0755 %{buildroot}%{_datadir}/appdata
install -Dm 0644 %{S:1} %{buildroot}%{_datadir}/appdata/abiword.appdata.xml
%fdupes %{buildroot}

%ldconfig_scriptlets -n libabiword-3_0

%files
%license COPYING
%doc AUTHORS COPYRIGHT.TXT
%{_bindir}/*
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
