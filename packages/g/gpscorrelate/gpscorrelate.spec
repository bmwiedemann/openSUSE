#
# spec file for package gpscorrelate
#
# Copyright (c) 2026 SUSE LLC
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


Name:           gpscorrelate
Version:        2.3
Release:        0
Summary:        Tool for setting EXIF GPS data
License:        GPL-2.0-or-later
URL:            https://dfandrich.github.io/gpscorrelate/
Source:         https://github.com/dfandrich/gpscorrelate/releases/download/%{version}/%{name}-%{version}.tar.xz
BuildRequires:  desktop-file-utils
# The exiv2 command line tool is what the regression test suite compares against
BuildRequires:  exiv2
BuildRequires:  gcc-c++
BuildRequires:  gettext-tools
BuildRequires:  make
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(exiv2)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libxml-2.0)
Recommends:     %{name}-doc
Recommends:     %{name}-gui

%description
GPS Correlate takes a GPS track stored by any of a number of
GPS devices and phone apps and correlates the time stamp of
a digital photo with the location of the track at that same
moment. The location of the image is then stamped directly
into the image file using the appropriate EXIF GPS tags. The
resulting image then contains not just the time the photo was
taken but its exact location, too. The location is used by
various other applications and services (such as Google Photos)
to display a map of where the photo was taken.

This package contains the command line tool and the documentation.

%package doc
Summary:        HTML manual for GPS Correlate
BuildArch:      noarch

%description doc
GPS Correlate stamps the location recorded in a GPS track into the EXIF
GPS tags of digital photos taken at the same time.

This package contains the HTML manual in English and French, which is also
what the graphical interface opens from its Help menu.

%package gui
Summary:        Graphical interface for GPS Correlate
Requires:       %{name} = %{version}
Requires:       %{name}-doc = %{version}

%description gui
GPS Correlate stamps the location recorded in a GPS track into the EXIF
GPS tags of digital photos taken at the same time.

This package contains the GTK graphical user interface.

%prep
%autosetup -p1
# The tarball ships the DocBook-generated manual page and HTML documentation
# with upstream's default /usr/local doc directory baked in.  Regenerating them
# would fetch the DocBook XSL over the network, so rewrite the path instead and
# make sure the build does not consider them out of date.
sed -i 's,%{_prefix}/local/share/doc/%{name},%{_docdir}/%{name},g' \
    doc/%{name}-manpage.xml doc/%{name}.1 doc/%{name}.html
touch doc/%{name}-manpage.xml doc/%{name}.1 doc/%{name}.html

%build
# prefix and docdir have to be passed here as well as to make install: the
# Makefile compiles both of them into the binaries (PACKAGE_LOCALE_DIR and
# PACKAGE_DOC_DIR), so with the defaults the GUI help would point into
# /usr/local and the message catalogs would never be found.
# Native language support is off unless ENABLE_NLS is defined, see INSTALL.
%make_build \
    prefix=%{_prefix} \
    docdir=%{_docdir}/%{name} \
    CFLAGS="%{optflags} -DENABLE_NLS" \
    CXXFLAGS="%{optflags} -DENABLE_NLS" \
    LDFLAGS="%{optflags} -lm"
%make_build build-po prefix=%{_prefix}

%install
%make_install prefix=%{_prefix} docdir=%{_docdir}/%{name}
make install-po DESTDIR=%{buildroot} prefix=%{_prefix}
make install-desktop-file DESTDIR=%{buildroot} prefix=%{_prefix} INSTALL="install -p"
install -Dpm 0644 io.github.dfandrich.%{name}.metainfo.xml \
    %{buildroot}%{_datadir}/metainfo/io.github.dfandrich.%{name}.metainfo.xml
# The icon is installed by install-desktop-file, no need to ship it twice
rm -f %{buildroot}%{_docdir}/%{name}/*.svg

%find_lang %{name}

%check
%make_build check CHECK_OPTIONS="-v"
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%files -f %{name}.lang
%license COPYING
%doc AUTHORS README.md RELEASES
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1%{?ext_man}

%files doc
%dir %{_docdir}/%{name}
%{_docdir}/%{name}/*.html
%{_docdir}/%{name}/*.png
%dir %{_docdir}/%{name}/fr
%{_docdir}/%{name}/fr/*.html
%{_docdir}/%{name}/fr/*.png

%files gui
%{_bindir}/%{name}-gui
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{name}-gui.svg
%{_datadir}/metainfo/io.github.dfandrich.%{name}.metainfo.xml

%changelog
