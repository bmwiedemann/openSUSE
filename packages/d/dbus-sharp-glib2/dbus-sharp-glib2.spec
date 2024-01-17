#
# spec file for package dbus-sharp-glib2
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


Name:           dbus-sharp-glib2
Version:        0.6.0
Release:        0
Summary:        Glib integration for DBus
License:        MIT
Group:          Development/Libraries/Other
URL:            http://mono.github.com/dbus-sharp-glib/
Source:         https://github.com/mono/dbus-sharp-glib/releases/download/v0.6/dbus-sharp-glib-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch
BuildRequires:  pkgconfig
%if 0%{?suse_version} >= 1130
BuildRequires:  pkgconfig(dbus-sharp-2.0)
BuildRequires:  pkgconfig(mono)
%else
BuildRequires:  dbus-sharp-devel
BuildRequires:  mono-devel
%endif
Requires:       dbus-sharp

%description
This package provides glib integration for Mono.DBus.

%package devel
Summary:        Glib integration for DBus - development files
Group:          Development/Libraries/Other
Requires:       %{name} = %{version}

%description devel
This package provides glib integration for Mono.DBus - Development
files.

%prep
%setup -q -n dbus-sharp-glib-%{version}

%build
# '--target' required on <= 1110 else build fails using configure macro
%configure \
%if 0%{?suse_version} <= 1110
   --target=%{_arch} \
%endif
   --libdir=%{_prefix}/lib
make %{?_smp_mflags}

%install
# For backward compatability with <= 1110
make DESTDIR=%{buildroot} install
# Move .pc file to /usr/share/pkgconfig (for no arch) and remove from libdir
install -Dm 0644 dbus-sharp-glib-2.0.pc %{buildroot}%{_datadir}/pkgconfig/dbus-sharp-glib-2.0.pc
find %{buildroot}%{_prefix}/lib -name dbus-sharp-glib-2.0.pc -type f -print -delete

%files
%defattr(-,root,root)
%doc COPYING README
%{_prefix}/lib/mono/gac/dbus-sharp-glib/
%{_prefix}/lib/mono/dbus-sharp-glib-2.0/

%files devel
%defattr(-,root,root)
%{_datadir}/pkgconfig/dbus-sharp-glib-2.0.pc

%changelog
