#
# spec file for package gtk2-engine-cleanice
#
# Copyright (c) 2011 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           gtk2-engine-cleanice
%define _name   gtk-engines-cleanice
Version:        2.4.1
Release:        7
Summary:        CleanIce GTK Theme Engine
License:        GPL-2.0
Url:            http://sourceforge.net/projects/elysium-project
Group:          System/GUI/GNOME
Source:         %{_name}-%{version}.tar.bz2
BuildRequires:  gtk2-devel
Enhances:       gtk2
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
# Prevent missing engine failures on bi-arch systems:
%ifarch x86_64 s390x
Recommends:     %{name}-32bit = %{version}
%endif
%ifarch ppc
Recommends:     %{name}-64bit = %{version}
%endif

%description
Simple, clean theme engine for GTK2.

%prep
%setup -q -n %{_name}-%{version}

%build
%configure --disable-static
make %{?jobs:-j%jobs}

%install
%makeinstall
find %{buildroot} -type f -name "*.la" -delete -print

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root)
# NEWS and TODO are empty
%doc AUTHORS COPYING ChangeLog README
%{_libdir}/gtk-2.0/*/engines/*.so

%changelog
