#
# spec file for package packETH
#
# Copyright (c) 2021 SUSE LLC
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


# Uses x86 ASM
%ifarch %ix86 x86_64 amd64 ia32e
%bcond_without cli
%else
%bcond_with cli
%endif
Name:           packETH
Version:        2.1
Release:        0
Summary:        Packet generator tool for ethernet
License:        GPL-3.0-or-later
Group:          Productivity/Networking/Diagnostic
URL:            http://packeth.sourceforge.net/packeth/Home.html
Source0:        https://github.com/jemcek/packETH/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
# PATCH-FIX-UPSTREAM e72195b573.patch -- https://github.com/jemcek/packETH/pull/22
Patch0:         https://github.com/jemcek/packETH/commit/e72195b573.patch
BuildRequires:  automake
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(glib-2.0) >= 2.4
BuildRequires:  pkgconfig(gthread-2.0)
BuildRequires:  pkgconfig(gtk+-2.0) >= 2.4

%description
packETH is tool for generating packets to send over ethernet.

%if %{with cli}

%package cli
Summary:        CLI only packet generator tool for ethernet
Group:          Productivity/Networking/Diagnostic

%description cli
packETHcli is a command line version of packETH.

It allows you to easily send packets from pcap file.
It has different sending options although not all features from packETH are supported.
It also has a receiver mode where packets sent by packETH or packETHcli can be captured
and checked for errors.

%files cli
%license COPYING
%doc cli/NEWS cli/README
%{_bindir}/packETHcli

%endif

%prep
%autosetup -p1

%build
autoreconf -fi
%configure
%make_build
%if %{with cli}
# CLI
pushd cli
%make_build CFLAGS="%{optflags}"
popd
%endif

%install
%make_install
%if %{with cli}
install -D -m 0755 cli/packETHcli %{buildroot}%{_bindir}/packETHcli
%endif

%files
%license COPYING
%doc CHANGELOG AUTHORS
%{_bindir}/%{name}
%{_datadir}/packeth

%changelog
