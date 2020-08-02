#
# spec file for package quvi
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           quvi
Version:        0.9.5
Release:        0
Summary:        Command line tool for parsing flash media stream URLs
License:        LGPL-2.1+
Group:          Productivity/Multimedia/Other
Url:            http://quvi.sourceforge.net/
Source:         http://sourceforge.net/projects/quvi/files/0.9/quvi/quvi-0.9.5.tar.xz
# PATCH-FIX-OPENSUSE
Patch0:         reproducible.patch
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(glib-2.0) >= 2.24
BuildRequires:  pkgconfig(gobject-2.0) >= 2.24
BuildRequires:  pkgconfig(json-glib-1.0) >= 0.12
BuildRequires:  pkgconfig(libcurl) >= 7.18.2
BuildRequires:  pkgconfig(libquvi-0.9) >= 0.9
BuildRequires:  pkgconfig(libxml-2.0) >= 2.7.8
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
quvi is a command line tool for parsing flash media stream URLs.
It supports many websites including YouTube and Dailymotion.

%prep
%setup -q
%patch0 -p1

%build
%configure \
    --disable-static
make %{?_smp_mflags}

%install
%make_install

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog COPYING NEWS README
%{_bindir}/quvi
%{_mandir}/man1/quvi.1%{?ext_man}
%{_mandir}/man1/quvi-dump.1%{?ext_man}
%{_mandir}/man1/quvi-get.1%{?ext_man}
%{_mandir}/man1/quvi-info.1%{?ext_man}
%{_mandir}/man1/quvi-scan.1%{?ext_man}
%{_mandir}/man5/quvirc.5%{?ext_man}

%changelog
