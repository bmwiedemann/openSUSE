#
# spec file for package SVT-AV1
#
# Copyright (c) 2024 SUSE LLC
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


Name:           SVT-AV1
Version:        2.1.1
Release:        0
Summary:        An AV1 decoder/encoder for video streams
License:        BSD-3-Clause-Clear
Group:          Productivity/Multimedia/Other
URL:            https://gitlab.com/AOMediaCodec/SVT-AV1
Source:         https://gitlab.com/AOMediaCodec/SVT-AV1/-/archive/v%version/SVT-AV1-v%version.tar.gz
BuildRequires:  cmake >= 3.5.1
BuildRequires:  fdupes
BuildRequires:  gcc-c++ >= 5.4.0
BuildRequires:  help2man
BuildRequires:  pkg-config
BuildRequires:  yasm >= 1.2.0
ExclusiveArch:  aarch64 riscv64 x86_64

%description
The Scalable Video Technology for AV1 (SVT-AV1 Encoder and Decoder) is an
AV1-compliant encoder/decoder library core. The SVT-AV1 encoder development is
a work-in-progress targeting performance levels applicable to both VOD and Live
encoding / transcoding video applications. The SVT-AV1 decoder implementation
is targeting future codec research activities.

%package -n libSvtAv1Enc2
Summary:        An AV1 decoder/encoder for video streams
Group:          System/Libraries

%description -n libSvtAv1Enc2
The Scalable Video Technology for AV1 (SVT-AV1 Encoder and Decoder) is an
AV1-compliant encoder/decoder library core. The SVT-AV1 encoder development is
a work-in-progress targeting performance levels applicable to both VOD and Live
encoding / transcoding video applications. The SVT-AV1 decoder implementation
is targeting future codec research activities.

%package devel
Summary:        Development files for %name
Group:          Development/Libraries/C and C++
Requires:       libSvtAv1Enc2 = %version

%description devel
An AV1 encoder for video streams from Intel.

This package contains the header files for svt-av1.

%prep
%autosetup -p1 -n %name-v%version

%build
%cmake
%cmake_build

%install
%cmake_install

# Generate manpages
install -d -m0755 %buildroot/%_mandir/man1

LD_LIBRARY_PATH="%buildroot%_libdir" \
help2man -N --help-option=-help --version-string=%version --no-discard-stderr %buildroot%_bindir/SvtAv1EncApp > %buildroot%_mandir/man1/SvtAv1EncApp.1

b="%buildroot/%_defaultdocdir/%name"
mkdir -p "$b"
cp -a Docs README.md "$b/"
%fdupes %buildroot/%_prefix

%ldconfig_scriptlets -n libSvtAv1Enc2

%files -n libSvtAv1Enc2
%license LICENSE.md PATENTS.md
%_libdir/libSvtAv1Enc.so.*

%files
%_bindir/Svt*
%_mandir/man1/Svt*
%doc %_defaultdocdir/%name/

%files devel
%_libdir/libSvtAv1Enc.so
%_libdir/pkgconfig/*.pc
%_includedir/svt-av1/

%changelog
