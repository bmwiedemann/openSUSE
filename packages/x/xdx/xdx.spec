#
# spec file for package xdx
#
# Copyright (c) 2017 Walter Fey DL8FCL
# Copyright (c) 2025 Andreas Stieger <Andreas.Stieger@gmx.de>
#
# This file is under MIT license

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Name:           xdx
Version:        2.91
Release:        0
Summary:        Dx-cluster client for amateur radio
License:        GPL-2.0-or-later
Group:          Productivity/Hamradio/Other
URL:            https://github.com/N0NB/xdx/
Source:         https://github.com/N0NB/xdx/releases/download/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gtk+-3.0)

%description
Xdx is a dedicated network client for amateur radio operators who want
to exchange DX (long distance) radio information. After connection
to a DX-cluster, xdx will show DX-spots in a list and other messages
('To all' and WWV/WCY messages) in a text widget.

%prep
%autosetup -p1

%build
%configure
%make_build

%install
%make_install
%find_lang %{name}
mkdir -p %{buildroot}/%{_docdir}/%{name}
mv -v %{buildroot}/%{_datadir}/%{name}/MANUAL* %{buildroot}/%{_docdir}/%{name}

%check
%make_build check

%files -f %{name}.lang
%license COPYING
%doc AUTHORS ChangeLog NEWS README TODO
%{_bindir}/xdx
%{_datadir}/%{name}
%{_docdir}/%{name}
%{_mandir}/man1/xdx.1%{?ext_man}
%{_datadir}/applications/Xdx.desktop

%changelog
