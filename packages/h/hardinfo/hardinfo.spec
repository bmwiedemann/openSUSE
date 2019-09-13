#
# spec file for package hardinfo
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           hardinfo
Version:        0.5.1
Release:        0
Summary:        Displays system information
License:        GPL-2.0-only
Group:          System/Benchmark
Url:            http://hardinfo.org/
Source:         http://downloads.sf.net/%{name}.berlios/%{name}-%{version}.tar.gz
# PATCH-FIX-UPSTREAM hardinfo-0.5.1-reproducible.patch bwiedemann@suse.com -- make build reproducible
Patch0:         hardinfo-0.5.1-reproducible.patch
BuildRequires:  fdupes
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(libffi)
BuildRequires:  pkgconfig(libselinux)
BuildRequires:  pkgconfig(libsoup-2.4)
BuildRequires:  pkgconfig(mount)
Recommends:     apcupsd
Recommends:     sensors
ExclusiveArch:  %ix86 x86_64

%description
HardInfo is a small application that displays information about your
hardware and operating system.

Currently it knows about PCI, ISA PnP, USB, IDE, SCSI, Serial and
parallel port devices.

%prep
%setup -q
%patch0 -p1

cat > %{name}.desktop << EOF
[Desktop Entry]
Type=Application
Name=HardInfo
GenericName=HardInfo
Exec=%{name} %U
Comment=System Profiler and Benchmark
Comment[pt_BR]=Informações e Testes do Sistema
Comment[ru]=Системный профайлер и бенчмарк
Comment[uk]=Системний профайлер і бенчмарк
Icon=%{name}
Categories=System;Utility;DesktopUtility;Monitor;
EOF

%build
%if 0%{?suse_version} < 1500
SOURCE_DATE="$(sed -n '/^----/n;s/ - .*$//;p;q' "%{_sourcedir}/%{name}.changes")"
export SOURCE_DATE_EPOCH="$(date -d "$SOURCE_DATE" "+%%s")"

%endif
%configure --prefix=%{_prefix}
make ARCHOPTS="%{optflags} -fgnu89-inline" %{?_smp_mflags}

%install
%make_install
install -Dpm 0644 pixmaps/logo.png %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/%{name}.png
%suse_update_desktop_file %{name}
%fdupes %{buildroot}

%if 0%{?suse_version} < 1500
%post
%desktop_database_post
%icon_theme_cache_post

%postun
%desktop_database_postun
%icon_theme_cache_postun
%endif

%files
%doc LICENSE
%{_bindir}/%{name}
%{_libdir}/%{name}/
%{_datadir}/%{name}/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.*

%changelog
