#
# spec file for package xtrans
#
# Copyright (c) 2020 SUSE LLC
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


Name:           xtrans
Version:        1.4.0
Release:        0
Summary:        Library to handle network protocol transport in X
License:        MIT
Group:          Development/Libraries/X11
URL:            https://xorg.freedesktop.org/
Source:         http://xorg.freedesktop.org/archive/individual/lib/%{name}-%{version}.tar.bz2
Patch0:         p_xauth.diff
Patch1:         n_unifdef-LBXPROXY_t-and-TEST_t.patch
Patch2:         u_xtrans-noarch-pkgconfig.patch
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(xorg-macros) >= 1.12
BuildRequires:  pkgconfig(xshmfence)
# Package was named xorg-x11-xtrans-devel until 12.2
# We use 7.7 for Provides/Obsoletes, since we're renaming the packages when
# X11R7.7 is in RC1, and xorg-x11-xtrans-devel was version 7.6
Provides:       xorg-x11-xtrans-devel = 7.7
Obsoletes:      xorg-x11-xtrans-devel < 7.7
BuildArch:      noarch

%description
xtrans is a library of code that is shared among various X packages to
handle network protocol transport in a modular fashion, allowing a
single place to add new transport types. It is used by the X server,
libX11, libICE, the X font server, and related components.

%prep
%setup -q
%patch0
%patch1 -p1 -R
%patch2 -p1

%build
%configure --docdir=%{_docdir}/xtrans
make %{?_smp_mflags}

%install
%make_install

%pre
test -L usr/include/X11 && rm usr/include/X11
exit 0

%files
%license COPYING
%doc AUTHORS ChangeLog README.md
%doc doc/xtrans.xml
%{_includedir}/X11/Xtrans/
%dir %{_datadir}/aclocal
%{_datadir}/aclocal/xtrans.m4
%{_datadir}/pkgconfig/xtrans.pc

%changelog
