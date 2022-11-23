#
# spec file for package shibboleth-sp
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


%define libvers 11
%define libvers_lite 11
%define runuser shibd
%define realname shibboleth
%define pkgdocdir %{_docdir}/%{realname}
Name:           shibboleth-sp
Version:        3.4.0
Release:        0
Summary:        System for attribute-based Web Single Sign On
License:        Apache-2.0
Group:          Productivity/Networking/Security
URL:            https://shibboleth.net/
Source0:        http://shibboleth.net/downloads/service-provider/%{version}/%{name}-%{version}.tar.bz2
Source1:        http://shibboleth.net/downloads/service-provider/%{version}/%{name}-%{version}.tar.bz2.asc
Source2:        %{name}.keyring
Source3:        shibd.service
Patch0:         shibboleth-sp-2.5.5-doxygen_timestamp.patch
BuildRequires:  apache2-devel
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  krb5-devel
BuildRequires:  libboost_headers-devel
BuildRequires:  liblog4shib-devel >= 2
BuildRequires:  libmemcached-devel
BuildRequires:  libsaml-devel >= 3.1.0
BuildRequires:  libtool
BuildRequires:  libxerces-c-devel >= 3.2
BuildRequires:  libxml-security-c-devel >= 2.0.0
BuildRequires:  libxmltooling-devel >= 3.1.0
BuildRequires:  pkgconfig
BuildRequires:  systemd-rpm-macros
BuildRequires:  unixODBC-devel
BuildRequires:  zlib-devel
BuildRequires:  pkgconfig(libsystemd)
Requires:       openssl
Requires(pre):  opensaml-schemas >= 3.1.0
Requires(pre):  xmltooling-schemas >= 3.1.0
Requires(pre):  shadow
Obsoletes:      shibboleth-sp = 2.5.0
%{?systemd_requires}

%description
Shibboleth is a Web Single Sign-On implementations based on OpenSAML
that supports multiple protocols, federated identity, and the extensible
exchange of rich attributes subject to privacy controls.

This package contains the Shibboleth Service Provider runtime libraries,
daemon, default plugins, and Apache module.

%package -n libshibsp%{libvers}
Summary:        Shared Library for Shibboleth
Group:          Productivity/Networking/Security

%description -n libshibsp%{libvers}
Shibboleth is a Web Single Sign-On implementations based on OpenSAML
that supports multiple protocols, federated identity, and the extensible
exchange of rich attributes subject to privacy controls.

This package contains just the shared library.

%package -n libshibsp-lite%{libvers_lite}
Summary:        Shared Library for Shibboleth
Group:          Productivity/Networking/Security

%description -n libshibsp-lite%{libvers_lite}
Shibboleth is a Web Single Sign-On implementations based on OpenSAML
that supports multiple protocols, federated identity, and the extensible
exchange of rich attributes subject to privacy controls.

This package contains just the shared library.

%package devel
Summary:        Shibboleth Development Headers
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}-%{release}
Requires:       liblog4shib-devel >= 2
Requires:       libsaml-devel >= 3.1.0
Requires:       libshibsp%{libvers} = %{version}-%{release}
Requires:       libshibsp-lite%{libvers_lite} = %{version}-%{release}
Requires:       libxerces-c-devel >= 3.2
Requires:       libxml-security-c-devel >= 2.0.0
Requires:       libxmltooling-devel >= 3.1.0
Obsoletes:      shibboleth-sp-devel = 2.5.0

%description devel
Shibboleth is a Web Single Sign-On implementations based on OpenSAML
that supports multiple protocols, federated identity, and the extensible
exchange of rich attributes subject to privacy controls.

This package includes files needed for development with Shibboleth.

%prep
%setup -q
%patch0 -p1

%build
export CXXFLAGS="%{optflags} --std=c++11"
autoreconf -f -i
%configure --with-gssapi --enable-systemd --with-memcached
%make_build pkgdocdir=%{pkgdocdir}

%install
%make_install NOKEYGEN=1 pkgdocdir=%{pkgdocdir}

install -D -m 644 %{SOURCE3} %{buildroot}%{_unitdir}/shibd.service
ln -sf %{_sbindir}/service %{buildroot}/%{_sbindir}/rcshibd

sed -i "s|/var/log/httpd|/var/log/apache2|g" \
		%{buildroot}%{_sysconfdir}/%{realname}/native.logger

sed -i "s|%{_bindir}/env bash|%{_bindir}/bash|" \
		%{buildroot}%{_sysconfdir}/%{realname}/metagen.sh

# Delete unnecessary files
pushd %{buildroot}/%{_sysconfdir}/%{realname}
rm shibd-debian shibd-redhat shibd-amazon shibd-suse shibd-osx.plist apache.config apache2.config apache22.config shibd-systemd
rm *.dist
popd
find %{buildroot} -type f -name "*.la" -delete -print

# Plug the SP into the Apache
touch rpm.filelist
APACHE_CONFIG="no"
if [ -f %{buildroot}%{_libdir}/%{realname}/mod_shib_24.so ] ; then
	APACHE_CONFIG="apache24.config"
