#
# spec file for package openh264
#
# Copyright (c) 2021 Red Hat, Inc.
# Copyright (c) 2022 Neal Gompa <ngompa@opensuse.org>.
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


# moz plugin commit hash
%global commit1 3a01c086d1b0394238ff1b5ad22e76022830625a

%global somajor 7
%global libname lib%{name}-%{somajor}
%global devname lib%{name}-devel

Name:           openh264
Version:        2.3.1
Release:        0
Summary:        H.264 codec library
Group:          Productivity/Multimedia/Other
License:        BSD-2-Clause
URL:            https://www.openh264.org/
Source0:        https://github.com/cisco/openh264/archive/v%{version}/openh264-%{version}.tar.gz
Source1:        https://github.com/mozilla/gmp-api/archive/%{commit1}/gmp-api-%{commit1}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  nasm

%description
OpenH264 is a codec library which supports H.264 encoding and decoding. It is
suitable for use in real time applications such as WebRTC.


%package     -n %{libname}
Summary:        H.264 codec library
Group:          System/Libraries

%description -n %{libname}
OpenH264 is a codec library which supports H.264 encoding and
decoding. It is suitable for use in real time applications such as
WebRTC.

This package contains libraries used by applications that use %{name}.

%package     -n %{devname}
Summary:        Development files for %{name}
Group:          Development/Libraries/C and C++
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-devel%{?_isa} = %{version}-%{release}
Requires:       %{libname}%{?_isa} = %{version}-%{release}

%description -n %{devname}
This package contains libraries and header files for developing
applications that use %{name}.

%package     -n mozilla-openh264
Summary:        H.264 codec support for Mozilla browsers
Group:          Productivity/Multimedia/Other
Requires:       %{libname}%{?_isa} = %{version}-%{release}
Supplements:    firefox

%description -n mozilla-openh264
The mozilla-openh264 package contains a H.264 codec plugin for Mozilla
browsers.


%prep
%autosetup -a1
mv gmp-api-%{commit1} gmp-api


%build
# Update the makefile with our build options
# Must be done in %%build in order to pick up correct LDFLAGS.
sed -i -e 's|^CFLAGS_OPT=.*$|CFLAGS_OPT=%{build_cflags}|' Makefile
sed -i -e 's|^PREFIX=.*$|PREFIX=%{_prefix}|' Makefile
sed -i -e 's|^LIBDIR_NAME=.*$|LIBDIR_NAME=%{_lib}|' Makefile
sed -i -e 's|^SHAREDLIB_DIR=.*$|SHAREDLIB_DIR=%{_libdir}|' Makefile
%if 0%{?suse_version} > 1550
sed -i -e '/^CFLAGS_OPT=/i LDFLAGS=%{build_ldflags}' Makefile
%endif

# First build the openh264 libraries
%make_build

# ... then build the mozilla plugin
%make_build plugin


%install
%make_install

# Install mozilla plugin
mkdir -p %{buildroot}%{_libdir}/mozilla/plugins/gmp-gmpopenh264/system-installed
cp -a libgmpopenh264.so* gmpopenh264.info %{buildroot}%{_libdir}/mozilla/plugins/gmp-gmpopenh264/system-installed/

mkdir -p %{buildroot}%{_libdir}/firefox/defaults/pref
cat > %{buildroot}%{_libdir}/firefox/defaults/pref/gmpopenh264.js << EOF
pref("media.gmp-gmpopenh264.autoupdate", false);
pref("media.gmp-gmpopenh264.version", "system-installed");
EOF

mkdir -p %{buildroot}%{_sysconfdir}/profile.d
cat > %{buildroot}%{_sysconfdir}/profile.d/gmpopenh264.sh << EOF
MOZ_GMP_PATH="%{_libdir}/mozilla/plugins/gmp-gmpopenh264/system-installed"
export MOZ_GMP_PATH
EOF

# Remove static libraries
rm -v %{buildroot}%{_libdir}/*.a


%ldconfig_scriptlets -n %{libname}


%files -n %{libname}
%license LICENSE
%doc README.md
%{_libdir}/libopenh264.so.%{somajor}
%{_libdir}/libopenh264.so.%{version}

%files -n %{devname}
%{_includedir}/wels/
%{_libdir}/libopenh264.so
%{_libdir}/pkgconfig/openh264.pc

%files -n mozilla-openh264
%config %{_sysconfdir}/profile.d/gmpopenh264.sh
%dir %{_libdir}/firefox
%dir %{_libdir}/firefox/defaults
%dir %{_libdir}/firefox/defaults/pref
%{_libdir}/firefox/defaults/pref/gmpopenh264.js
%dir %{_libdir}/mozilla
%dir %{_libdir}/mozilla/plugins
%{_libdir}/mozilla/plugins/gmp-gmpopenh264/


%changelog
