#
# spec file for package gkeyfile-sharp (Version 0.2)
#
# Copyright (c) 2010 SUSE LINUX Products GmbH, Nuernberg, Germany.
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

# norootforbuild


Name:           gkeyfile-sharp
Version:        0.2
Release:        1
License:        LGPL-2.1
Group:          Development/Languages/Mono
Summary:        .NET/C# Bindings for GKeyFile
Url:            http://github.com/mono/gkeyfile-sharp
Source:         %{name}-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

BuildRequires:  glib2-devel >= 2.6
BuildRequires:  glib-sharp2 >= 2.12.9
BuildRequires:  gtk-sharp2-gapi
BuildRequires:  mono-devel
BuildRequires:  monodoc-core

Requires:       mono-core
Requires:       glib-sharp2 >= 2.12.9

%description
C#/CLI bindings for GKeyFile

%package devel
License:        LGPL-2.1
Group:          Development/Languages/Mono
Summary:        .NET/C# Bindings for GKeyFile
Requires:       %{name} = %{version}

%description devel
Files for developing programs that use gkeyfile-sharp

%prep
%setup -q

%build
%{?env_options}
%configure
make

%install
%makeinstall

%clean
rm -rf "$RPM_BUILD_ROOT"

%files
%defattr(-,root,root)
%doc ChangeLog NEWS COPYING AUTHORS README
%dir %{_prefix}/lib/mono/gkeyfile-sharp
%{_prefix}/lib/mono/gkeyfile-sharp/*.dll*
%dir %{_prefix}/lib/mono/gac/gkeyfile-sharp/
%dir %{_prefix}/lib/mono/gac/gkeyfile-sharp/*
%{_prefix}/lib/mono/gac/gkeyfile-sharp/*/gkeyfile-sharp.dll*

%files devel
%defattr(-,root,root)
%{_libdir}/pkgconfig/gkeyfile-sharp.pc

%changelog
