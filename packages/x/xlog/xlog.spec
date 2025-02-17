#
# spec file for package xlog
#
# Copyright (c) 2019 Walter Fey DL8FCL
# Copyright (c) 2025 Andreas Stieger <Andreas.Stieger@gmx.de>
#
# This file is under MIT license

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Name:           xlog
Version:        2.0.25
Release:        0
Summary:        Logging program for Amateur radio
License:        GPL-3.0-or-later
Group:          Productivity/Hamradio/Logging
URL:            https://www.nongnu.org/xlog/
Source:         https://download.savannah.nongnu.org/releases/xlog/%{name}-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(hamlib)

%description
Xlog, a logging program for Amateur Radio Operators.

%prep
%autosetup -p1

%build
%configure
%make_build

%install
%make_install
%find_lang %{name}
mkdir -p %{buildroot}/%{_docdir}/%{name}
mv %{buildroot}/%{_datadir}/doc/xlog/* %{buildroot}/%{_docdir}/%{name}/
%fdupes %{buildroot}/%{_prefix}

%check
%make_build check

%files -f %{name}.lang
%license COPYING
%doc AUTHORS NEWS README
%{_bindir}/%{name}
%{_datadir}/xlog/
%{_datadir}/applications/*
%{_mandir}/man1/xlog.1%{?ext_man}
%{_datadir}/mime/packages/xlog.xml
%{_datadir}/pixmaps/xlog*
%{_datadir}/icons/hicolor/scalable/apps/xlog.svg
%doc %{_docdir}/xlog

%changelog
