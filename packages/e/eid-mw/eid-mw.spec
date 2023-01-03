#
# spec file for package eid-mw
#
# Copyright (c) 2023 SUSE LLC
# Copyright (c) 2014 Philipp Thomas <psmt@opensuse.org>
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


#define revision 8.g1beb6f2f
#define src_name eid-mw-%{version}-v%{version}.%{revision}

%define src_name eid-mw-%{version}-v%{version}

Name:           eid-mw
Version:        5.1.4
Release:        0
URL:            https://eid.belgium.be/nl
Summary:        Belgium electronic identity card PKCS#11 module and Firefox plugin
License:        LGPL-3.0-or-later
Group:          Productivity/Security
Source:         https://dist.eid.belgium.be/continuous/sources/%{src_name}.tar.gz
Source2:        https://dist.eid.belgium.be/continuous/sources/%{src_name}.tar.gz.asc
Source1:        baselibs.conf
#Source2:            eid-mw-rpmlintrc
Source99:       eid-mw.keyring
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gtk2-devel
BuildRequires:  libbsd-devel
BuildRequires:  libtool
BuildRequires:  pcsc-lite-devel
BuildRequires:  subversion
%if 0%{?suse_version}
Requires:       pcsc-ccid
BuildRequires:  MozillaFirefox
BuildRequires:  gcc-c++
BuildRequires:  glibc-devel
BuildRequires:  gtk3-devel
BuildRequires:  libproxy-devel
BuildRequires:  libxml2-devel
BuildRequires:  make
#BuildRequires:  libassuan-devel
BuildRequires:  libcurl-devel
BuildRequires:  libopenssl-devel
BuildRequires:  p11-kit-devel
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
Recommends:     pcsc-acr38
BuildRequires:  pcsc-acr38
Recommends:     pcsc-lite
BuildRequires:  pcsc-lite
Recommends:     zip
BuildRequires:  zip
%else
Requires:       ccid
%endif
Conflicts:      openct

%description
The eID Middleware provides the libraries, a PKCS#11 module and a Firefox
plugin to use Belgian eID (electronic identity) card in order to access
websites and/or sign documents. This package contains a few helper
programs needed by the eID Middleware and the infrastructure for eid-mw.

%package        devel
Summary:        Belgium electronic identity card PKCS#11 module - development package
Group:          Development/Libraries/C and C++
Requires:       eid-mw = %{version}

%description devel
The eID Middleware provides the libraries, a PKCS#11 module and a Firefox
plugin to use Belgian eID (electronic identity) card in order to access
websites and/or sign documents. This package contains the files needed
to develop against the eID Middleware.

%package        libs
Summary:        Belgium electronic identity card PKCS#11 module - libraries
Group:          System/Libraries

%description    libs
The eID Middleware provides the libraries, a PKCS#11 module and a Firefox
plugin to use Belgian eID (electronic identity) card in order to access
websites and/or sign documents. This package contains the actual libraries.

%package        firefox
Summary:        Firefox Extension for Belgium eID Middleware
Group:          Productivity/Networking/Web/Browsers
Recommends:     MozillaFirefox

%description firefox
Mozilla Firefox extension for using the Belgian eID (electronic identity card).

%package -n eid-viewer
Summary:        Belgium electronic identity card viewer
Group:          Productivity/Security
Requires:       eid-mw
%if 0%{?suse_version}
Requires:       pcsc-ccid
%else
Requires:       ccid
%endif
Requires:       pcsc-lite
Conflicts:      openct

%description -n eid-viewer
The eid-viewer application allows the user to read out any information from
a Belgian electronic identity card. Both identity information and information
about the stored cryptographic keys can be read in a user-friendly manner,
and can easily be printed out or stored for later reviewal.

The application verifies the signature of the identity information,
checks whether it was signed by a government-issued key, and optionally
checks the certificate against the government's Trust Service.

%prep
%setup -q -n %{src_name}

%build

%configure --enable-p11v220 --enable-webextension --disable-static

%{__make} %{?_smp_mflags}

