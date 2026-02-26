#
# spec file for package libigloo
#
# Copyright (c) 2026 SUSE LLC and contributors
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

%define sover	0

Name:           libigloo
Version:        0.9.5
Release:        0
Summary:        Generic C framework used and developed by the Icecast project
License:        LGPL-2.1-or-later
URL:            http://www.icecast.org/
Source:         http://downloads.xiph.org/releases/igloo/%{name}-%{version}.tar.gz
BuildRequires:  rhash-devel

%description
libigloo is a generic C framework. It is developed and used by the Icecast project.

%package -n %{name}%{sover}
Summary:        Generic C framework used and developed by the Icecast project

%description -n %{name}%{sover}
libigloo is a generic C framework. It is developed and used by the Icecast project.

%package devel
Summary:        Development Environment for libigloo
Requires:       %{name}%{sover} = %{version}

%description devel
This package contains the include-files and static libraries for libigloo.

%prep
%autosetup -p1

%build
%configure --disable-static
%make_build

%install
%make_install
rm -f %{buildroot}%{_libdir}/*.la

%ldconfig_scriptlets -n %{name}%{sover}

%files -n %{name}%{sover}
%license COPYING
%doc README NEWS
%{_libdir}/%{name}.so.%{sover}
%{_libdir}/%{name}.so.%{sover}.*

%files devel
%{_includedir}/igloo
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/*.pc

%changelog
