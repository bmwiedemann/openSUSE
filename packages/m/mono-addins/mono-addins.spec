#
# spec file for package mono-addins
#
# Copyright (c) 2020 SUSE LLC.
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


Name:           mono-addins
Version:        1.3.3
Release:        0
Summary:        Mono Addins Framework
License:        MIT
Group:          Development/Languages/Mono
URL:            https://github.com/mono/mono-addins
Source:         https://github.com/mono/mono-addins/archive/%{name}-%{version}.tar.gz
Patch0:         fix-delay-sign.patch
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gtk-sharp-2.0)
BuildRequires:  pkgconfig(mono)
BuildArch:      noarch

%description
Mono.Addins is a generic framework for creating extensible
applications, and for creating libraries which extend those
applications.

%package msbuild
Summary:        Mono Addins Framework, MSBuild Support
Group:          Development/Languages/Mono
Requires:       %{name} = %{version}

%description msbuild
Mono.Addins is a generic framework for creating extensible
applications, and for creating libraries which extend those
applications.

This package contains MSBuild tasks file and target, which allows
using add-in references directly in a build file (still experimental).

%package devel
Summary:        Mono Addins Framework, MSBuild Support
Group:          Development/Languages/Mono
Requires:       %{name} = %{version}

%description devel
Mono.Addins is a generic framework for creating extensible
applications, and for creating libraries which extend those
applications.

This package contains the pkgconfig files.

%prep
%setup -q -n mono-addins-mono-addins-%{version}
%patch0 -p1

%build
./autogen.sh
%configure --libdir=%{_prefix}/lib
%make_build

%install
make install DESTDIR=%{buildroot} GACUTIL_FLAGS="/package mono-addins /root %{buildroot}%{_prefix}/lib"
mkdir -p %{buildroot}%{_datadir}/pkgconfig
mv %{buildroot}%{_prefix}/lib/pkgconfig/*.pc %{buildroot}%{_datadir}/pkgconfig

%files
%{_bindir}/mautil
%{_prefix}/lib/mono/gac/*Mono.Addins
%{_prefix}/lib/mono/gac/*Mono.Addins.Cecil*
%{_prefix}/lib/mono/gac/*Mono.Addins.Gui*
%{_prefix}/lib/mono/gac/*Mono.Addins.Setup*
%dir %{_prefix}/lib/mono/mono-addins
%{_prefix}/lib/mono/mono-addins/mautil.exe
%{_prefix}/lib/mono/mono-addins/Mono.Addins.dll
%{_prefix}/lib/mono/mono-addins/Mono.Addins.Cecil*
%{_prefix}/lib/mono/mono-addins/Mono.Addins.Gui*
%{_prefix}/lib/mono/mono-addins/Mono.Addins.Setup*
%{_mandir}/man1/mautil.1%{?ext_man}

%files msbuild
%{_prefix}/lib/mono/gac/*Mono.Addins.MSBuild*
%{_prefix}/lib/mono/mono-addins/*MSBuild*

%files devel
%{_datadir}/pkgconfig/mono-addins.pc
%{_datadir}/pkgconfig/mono-addins-gui.pc
%{_datadir}/pkgconfig/mono-addins-setup.pc
%{_datadir}/pkgconfig/mono-addins-msbuild.pc

%changelog
