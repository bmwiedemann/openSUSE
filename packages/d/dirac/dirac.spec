#
# spec file for package dirac
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           dirac
Version:        1.0.2
Release:        0
Summary:        The Dirac_Video Codec
License:        MPL-1.1
Group:          Productivity/Multimedia/Video/Editors and Convertors
Url:            https://sourceforge.net/projects/dirac/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Source1:        baselibs.conf
Patch0:         0001-Fix-uninitialised-memory-read-that-causes-the-encode.patch
Patch1:         %{name}-%{version}-gcc45.patch
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(cppunit)

%description
Dirac is an open source video codec. It uses a traditional hybrid video
codec architecture, but with the wavelet transform instead of the usual
block transforms.  Motion compensation uses overlapped blocks to reduce
block artefacts that would upset the transform coding stage.

Dirac can code just about any size of video, from streaming up to HD
and beyond, although certain presets are defined for different
applications and standards.  These cover the parameters that need to be
set for the encoder to work, such as block sizes and temporal
prediction structures, which must otherwise be set by hand.

%package -n libdirac_decoder0
Summary:        Dirac Video Codec Decoder Library
Group:          System/Libraries

%description -n libdirac_decoder0
Dirac is an open source video codec. It uses a traditional hybrid video
codec architecture, but with the wavelet transform instead of the usual
block transforms.  Motion compensation uses overlapped blocks to reduce
block artefacts that would upset the transform coding stage.

Dirac can code just about any size of video, from streaming up to HD
and beyond, although certain presets are defined for different
applications and standards.  These cover the parameters that need to be
set for the encoder to work, such as block sizes and temporal
prediction structures, which must otherwise be set by hand.

%package -n libdirac_encoder0
Summary:        Dirac Video Codec Encoder Library
Group:          System/Libraries

%description -n libdirac_encoder0
Dirac is an open source video codec. It uses a traditional hybrid video
codec architecture, but with the wavelet transform instead of the usual
block transforms.  Motion compensation uses overlapped blocks to reduce
block artefacts that would upset the transform coding stage.

Dirac can code just about any size of video, from streaming up to HD
and beyond, although certain presets are defined for different
applications and standards.  These cover the parameters that need to be
set for the encoder to work, such as block sizes and temporal
prediction structures, which must otherwise be set by hand.

%package devel
Summary:        Development Files for Dirac Video Codec
Group:          Development/Libraries/C and C++
Requires:       libdirac_decoder0 = %{version}
Requires:       libdirac_encoder0 = %{version}
Provides:       libdirac-devel = %{version}-%{release}
Obsoletes:      libdirac-devel < %{version}-%{release}

%description devel
Dirac is an open source video codec. It uses a traditional hybrid video
codec architecture, but with the wavelet transform instead of the usual
block transforms.  Motion compensation uses overlapped blocks to reduce
block artefacts that would upset the transform coding stage.

Dirac can code just about any size of video, from streaming up to HD
and beyond, although certain presets are defined for different
applications and standards.  These cover the parameters that need to be
set for the encoder to work, such as block sizes and temporal
prediction structures, which must otherwise be set by hand.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
# Code is not mature enough for -Werror (unused results)
sed -i 's/-Werror//' configure.ac

%build
ACLOCAL="aclocal -I m4" autoreconf -fvi
%configure \
	--disable-silent-rules \
	--disable-static \
	--docdir=%{_docdir}/packages/%{name} \
	--enable-mmx \
	--enable-overlay
make %{?_smp_mflags}

%install
%make_install htmldir=%{_docdir}/%{name}/code/api_html
# remove the docs we want with main pkg
find %{buildroot} -type f -name "*.la" -delete -print
%fdupes %{buildroot}%{_docdir}/%{name}

%post -n libdirac_decoder0 -p /sbin/ldconfig
%postun -n libdirac_decoder0 -p /sbin/ldconfig
%post -n libdirac_encoder0 -p /sbin/ldconfig
%postun -n libdirac_encoder0 -p /sbin/ldconfig

%files
%doc AUTHORS COPYING ChangeLog NEWS README TODO
%{_bindir}/*

%files -n libdirac_decoder0
%{_libdir}/libdirac_decoder.so.0*

%files -n libdirac_encoder0
%{_libdir}/libdirac_encoder.so.0*

%files devel
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/%{name}

%changelog
