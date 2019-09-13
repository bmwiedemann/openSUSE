#
# spec file for package gudev-sharp
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


Name:           gudev-sharp
Version:        0.2
Release:        1
License:        LGPL-2.1
Group:          Development/Languages/Mono
Summary:        .NET/C# Bindings for GUDev
Url:            http://github.com/mono/gudev-sharp
Source:         %{name}-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

BuildRequires:  glib2-devel >= 2.6
BuildRequires:  glib-sharp2
BuildRequires:  gtk-sharp2-gapi
BuildRequires:  gtk-sharp2
BuildRequires:  mono-devel
BuildRequires:  monodoc-core
BuildRequires:  libgudev-1_0-devel
BuildRequires:  gtk2-devel

Requires:       mono-core
Requires:       libgudev-1_0-0
Requires:       gtk-sharp2

%description
C#/CLI bindings for GUDev

%package devel
License:        LGPL-2.1
Group:          Development/Languages/Mono
Summary:        .NET/C# Bindings for GUDev
Requires:       %{name} = %{version}

%description devel
Files for developing programs that use gudev-sharp

%prep
%setup -q -n %{name}-%{version}

%build
%configure
make

%install
%makeinstall

%files
%defattr(-,root,root)
%doc ChangeLog NEWS COPYING AUTHORS README
%dir %{_prefix}/lib/mono/gudev-sharp-1.0
%{_prefix}/lib/mono/gudev-sharp-1.0/*.dll*
%dir %{_prefix}/lib/mono/gac/gudev-sharp/
%dir %{_prefix}/lib/mono/gac/gudev-sharp/*
%{_prefix}/lib/mono/gac/gudev-sharp/*/gudev-sharp.dll*

%files devel
%defattr(-,root,root)
%{_libdir}/pkgconfig/gudev-sharp-1.0.pc

%changelog
