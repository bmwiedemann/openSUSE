#
# spec file for package nant
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


Name:           nant
Version:        0.92+git20130131
Release:        0
BuildArch:      noarch
Url:            http://nant.sourceforge.net
# git clone //github.com/letiemble/nant.git
Source0:        %{name}.tar.xz
# PATCH-FIX-OPENSUSE boo#1047218
Patch0:         reproducible.patch
Summary:        Ant for .NET
License:        GPL-2.0+ and LGPL-2.1+
Group:          Development/Tools/Building
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  dos2unix
BuildRequires:  mono-data
BuildRequires:  mono-devel
%define _use_internal_dependency_generator 0
# ignore some bundled dlls
%define __find_provides env sh -c 'filelist=($(grep -v log4net.dll | grep -v scvs.exe | grep -v nunit | grep -v NDoc | grep -v neutral)) && { printf "%s\\n" "${filelist[@]}" | /usr/lib/rpm/find-provides && printf "%s\\n" "${filelist[@]}" | /usr/bin/mono-find-provides ; } | sort | uniq'
%define __find_requires env sh -c 'filelist=($(cat)) && { printf "%s\\n" "${filelist[@]}" |  /usr/bin/mono-find-requires ; } | sort | uniq'

%description
NAnt is a free .NET build tool. In theory it is kind of like make
without make's wrinkles. In practice it's a lot like Ant.

%package devel
Summary:        NAnt pkgconfig files
License:        LGPL-2.1
Group:          Development/Languages/Mono
Requires:       nant

%description devel
This package contains the pkgconfig files for NAnt.

%prep
%setup -q -n %{name}
%patch0 -p1

%build
make TARGET=mono-4.5 MCS="mcs -sdk:4"

%install
make install prefix=%{_prefix} DESTDIR=%{buildroot} TARGET=mono-4.5 MCS="mcs -sdk:4" docdir=%{_docdir}
mkdir -p %{buildroot}%{_datadir}
mv %{buildroot}%{_prefix}/lib/pkgconfig %{buildroot}%{_datadir}/

chmod -x %{buildroot}%{_datadir}/NAnt/bin/lib/common/2.0/nunit-console.exe.config
dos2unix %{buildroot}%{_datadir}/NAnt/bin/lib/common/2.0/nunit-console.exe.config
dos2unix -r %{buildroot}%{_datadir}/pkgconfig/%{name}.pc

%files
%defattr(-, root, root)
%doc COPYING.txt
%{_bindir}/%{name}
%{_datadir}/NAnt
%doc %{_docdir}/NAnt/

%files devel
%defattr(-, root, root)
%{_datadir}/pkgconfig/%{name}.pc

%changelog
