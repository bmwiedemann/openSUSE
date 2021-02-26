#
# spec file for package bitlbee-facebook
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


%define from_checkout 1
Name:           bitlbee-facebook
Version:        1.2.2+git.1614281748.a31ccbe
Release:        0
Summary:        The Facebook protocol plugin for bitlbee
License:        GPL-2.0-only
Group:          Productivity/Networking/IRC
URL:            https://github.com/bitlbee/bitlbee-facebook
%if 0%{?from_checkout}
Source:         %{name}-%{version}.tar.gz
%else
Source:         https://github.com/bitlbee/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.gz
%endif
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(bitlbee)
BuildRequires:  pkgconfig(json-glib-1.0)

%description
The Facebook protocol plugin for bitlbee. This plugin uses the Facebook Mobile API.

%prep
%setup -q

%build
%if 0%{?from_checkout}
./autogen.sh
%endif
%configure
make %{?_smp_mflags}
 
%install
make %{?_smp_mflags} DESTDIR=%{buildroot} install
rm %{buildroot}%{_libdir}/bitlbee/facebook.la

%files
%doc ChangeLog README COPYING
%dir %{_libdir}/bitlbee
%{_libdir}/bitlbee/facebook.so

%changelog
