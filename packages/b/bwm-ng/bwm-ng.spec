#
# spec file for package bwm-ng
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           bwm-ng
Version:        0.6.2
Release:        0
Summary:        Realtime Bandwidth Monitor
License:        GPL-2.0-or-later
Group:          System/Monitoring
URL:            https://www.gropp.org/?id=projects&sub=bwm-ng
Source0:        https://github.com/vgropp/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        %{name}-icons.tar
Source2:        %{name}.desktop
BuildRequires:  glibc-devel
BuildRequires:  hicolor-icon-theme
BuildRequires:  libstatgrab-devel >= 0.91
BuildRequires:  libtool
BuildRequires:  ncurses-devel
BuildRequires:  net-tools

%description
Bandwidth Monitor NG is a console-based live bandwidth monitor.

- supports /proc/net/dev, netstat, getifaddr, sysctl, kstat and libstatgrab
- unlimited number of interfaces supported
- interfaces are added or removed dynamically from list
- white-/blacklist of interfaces
- output of KB/s, Kb/s, packets, errors, average, max and total sum
- output in curses, plain console, CSV or HTML
- configfile

%prep
%setup -q -a 1

%build
autoreconf -fi

%configure \
%ifarch x86_64 ppc64 s390x
	--enable-64bit \
%endif
	--enable-configfile \
	--enable-extendedstats \
	--with-ncurses \
	--with-time \
	--with-getopt_long \
	--with-getifaddrs \
	--with-sysctl \
	--with-sysctldisk \
	--with-procnetdev \
	--without-diskstats \
	--with-partitions \
	--with-libstatgrab \
	--with-netstatlinux \
	--with-strip=/usr/bin/touch
make %{?_smp_mflags}

%install
%make_install

# install icons
for i in 22 32 48 64 72 96 128 256; do
    install -Dm 0644 icons/%{name}_${i}x${i}.png %{buildroot}%{_datadir}/icons/hicolor/${i}x${i}/apps/%{name}.png
done

# install Desktop file
install -Dm 0644 %{S:2} %{buildroot}%{_datadir}/applications/%{name}.desktop

%files
%doc AUTHORS ChangeLog NEWS README THANKS bwm-ng.css bwm-ng.conf-example
%license COPYING
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1%{ext_man}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png

%changelog
