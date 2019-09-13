#
# spec file for package ndesk-dbus
#
# Copyright (c) 2013 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           ndesk-dbus
Version:        0.6.0
Release:        0
%if 0%{?fedora_version}  
   %define env_options export MONO_SHARED_DIR=/tmp  
%endif  
%if 0%{?sles_version} == 9
   %define exp_env export PKG_CONFIG_PATH=$PKG_CONFIG_PATH:/opt/gnome/%{_lib}/pkgconfig
%endif
Summary:        Managed C# implementation of D-Bus
License:        MIT
Group:          Development/Libraries/Other
Url:            http://www.ndesk.org/DBusSharp
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Source0:        %{name}-%{version}.tar.bz2
Provides:       ndesk-dbus-devel < %{version}
Obsoletes:      ndesk-dbus-devel < %{version}
BuildRequires:  mono-devel
BuildRequires:  pkgconfig
%if 0%{?sles_version} == 9 || 0%{?suse_version} == 1000
BuildRequires:  glib2-devel
%endif
BuildArch:      noarch

%description
This is a C# implementation of D-Bus. It's often referred to as
"managed D-Bus" to avoid confusion with existing bindings (which wrap
libdbus).

It is a clean-room implementation based on the D-Bus Specification
Version 0.11 and study of the wire protocol of existing tools.



%prep
%setup

%build
%{?exp_env}
%{?env_options}
%configure --libdir="%_prefix/lib"
make %{?_smp_mflags}

%install
%{?env_options}
# This is all noarch, so the .pc file can go to %%_datadir.
make install DESTDIR="%buildroot" pkgconfigdir="%_datadir/pkgconfig"

%files
%defattr(-,root,root)
%doc COPYING README
%_prefix/lib/mono/gac/NDesk.DBus
%_prefix/lib/mono/ndesk-dbus-1.0
%_datadir/pkgconfig/ndesk-dbus-1.0.pc
%if 0%{?fedora_version}
# Allows overrides of __find_provides in fedora distros... (already set to zero on newer suse distros)
%define _use_internal_dependency_generator 0
%endif
%define __find_provides env sh -c 'filelist=($(cat)) && { printf "%s\\n" "${filelist[@]}" | /usr/lib/rpm/find-provides && printf "%s\\n" "${filelist[@]}" | /usr/bin/mono-find-provides ; } | sort | uniq'
%define __find_requires env sh -c 'filelist=($(cat)) && { printf "%s\\n" "${filelist[@]}" | /usr/lib/rpm/find-requires && printf "%s\\n" "${filelist[@]}" | /usr/bin/mono-find-requires ; } | sort | uniq'

%changelog
