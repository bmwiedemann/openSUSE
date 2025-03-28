#
# spec file for package liblognorm
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2025 Andreas Stieger <Andreas.Stieger@gmx.de>
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


%define sover 5
Name:           liblognorm
Version:        2.0.6
Release:        0
Summary:        Library and tool to normalize log data
License:        Apache-2.0 AND LGPL-2.1-or-later
Group:          Development/Libraries/C and C++
URL:            https://www.liblognorm.com/
Source0:        https://www.liblognorm.com/download/files/download/%{name}-%{version}.tar.gz
Patch0:         liblognorm-2.0.6-pcre2.patch
# for liblognorm-2.0.6-pcre2.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
#
BuildRequires:  pkgconfig >= 0.9.0
BuildRequires:  pkgconfig(libestr)
BuildRequires:  pkgconfig(libfastjson) >= 0.99.0
BuildRequires:  pkgconfig(libpcre2-8) >= 10.00

%description
Liblognorm is a fast-samples based normalization library. It is a library and
a tool to normalize log data.

Liblognorm shall help to make sense out of syslog data, or, actually, any event
data that is present in text form.

In short words, one will be able to throw arbitrary log message to liblognorm,
one at a time, and for each message it will output well-defined name-value
pairs and a set of tags describing the message.

So, for example, if you have traffic logs from three different firewalls,
liblognorm will be able to "normalize" the events into generic ones. Among
others, it will extract source and destination ip addresses and ports and make
them available via well-defined fields. As the end result, a common log
analysis application will be able to work on that common set and so this
backend will be independent from the actual firewalls feeding it. Even better,
once we have a well-understood interim format, it is also easy to convert that
into any other vendor specific format, so that you can use that vendor's
analysis tool.

%package -n     liblognorm%{sover}
Summary:        Library and tool to normalize log data
Group:          Development/Libraries/C and C++

%description  -n liblognorm%{sover}
Liblognorm is a library and a tool to normalize log data.

Liblognorm shall help to make sense out of syslog data, or, actually, any event
data that is present in text form.

In short words, one will be able to throw arbitrary log message to liblognorm,
one at a time, and for each message it will output well-defined name-value
pairs and a set of tags describing the message.

So, for example, if you have traffic logs from three different firewalls,
liblognorm will be able to "normalize" the events into generic ones. Among
others, it will extract source and destination ip addresses and ports and make
them available via well-defined fields. As the end result, a common log
analysis application will be able to work on that common set and so this
backend will be independent from the actual firewalls feeding it. Even better,
once we have a well-understood interim format, it is also easy to convert that
into any other vendor specific format, so that you can use that vendor's
analysis tool.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries/C and C++
Requires:       %{name}%{sover} = %{version}
Conflicts:      %{name}0-devel

%description    devel
Liblognorm is a library and a tool to normalize log data.

Liblognorm shall help to make sense out of syslog data, or, actually, any event
data that is present in text form.

In short words, one will be able to throw arbitrary log message to liblognorm,
one at a time, and for each message it will output well-defined name-value
pairs and a set of tags describing the message.

So, for example, if you have traffic logs from three different firewalls,
liblognorm will be able to "normalize" the events into generic ones. Among
others, it will extract source and destination ip addresses and ports and make
them available via well-defined fields. As the end result, a common log
analysis application will be able to work on that common set and so this
backend will be independent from the actual firewalls feeding it. Even better,
once we have a well-understood interim format, it is also easy to convert that
into any other vendor specific format, so that you can use that vendor's
analysis tool.

The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -p1

%build
# for liblognorm-2.0.6-pcre2.patch
autoreconf -fiv
#
%configure \
	--disable-static \
	--enable-regexp \
	--disable-testbench \
	--enable-advanced-stats \
	--enable-tools \
	--disable-docs \
	%{nil}
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%check
%make_build check

%ldconfig_scriptlets -n liblognorm%{sover}

%files -n liblognorm%{sover}
%license COPYING
%{_libdir}/*.so.*
%{_bindir}/lognormalizer

%files devel
%license COPYING
%doc NEWS README AUTHORS ChangeLog
%{_includedir}/*
%{_libdir}/*.so
%{_includedir}/*.h
%{_libdir}/pkgconfig/lognorm.pc

%changelog
