#
# spec file for package libmbim
#
# Copyright (c) 2023 SUSE LLC
# Copyright (c) 2013 Dominique Leuenberger, Amsterdam, The Netherlands
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


Name:           libmbim
Version:        1.28.4
Release:        0
Summary:        Mobile Broadband Interface Model (MBIM) protocol
License:        GPL-2.0-or-later AND LGPL-2.0-or-later
Group:          Productivity/Networking/System
URL:            https://gitlab.freedesktop.org/mobile-broadband/libmbim
Source:         %{name}-%{version}.tar.xz
# PATCH-FIX-UPSTREAM 0001-intel-mutual-authentication-new-service-fcc-lock.patch -- intel-mutual-authentication: new service, fcc-lock
Patch:          0001-intel-mutual-authentication-new-service-fcc-lock.patch
# PATCH-FIX-UPSTREAM 0002-intel-tools-new-service-trace-config.patch --intel-tools: new service, trace-config
Patch2:         0002-intel-tools-new-service-trace-config.patch

BuildRequires:  help2man
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  python3-base
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(glib-2.0) >= 2.48
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(udev)

%description
libmbim is a glib-based library for talking to WWAN modems and devices
which speak the Mobile Broadband Interface Model (MBIM) protocol.

%package -n libmbim-glib4
Summary:        Mobile Broadband Interface Model (MBIM) protocol
License:        LGPL-2.1-or-later
Group:          System/Libraries

%description -n libmbim-glib4
libmbim is a glib-based library for talking to WWAN modems and devices
which speak the Mobile Broadband Interface Model (MBIM) protocol.

%package devel
Summary:        Mobile Broadband Interface Model (MBIM) protocol - Development files
License:        LGPL-2.1-or-later
Group:          Development/Languages/C and C++
Requires:       libmbim-glib4 = %{version}

%description devel
libmbim is a glib-based library for talking to WWAN modems and devices
which speak the Mobile Broadband Interface Model (MBIM) protocol.

%package -n mbimcli-bash-completion
Summary:        Bash completion for mbimcli
License:        GPL-2.0-or-later AND LGPL-2.0-or-later
Group:          Productivity/Networking/System
BuildArch:      noarch
BuildRequires:  pkgconfig(bash-completion)
Requires:       bash-completion
Supplements:    (%{name} and bash-completion)

%description -n mbimcli-bash-completion
This package contain de bash completion command for mbimcli tools.

%package -n typelib-1_0-Mbim-1_0
Summary:        Introspection bindings for libmbim
License:        GPL-2.0-or-later AND LGPL-2.0-or-later
Group:          System/Libraries

%description -n typelib-1_0-Mbim-1_0
libmbim is a glib-based library for talking to WWAN modems and devices
which speak the Mobile Broadband Interface Model (MBIM) protocol.

This package provides the GObject Introspection bindings for libmbim.

%prep
%autosetup -p1

%build
%meson \
	%{nil}
%meson_build

%install
%meson_install

%check
%meson_test

%ldconfig_scriptlets -n libmbim-glib4

%files
%doc NEWS
%{_bindir}/mbim-network
%{_bindir}/mbimcli
%{_libexecdir}/mbim-proxy
%{_mandir}/man1/mbim-network.1%{?ext_man}
%{_mandir}/man1/mbimcli.1%{?ext_man}

%files -n libmbim-glib4
%license LICENSES
%{_libdir}/libmbim-glib.so.*

%files devel
%doc AUTHORS README.md
%{_datadir}/gir-1.0/*.gir
%{_includedir}/libmbim-glib/
%{_libdir}/libmbim-glib.so
%{_libdir}/pkgconfig/mbim-glib.pc

%files -n mbimcli-bash-completion
%{_datadir}/bash-completion/completions/mbimcli

%files -n typelib-1_0-Mbim-1_0
%{_libdir}/girepository-1.0/Mbim-1.0.typelib

%changelog
