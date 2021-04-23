#
# spec file for package hyena
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           hyena
Version:        0.5
Release:        0
Summary:        Library for .NET applications
License:        MIT
Group:          Development/Libraries/GNOME
Url:            http://banshee-project.org/
Source:         %{name}-%{version}.tar.bz2
# PATCH-FIX-UPSTREAM coolo@opensuse.org - broken Makefile syntax
Patch0:         fix-makefile.diff
Patch1:         hyena-dotnet4.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  glib-sharp2
BuildRequires:  gtk-sharp2
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  mono-basic
BuildRequires:  mono-devel
BuildRequires:  mono-nunit
BuildRequires:  perl-XML-Parser
BuildRequires:  pkgconfig
Requires:       gtk-sharp2
Requires:       mono
Requires:       mono-core

%description
Hyena is a .NET library that powers Banshee and PDF Mod, among others.

%prep
%setup
%patch0 -p1
%patch1 -p1

%build
autoreconf -fiv -I build/m4/shamrock
%configure 
make

%install
%makeinstall
#%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root)
#%doc AUTHORS NEWS README COPYING
%{_libdir}/%{name}
%{_libdir}/pkgconfig/*.pc

%changelog
