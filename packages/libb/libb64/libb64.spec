#
# spec file for package libb64
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


%define shared_lib libb64.so
%define soversion 1
%define soname %{shared_lib}.%{soversion}
%define libname %{name}-%{soversion}
Name:           libb64
Version:        2.0.0.1
Release:        0
Summary:        Base64 Encoding/Decoding Routines
License:        SUSE-Public-Domain
URL:            https://github.com/libb64/libb64
Source:         https://github.com/libb64/libb64/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
# PATCH-FIX-UPSTREAM bufsiz-as-buffer-size.diff -- default the C++ en/decoder buffersize to BUFSIZ so the headers are usable standalone
Patch0:         bufsiz-as-buffer-size.diff
# PATCH-FIX-UPSTREAM no-hardcoded-lib-path.diff -- link the base64 tool against the library
Patch1:         no-hardcoded-lib-path.diff
# PATCH-FIX-UPSTREAM override-cflags.diff -- respect externally supplied CFLAGS
Patch2:         override-cflags.diff
# PATCH-FIX-UPSTREAM disable-werror.diff -- do not add -Werror as it is prone to break
Patch3:         disable-werror.diff
BuildRequires:  gcc-c++

%description
libb64 is a library of ANSI C routines for fast encoding/decoding data into and
from a base64-encoded format. C++ wrappers are included, as well as the source
code for standalone encoding and decoding executables.

%package        -n %{libname}
Summary:        A library for working with base64 encoding/decoding

%description    -n %{libname}
libb64 is a library of ANSI C routines for fast encoding/decoding data into and
from a base64-encoded format. C++ wrappers are included, as well as the source
code for standalone encoding and decoding executables.

%package        devel
Summary:        A library for working with base64 encoding/decoding
Requires:       %{libname} = %{version}-%{release}

%description    devel
libb64 is a library of ANSI C routines for fast encoding/decoding data into and
from a base64-encoded format. C++ wrappers are included, as well as the source
code for standalone encoding and decoding executables.

%prep
%autosetup -p1

%build
export CFLAGS="%{optflags}"
cp -a src src-shlib/
pushd src-shlib
CFLAGS="%{optflags} -fPIC" make -j1
cc -shared -Wl,-soname,%{soname} *.o -o %{soname}
ln -sf %{soname} %{shared_lib}
popd
%make_build -j1 all_src all_base64

%install
# We need to use different name to avoid conflict with coreutils
install -Dpm 0755 base64/base64 \
  %{buildroot}%{_bindir}/libb64-base64
install -Dpm 0755 src-shlib/%{soname} \
  %{buildroot}%{_libdir}/%{soname}
mkdir -p %{buildroot}/%{_includedir}
cp -r include/b64 %{buildroot}/%{_includedir}
cd %{buildroot}%{_libdir}
ln -s %{soname} %{shared_lib}

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files
%doc CHANGELOG.md README.md
%{_bindir}/libb64-base64

%files -n %{libname}
%license LICENSE.md
%{_libdir}/%{soname}

%files devel
%{_libdir}/%{shared_lib}
%dir %{_includedir}/b64
%{_includedir}/b64/ccommon.h
%{_includedir}/b64/cdecode.h
%{_includedir}/b64/cencode.h
%{_includedir}/b64/decode.h
%{_includedir}/b64/encode.h

%changelog
