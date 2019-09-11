#
# spec file for package packETH
#
# Copyright (c) 2015 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           packETH
Version:        1.8.1
Release:        0
Summary:        Packet generator tool for ethernet
License:        GPL-3.0+
Group:          Productivity/Networking/Diagnostic
Url:            http://packeth.sourceforge.net/packeth/Home.html
Source0:        http://downloads.sourceforge.net/project/packeth/packETH-%{version}.tar.bz2
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
packETH is tool for generating packets to send over ethernet.

%prep
%setup -q
# yay, lm is not in checked libs
sed -i -e 's:$(DEPS_LIBS):$(DEPS_LIBS) -lm:' Makefile.in

%build
%configure
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install %{?_smp_mflags}

%files
%defattr(-,root,root)
%doc COPYING CHANGELOG AUTHORS
%{_bindir}/%{name}
%{_datadir}/packeth

%changelog
