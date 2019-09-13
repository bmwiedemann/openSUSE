#
# spec file for package libquvi
#
# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define         soname -0_9-0_9_4

Name:           libquvi
Version:        0.9.4
Release:        0
Summary:        Library to parse flash media stream URLs
License:        LGPL-2.1+
Group:          System/Libraries
Url:            http://quvi.sourceforge.net/
Source:         http://sourceforge.net/projects/quvi/files/0.9/libquvi/libquvi-0.9.4.tar.xz
Source1:        %{name}.rpmlintrc
# PATCH-FEATURE-OPENSUSE libquvi-stable-build-date.patch sbrabec@suse.cz -- Don't embed build date. Triggers rebuild.
Patch0:         %{name}-stable-build-date.patch
# PATCH-FIX-UPSTREAM marguerite@opensuse.org -- compatibility for lua 5.2+
Patch1:         %{name}-%{version}-lua-5.2.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  lua-devel
# For pkgconfig() Provides
BuildRequires:  libgcrypt-devel
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(glib-2.0) >= 2.24
BuildRequires:  pkgconfig(libcurl) >= 7.18.2
BuildRequires:  pkgconfig(libproxy-1.0) >= 0.3.1
BuildRequires:  pkgconfig(libquvi-scripts-0.9) >= 0.9
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
libquvi is a cross-platform library for parsing flash media stream
URLs with C API.

%package -n libquvi%{soname}
Summary:        Library to parse flash media stream URLs
Group:          System/Libraries
Recommends:     libquvi-scripts
# Up to openSUSE 13.2 and SLE 12 *.so files were in the main package. Now it does not exist.
Provides:       libquvi = %{version}-%{release}
Obsoletes:      libquvi < %{version}-%{release}

%description -n libquvi%{soname}
libquvi is a cross-platform library for parsing flash media stream
URLs with C API.

%package devel
Summary:        Library to parse flash media stream URLs -- Development Files
Group:          Development/Libraries/C and C++
Requires:       libquvi%{soname} = %{version}

%description devel
libquvi is a cross-platform library for parsing flash media stream
URLs with C API.

%prep
%setup -q
if test -f %{_sourcedir}/%{name}.changes ; then
%patch0
echo "timestamp for BUILD_TIME" >stamp-build-time
touch -d "$(sed -n '2s/ - .*$//p' <%{_sourcedir}/%{name}.changes)" stamp-build-time
fi
%patch1 -p1

%build
export CFLAGS="%{optflags} -DLUA_COMPAT_MODULE"
autoreconf -f -i
%configure \
    --disable-static
make %{?_smp_mflags}

%install
%make_install
find %{buildroot}%{_libdir} -name '*.la' -type f -delete -print

%post -n libquvi%{soname} -p /sbin/ldconfig

%postun -n libquvi%{soname} -p /sbin/ldconfig

%files -n libquvi%{soname}
%defattr(-,root,root)
%doc AUTHORS ChangeLog COPYING NEWS README
%{_libdir}/*.so

%files devel
%defattr(-,root,root)
%{_includedir}/quvi-0.9/
#{_libdir}/*.so
%{_libdir}/pkgconfig/libquvi-0.9.pc
%{_mandir}/man3/libquvi.3%{?ext_man}
%{_mandir}/man7/quvi-object.7%{?ext_man}

%changelog
