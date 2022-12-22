#
# spec file for package guile-cairo
#
# Copyright (c) 2022 SUSE LLC
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


%define sover 0
Name:           guile-cairo
Version:        1.11.2
Release:        0
Summary:        Guile bindings to Cairo
License:        LGPL-3.0-or-later
Group:          Development/Libraries/Other
URL:            https://www.nongnu.org/guile-cairo/
Source0:        http://download.savannah.gnu.org/releases/guile-cairo/guile-cairo-%{version}.tar.gz
Source1:        http://download.savannah.gnu.org/releases/guile-cairo/guile-cairo-%{version}.tar.gz.sig
BuildRequires:  cairo-devel >= 1.10.0
BuildRequires:  guile-devel
Requires(post): %{install_info_prereq}
Requires(preun):%{install_info_prereq}
Requires:       lib%{name}%{sover}

%description
Guile bindings to Cairo library.

%package -n lib%{name}%{sover}
Summary:        Guile cairo libary
Group:          System/Libraries

%description -n lib%{name}%{sover}
Libraries for Guile bindings for Cairo.

%package devel
Summary:        Development files for Guile Cairo bindings
Group:          Development/Libraries/Other
Requires:       %{name} = %{version}
Requires:       cairo-devel
Requires:       guile-devel

%description devel
Files required to build software using Guile Cairo bindings.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
%make_install
# get rid of unused library
rm %{buildroot}%{_libdir}/lib%{name}.la

%post
%install_info --info-dir=%{_infodir} %{_infodir}/%{name}.info.gz

%preun
%install_info_delete --info-dir=%{_infodir} %{_infodir}/%{name}.info.gz

%post -n lib%{name}%{sover} -p /sbin/ldconfig
%postun -n lib%{name}%{sover} -p /sbin/ldconfig

%files
%license COPYING.LESSER COPYING
%doc AUTHORS HACKING NEWS README TODO ChangeLog
%{_datadir}/guile
%{_infodir}/%{name}.info*

%files -n lib%{name}%{sover}
%{_libdir}/lib%{name}.so.*

%files devel
%{_libdir}/pkgconfig/%{name}.pc
%{_libdir}/lib%{name}.so
%{_includedir}/%{name}

%changelog
