#
# spec file for package smssend
#
# Copyright (c) 2011 SUSE LINUX Products GmbH, Nuernberg, Germany.
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



Name:           smssend
BuildRequires:  libtool openssl-devel pcre-devel zlib-devel
License:        GPL-2.0+
Group:          Hardware/Mobile
Version:        3.4
Release:        0
Source0:        %{name}-%{version}.tar.bz2
%define       skyutils_version  2.7
Source1:        skyutils-%{skyutils_version}.tar.bz2
Patch1:         %{name}-%{version}-updated_scripts.diff.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Summary:        interface to internet SMS forwarding services
URL:            http://zekiller.skytech.org/smssend_menu_en.html

%description
smssend is a utility providing a command line interface to the GSM
Short Message Service (SMS) via internet gateways. It requires an
active internet connection (HTTP proxy is suitable) and may require a
registration for such gateways. The program is quite configurable for
other gateways than provided, examples are included.

Keep in mind that these internet to SMS gateways may not tolerate and
may even forbid their use via scripts.

%prep
%setup -a 1
%patch1

%build
%{?suse_update_config:%{suse_update_config -f . skyutils-2.4}}
libtoolize --force
autoreconf --force --install
cd skyutils-%{skyutils_version}
autoreconf --force --install
%configure --libdir=${PWD}/src/.libs \
		--disable-shared \
		--enable-static
make %{?_smp_mflags}
cd ..
%configure \
		--datadir=/usr/share \
		--disable-shared \
		--with-skyutils=${PWD}/skyutils-%{skyutils_version} \
		--with-data-dir=/usr/share/xfce
# feel free to improve following change and please notify upstream
sed -i "s:\(^LIBS =.*\):\1 -lcrypto:" Makefile
make %{?_smp_mflags}

%install
make DESTDIR=$RPM_BUILD_ROOT install 
cd skyutils-%{skyutils_version}
mkdir -p ${RPM_BUILD_ROOT}/usr/share/doc/packages/smssend/skyutils
cp -p AUTHORS COPYING ChangeLog INSTALL NEWS README ${RPM_BUILD_ROOT}/usr/share/doc/packages/smssend/skyutils/
cd ..
cp -p INSTALL ChangeLog AUTHORS COPYING NEWS README AUTHORS ${RPM_BUILD_ROOT}/usr/share/doc/packages/smssend
install -m 644 scripts/*.sms ${RPM_BUILD_ROOT}/usr/share/smssend/

%files
%defattr(-,root,root)
%doc /usr/share/doc/packages/smssend
/usr/bin/smssend
/usr/bin/email2smssend
/usr/bin/bestsms.sh
/usr/share/smssend/
%doc %{_mandir}/man1/*
%lang(fr) %doc %{_mandir}/fr

%changelog
