#
# spec file for package iometer
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Name:           iometer
Version:        1.1.0
Release:        0
Summary:        I/O subsystem measurement and characterization tool
License:        GPL-2.0-only
Group:          System/Benchmark
URL:            http://www.iometer.org/
Source0:        http://sourceforge.net/projects/iometer/files/iometer-stable/%{version}/iometer-%{version}-src.tar.bz2
BuildRequires:  dos2unix
BuildRequires:  gcc-c++
BuildRequires:  libaio-devel
ExclusiveArch:  %{ix86} x86_64

%description
Iometer is an I/O subsystem measurement and characterization tool for
single and clustered systems.

%prep
%setup -q

%build
make %{?_smp_mflags} -C src -f Makefile-Linux.%{_arch} CXX="c++ %{optflags}" all
dos2unix *.txt

%install
install -Dpm 0755 src/dynamo \
  %{buildroot}%{_bindir}/dynamo

%files
%license LICENSE.txt
%doc CHANGELOG.txt CREDITS.txt DEVGUIDE.txt README.txt
%{_bindir}/dynamo

%changelog
