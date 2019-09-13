#
# spec file for package at-spi-sharp
#
# Copyright (c) 2013 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           at-spi-sharp
Version:        1.1.0
Release:        0
Url:            http://www.mono-project.com/Accessibility
Source0:        %{name}-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Requires:       mono-core >= 2.4
BuildRequires:  mono-devel >= 2.4
BuildRequires:  mono-uia >= 2.0
BuildRequires:  ndesk-dbus-glib-devel
BuildRequires:  pkg-config
BuildArch:      noarch
Summary:        Mono bindings for AT-SPI
License:        MIT
Group:          System/Libraries

%description
C-Sharp/Mono bindings for Assistive Technology Service Provider Interface

%package devel
Summary:        Development package for at-spi-sharp mono bindings
Group:          Development/Languages/Mono
Requires:       %{name} = %{version}

%description devel
Development package that contains the pkgconfig file for at-spi-sharp.

%prep
%setup -q

%build
%configure --disable-tests --libdir=%{_prefix}/lib
make %{?_smp_flags}

%install
%makeinstall
# -- move pkgconfig files to /usr/share
mkdir %{buildroot}%{_datadir}/pkgconfig -p
pushd %{buildroot}%{_prefix}/lib/pkgconfig
for i in `ls | grep \.pc`; do
   %{__install} -D -m 0644 $i %{buildroot}%{_datadir}/pkgconfig/$i
   %{__rm} $i
done
popd

%files
%defattr(-,root,root)
%dir %{_prefix}/lib/mono/gac/at-spi-sharp/
%{_prefix}/lib/mono/accessibility/at-spi-sharp.dll
%{_prefix}/lib/mono/gac/at-spi-sharp/*

%files devel
%defattr(-,root,root)
%{_datadir}/pkgconfig/at-spi-sharp.pc

%changelog
