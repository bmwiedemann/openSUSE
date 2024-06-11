#
# spec file for package engrampa
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


%define _version 1.28

Name:           engrampa
Version:        1.28.1
Release:        0
Summary:        MATE Desktop archive manager
License:        GPL-2.0-or-later AND LGPL-2.0-or-later
Group:          Productivity/Archiving/Compression
URL:            https://mate-desktop.org/
Source:         https://pub.mate-desktop.org/releases/%{_version}/%{name}-%{version}.tar.xz
BuildRequires:  caja >= %{_version}
BuildRequires:  hicolor-icon-theme
BuildRequires:  mate-common >= %{_version}
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  yelp-tools
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libcaja-extension) >= %{_version}
%if 0%{?suse_version} >= 1560
BuildRequires:  pkgconfig(libmagic)
%else
BuildRequires:  file-devel
%endif
BuildRequires:  pkgconfig(sm)
Recommends:     %{name}-lang
# Formats that we likely want to support by default.
Recommends:     bzip2
Recommends:     cpio
Recommends:     gzip
Recommends:     rpm
Recommends:     unar
Recommends:     unzip
Recommends:     xz
Recommends:     zip
# Additional formats that are supported.
Suggests:       lhasa
Suggests:       lzip
Suggests:       lzop
Suggests:       rzip
Suggests:       zoo
# FIXME: Formats for which we don't have packages. Some are free software that
# we could package.
#Suggests:       lrzip
#Suggests:       arj
#Suggests:       ncompress
#Suggests:       rar
#Suggests:       unace
#Suggests:       unalz
#Suggests:       unstuff
# mate-file-archiver was last used in openSUSE 13.1.
Provides:       mate-file-archiver = %{version}
Obsoletes:      mate-file-archiver < %{version}
Obsoletes:      mate-file-archiver-lang < %{version}
%glib2_gsettings_schema_requires
%if 0%{?suse_version} > 1500
Recommends:     7zip
%else
Recommends:     p7zip
%endif

%description
Engrampa is an archive manager for the MATE Desktop Environment.
This means that you can create and modify archives; view the
content of an archive; view and modify a file contained in the
archive; extract files from the archive.

%lang_package

%package -n caja-%{name}
Summary:        MATE Desktop engrampa plugin for caja
Requires:       %{name} = %{version}-%{release}
# mate-file-manager-engrampa was last used in openSUSE 13.1.
Provides:       mate-file-manager-%{name} = %{version}
Obsoletes:      mate-file-manager-%{name} < %{version}

%description -n caja-engrampa
Engrampa is an archive manager for the MATE Desktop Environment.
This means that you can create and modify archives; view the
content of an archive; view and modify a file contained in the
archive; extract files from the archive.

%prep
%autosetup -p1

%build
NOCONFIGURE=1 mate-autogen
%configure \
  --disable-static                    \
  --disable-scrollkeeper              \
  --enable-magic                      \
  --libexecdir=%{_libexecdir}/%{name}
%make_build

%install
%make_install

%find_lang %{name} %{?no_lang_C}
find %{buildroot} -type f -name "*.la" -delete -print

%files
%license COPYING
%doc AUTHORS NEWS README
%{_bindir}/%{name}
%{_libexecdir}/%{name}/
%{_datadir}/dbus-1/services/org.mate.Engrampa.service
%{_datadir}/%{name}/
%{_datadir}/glib-2.0/schemas/*.xml
%{_datadir}/help/C/%{name}/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/*/*
%dir %{_datadir}/metainfo/
%{_datadir}/metainfo/%{name}.appdata.xml
%{_mandir}/man?/%{name}.?%{?ext_man}

%files -n caja-%{name}
%{_datadir}/caja/extensions/libcaja-engrampa.caja-extension
%{_libdir}/caja/extensions-2.0/libcaja-%{name}.so

%files lang -f %{name}.lang

%changelog
