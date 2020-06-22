#
# spec file for package jxrlib
#
# Copyright (c) 2020 SUSE LLC
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


%define sover 0
Name:           jxrlib
Version:        1.1
Release:        0
Summary:        Open source implementation of jpegxr
# See JPEGXR_DPK_Spec_1.0.doc. Upstream request for plain text license file at
# https://jxrlib.codeplex.com/workitem/13
License:        BSD-2-Clause
URL:            https://jxrlib.codeplex.com/
Source0:        %{name}_1_1.zip
# Use CMake to build to facilitate creation of shared libraries
# See https://jxrlib.codeplex.com/workitem/13
Source1:        CMakeLists.txt
# Fix various warnings, upstreamable
# See https://jxrlib.codeplex.com/workitem/13
Patch0:         jxrlib_warnings.patch
BuildRequires:  cmake
BuildRequires:  unzip

%description
This is an open source implementation of the jpegxr image format standard.

This package contains the encoder and the decoder tools.

%package -n libjpegxr%{sover}
Summary:        Open source implementation of jpegxr

%description -n libjpegxr%{sover}
This is an open source implementation of the jpegxr image format standard.

This package the libjpegexr shared library

%package -n libjxrglue%{sover}
Summary:        Open source implementation of jpegxr

%description -n libjxrglue%{sover}
This is an open source implementation of the jpegxr image format standard.

This package the libjxrglue shared library

%package        devel
Summary:        Development files for %{name}
Requires:       libjpegxr%{sover} = %{version}-%{release}
Requires:       libjxrglue%{sover} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q -n %{name}

# Sanitize charset and line endings
for file in `find . -type f -name '*.c' -or -name '*.h' -or -name '*.txt'`; do
  iconv --from=ISO-8859-15 --to=UTF-8 $file > $file.new && \
  sed -i 's|\r||g' $file.new && \
  touch -r $file $file.new && mv $file.new $file
done

%patch0 -p1

# Remove shipped binaries
rm -rf bin
cp -a %{SOURCE1} .

%build
%cmake
%cmake_build

%install
%cmake_install

%post -n libjpegxr%{sover} -p /sbin/ldconfig
%post -n libjxrglue%{sover} -p /sbin/ldconfig
%postun -n libjpegxr%{sover} -p /sbin/ldconfig
%postun -n libjxrglue%{sover} -p /sbin/ldconfig

%files
%doc doc/readme.txt
%{_bindir}/JxrEncApp
%{_bindir}/JxrDecApp

%files -n libjpegxr%{sover}
%{_libdir}/libjpegxr.so.*

%files -n libjxrglue%{sover}
%{_libdir}/libjxrglue.so.*

%files devel
%{_includedir}/jxrlib/
%{_libdir}/libjpegxr.so
%{_libdir}/libjxrglue.so

%changelog
