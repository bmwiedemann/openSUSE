#
# spec file for package mozilla-jss
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


Name:           mozilla-jss
Summary:        Java Security Services (JSS)
License:        MPL-1.1 OR GPL-2.0-only OR LGPL-2.1-only
Group:          Development/Libraries/Java
URL:            http://www.dogtagpki.org/wiki/JSS
Version:        4.6.3
Release:        0
Source0:        https://github.com/dogtagpki/jss/archive/v%{version}/jss-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  git
BuildRequires:  make
BuildRequires:  unzip
BuildRequires:  zip

BuildRequires:  apache-commons-lang
BuildRequires:  gcc-c++
BuildRequires:  glassfish-jaxb-api
BuildRequires:  java-devel
BuildRequires:  jpackage-utils
BuildRequires:  libfreebl3-hmac
BuildRequires:  libsoftokn3-hmac
BuildRequires:  mozilla-nspr-devel >= 4.13.1
BuildRequires:  mozilla-nss-devel >= 3.44
BuildRequires:  mozilla-nss-sysinit >= 3.44
BuildRequires:  mozilla-nss-tools >= 3.44
BuildRequires:  slf4j
BuildRequires:  slf4j-jdk14

BuildRequires:  junit

Requires:       apache-commons-lang
Requires:       glassfish-jaxb-api
Requires:       java-headless
Requires:       jpackage-utils
Requires:       mozilla-nss >= 3.44
Requires:       slf4j
Requires:       slf4j-jdk14

Conflicts:      ldapjdk < 4.20
Conflicts:      idm-console-framework < 1.2
Conflicts:      tomcatjss < 7.3.4
Conflicts:      pki-base < 10.6.5

%description
Java Security Services (JSS) is a java native interface which provides a bridge
for java-based applications to use native Network Security Services (NSS).
This only works with gcj. Other JREs require that JCE providers be signed.

%package javadoc

Summary:        Java Security Services (JSS) Javadocs
Group:          Development/Libraries/Java
Requires:       mozilla-jss = %{version}

%description javadoc
This package contains the API documentation for JSS.

%prep
%autosetup -n jss-%{version}

%build
%set_build_flags

[ -z "$JAVA_HOME" ] && export JAVA_HOME=%{_jvmdir}/java

# Enable compiler optimizations
export BUILD_OPT=1

# Generate symbolic info for debuggers
CFLAGS="-g $RPM_OPT_FLAGS"
export CFLAGS

# Check if we're in FIPS mode
modutil -dbdir /etc/pki/nssdb -chkfips true | grep -q enabled && export FIPS_ENABLED=1

%cmake \
    -DJAVA_HOME=%{java_home} \
    -DJAVA_LIB_INSTALL_DIR=%{_jnidir} \
    ..

%{__make} all
%{__make} javadoc
ctest --output-on-failure

%install
install -d -m 0755 %{buildroot}%{_jnidir}
install -m 644 build/jss4.jar %{buildroot}%{_jnidir}/jss4.jar

install -d -m 0755 %{buildroot}%{_libdir}/jss
install -m 0755 build/libjss4.so %{buildroot}%{_libdir}/jss/
pushd  %{buildroot}%{_libdir}/jss
    ln -fs %{_jnidir}/jss4.jar jss4.jar
popd

install -d -m 0755 %{buildroot}%{_javadocdir}/jss-%{version}
cp -rp build/docs/* %{buildroot}%{_javadocdir}/jss-%{version}
cp -p jss.html %{buildroot}%{_javadocdir}/jss-%{version}
cp -p *.txt %{buildroot}%{_javadocdir}/jss-%{version}

%files
%doc jss.html MPL-1.1.txt gpl.txt lgpl.txt
%dir %{_libdir}/jss/
%{_libdir}/jss/*
%{_jnidir}/*

%files javadoc
%{_javadocdir}/jss-%{version}/

%changelog
