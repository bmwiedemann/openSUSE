#
# spec file for package fwknop-gui
#
# Copyright (c) 2022 SUSE LLC
# Copyright (c) 2019, Martin Hauke <mardnh@gmx.de>
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


Name:           fwknop-gui
Version:        1.3.1
Release:        0
Summary:        FireWall KNock OPerator Graphical User Interface
License:        GPL-3.0-or-later
Group:          Productivity/Networking/Security
URL:            https://incomsystems.biz/fwknop-gui/
#Git-Clone:     https://github.com/jp-bennett/fwknop-gui.git
Source:         https://incomsystems.biz/fwknop-gui/downloads/fwknop-gui-%{version}.tar.gz
Patch0:         fwknop-gui-fix-manpage-path.patch
BuildRequires:  asciidoc
BuildRequires:  cmake
BuildRequires:  dblatex
BuildRequires:  gcc-c++
BuildRequires:  libfko-devel
BuildRequires:  libgpgmepp-devel
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  wxWidgets-devel >= 3.0.0
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libqrencode)

%description
The FireWall KNock OPerator implements an authorization scheme called
Single Packet Authorization (SPA), based on Netfilter and libpcap.

Its main application is to protect services such as OpenSSH with an
additional layer of security in order to make the exploitation of
vulnerabilities (both 0-day and unpatched code) much more difficult.

Fwknop GUI is a graphical user interface integrated with an Fwknop
client that provides the ability to send SPA packets to a remote
Fwknop server, as well as a front-end for creating and managing client
configurations for multiple Fwknop servers.

It supports exporting saved configuration data to a QR code format
readable by the Android client, as well as to the .fwknoprc format
readable by the command line client.

%prep
%setup -q -n %{name}
%patch0 -p1

%build
%cmake
%make_jobs

%install
%cmake_install
%suse_update_desktop_file -r %{name} Network RemoteAccess
install -D -m 0644 %{name}.appdata.xml %{buildroot}%{_datadir}/appdata/%{name}.appdata.xml

%files
%license LICENSE
%doc Changes README.md
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/appdata/%{name}.appdata.xml
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/help.html
%{_mandir}/man8/%{name}.8%{?ext_man}

%changelog