%install
%{__make} install DESTDIR="%{buildroot}"
mkdir -p %{buildroot}%{_libdir}/mozilla/
mv %{buildroot}/usr/lib/mozilla/pkcs11-modules %{buildroot}%{_libdir}/mozilla/ || true
mv %{buildroot}/usr/lib/mozilla/managed-storage %{buildroot}%{_libdir}/mozilla/ || true
rm -f %{buildroot}%{_datadir}/applications/eid-viewer.desktop
desktop-file-install --dir %{buildroot}%{_datadir}/applications --add-category="Office;Viewer;" --vendor fedict plugins_tools/eid-viewer/eid-viewer.desktop || true

%find_lang about-eid-mw
%find_lang dialogs-beid
%find_lang eid-viewer

%post -n eid-mw-libs -p /sbin/ldconfig

%post -n eid-mw-firefox
if /usr/bin/pgrep 'firefox' &>/dev/null; then
    echo "INFO: You may have to restart Firefox for the Belgium eID add-on to work." >&2
elif /usr/bin/pgrep 'iceweasel' &>/dev/null; then
    echo "INFO: You may have to restart Iceweasel for the Belgium eID add-on to work." >&2
fi

%postun -n eid-mw-libs
/sbin/ldconfig
### Make pcscd reread configuration and rescan USB bus.
if /sbin/service pcscd status &>/dev/null; then
    %{_sbindir}/pcscd -H &>/dev/null || :
fi

%files -f about-eid-mw.lang -f dialogs-beid.lang
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING
%exclude %{_libdir}/*.la
%{_libexecdir}/beid-askaccess
%{_libexecdir}/beid-askpin
%{_libexecdir}/beid-badpin
%{_libexecdir}/beid-changepin
%{_libexecdir}/beid-spr-askpin
%{_libexecdir}/beid-spr-changepin
/etc/xdg/autostart/beid-update-nssdb.desktop
%{_bindir}/about-eid-mw
%{_bindir}/beid-update-nssdb

%files libs
%defattr(-,root,root)
%{_libdir}/libbeidpkcs11.so.*
%{_libdir}/libeidviewer.so.*
%dir %{_libdir}/pkcs11
%{_libdir}/pkcs11/beidpkcs11.so
%dir /usr/share/p11-kit
%dir /usr/share/p11-kit/modules
/usr/share/p11-kit/modules/beid.module

%files firefox
%defattr(-,root,root)
%dir %{_datadir}/mozilla/
%dir %{_libdir}/mozilla/pkcs11-modules
%dir %{_libdir}/mozilla/managed-storage
%{_libdir}/mozilla/pkcs11-modules/beidpkcs11_alt.json
%{_libdir}/mozilla/pkcs11-modules/beidpkcs11.json
%{_datadir}/mozilla/extensions/{ec8030f7-c20a-464f-9b0e-13a3a9e97384}/belgiumeid@eid.belgium.be.xpi
%{_libdir}/mozilla/managed-storage/belgiumeid@eid.belgium.be.json

%files devel
%defattr(-,root,root)
%{_libdir}/libbeidpkcs11.so
%{_libdir}/libeidviewer.so
%dir /usr/include/eid-util
%dir /usr/include/eid-viewer
%dir /usr/include/beid
%dir /usr/include/beid/rsaref220
/usr/include/eid-util/utftranslate.h
/usr/include/eid-viewer/certhelpers.h
/usr/include/eid-viewer/eid-viewer.h
/usr/include/eid-viewer/macros.h
/usr/include/eid-viewer/oslayer.h
/usr/include/eid-viewer/verify_cert.h
/usr/include/beid/rsaref220/pkcs11.h
/usr/include/beid/rsaref220/pkcs11f.h
/usr/include/beid/rsaref220/pkcs11t.h
/usr/include/beid/rsaref220/unix.h
%{_libdir}/pkgconfig/libbeidpkcs11.pc

%files -n eid-viewer -f eid-viewer.lang
%defattr(-,root,root,0755)
%{_bindir}/eid-viewer
%{_datadir}/applications/fedict-eid-viewer.desktop
%{_datadir}/eid-mw/
%{_datadir}/metainfo/
%exclude %{_datadir}/metainfo/*metainfo.xml
%{_datadir}/icons/hicolor/*/*/eid-viewer.png
%if ! 0%{?el6}
%{_datadir}/glib-2.0/schemas/
%endif

%changelog
