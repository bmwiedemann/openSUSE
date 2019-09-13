#
# spec file for package gio-sharp
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


Name:           gio-sharp
Version:        2.22.3
Release:        0
Summary:        .NET/C# Bindings for GIO
License:        GPL-2.0 and MIT
Group:          Development/Languages/Mono
Url:            https://github.com/mono/gio-sharp
Source:         %{name}-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

BuildRequires:  glib-sharp2
BuildRequires:  glib2-devel >= 2.22
BuildRequires:  gtk-sharp2-gapi
BuildRequires:  mono-devel
BuildRequires:  monodoc-core

Requires:       glib-sharp2 >= 2.12
Requires:       glib2 >= 2.22
Requires:       mono-core

%description
C#/CLI bindings for GIO

%package devel
Summary:        .NET/C# Bindings for GIO
Group:          Development/Languages/Mono
Requires:       %{name} = %{version}

%description devel
Files for developing programs that use gio-sharp

#%package docs
#Group:          Development/Languages/Mono
#Summary:        .NET/C# Bindings for GStreamer
#Requires:       %{name} = %{version}
#BuildRequires:  monodoc-core

#%description docs
#Documentation for developers using gstreamer-sharp

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
%dir %_prefix/lib/gio-sharp
%_prefix/lib/gio-sharp/*.dll*

#%files docs
#%defattr(-,root,root)
#%_prefix/lib/monodoc/sources/gstreamer-sharp-docs.*

%files devel
%defattr(-,root,root)
%{_libdir}/pkgconfig/gio-sharp-2.0.pc
%dir %_prefix/share/gapi-2.0
%_prefix/share/gapi-2.0/gio-api.xml

%changelog
