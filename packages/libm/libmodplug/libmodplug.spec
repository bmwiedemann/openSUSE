#
# spec file for package libmodplug
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define soname 1
Name:           libmodplug
Version:        0.8.9.0+git20170610.f6dd59a
Release:        0
Summary:        A MOD playing library
License:        SUSE-Public-Domain
Group:          System/Libraries
Url:            https://github.com/Konstanty/libmodplug/
Source:         %{name}-%{version}.tar.xz
Source1:        baselibs.conf
# PATCH-FIX-OPENSUSE libmodplug-timidity.patch -- set paths to openSUSE timidity package
Patch1:         libmodplug-timidity.patch
# PATCH-FIX-UPSTREAM libmodplug-0.8.8.5-fix-missing-include-path.patch -- set includedir in pc file
Patch2:         libmodplug-0.8.8.5-fix-missing-include-path.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  pkgconfig

%description
Libmodplug is the library behind -- Modplug-XMMS is a fully featured, complete
input plugin for XMMS which plays mod-like music formats. It is based on the
mod rendering code from ModPlug, a popular windows mod player written by
Olivier Lapicque, found at http://www.modplug.com/.

%package -n libmodplug%{soname}
Summary:        Development files for libmodplug
Group:          Development/Libraries/C and C++

%description -n libmodplug%{soname}
Modplug library based on the ModPlug sound engine.
- plays 22 different mod formats.
- plays zip, rar, gzip, and bzip2 compressed mods.
- plays timidity's GUS patch files (*.pat).
- plays all types of MIDI files (*.mid).
- plays textfiles written in the ABC music notation (*.abc).

%package devel
Summary:        Development files for libmodplug
Group:          Development/Libraries/C and C++
Requires:       libmodplug%{soname} = %{version}

%description devel
Files needed to program against libmodplug.

%prep
%setup -q
%patch1
%patch2 -p1
sed -i 's/\r$//' ChangeLog

%build
autoreconf -fvi
%configure \
    --disable-silent-rules \
    --disable-static
make %{?_smp_mflags}

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%post -n libmodplug%{soname} -p /sbin/ldconfig
%postun -n libmodplug%{soname} -p /sbin/ldconfig

%files -n libmodplug%{soname}
%license COPYING
%{_libdir}/%{name}.so.%{soname}*

%files devel
%doc AUTHORS ChangeLog NEWS README TODO
%{_includedir}/%{name}
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog
