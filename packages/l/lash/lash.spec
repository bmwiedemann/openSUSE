#
# spec file for package lash
#
# Copyright (c) 2021 SUSE LLC
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


Name:           lash
Version:        0.5.4
Release:        0
Summary:        Linux Audio Session Handler
License:        GPL-2.0-or-later
Group:          Productivity/Multimedia/Sound/Utilities
URL:            http://git.savannah.gnu.org/cgit/lash.git
Source:         %{name}-%{version}.tar.bz2
Source1:        %{name}.desktop
Source1000:     baselibs.conf
Patch0:         lash-gcc44.patch
Patch1:         lash-implicit-fortify-decl.patch
Patch2:         lash-info-entry.diff
Patch3:         lash-swig-2x.patch
Patch4:         lash-add-needed.patch
Patch5:         lash-resource.patch
Patch6:         lash-glibc-2.22.patch
Patch7:         0001-Fix-detection-of-Python-3.patch
BuildRequires:  alsa-devel
BuildRequires:  glibc-devel
BuildRequires:  gtk2-devel
BuildRequires:  libjack-devel
BuildRequires:  libtool
BuildRequires:  libuuid-devel
BuildRequires:  libxml2-devel
BuildRequires:  python3-devel
BuildRequires:  readline-devel
BuildRequires:  swig

%description
LASH (formerly LADCCA) is a session management system for JACK and ALSA
audio applications on GNU/Linux. Its aim is to allow you to have many
different audio programs running at once and to save the setup, close
them down, then reload the setup at some other time.

%package -n liblash1
Summary:        Development package for LASH
Group:          Development/Libraries/C and C++

%description -n liblash1
This package contains the library for the LASH system.

%package -n python3-lash
Summary:        Python bindings for LASH
Group:          Development/Languages/Python
Requires:       %{name} = %{version}

%description -n python3-lash
This package contains the language bindings for Python.

%package -n lash-devel
Summary:        Development package for LASH
Group:          Development/Libraries/C and C++
Requires:       glibc-devel
Requires:       liblash1 = %{version}
Requires:       libuuid-devel
Requires:       readline-devel

%description -n lash-devel
This package contains the development files for the LASH system.

%prep
%setup -q

%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3
%patch4
%patch5 -p1
%patch6 -p1
%patch7 -p1

%build
./autogen.sh
%configure \
  --enable-static=no \
  --datadir=%{_datadir}/%{name}-%{version}
%make_build

%install
%make_install
rm -f %{buildroot}%{python3_sitelib}/_lash.la
rm -f %{buildroot}%{python3_sitelib}/_lash.a
chmod 644 %{buildroot}/%{python3_sitelib}/lash.py
find %{buildroot} -type f -name "*.la" -delete -print

# links for so.2 have to be made for older packages that link against liblash
pushd %{buildroot}%{_libdir}
        ln -s liblash.so.1 liblash.so.2
        ln -s liblash.so.1 liblash.so.2.0.0
popd

%files
%doc AUTHORS ChangeLog NEWS README TODO
%license COPYING
%{_bindir}/*
%{_datadir}/%{name}-%{version}/

%files -n liblash1
%{_libdir}/liblash.so.*

%files -n lash-devel
%{_includedir}/*
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*.pc

%files -n python3-lash
%doc pylash/test.py
%{python3_sitelib}/_lash.so
%{python3_sitelib}/lash.py

%post -n liblash1 -p /sbin/ldconfig
%postun -n liblash1 -p /sbin/ldconfig

%changelog