fi

if [ "$APACHE_CONFIG" != "no" ] ; then
	APACHE_CONFD="no"
	if [ -d %{_sysconfdir}/apache2/conf.d ] ; then
		APACHE_CONFD="%{_sysconfdir}/apache2/conf.d"
	fi
	if [ "$APACHE_CONFD" != "no" ] ; then
		mkdir -p $RPM_BUILD_ROOT$APACHE_CONFD
		cp -p %{buildroot}%{_sysconfdir}/%{realname}/$APACHE_CONFIG $RPM_BUILD_ROOT$APACHE_CONFD/shib.conf
		echo "%config(noreplace) $APACHE_CONFD/shib.conf" >> rpm.filelist
	fi
fi

# Get run directory created at boot time.
mkdir -p %{buildroot}%{_tmpfilesdir}
echo "%attr(0444,-,-) %{_tmpfilesdir}/%{realname}.conf" >> rpm.filelist
cat > %{buildroot}%{_tmpfilesdir}/%{realname}.conf <<EOF
d /run/%{realname} 755 %{runuser} %{runuser} -
EOF

%check
%make_build check

%pre
getent group %{runuser} >/dev/null || groupadd -r %{runuser}
getent passwd %{runuser} >/dev/null || useradd -r -g %{runuser} \
	-d  %{_localstatedir}/run/%{realname} -s /sbin/nologin -c "Shibboleth SP daemon" %{runuser}
%service_add_pre shibd.service
exit 0

%post -n libshibsp%{libvers} -p /sbin/ldconfig
%post -n libshibsp-lite%{libvers_lite} -p /sbin/ldconfig

%post

# Generate two keys on new installs.
if [ $1 -eq 1 ] ; then
        cd %{_sysconfdir}/shibboleth
        /bin/sh ./keygen.sh -b -n sp-signing -u %{runuser} -g %{runuser}
        /bin/sh ./keygen.sh -b -n sp-encrypt -u %{runuser} -g %{runuser}
fi

%service_add_post shibd.service

%tmpfiles_create %{_tmpfilesdir}/%{realname}.conf

%preun
# On final removal, stop shibd and remove service, restart Apache if running.
%service_del_preun shibd.service
if [ $1 -eq 0 ] ; then
	/sbin/service apache2 status 1>/dev/null && /sbin/service apache2 restart 1>/dev/null
fi
exit 0

%postun -n libshibsp%{libvers} -p /sbin/ldconfig
%postun -n libshibsp-lite%{libvers_lite} -p /sbin/ldconfig

%postun
%service_del_postun shibd.service
%restart_on_update apache2

%posttrans
# One-time extra restart of shibd and Apache to work around
# SUSE bug that breaks old %%restart_on_update macro.
# If we remove, upgrades from pre-systemd to post-systemd
# will stop doing the final restart.
%{_bindir}/systemctl try-restart shibd >/dev/null 2>&1 || :
%{_bindir}/systemctl try-restart apache2 >/dev/null 2>&1 || :
exit 0

%files -f rpm.filelist
%{_sbindir}/shibd
%{_sbindir}/rcshibd
%{_bindir}/mdquery
%{_bindir}/resolvertest
%dir %{_libdir}/%{realname}
%{_libdir}/%{realname}/*
%{_unitdir}/shibd.service
%attr(0750,%{runuser},%{runuser}) %dir %{_localstatedir}/log/%{realname}
%attr(0755,%{runuser},%{runuser}) %dir %{_localstatedir}/cache/%{realname}
%ghost %attr(0755,%{runuser},%{runuser}) %dir /run/%{realname}
%dir %{_datadir}/xml/%{realname}
%{_datadir}/xml/%{realname}/*
%dir %{_datadir}/%{realname}
%{_datadir}/%{realname}/*
%dir %{_sysconfdir}/%{realname}
%config(noreplace) %{_sysconfdir}/%{realname}/*.xml
%config(noreplace) %{_sysconfdir}/%{realname}/*.html
%config(noreplace) %{_sysconfdir}/%{realname}/*.logger
%{_tmpfilesdir}/%{realname}.conf
%{_sysconfdir}/%{realname}/apache24.config
%attr(0755,root,root) %{_sysconfdir}/%{realname}/keygen.sh
%attr(0755,root,root) %{_sysconfdir}/%{realname}/metagen.sh
%attr(0755,root,root) %{_sysconfdir}/%{realname}/seckeygen.sh
%doc %{pkgdocdir}
%exclude %{pkgdocdir}/api

%files -n libshibsp%{libvers}
%{_libdir}/libshibsp.so.*

%files -n libshibsp-lite%{libvers_lite}
%{_libdir}/libshibsp-lite.so.*

%files devel
%{_includedir}/*
%{_libdir}/libshibsp.so
%{_libdir}/libshibsp-lite.so
%{_libdir}/pkgconfig/*.pc
%doc %{pkgdocdir}/api

%changelog
