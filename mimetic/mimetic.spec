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
Summary:        A full featured C++ MIME library
License:        MIT
Group:          Development/Libraries/C and C++
URL:            http://www.codesink.org/mimetic_mime_library.html
Source0:        http://www.codesink.org/download/%{name}-%{version}.tar.gz
Patch0:         signedness-fix.patch
BuildRequires:  gcc-c++

%description
mimetic is an Email library (MIME) written in C++ designed to be easy to use and integrate but
yet fast and efficient.

It has been built around the standard lib. This means that you'll not find yet another string class
or list implementation and that you'll feel comfortable in using this library from the very first time.

Most classes functionalities and behavior will be clear if you ever studied MIME and its components;
if you don't know anything about Internet messages you'll probably want to read
some RFCs to understand the topic and, therefore, easily use the library whose names,
whenever possible, overlap terms adopted in the standard RFC documents.
At the very least: RFC 822, RFC 2045 and RFC 2046.

%package -n lib%{name}0
Summary:        A full featured C++ MIME library

%description -n lib%{name}0
mimetic is an Email library (MIME) written in C++ designed to be easy to use
and integrate but yet fast and efficient.

It has been built around the standard lib. This means that you'll not find yet
another string class or list implementation and that you'll feel comfortable
in using this library from the very first time.

Most classes functionalities and behavior will be clear if you ever studied
MIME and its components; if you don't know anything about Internet messages
you'll probably want to read some RFCs to understand the topic and, therefore,
easily use the library whose names, whenever possible, overlap terms adopted
in the standard RFC documents. At the very least: RFC 822, RFC 2045 and RFC
2046.

%package -n lib%{name}-devel
Summary:        Development files for %{name}
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
%defattr(0644,root,root,-)
%license LICENSE
%doc AUTHORS ChangeLog README
%{_libdir}/lib%{name}.so.*

%files -n lib%{name}-devel
%defattr(0644,root,root,-)
%{_includedir}/%{name}
%{_libdir}/lib%{name}.so

%changelog
