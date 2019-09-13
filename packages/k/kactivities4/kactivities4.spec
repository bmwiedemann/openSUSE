#
# spec file for package kactivities4
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
# Copyright 2010 Open-SLX GmbH <sebas@open-slx.com>
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


Name:           kactivities4
Version:        4.13.3
Release:        0
Summary:        KDE Plasma Activities support
License:        GPL-2.0+ and LGPL-2.1+
Group:          System/GUI/KDE
Url:            http://www.kde.org
Source:         kactivities-%{version}.tar.xz
Source1:        baselibs.conf
BuildRequires:  libkde4-devel >= %version
BuildRequires:  update-desktop-files
BuildRequires:  xz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%kde4_runtime_requires

%description
Kactivities provides an API for using and interacting with the Plasma Active
Activities Manager.

%package -n libkactivities6
Provides:       libkactivities = %version
Obsoletes:      libkactivities <= 4.8.0
Summary:        Development files and headers for kactivities
Group:          System/Libraries

%description -n libkactivities6
Kactivities provides an API for using and interacting with the Plasma Active
Activities Manager.

%package -n libkactivities-devel
Summary:        Development files and headers for kactivities
Group:          Development/Libraries/KDE
Requires:       libkactivities6 = %{version}
Requires:       libkde4-devel >= %{version}

%description -n libkactivities-devel
Development headers for the kactivities4 library

%prep
%setup -qn kactivities-%{version}

%build
%cmake_kde4 -d builddir -- -DKACTIVITIES_LIBRARY_ONLY=ON
%make_jobs

%install
%kde4_makeinstall -C builddir
%kde_post_install

rm -rf %{buildroot}%{_kde4_datadir}/ontology/

%post -n libkactivities6 -p /sbin/ldconfig

%postun -n libkactivities6 -p /sbin/ldconfig

%files -n libkactivities6
%defattr(-,root,root,-)
%{_kde4_libdir}/libkactivities.so.*

%files -n libkactivities-devel
%defattr(-,root,root,-)
%{_kde4_libdir}/libkactivities.so
%{_kde4_includedir}/kactivities/
%{_kde4_includedir}/KDE/KActivities/
%{_kde4_libdir}/cmake/KActivities/
%{_kde4_libdir}/pkgconfig/*

%changelog
