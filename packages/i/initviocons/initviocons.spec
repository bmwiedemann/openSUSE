#
# spec file for package initviocons
#
# Copyright (c) 2023 SUSE LLC
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


Name:           initviocons
URL:            http://svn.poeml.de/viewcvs/initviocons/
Version:        0.5
Release:        0
Summary:        Terminal Initialization, e.g. for the iSeries Virtual Console
License:        GPL-2.0-or-later
Group:          System/Console
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  automake
Source:         initviocons-%{version}.tar.bz2

%description
Initviocons can be used on the iSeries platform to recognize terminal
features of a telnet client that is connected to the virtual console
(similar to a serial console). It probes the terminal via escape
sequences to find out the screen size and a suitable TERM type. It also
does special initialization if possible (for example, carriage return
suppression for Windows telnet clients). On the iSeries platform, it
additionally checks for the presence of more than one terminal
connected on the same line. See /etc/profile for a usage example.



Authors:
--------
    Peter Poeml <poeml@suse.de>

%prep
%setup -n initviocons-%{version}

%build
autoreconf -fi
%configure
make CFLAGS="$RPM_OPT_FLAGS -Wall"

%install
%make_install
install -m 0755 termprobes $RPM_BUILD_ROOT/%{_bindir}/termprobes
%if 0%{?suse_version} < 1550
mkdir -p $RPM_BUILD_ROOT/bin
ln -sf %{_bindir}/initviocons $RPM_BUILD_ROOT/bin
%endif

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog COPYING NEWS README
%if 0%{?suse_version} < 1550
/bin/*
%endif
%{_bindir}/*

%changelog
