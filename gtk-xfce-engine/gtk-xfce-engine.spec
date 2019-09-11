#
# spec file for package gtk-xfce-engine
#
# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           gtk-xfce-engine
Version:        3.2.0
Release:        0
Summary:        Xfce GTK+-2.0 Theme Engine
License:        GPL-2.0+
Group:          System/GUI/XFCE
Url:            http://www.xfce.org/
Source0:        http://archive.xfce.org/src/xfce/gtk-xfce-engine/3.2/%{name}-%{version}.tar.bz2
Source1:        baselibs.conf
BuildRequires:  fdupes
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gmodule-2.0)
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
The Xfce GTK theme engine provides various different themes which allow
for homogeneity in applications for both business and personal desktops.

%prep
%setup -q

%build
%configure --disable-static
make %{?_smp_mflags} V=1

%install
%make_install

find %{buildroot} -type f -name "*.la" -delete -print

%fdupes %{buildroot}%{_datadir}

%files
%defattr(-,root,root)
%doc AUTHORS NEWS COPYING ChangeLog
%{_libdir}/gtk-2.0/
%{_datadir}/themes/*

%changelog
