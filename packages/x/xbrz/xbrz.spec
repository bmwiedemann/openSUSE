#
# spec file for package xbrz
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


Name:           xbrz
%define lname   libxbrz-1_8
Version:        1.8
Release:        0
Summary:        Pattern recognition rule-based bitmap upscaler
License:        GPL-3.0-only
Group:          Development/Libraries/C and C++
URL:            https://sourceforge.net/projects/xbrz/

Source:         http://downloads.sf.net/xbrz/xBRZ_%version.zip
BuildRequires:  c++_compiler
BuildRequires:  unzip

%description
xBRZ is a bitmap upscaler employing pattern recognition and
substituion rules. ("xBRZ" = Scale By Rules, Zenju enhanced variant.)

%package -n %lname
Summary:        Pattern recognition rule-based bitmap upscaler
Group:          System/Libraries

%description -n %lname
The idea of xBR is to scale bitmaps using pattern recognition (like
HQx), but also uses a 2-stage set of interpolation rules, which
better handle more complex patterns such as antialiased lines and
curves. Background textures keep the sharp characteristics of the
original image rather than becoming blurry like with HQx.

xBRZ follows this idea, but has a different set of rules, focusing on
preserving small image features consisting of few pixels only, like
commonly used in faces.

%package devel
Summary:        Development files for the xBRZ library
Group:          Development/Libraries/C and C++
Requires:       %lname = %version

%description devel
xBRZ is a bitmap upscaler employing pattern recognition and
substituion rules. ("xBRZ" = Scale By Rules, Zenju enhanced variant.)

%prep
%setup -cqn xBRZ

%build
c++ -DNDEBUG -D"__declspec(x)=" -fPIC -shared -Wl,-soname,libxbrz-%version.so \
	-o libxbrz-%version.so -std=c++17 xbrz.cpp

%install
b="%buildroot"
mkdir -p "$b/%_libdir" "$b/%_includedir"
cp -a libxbrz-%version.so "$b/%_libdir/"
cp -a *.h "$b/%_includedir/"
ln -s libxbrz-%version.so "$b/%_libdir/libxbrz.so"

%post   -n %lname -p /sbin/ldconfig
%postun -n %lname -p /sbin/ldconfig

%files -n %lname
%_libdir/libxbrz-%version.so
%license License.txt

%files devel
%_includedir/xbrz*.h
%_libdir/libxbrz.so

%changelog
