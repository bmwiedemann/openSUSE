#
# spec file for package p11-kit
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


%define pkidir_cfg       %{_sysconfdir}/pki
%define pkidir_static    %{_datadir}/pki
%define trustdir_cfg     %{pkidir_cfg}/trust
%define trustdir_static  %{pkidir_static}/trust
Name:           p11-kit
Version:        0.23.20
Release:        0
Summary:        Library to work with PKCS#11 modules
License:        BSD-3-Clause
Group:          Development/Libraries/C and C++
URL:            https://p11-glue.freedesktop.org/p11-kit.html
Source0:        https://github.com/p11-glue/p11-kit/releases/download/%{version}/p11-kit-%{version}.tar.xz
Source1:        https://github.com/p11-glue/p11-kit/releases/download/%{version}/p11-kit-%{version}.tar.xz.sig
Source98:       p11-kit.keyring
Source99:       baselibs.conf
BuildRequires:  gtk-doc
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libffi) >= 3.0.0
BuildRequires:  pkgconfig(libtasn1) >= 2.3

%description
p11-kit provides a way to load and enumerate PKCS#11 modules, as well
as a standard configuration setup for installing PKCS#11 modules in
such a way that they're discoverable.

%package -n libp11-kit0
Summary:        Library to work with PKCS#11 modules
Group:          System/Libraries

%description -n libp11-kit0
p11-kit provides a way to load and enumerate PKCS#11 modules, as well
as a standard configuration setup for installing PKCS#11 modules in
such a way that they're discoverable.

%package tools
Summary:        Library to work with PKCS#11 modules -- Tools
Group:          Development/Libraries/C and C++

%description tools
p11-kit provides a way to load and enumerate PKCS#11 modules, as well
as a standard configuration setup for installing PKCS#11 modules in
such a way that they're discoverable.

%package devel
Summary:        Library to work with PKCS#11 modules -- Development Files
Group:          Development/Libraries/C and C++
Requires:       libp11-kit0 = %{version}

%description devel
p11-kit provides a way to load and enumerate PKCS#11 modules, as well
as a standard configuration setup for installing PKCS#11 modules in
such a way that they're discoverable.

%package nss-trust
Summary:        Adaptor to make NSS read the p11-kit trust store
Group:          Productivity/Networking/Security
Requires:       p11-kit = %{version}
Conflicts:      mozilla-nss-certs
%if "%{_lib}" == "lib64"
Provides:       libnssckbi.so()(64bit)
%else
Provides:       libnssckbi.so
%endif

%description nss-trust
Adaptor library to make NSS read the p11-kit trust store. It has
to be installed intead of mozilla-nss-certs.

%package server
Summary:        Server and client commands for p11-kit
Group:          Development/Libraries/C and C++
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description server
Command line tools that enable to export PKCS#11 modules through a
Unix domain socket.  Note that this feature is still experimental.

%prep
%autosetup

%build
%configure \
  --with-trust-paths=%{trustdir_cfg}:%{trustdir_static} \
  --enable-doc
%make_build

%install
%make_install
#
install -d m 755 %{buildroot}%{trustdir_cfg}/{anchors,blacklist}
install -d m 755 %{buildroot}%{trustdir_static}/{anchors,blacklist}
# Create pkcs11 config directory
test ! -e %{buildroot}%{_sysconfdir}/pkcs11/modules
install -d %{buildroot}%{_sysconfdir}/pkcs11/modules
# Remove sample config away to doc folder. Having the sample there would conflict
# with future versions of the library on file level. As replacement, we package
# the file as documentation file.
rm %{buildroot}%{_sysconfdir}/pkcs11/pkcs11.conf.example
find %{buildroot} -type f -name "*.la" -delete -print
#
install -d -m 755 %{buildroot}%{_rpmmacrodir}
cat <<'FIN' >%{buildroot}%{_rpmmacrodir}/macros.%{name}
# Macros from p11-kit package
%%pkidir_cfg             %{pkidir_cfg}
%%pkidir_static          %{pkidir_static}
%%trustdir_cfg           %{trustdir_cfg}
%%trustdir_static        %{trustdir_static}
FIN
#
# nss compat lib
ln -s %{_libdir}/pkcs11/p11-kit-trust.so %{buildroot}%{_libdir}/libnssckbi.so
#
# call update-ca-certificates when trust changes
rm %{buildroot}%{_libexecdir}/%{name}/trust-extract-compat
ln -s ../../sbin/update-ca-certificates %{buildroot}%{_libexecdir}/%{name}/p11-kit-extract-trust
export NO_BRP_STALE_LINK_ERROR=yes # *grr*

%check
make %{?_smp_mflags} check

%post -n libp11-kit0 -p /sbin/ldconfig

%postun -n libp11-kit0 -p /sbin/ldconfig

%files
%defattr(-,root,root)
%dir %{_libdir}/pkcs11
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/modules
%dir %{pkidir_cfg}
%dir %{trustdir_cfg}
%dir %{trustdir_cfg}/anchors
%dir %{trustdir_cfg}/blacklist
%dir %{pkidir_static}
%dir %{trustdir_static}
%dir %{trustdir_static}/anchors
%dir %{trustdir_static}/blacklist
%{_datadir}/%{name}/modules/p11-kit-trust.module
%{_libdir}/pkcs11/p11-kit-trust.so
%dir %{_libexecdir}/%{name}
%{_libexecdir}/%{name}/p11-kit-remote
%{_libexecdir}/%{name}/p11-kit-extract-trust

%files -n libp11-kit0
%defattr(-,root,root)
%license COPYING
# Package the example conf file as documentation. Like this we're sure that we will
# not introduce conflicts with this version of the library and future ones.
%doc p11-kit/pkcs11.conf.example
%doc AUTHORS ChangeLog NEWS README
%dir %{_sysconfdir}/pkcs11
%dir %{_sysconfdir}/pkcs11/modules/
%{_libdir}/libp11-kit.so.*
%{_libdir}/p11-kit-proxy.so

%files tools
%defattr(-,root,root)
%{_bindir}/p11-kit
%{_bindir}/trust
%{_mandir}/man1/trust.1.gz
%{_mandir}/man5/pkcs11.conf.5.gz
%{_mandir}/man8/p11-kit.8.gz

%files devel
%defattr(-,root,root)
%{_rpmmacrodir}/macros.%{name}
%{_includedir}/p11-kit-1/
%{_libdir}/libp11-kit.so
%{_libdir}/pkgconfig/p11-kit-1.pc
%doc %dir %{_datadir}/gtk-doc
%doc %dir %{_datadir}/gtk-doc/html
%doc %{_datadir}/gtk-doc/html/p11-kit/

%files nss-trust
%defattr(-,root,root)
%{_libdir}/libnssckbi.so

%files server
%{_libdir}/pkcs11/p11-kit-client.so
%{_libexecdir}/p11-kit/p11-kit-server

%changelog
