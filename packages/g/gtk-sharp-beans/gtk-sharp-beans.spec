#
# spec file for package gtk-sharp-beans
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


Name:           gtk-sharp-beans
Version:        2.14.1
Release:        0
Summary:        Extra Gtk# bindings
License:        LGPL-2.1+
Group:          Development/Languages/Mono
Url:            http://gitorious.org/gtk-sharp-beans
Source:         %{name}-%{version}.tar.bz2
# PATCH-FEATURE-OPENSUSE gtk-sharp-beans-pc-fix.patch 782905 sshaw@decriptor.com -- This allows MonoDevelop to see gtk-sharp-beans. This will completely go away with gtk-sharp3 
Patch0:         gtk-sharp-beans-pc-fix.patch	
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

BuildRequires:  gio-sharp-devel
BuildRequires:  gtk-sharp2
BuildRequires:  gtk-sharp2-gapi
BuildRequires:  mono-devel
BuildRequires:  monodoc-core

Requires:       gio-sharp
Requires:       gtk-sharp2 >= 2.12
Requires:       mono-core

%description
Gtk# Beans aims to fill the gap between the current Gtk# packages state and all the blings and desktop integration stuffs anyone would want to use.

It builds on top of Gtk# and extend it by adding new classes and extension methods.


%package devel
Summary:        Extra Gtk# bindings
Group:          Development/Languages/Mono
Requires:       %{name} = %{version}

%description devel
Files for developing programs that use gtk-sharp-beans

#%package docs
#Group:          Development/Languages/Mono
#Summary:        .NET/C# Bindings for GStreamer
#Requires:       %{name} = %{version}
#BuildRequires:  monodoc-core

#%description docs
#Documentation for developers using gstreamer-sharp

%prep
%setup -q
%patch0 -p1

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
%dir %_prefix/lib/gtk-sharp-beans
%_prefix/lib/gtk-sharp-beans/*.dll*

#%files docs
#%defattr(-,root,root)
#%_prefix/lib/monodoc/sources/gstreamer-sharp-docs.*

%files devel
%defattr(-,root,root)
%{_libdir}/pkgconfig/gtk-sharp-beans-2.0.pc

%changelog
