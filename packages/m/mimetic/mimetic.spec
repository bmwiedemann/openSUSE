#
# spec file for package mimetic
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           mimetic
Version:        0.9.8
Release:        0
Summary:        A C++ MIME library
License:        MIT
Group:          Development/Libraries/C and C++
URL:            http://www.codesink.org/mimetic_mime_library.html
Source0:        http://www.codesink.org/download/%{name}-%{version}.tar.gz
Patch0:         signedness-fix.patch
BuildRequires:  gcc-c++

%description
mimetic is an Email library written in C++. It supports MIME.

It has been built around the standard library; there are no custom
string classes or list implementations. Class functionalities and
behavior is modeled around MIME and the Internet message RFCs. See
RFC 5322, 2045 and 2046 for terminology, etc.

%package -n lib%{name}0
Summary:        A C++ MIME library
Group:          System/Libraries

%description -n lib%{name}0
It has been built around the standard library; there are no custom
string classes or list implementations. Class functionalities and
behavior is modeled around MIME and the Internet message RFCs. See
RFC 5322, 2045 and 2046 for terminology, etc.
2046.

%package -n lib%{name}-devel
Summary:        Development files for %{name}
Group:          Development/Libraries/C and C++
Requires:       lib%{name}0 = %{version}

%description -n lib%{name}-devel
This package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q
%autopatch -p1

%build
%configure --disable-static
%make_build

%install
%make_install
rm %{buildroot}%{_libdir}/lib%{name}.la

%check
make %{?_smp_mflags} check

%post -n lib%{name}0 -p /sbin/ldconfig
%postun -n lib%{name}0 -p /sbin/ldconfig

%files -n lib%{name}0
%license LICENSE
%doc AUTHORS ChangeLog README
%{_libdir}/lib%{name}.so.*

%files -n lib%{name}-devel
%{_includedir}/%{name}
%{_libdir}/lib%{name}.so

%changelog
