#
# spec file for package at-spi-sharp
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


Name:           at-spi-sharp
Version:        1.1.1
Release:        0
Summary:        Mono bindings for AT-SPI
License:        MIT
Group:          Development/Languages/Other
URL:            https://github.com/mono/at-spi-sharp
#Source:         https://github.com/mono/at-spi-sharp/archive/%{version}/%{name}-%{version}.tar.gz
# run ./autogen.sh locally to git clone ndesk-dbus
Source:         %{name}-%{version}.tar.gz
BuildRequires:  glib-sharp2
BuildRequires:  gtk-sharp2
BuildRequires:  libtool
BuildRequires:  mono-devel
BuildRequires:  ndesk-dbus-glib-devel
BuildRequires:  nunit-devel
BuildRequires:  pkgconfig
Requires:       mono-core
BuildArch:      noarch

%description
C-Sharp/Mono bindings for Assistive Technology Service Provider Interface

%package devel
Summary:        Development package for at-spi-sharp mono bindings
Group:          Development/Languages/Other
Requires:       %{name} = %{version}

%description devel
Development package that contains the pkgconfig file for at-spi-sharp.

%prep
%setup -q
#NOCONFIGURE=1 ./autogen.sh

%build
%configure --disable-tests --libdir=%{_prefix}/lib
mkdir -p at-spi/bin # work around Makefile parallelism issue
%make_build

%install
%make_install
# -- move pkgconfig files to /usr/share
mkdir %{buildroot}%{_datadir}/pkgconfig -p
pushd %{buildroot}%{_prefix}/lib/pkgconfig
for i in `ls | grep \.pc`; do
   install -D -m 0644 $i %{buildroot}%{_datadir}/pkgconfig/$i
   rm $i
done
popd

%files
%dir %{_prefix}/lib/mono/accessibility
%dir %{_prefix}/lib/mono/gac/at-spi-sharp/
%{_prefix}/lib/mono/accessibility/at-spi-sharp.dll
%{_prefix}/lib/mono/gac/at-spi-sharp/*

%files devel
%{_datadir}/pkgconfig/at-spi-sharp.pc

%changelog
