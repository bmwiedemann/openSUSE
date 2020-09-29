#
# spec file for package dbus-sharp2
#
# Copyright (c) 2020 SUSE LLC
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


Name:           dbus-sharp2
Version:        0.8.1
Release:        0
Summary:        Managed C# implementation of D-Bus
License:        MIT
Group:          Development/Libraries/Other
URL:            http://mono.github.com/dbus-sharp/
Source0:        https://github.com/mono/dbus-sharp/releases/download/v%{version}/dbus-sharp-%{version}.tar.gz
Patch0:         fix-delay-sign.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildArch:      noarch
%if 0%{?suse_version} >= 1130
BuildRequires:  pkgconfig(mono)
%else
BuildRequires:  mono-devel
%endif

%description
This is DBus-Sharp, a fork of ndesk-dbus or simply a C# implementation
of D-Bus.

It is a clean-room implementation based on the D-Bus Specification
Version 0.11 and study of the wire protocol of existing tools.

%package devel
Summary:        Managed C# implementation of D-Bus
Group:          Development/Libraries/Other
Requires:       %{name} = %{version}

%description devel
This is DBus-Sharp, a fork of ndesk-dbus or simply a C# implementation
of D-Bus.

It is a clean-room implementation based on the D-Bus Specification
Version 0.11 and study of the wire protocol of existing tools.

%prep
%setup -q -n dbus-sharp-%{version}
%patch0 -p1

%build
autoreconf -fiv
%configure \
   --libdir=%{_prefix}/lib
make %{?_smp_mflags}

%install
# For backward compatability with <= 1110
make DESTDIR=%{buildroot} install
# Move .pc file to /usr/share/pkgconfig (for no arch) and remove from libdir
install -Dm 0644 dbus-sharp-2.0.pc %{buildroot}%{_datadir}/pkgconfig/dbus-sharp-2.0.pc
find %{buildroot}%{_prefix}/lib -name dbus-sharp-2.0.pc -type f -print -delete

%files
%defattr(-,root,root)
%doc COPYING README
%{_prefix}/lib/mono/gac/dbus-sharp/
%{_prefix}/lib/mono/dbus-sharp-2.0/

%files devel
%defattr(-,root,root)
%{_datadir}/pkgconfig/dbus-sharp-2.0.pc

%changelog
