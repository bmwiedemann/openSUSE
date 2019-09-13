#
# spec file for package kate4-parts
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


Name:           kate4-parts
Version:        4.14.3
Release:        0
Summary:        Kate parts for Dolphin
License:        GPL-2.0+
Group:          Productivity/Editors/Other
Url:            http://www.kde.org/
Source0:        kate-%{version}.tar.xz
# PATCH-FIX-UPSTREAM gcc7-fix.patch -- fix build with GCC7
Patch:          gcc7-fix.patch
BuildRequires:  libkactivities-devel
BuildRequires:  libkde4-devel >= %version
BuildRequires:  libqjson-devel
BuildRequires:  xz
Provides:       libktexteditor = %{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Requires:       libkatepartinterfaces4 = %{version}
%kde4_runtime_requires

%description
The Kate parts that are required for integration with Dolphin


%package -n libkatepartinterfaces4
Summary:        Library to interface with kateparts
Group:          Productivity/Editors/Other

%description -n libkatepartinterfaces4
The library required by Kate parts.

%prep
%setup -q -n kate-%{version}
%patch -p1

%build
%ifarch ppc64
RPM_OPT_FLAGS="%{optflags} -mminimal-toc"
%endif
  %cmake_kde4 -d build
  %make_jobs

%install
  pushd build/addons/ktexteditor
  %kde4_makeinstall
  popd
  pushd build/part
  %kde4_makeinstall
  popd

%post -n libkatepartinterfaces4 -p /sbin/ldconfig

%postun -n libkatepartinterfaces4 -p /sbin/ldconfig

%clean
  rm -rf %{buildroot}

%files -n libkatepartinterfaces4
%defattr(-,root,root)
%{_kde4_libdir}/libkatepartinterfaces.so*

%files
%defattr(-,root,root)
%{_kde4_modulesdir}/ktexteditor_*.so
%{_kde4_modulesdir}/katepart.so
%{_kde4_servicesdir}/ktexteditor_*.desktop
%{_kde4_servicesdir}/katepart.desktop
%{_kde4_appsdir}/ktexteditor_*
%{_kde4_iconsdir}/hicolor/scalable/apps/*.svgz
%{_kde4_configdir}/ktexteditor_*.knsrc
%{_kde4_configdir}/kate*
%{_kde4_appsdir}/katepart/

%changelog
