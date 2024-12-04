#
# spec file for package mozldap
#
# Copyright (c) 2024 SUSE LLC
# Copyright (c) 2009-2011 Wolfgang Rosenauer
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


%define libsuffix 60
%define nspr_ver %(rpm -q --queryformat '%%{VERSION}' mozilla-nspr)
%define nss_ver  %(rpm -q --queryformat '%%{VERSION}' mozilla-nss)
%define svrcore_ver %(rpm -q --queryformat '%%{VERSION}' svrcore-devel)
Name:           mozldap
Version:        6.0.7
Release:        0
Summary:        Mozilla LDAP C SDK
License:        MPL-1.1 OR GPL-2.0-or-later OR LGPL-2.1-or-later
Group:          System/Libraries
URL:            https://wiki.mozilla.org/LDAP_C_SDK
Source0:        ftp://ftp.mozilla.org/pub/mozilla.org/directory/c-sdk/releases/v%{version}/src/%{name}-%{version}.tar.gz
Source200:      baselibs.conf
# PATCH-FIX-UPSTREAM mozldap-6.0.7-support-tls1.1-and-later.patch - disable SSL3, support TLS1.1 and later
Patch0:         mozldap-6.0.7-support-tls1.1-and-later.patch
# PATCH-FIX-UPSTREAM mozldap-6.0.7-fix_typo.patch - fix a typo in libssldap/sslerrstrs.h
Patch1:         mozldap-6.0.7-fix_typo.patch
# PATCH-FIX-UPSTREAM mozldap-6.0.7-replace_mktemp.patch - use mkstemp instead of mktemp
Patch2:         mozldap-6.0.7-replace_mktemp.patch
# PATCH-FIX-UPSTREAM mozldap-perl-5.24.patch dimstar@opensuse.org -- Fix build tools for usage with perl 5.24
Patch3:         mozldap-perl-5.24.patch
BuildRequires:  cyrus-sasl-devel
BuildRequires:  gcc-c++
BuildRequires:  svrcore-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
# 389-ds does not support i686 - and svrcore-devel comes from 389-ds
ExcludeArch:    %ix86

%description
The Mozilla LDAP C SDK is a set of libraries that allow applications to communicate with LDAP directory servers.
These libraries are derived from the University of Michigan and Netscape LDAP libraries. They use Mozilla NSPR and NSS for crypto.

%package libs
Summary:        Mozilla LDAP C SDK
Group:          System/Libraries
Obsoletes:      %{name} < %{version}-%{release}
Provides:       %{name} = %{version}-%{release}

%description libs
The Mozilla LDAP C SDK is a set of libraries that allow applications to communicate with LDAP directory servers.
These libraries are derived from the University of Michigan and Netscape LDAP libraries. They use Mozilla NSPR and NSS for crypto.

%package tools
Summary:        Tools for the Mozilla LDAP C SDK
Group:          System/Management
Requires:       %{name}-libs = %{version}-%{release}

%description tools
The mozldap-tools package provides the ldapsearch, ldapmodify, and ldapdelete tools that use the Mozilla LDAP C SDK libraries.

%package devel
Summary:        Development libraries and examples for Mozilla LDAP C SDK
Group:          Development/Libraries/Other
Requires:       %{name}-libs = %{version}-%{release}
Requires:       mozilla-nspr-devel
Requires:       mozilla-nss-devel
Requires:       pkgconfig

%description devel
Header and Library files for doing development with the Mozilla LDAP C SDK.

%prep
%autosetup -p1
# quick fix for building in C99 standard; explicitly define the return type
sed -i 's\^main(){return(0);}\int main(){return(0);}\g' c-sdk/configure

%build
cd c-sdk
%configure \
%ifarch x86_64 ppc64 ia64 s390x
    --enable-64bit \
%endif
    --with-sasl \
    --enable-clu \
    --with-system-svrcore \
    --enable-optimize \
    --disable-debug
