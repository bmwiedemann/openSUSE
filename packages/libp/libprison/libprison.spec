#
# spec file for package libprison
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           libprison
%define rname   prison
Version:        1.1.1
Release:        0
Summary:        Qt api to produce QRCode and DataMatrix barcodes
License:        MIT
Group:          Development/Libraries/C and C++
Url:            https://projects.kde.org/projects/prison
Source:         http://download.kde.org/stable/prison/%{version}/src/%{rname}-%{version}.tar.xz
Source1:        baselibs.conf
BuildRequires:  cmake
BuildRequires:  kde4-filesystem
BuildRequires:  libdmtx-devel
BuildRequires:  libqt4-devel
BuildRequires:  qrencode-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Prison is a barcode api currently offering a nice Qt api to produce QRCode
barcodes and DataMatrix barcodes, and can easily be made support more.

%package -n libprison0
Summary:        Qt api to produce QRCode and DataMatrix barcodes
Group:          Development/Libraries/C and C++

%description -n libprison0
Prison is a barcode api currently offering a nice Qt api to produce QRCode
barcodes and DataMatrix barcodes, and can easily be made support more.

%package devel
Summary:        Qt api to produce QRCode and DataMatrix barcodes
Group:          Development/Libraries/C and C++
Requires:       libprison0 = %{version}

%description devel
Prison is a barcode api currently offering a nice Qt api to produce QRCode
barcodes and DataMatrix barcodes, and can easily be made support more.

%prep
%setup -q -n %{rname}-%{version}

%build
export RPM_OPT_FLAGS="%optflags -fvisibility-inlines-hidden"
%cmake_kde4 -d build
%make_jobs

%install
cd build
%kde4_makeinstall

%post -n libprison0 -p /sbin/ldconfig

%postun -n libprison0 -p /sbin/ldconfig

%files -n libprison0
%defattr(-,root,root)
%{_libdir}/libprison.so.*

%files devel
%defattr(-,root,root)
%{_includedir}/prison/
%{_libdir}/cmake/Prison/
%{_libdir}/libprison.so

%changelog
