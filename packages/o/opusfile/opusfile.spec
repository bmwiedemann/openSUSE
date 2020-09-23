#
# spec file for package opusfile
#
# Copyright (c) 2020 SUSE LLC
# Copyright (c) 2013 Bjørn Lie (zaitor@opensuse.org).
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


%define soname 0
Name:           opusfile
Version:        0.12
Release:        0
Summary:        A high-level API for decoding and seeking within .opus files
License:        BSD-3-Clause
Group:          System/Libraries
URL:            https://www.opus-codec.org/
Source:         https://downloads.xiph.org/releases/opus/opusfile-%{version}.tar.gz
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(ogg) >= 1.3
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(opus)

%description
opusfile provides a high-level API for decoding and seeking within .opus files.
It includes:
* Support for all files with at least one Opus stream
  (including multichannel files or Ogg files where Opus is muxed with something else).
* Full support, including seeking, for chained files.
* A simple stereo downmixing API
  (allowing chained files to be decoded with a single output format, even if the channel count changes).
* Support for reading from a file, memory buffer, or over HTTP(S) (including seeking).
* Support for both random access and streaming data sources.

%package -n libopusfile%{soname}
Summary:        A high-level API for decoding and seeking within .opus files
Group:          System/Libraries

%description -n libopusfile%{soname}
opusfile provides a high-level API for decoding and seeking within .opus files.
It includes:
* Support for all files with at least one Opus stream
  (including multichannel files or Ogg files where Opus is muxed with something else).
* Full support, including seeking, for chained files.
* A simple stereo downmixing API
  (allowing chained files to be decoded with a single output format, even if the channel count changes).
* Support for reading from a file, memory buffer, or over HTTP(S) (including seeking).
* Support for both random access and streaming data sources.

%package devel
Summary:        Development package for %{name}
Group:          Development/Libraries/Other
Requires:       libopusfile%{soname} = %{version}
Requires:       pkgconfig

%description devel
Files for development with %{name}.

%prep
%setup -q

%build
%configure \
  --disable-static \
  --disable-silent-rules
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%post -n libopusfile%{soname} -p /sbin/ldconfig
%postun -n libopusfile%{soname} -p /sbin/ldconfig

%files -n libopusfile%{soname}
%license COPYING
%doc AUTHORS
%{_libdir}/libopusfile.so.%{soname}
%{_libdir}/libopusfile.so.%{soname}.*
%{_libdir}/libopusurl.so.%{soname}
%{_libdir}/libopusurl.so.%{soname}.*

%files devel
%doc %{_datadir}/doc/opusfile/
%{_includedir}/opus/opusfile.h
%{_libdir}/pkgconfig/opusfile.pc
%{_libdir}/pkgconfig/opusurl.pc
%{_libdir}/libopusfile.so
%{_libdir}/libopusurl.so

%changelog
