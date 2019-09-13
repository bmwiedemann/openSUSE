#
# spec file for package libfm-extra
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


Name:           libfm-extra
Version:        1.3.1
Release:        0
Summary:        A glib/gio-based lib used to develop file managers
License:        GPL-2.0-or-later
Group:          Development/Libraries/C and C++
Url:            http://www.lxde.org/
Source:         https://github.com/lxde/libfm/archive/%{version}.tar.gz
BuildRequires:  gcc-c++
BuildRequires:  gtk2-devel
BuildRequires:  intltool
BuildRequires:  libtool
BuildRequires:  pkg-config
# Optional: HTML developers documentation
BuildRequires:  gtk-doc >= 1.14
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
A glib/gio-based library providing some file management utilities and
related-widgets missing in gtk+/glib. This is the core of PCManFM. The
library is desktop independent (not LXDE specific) and has clean API.
It can be used to develop other applications requiring file management
functionality. For example, you can create your own file manager with
facilities provided by libfm.

%package -n libfm-extra4
Summary:        A glib/gio-based lib used to develop file managers
Group:          Development/Libraries/C and C++

%description -n libfm-extra4
A glib/gio-based library providing some file management utilities and
related-widgets missing in gtk+/glib. This is the core of PCManFM. The
library is desktop independent (not LXDE specific) and has clean API.
It can be used to develop other applications requiring file management
functionality. For example, you can create your own file manager with
facilities provided by libfm.

%package devel
Summary:        Devel files for libfm
Group:          Development/Libraries/C and C++
Requires:       libfm-extra4 = %{version}
Requires:       pkg-config

%description devel
A glib/gio-based lib used to develop file managers providing some
file management utilities and related-widgets missing in gtk+/glib.

%prep
%setup -q -n libfm-%{version}

%build
./autogen.sh
%configure \
	--disable-static \
	--with-extra-only

# remove rpath
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
# macro for parallel make
make %{?_smp_mflags}

%install
%make_install
rm -f %{buildroot}%{_libdir}/*.la

%post   -n libfm-extra4 -p /sbin/ldconfig

%postun -n libfm-extra4 -p /sbin/ldconfig

%files -n libfm-extra4
%defattr(-,root,root)
%doc AUTHORS COPYING NEWS  README  TODO
%{_libdir}/libfm-extra.so.4
%{_libdir}/libfm-extra.so.4.*

%files devel
%defattr(-,root,root)
%dir %{_includedir}/libfm-1.0
%{_includedir}/libfm-1.0/fm-extra.h
%{_includedir}/libfm-1.0/fm-version.h
%{_includedir}/libfm-1.0/fm-xml-file.h
%{_includedir}/libfm
%{_libdir}/pkgconfig/libfm-extra.pc
%{_libdir}/libfm-extra.so

%changelog
