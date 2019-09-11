#
# spec file for package ifuse
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           ifuse
Version:        1.1.3
Release:        0
Summary:        Filesystem access for Apple devices
License:        LGPL-2.0+
Group:          System/Filesystems
Url:            http://www.libimobiledevice.org
Source:         %{name}-%{version}.tar.bz2
BuildRequires:  fuse-devel
BuildRequires:  libimobiledevice-devel
BuildRequires:  libplist-devel
BuildRequires:  pkg-config
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
iFuse is a FUSE filesystem driver which uses `libimobiledevice` to connect to
devices without the need for a jailbreak.
It is using the native Apple "AFC" protocol, over the normal USB cable in order
to access the iPhone's, iPod Touch's or iPad's media files under Linux.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root)
%doc AUTHORS COPYING README NEWS
%{_bindir}/ifuse
%doc %{_mandir}/man1/ifuse.1.*

%changelog
