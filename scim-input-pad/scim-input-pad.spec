#
# spec file for package scim-input-pad
#
# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           scim-input-pad
Version:        0.1.3.20130804
Release:        0
Summary:        An onscreen input pad to easily input symbols
License:        GPL-2.0+
Group:          System/I18n/Chinese
Url:            https://github.com/scim-im/scim-input-pad
Source:         %{name}-%{version}.tar.gz
Patch:          scim-input-pad-missing-fclose.diff
BuildRequires:  gcc-c++
BuildRequires:  intltool
BuildRequires:  libtool
BuildRequires:  scim-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%if 0%{?sles_version}
BuildRequires:  gtk2-devel
%else
BuildRequires:  gtk3-devel
%endif

%description
An onscreen input pad to easily input symbols

%prep
%setup -q
%patch -p1
./bootstrap

%build
CXXFLAGS="%{optflags}" \
%configure --with-pic \
	   --disable-static \
	   --enable-debug \
	   --disable-rpath \
%if 0%{?sles_version}
	   --with-gtk-version=2
%endif

make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install %{?_smp_mflags}
find %{buildroot} -name "*.la" -delete -print

%find_lang %{name}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(-, root, root)
%doc COPYING README ChangeLog
%{_bindir}/scim-input-pad
%{_libdir}/libscim-input-pad.so
%{_libdir}/libscim-input-pad.so.0
%{_libdir}/libscim-input-pad.so.0.1.0
%{_scim_helperdir}/input-pad.so
%{_scim_icondir}/input-pad.png

%changelog
