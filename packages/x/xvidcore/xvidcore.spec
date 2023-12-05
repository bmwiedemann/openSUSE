#
# spec file for package xvidcore
#
# Copyright (c) 2023 SUSE LLC
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

%define sovermajor 4

Name:           xvidcore
Version:        1.3.7
Release:        0
Summary:        MPEG-4 Simple and Advanced Simple Profile codec
License:        GPL-2.0-or-later
URL:            https://www.xvid.com/
Source0:        https://downloads.xvid.com/downloads/%{name}-%{version}.tar.bz2

BuildRequires:  c_compiler
BuildRequires:  make
%ifarch %{ix86} x86_64
BuildRequires:  nasm >= 2.0
%endif

%description
The Xvid video codec implements MPEG-4 Simple Profile and Advanced
Simple Profile standards. It permits compressing and decompressing
digital video in order to reduce the required bandwidth of video
data for transmission over computer networks or efficient storage
on CDs or DVDs. Due to its unrivalled quality Xvid has gained great
popularity and is used in many other GPLed applications, like e.g.
Transcode, MEncoder, MPlayer, Xine and many more.

%package -n lib%{name}%{sovermajor}
Summary:        Shared library for xvidcore

%description -n lib%{name}%{sovermajor}
Xvid is a high quality MPEG-4 ASP video codec.
Shared library of XviD video codec.

%package        devel
Summary:        Development files for the Xvid video codec
Requires:       lib%{name}%{sovermajor} = %{version}
 
%description    devel
This package contains header files, static library and API
documentation for the Xvid video codec.

%prep
%autosetup  -p1 -n %{name}
chmod -x examples/*.pl
# Convert to utf-8
for file in AUTHORS ChangeLog; do
    iconv -f ISO-8859-1 -t UTF-8 -o $file.new $file && \
    touch -r $file $file.new && \
    mv $file.new $file
done
# Fix rpmlint wrong-file-end-of-line-encoding
for file in ChangeLog; do
 sed "s|\r||g" $file > $file.new && \
 touch -r $file $file.new && \
 mv $file.new $file
done
# Yes, we want to see the build output.
%{__sed} -i -e 's|@$(|$(|g' build/generic/Makefile
# Fix permissions
%{__sed} -i -e 's|644 $(BUILD_DIR)/$(SHARED_LIB)|755 $(BUILD_DIR)/$(SHARED_LIB)|g' build/generic/Makefile

%build
cd build/generic
%configure
%make_build

%install
%make_install -C build/generic
find %{buildroot} -type f -name "*.a" -delete -print

%ldconfig_scriptlets -n lib%{name}%{sovermajor}

%files -n lib%{name}%{sovermajor}
%doc README
%license LICENSE
%{_libdir}/libxvidcore.so.%{sovermajor}{,.*}

%files devel
%doc AUTHORS ChangeLog CodingStyle TODO examples/
%{_includedir}/xvid.h
%{_libdir}/libxvidcore.so

%changelog

