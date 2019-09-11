#
# spec file for package evemu
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


%define soname  libevemu
%define sover   3
Name:           evemu
Version:        2.7.0
Release:        0
Summary:        Input Event Device Emulation Library
License:        GPL-3.0-only
Group:          Hardware/Other
Url:            https://freedesktop.org/wiki/Evemu
Source:         https://freedesktop.org/software/%{name}/%{name}-%{version}.tar.xz
Source1:        https://freedesktop.org/software/%{name}/%{name}-%{version}.tar.xz.sig
Source2:        %{name}.keyring
BuildRequires:  asciidoc
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  python-devel
BuildRequires:  python3-devel
BuildRequires:  xmlto
BuildRequires:  pkgconfig(libevdev) >= 1.2.99.902
Provides:       %{name}-tools = %{version}
Obsoletes:      %{name}-tools < %{version}

%description
The evemu library and tools are used to describe devices, record
data, create emulation devices and replay data from kernel evdev
(input event) devices.

%package -n %{soname}%{sover}
Summary:        Input Event Device Emulation Library
Group:          System/Libraries

%description -n %{soname}%{sover}
The evemu library and tools are used to describe devices, record
data, create emulation devices and replay data from kernel evdev
(input event) devices.

%if 0%{?suse_version} >= 1500
%package -n python2-%{name}
%else
%package -n python-%{name}
%endif
Summary:        Python2 bindings for evemu
Group:          Development/Languages/Python
Requires:       %{soname}%{sover} = %{version}
%if 0%{?suse_version} >= 1500
# python-evemu was last used in openSUSE Leap 42.3.
Provides:       python-%{name} = %{version}-%{release}
Obsoletes:      python-%{name} < %{version}-%{release}

%description -n python2-%{name}
%else

%description -n python-%{name}
%endif
The evemu library and tools are used to describe devices, record
data, create emulation devices and replay data from kernel evdev
(input event) devices.

This package provides the Python2 bindings for evemu.

%package -n python3-%{name}
Summary:        Python3 bindings for evemu
Group:          Development/Languages/Python
Requires:       %{soname}%{sover} = %{version}

%description -n python3-%{name}
The evemu library and tools are used to describe devices, record
data, create emulation devices and replay data from kernel evdev
(input event) devices.

This package provides the Python3 bindings for evemu.

%package devel
Summary:        Development files for evemu
Group:          Development/Tools/Other
Requires:       %{name} = %{version}
Requires:       %{soname}%{sover} = %{version}

%description devel
The evemu library and tools are used to describe devices, record
data, create emulation devices and replay data from kernel evdev
(input event) devices.

This package provides the development files.

%prep
%setup -q
evdev_sover="$(basename "$(readlink -f %{_libdir}/libevdev.so)")"
sed -i \
  -e 's|\"%{soname}.so\"|\"%{soname}.so.%{sover}\"|' \
  -e "s|\"libevdev.so\"|\"$evdev_sover\"|"           \
  python/%{name}/{base,const}.py

%build
%global _configure ../configure
for py in python2 python3; do
    export PYTHON=$py
    mkdir -p build-$py
    pushd build-$py
    %configure \
      --disable-static       \
      --disable-silent-rules \
      --disable-tests
    make %{?_smp_mflags}
    popd
done

%install
%make_install -C build-python2
%make_install -C build-python3

find %{buildroot} -type f -name "*.la" -delete -print

# Remove useless "optimised" Python byte-code.
rm -f %{buildroot}%{python_sitelib}/%{name}/*.pyo \
  %{buildroot}%{python3_sitelib}/%{name}/__pycache__/*.opt-?.pyc

%fdupes %{buildroot}%{_bindir}/
%fdupes %{buildroot}%{_mandir}/

%post -n %{soname}%{sover} -p /sbin/ldconfig

%postun -n %{soname}%{sover} -p /sbin/ldconfig

%files
%if 0%{?suse_version} >= 1500
%license COPYING
%else
%doc COPYING
%endif
%{_bindir}/%{name}-*
%{_mandir}/man?/%{name}-*?%{?ext_man}

%files -n %{soname}%{sover}
%if 0%{?suse_version} >= 1500
%license COPYING
%else
%doc COPYING
%endif
%{_libdir}/%{soname}.so.%{sover}*

%if 0%{?suse_version} >= 1500
%files -n python2-%{name}
%license COPYING
%else
%files -n python-%{name}
%doc COPYING
%endif
%{python_sitelib}/%{name}/

%files -n python3-%{name}
%if 0%{?suse_version} >= 1500
%license COPYING
%else
%doc COPYING
%endif
%{python3_sitelib}/%{name}/

%files devel
%{_includedir}/%{name}.h
%{_libdir}/%{soname}.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog
