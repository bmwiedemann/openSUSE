#
# spec file for package ndesk-dbus
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


Name:           ndesk-dbus
Version:        0.6.1a
Release:        0
Summary:        Managed C# implementation of D-Bus
License:        MIT
Group:          Development/Libraries/Other
URL:            http://www.ndesk.org/DBusSharp
Source0:        http://www.ndesk.org/archive/dbus-sharp/ndesk-dbus-0.6.1a.tar.gz
BuildRequires:  mono-devel
BuildRequires:  pkgconfig
Provides:       ndesk-dbus-devel = %version
Obsoletes:      ndesk-dbus-devel < %version
BuildArch:      noarch

%description
This is a C# implementation of D-Bus. It's often referred to as
"managed D-Bus" to avoid confusion with existing bindings (which wrap
libdbus).

It is a clean-room implementation based on the D-Bus Specification
Version 0.11 and study of the wire protocol of existing tools.

%prep
%setup -q

%build
%configure --libdir="%_prefix/lib"
%make_build

%install
# This is all noarch, so the .pc file can go to %%_datadir.
%make_install pkgconfigdir="%_datadir/pkgconfig"

%files
%license COPYING
%doc README
%_prefix/lib/mono/gac/NDesk.DBus
%_prefix/lib/mono/ndesk-dbus-1.0
%_datadir/pkgconfig/ndesk-dbus-1.0.pc

%define _use_internal_dependency_generator 0
%define __find_provides env sh -c 'filelist=($(cat)) && { printf "%s\\n" "${filelist[@]}" | /usr/lib/rpm/find-provides && printf "%s\\n" "${filelist[@]}" | /usr/bin/mono-find-provides ; } | sort | uniq'
%define __find_requires env sh -c 'filelist=($(cat)) && { printf "%s\\n" "${filelist[@]}" | /usr/lib/rpm/find-requires && printf "%s\\n" "${filelist[@]}" | /usr/bin/mono-find-requires ; } | sort | uniq'

%changelog
