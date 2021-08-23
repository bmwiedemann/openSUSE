#
# spec file for package molequeue
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


Name:           molequeue
Version:        0.9.0
Release:        0
Summary:        Desktop integration of high performance computing resources
License:        BSD-3-Clause
URL:            https://github.com/OpenChemistry/molequeue
Source0:        https://github.com/openchemistry/molequeue/releases/download/0.9.0/%{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  python3-devel
BuildRequires:  zeromq-devel
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5Widgets)
Requires:       %{name}-libs0%{?_isa} = %{version}-%{release}

%description
System-tray resident desktop application for abstracting, managing,
and coordinating the execution of tasks both locally and on remote
computational resources.

Features:

 * Open source distributed under the liberal 3-clause BSD license
 * Cross platform with nightly builds on Linux, Mac OS X and Windows
 * Intuitive interface designed to be useful to whole community
 * Support for local executation and remote schedulers (SGE, PBS, SLURM)
 * System tray resident application managing queue of queues and job lifetime
 * Simple, lightweight JSON-RPC 2.0 based communication over local sockets
 * Qt 5 client library for simple integration in Qt applications

%package libs0
Summary:        Shared and private libraries of %{name}
Group:          System/Libraries

%description libs0
Shared and private libraries of %{name}.

%package  devel
Summary:        Development files of %{name}
Group:          Development/Libraries/C and C++
Requires:       %{name}-libs0%{?_isa} = %{version}-%{release}
Requires:       libqt5-qtbase-devel

%description devel
This package contains libraries and header files for developing
applications that use %{name}.

%package doc
Summary:        HTML documentation of %{name}
Group:          Documentation/Man
BuildArch:      noarch

%description doc
HTML documentation of %{name}.

%prep
%setup -q

%build
%cmake -Wno-dev \
  -DCMAKE_C_FLAGS:STRING="%optflags -fPIC" \
  -DCMAKE_CXX_FLAGS:STRING="%optflags -fPIC" \
  -DCMAKE_LD_FLAGS:STRING="%optflags -pie" \
  -DENABLE_TESTING:BOOL=OFF \
  -DBUILD_DOCUMENTATION:BOOL=ON \
  -DPYTHON_EXECUTABLE:FILEPATH=python3 \
  -Wno-dev
%cmake_build
pushd docs
doxygen
popd

%install
%cmake_install

rm -rf %{buildroot}%{_datadir}/doc

cat >%{name}.desktop <<EOF
[Desktop Entry]
Name=MoleQueue
GenericName=MoleQueue
Comment=Manage HPC jobs from the system tray
Exec=%{name}
Terminal=false
Type=Application
Icon=%{name}
Categories=Science;Chemistry;
X-SuSE-translate=false
EOF
install -Dpm0644 molequeue/app/icons/molequeue.png %{buildroot}%{_datadir}/pixmaps/%{name}.png

desktop-file-install %{name}.desktop --dir %{buildroot}%{_datadir}/applications

sed -i -e 's|//usr|/|g' %{buildroot}%{_libdir}/cmake/molequeue/MoleQueueConfig.cmake

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png

%files libs0
%doc README.md
%license LICENSE
%{_libdir}/*.so
%{_libdir}/%{name}/

%files devel
%{_libdir}/cmake/%{name}/
%{_includedir}/%{name}/

%files doc
%doc README.md build/docs/html
%license LICENSE

%changelog
