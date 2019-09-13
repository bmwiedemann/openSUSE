#
# spec file for package lv2-swh-plugins
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

%global pkgsrc lv2-1.0.16

Name:           lv2-swh-plugins
Version:        1.0.16
Release:        0
Summary:        LV2 ports of LADSPA swh plugins
License:        GPL-3.0
Group:          Productivity/Multimedia/Other
Url:            https://github.com/swh/lv2
Source:         https://github.com/swh/lv2/archive/v%{version}.tar.gz
Patch0:         source-xsl.patch
BuildRequires:  fftw3-devel
BuildRequires:  libxslt
BuildRequires:  lv2-devel
Requires:       lv2

%description
This is an early experimental port of my LADSPA plugins to the LV2
specification, c.f. http://lv2plug.in/ . It is still quite early days, but most
things should work as well or not as they did in LADSPA.

%prep
%setup -q -n %{pkgsrc}
%patch0 -p1

# We are using the system header:
rm -f include/lv2.h

%build
make %{?_smp_mflags} real-clean
make %{?_smp_mflags} \
	CFLAGS="-I%{_includedir} %{optflags}" \
	LDFLAGS="%{optflags}"


%install
make install-system INSTALL_DIR="%{buildroot}%{_libdir}/lv2"

%files
%doc COPYING README
%{_libdir}/lv2/*

%changelog
