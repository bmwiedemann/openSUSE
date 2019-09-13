#
# spec file for package sobby
#
# Copyright (c) 2012 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           sobby
Version:        0.4.8
Release:        0
Summary:        Stand-alone obby server
License:        GPL-2.0+
Group:          System/GUI/GNOME
Url:            http://gobby.0x539.de/
Source:         http://releases.0x539.de/sobby/%{name}-%{version}.tar.gz
BuildRequires:  gcc-c++
BuildRequires:  gmp-devel
BuildRequires:  libavahi-glib-devel
BuildRequires:  obby-devel
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(glibmm-2.4)
BuildRequires:  pkgconfig(libxml++-2.6)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
sobby is a stand-alone obby server. It currently runs under Unix-like
platforms only.

%prep
%setup -q

%build
%configure --disable-static --with-pic
make %{?jobs:-j%jobs}

%install
%makeinstall

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-, root, root)
%doc AUTHORS COPYING ChangeLog NEWS README
%{_bindir}/sobby
%doc %{_mandir}/man1/sobby.*

%changelog
