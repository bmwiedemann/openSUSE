#
# spec file for package gr-iqbal
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

%define libname libgnuradio-iqbalance
Name:           gr-iqbal
Version:        0.37.2+git.20151121
Release:        0
Summary:        Gnuradio I/Q balancing
License:        GPL-2.0
Group:          Productivity/Hamradio/Other
Url:            http://git.osmocom.org/gr-iqbal/
Source:         %{name}-%{version}.tar.xz
%if 0%{?suse_version} > 1325
BuildRequires:  libboost_system-devel
%else
BuildRequires:  boost-devel
%endif
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  git-core
BuildRequires:  gnuradio-devel
BuildRequires:  libosmo-dsp-devel
BuildRequires:  pkgconfig
BuildRequires:  python-wxWidgets
BuildRequires:  swig
BuildRequires:  pkgconfig(fftw3)
BuildRequires:  pkgconfig(python)
BuildRequires:  pkgconfig(python2)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
I/Q balancing for Gnuradio

%package -n %{libname}
Summary:        Libraries for gr-iqbal
Group:          System/Libraries

%description -n %{libname}
I/Q balancing for Gnuradio

%package -n python-gr-iqbal
Summary:        Python bindings for gr-iqbal
Group:          Development/Libraries/Python
Requires:       libgnuradio-iqbalance = %{version}

%description -n python-gr-iqbal
The Python Bindings for gr-iqbal.

%package -n %{libname}-devel
Summary:        Development files for gr-iqbal
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}

%description -n %{libname}-devel
Library headers for gr-iqbal, I/Q balancing for Gnuradio

%prep
%setup -q

%build
%cmake \
  -Wno-dev
make %{?_smp_mflags}

%install
%cmake_install
%fdupes %{buildroot}/%{python_sitearch}

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files -n libgnuradio-iqbalance
%defattr(-,root,root)
%{_datadir}/gnuradio
%{_libdir}/libgnuradio-iqbalance.so
%doc AUTHORS COPYING

%files -n python-gr-iqbal
%defattr(-,root,root)
%{python_sitearch}/gnuradio/iqbalance

%files -n libgnuradio-iqbalance-devel
%defattr(-,root,root)
%{_includedir}/gnuradio/iqbalance
%{_includedir}/gnuradio/swig
%{_libdir}/pkgconfig/gnuradio-iqbalance.pc

%changelog
