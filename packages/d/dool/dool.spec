#
# spec file for package dool
#
# Copyright (c) 2025 SUSE LLC
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


Name:           dool
Version:        1.3.8
Release:        0
Summary:        Versatile vmstat, iostat and ifstat replacement
License:        GPL-2.0-only
Group:          System/Monitoring
URL:            https://github.com/scottchiefbaker/dool
Source:         https://github.com/scottchiefbaker/dool/archive/refs/tags/v%{version}.tar.gz
Source1:        %{name}.desktop
BuildRequires:  fdupes
BuildRequires:  make
Requires:       python3-curses
Requires:       python3-six
Provides:       dstat = %{version}
Obsoletes:      dstat <= 0.7.4
BuildArch:      noarch

%description
Dool is a command line tool to monitor many aspects of your Linux system: CPU, Memory, Network, Load Average, etc. It also includes a robust plug-in architecture to allow monitoring other system metrics.

Dool is a Python3 compatible fork of Dstat.

%prep
%autosetup -p1
sed -i 's/#!\/usr\/bin\/env python/#!\/usr\/bin\/python/' dool

%build

%install
make %{?_smp_mflags} DESTDIR=%{buildroot} install docs-install
install -D -m 0644 "%{SOURCE1}" "%{buildroot}%{_datadir}/applications/%{name}.desktop"

rm docs/Makefile
%fdupes "%{buildroot}%{_datadir}/%{name}"

%files
%license LICENSE
%doc AUTHORS ChangeLog README.md
%doc docs/*.html docs/*.adoc
%{_bindir}/%{name}
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*
%{_mandir}/man1/%{name}.1%{?ext_man}
%{_datadir}/applications/%{name}.desktop

%changelog
