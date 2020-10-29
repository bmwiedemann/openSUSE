#
# spec file for package libtorrent-rasterbar
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


%define _name   libtorrent
%define _ver    2.0
%define libver  2_0
%define sover   2.0
%define _legacy 1
%bcond_with     examples
%bcond_with     tests
Name:           libtorrent-rasterbar
Version:        2.0.0
Release:        0
Summary:        A C++ implementation of the BitTorrent protocol
License:        BSD-3-Clause
Group:          Development/Libraries/C and C++
URL:            https://libtorrent.org/
Source:         https://github.com/arvidn/%{_name}/releases/download/%{_ver}/%{name}-%{version}.tar.gz
BuildRequires:  cmake >= 3.12.0
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  libboost_chrono-devel >= 1.66
BuildRequires:  libboost_python3-devel >= 1.66
BuildRequires:  libboost_random-devel >= 1.66
BuildRequires:  libboost_system-devel >= 1.66
BuildRequires:  pkgconfig
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  pkgconfig(openssl) >= 1.0.0

%description
libtorrent-rasterbar is a C++ library that aims to be a good
alternative to all the other bittorrent implementations around.
It is a library and not a full featured client, although it comes
with a working example client.

This package holds the sample client and example files for
libtorrent-rasterbar.

%package -n %{name}%{libver}
Summary:        A C++ implementation of the BitTorrent protocol
Group:          System/Libraries

%description -n %{name}%{libver}
libtorrent-rasterbar is a C++ library that aims to be a good
alternative to all the other bittorrent implementations around.
It is a library and not a full featured client, although it comes
with a working example client.

%package -n python3-%{name}
Summary:        Python Bindings for libtorrent-rasterbar
Group:          Development/Libraries/Python
Conflicts:      python3-%{name}-%{_legacy}

%description -n python3-%{name}
Python Bindings for the libtorrent-rasterbar package.

%if %{with examples}
%package tools
Summary:        Example tools from libtorrent-rasterbar
Group:          Development/Libraries/C and C++

%description tools
Example tools from the libtorrent-rasterbar package.
%endif

%package devel
Summary:        Header files for libtorrent, a C++ implementation of the BitTorrent protocol
Group:          Development/Libraries/C and C++
Requires:       %{name}%{libver} = %{version}
Requires:       gcc-c++
Requires:       libboost_headers-devel
Requires:       pkgconfig(openssl)
Conflicts:      %{name}-%{_legacy}-devel

%description devel
libtorrent-rasterbar is a C++ library that aims to be a good
alternative to all the other bittorrent implementations around.
It is a library and not a full featured client, although it comes
with a working example client.

This package holds the development files for libtorrent-rasterbar.

%package doc
Summary:        Documentation for libtorrent-rasterbar
Group:          Documentation/HTML
BuildArch:      noarch

%description doc
Documentation for the libtorrent-rasterbar package.

%prep
%autosetup -p1

%build
%cmake \
%if %{with tests}
   -Dbuild_tests=ON \
%endif
%if %{with examples}
   -Dbuild_examples=ON \
%endif
   -Dpython-bindings=ON \
   -Dboost-python-module-name=python
%cmake_build

%install
%cmake_install

# Move doc to a separate package.
mkdir -p %{buildroot}%{_docdir}/%{name}/
cp -r docs/* %{buildroot}%{_docdir}/%{name}/

%if %{with examples}
install -Dm0755 build/examples/dump_torrent build/examples/make_torrent \
  build/examples/simple_client -t %{buildroot}%{_bindir}
%endif

%fdupes %{buildroot}%{python3_sitearch}

%if %{with tests}
%check
export LD_LIBRARY_PATH=$PWD/build
ln -s build/web_server.py .
# test_flags until gh#arvidn/libtorrent#4985 is fixed
%ctest --verbose --exclude-regex "(test_flags|test_upnp)"
%endif

%post -n %{name}%{libver} -p /sbin/ldconfig
%postun -n %{name}%{libver} -p /sbin/ldconfig

%if %{with examples}
%files tools
%{_bindir}/dump_torrent
%{_bindir}/make_torrent
%{_bindir}/simple_client
%endif

%files -n %{name}%{libver}
%license COPYING
%doc AUTHORS ChangeLog
%{_libdir}/%{name}.so.%{sover}*

%files -n python3-%{name}
%{python3_sitearch}/%{_name}*.so
%{python3_sitearch}/%{_name}.egg-info

%files devel
%{_datadir}/cmake/Modules/FindLibtorrentRasterbar.cmake
%{_includedir}/%{_name}/
%{_libdir}/cmake/LibtorrentRasterbar
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%files doc
%doc %{_docdir}/%{name}/

%changelog