# Enable compiler optimizations and disable debugging code
BUILD_OPT=1
export BUILD_OPT
# Generate symbolic info for debuggers
XCFLAGS="%{optflags}"
export XCFLAGS
PKG_CONFIG_ALLOW_SYSTEM_LIBS=1
PKG_CONFIG_ALLOW_SYSTEM_CFLAGS=1
export PKG_CONFIG_ALLOW_SYSTEM_LIBS
export PKG_CONFIG_ALLOW_SYSTEM_CFLAGS
make %{?_smp_mflags} \
%ifarch x86_64 ppc64 ia64 s390x
    USE_64=1
%endif

%install
# Set up our package file
mkdir -p %{buildroot}%{_libdir}/pkgconfig
cat c-sdk/mozldap.pc.in \
    | sed -e "s,%%libdir%%,%{_libdir},g" \
          -e "s,%%prefix%%,%{_prefix},g" \
          -e "s,%%major%%,%{major},g" \
          -e "s,%%minor%%,%{minor},g" \
          -e "s,%%submin%%,%{submin},g" \
          -e "s,%%libsuffix%%,%{libsuffix},g" \
          -e "s,%%bindir%%,%{_libexecdir}/%{name},g" \
          -e "s,%%exec_prefix%%,%{_prefix},g" \
          -e "s,%%includedir%%,%{_includedir}/%{name},g" \
          -e "s,%%NSPR_VERSION%%,%{nspr_ver},g" \
          -e "s,%%NSS_VERSION%%,%{nss_ver},g" \
          -e "s,%%SVRCORE_VERSION%%,%{svrcore_ver},g" \
          -e "s,%%MOZLDAP_VERSION%%,%{version},g" \
    > %{buildroot}%{_libdir}/pkgconfig/%{name}.pc
# There is no make install target so we'll do it ourselves.
mkdir -p %{buildroot}%{_includedir}/%{name}
mkdir -p %{buildroot}%{_libdir}/%{name}
echo $(pwd)
# Copy the binary libraries we want
for file in libssldap%{libsuffix}.so libprldap%{libsuffix}.so libldap%{libsuffix}.so libldif%{libsuffix}.so
do
  install -m 755 ../dist/lib/$file %{buildroot}%{_libdir}
done
# Copy the binaries we want
mkdir -p %{buildroot}%{_libexecdir}/%{name}
for file in ldapsearch ldapmodify ldapdelete ldapcmp ldapcompare ldappasswd
do
  install -m 755 ../dist/bin/$file %{buildroot}%{_libexecdir}/%{name}
done
# Copy the include files
for file in ../dist/public/ldap/*.h
do
  install -p -m 644 $file %{buildroot}%{_includedir}/%{name}
done
# Copy the developer files
mkdir -p %{buildroot}%{_datadir}/%{name}
cp -r c-sdk/ldap/examples %{buildroot}%{_datadir}/%{name}
mkdir -p %{buildroot}%{_datadir}/%{name}/etc
install -m 644 c-sdk/ldap/examples/xmplflt.conf %{buildroot}%{_datadir}/%{name}/etc
install -m 644 c-sdk/ldap/libraries/libldap/ldaptemplates.conf %{buildroot}%{_datadir}/%{name}/etc
install -m 644 c-sdk/ldap/libraries/libldap/ldapfilter.conf %{buildroot}%{_datadir}/%{name}/etc
install -m 644 c-sdk/ldap/libraries/libldap/ldapsearchprefs.conf %{buildroot}%{_datadir}/%{name}/etc

%files libs
%defattr(-,root,root,-)
%{_libdir}/libssldap*.so
%{_libdir}/libprldap*.so
%{_libdir}/libldap*.so
%{_libdir}/libldif*.so

%files tools
%defattr(-,root,root,-)
%dir %{_libexecdir}/%{name}
%{_libexecdir}/%{name}/ldapsearch
%{_libexecdir}/%{name}/ldapmodify
%{_libexecdir}/%{name}/ldapdelete
%{_libexecdir}/%{name}/ldapcmp
%{_libexecdir}/%{name}/ldapcompare
%{_libexecdir}/%{name}/ldappasswd

%files devel
%defattr(-,root,root,-)
%{_libdir}/pkgconfig/%{name}.pc
%{_includedir}/%{name}
%{_datadir}/%{name}

%changelog
