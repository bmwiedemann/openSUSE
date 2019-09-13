#
# spec file for package mozilla-jss
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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
Version:        4.5.0
Release:        0
Summary:        Network Security Services for Java (JSS)
License:        MPL-1.1 OR GPL-2.0-only OR LGPL-2.1-only
Group:          Development/Libraries/Java
URL:            https://developer.mozilla.org/en-US/docs/Mozilla/Projects/NSS/JSS
Source0:        jss-%{version}.tar.gz
Source1:        MPL-1.1.txt
Source2:        GPL-2.0.txt
Source3:        LGPL-2.1.txt
Source100:      mozilla-jss-rpmlintrc
Patch0:         jss-4.5.0-slf4j.patch
Patch1:         jss-4.5.0-deprecation-warnings.patch
Patch2:         jss-4.5.0-pkcs11-constants.patch
Patch3:         jss-4.5.0-nojavah.patch
Patch4:         jss-4.5.0-sourcetarget.patch
BuildRequires:  apache-commons-codec
BuildRequires:  apache-commons-lang
BuildRequires:  fdupes
BuildRequires:  java-devel >= 1.8
BuildRequires:  libopenssl-1_1-devel
BuildRequires:  mozilla-nspr-devel >= 4.13.1
BuildRequires:  mozilla-nss-devel >= 3.28
BuildRequires:  pkgconfig
BuildRequires:  slf4j
Requires:       java
Requires:       mozilla-nss >= 3.28
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Java Security Services (JSS) is a java native interface which provides a bridge
for java-based applications to use native Network Security Services (NSS).
This only works with gcj. Other JREs require that JCE providers be signed.

%package javadoc
Summary:        Java Security Services (JSS) Javadocs
Group:          Development/Libraries/Java
Requires:       mozilla-jss = %{version}-%{release}

%description javadoc
This package contains the API documentation for JSS.

%prep
%setup -q -n jss-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
mkdir jss
mv build_java.pl  config  coreconf  jss.html  lib  Makefile  manifest.mn  org  pkg  README.md  rules.mk  samples \
  jss

%build
[ -z "$JAVA_HOME" ] && export JAVA_HOME=%{_jvmdir}/java
# Enable compiler optimizations and disable debugging code
export BUILD_OPT=1
# Generate symbolic info for debuggers
export XCFLAGS="-g %{optflags}"

export PKG_CONFIG_ALLOW_SYSTEM_LIBS=1
export PKG_CONFIG_ALLOW_SYSTEM_CFLAGS=1
export USE_INSTALLED_NSPR=1
export USE_INSTALLED_NSS=1
export NSPR_INCLUDE_DIR=`%{_bindir}/pkg-config --cflags-only-I nspr | sed 's/-I//'`
export NSPR_LIB_DIR=`%{_bindir}/pkg-config --libs-only-L nspr | sed 's/-L//'`
export NSS_INCLUDE_DIR=`%{_bindir}/pkg-config --cflags-only-I nss | sed 's/-I//'`
export NSS_LIB_DIR=`%{_bindir}/pkg-config --libs-only-L nss | sed 's/-L//'`

%ifarch x86_64 ppc64 ppc64le ia64 s390x sparc64 aarch64 riscv64
export USE_64=1
%endif

# Fix for Kernel >= 3 (autoget kernel version)
if [[ `uname -r | cut -f1 -d.` > 2 ]]; then
%global majorrel `uname -r | cut -f1 -d.`
%global minorrel `uname -r | cut -f2 -d.`
cp -p jss/coreconf/Linux.mk jss/coreconf/Linux%{majorrel}.%{minorrel}.mk
sed -i -e 's;LINUX2_1;LINUX%{majorrel}_%{minorrel};' jss/coreconf/Linux%{majorrel}.%{minorrel}.mk
fi

# For some reason jss can't find nss on SUSE unless we do the following
export C_INCLUDE_PATH="%{_includedir}/nss3"
# The Makefile is not thread-safe
make -C jss/coreconf
make -C jss
make -C jss javadoc

%install
# Supress SUSE bytecode version error check
export NO_BRP_CHECK_BYTECODE_VERSION=true
# Copy the license files here so we can include them in %%doc
cp -p %{SOURCE1} .
cp -p %{SOURCE2} .
cp -p %{SOURCE3} .

# There is no install target so we'll do it by hand
# jars
install -d -m 0755 %{buildroot}%{_jnidir}
install -m 644 dist/xpclass.jar %{buildroot}%{_jnidir}/jss4-%{version}.jar
pushd %{buildroot}%{_jnidir}
    ln -fs jss4-%{version}.jar jss4.jar
popd

# We have to use the name libjss4.so because this is dynamically
# loaded by the jar file.
install -m 0755 dist/Linux*.OBJ/lib/libjss4.so %{buildroot}%{_libdir}/

# FIXME - sign jss4.jar. In order to use JSS as a JCE provider it needs to be
# signed with a Sun-issued certificate. Since we would need to make this
# certificate and private key public to provide reproducability in the rpm
# building we have to ship an unsigned jar.
#
# Instructions for getting a signing cert can be found here:
# http://java.sun.com/javase/6/docs/technotes/guides/security/crypto/HowToImplAProvider.html#Step61
#
# This signing is not required by every JVM. gcj ignores the signature and does
# not require one. The Sun and IBM JVMs both check and enforce the signature.
# Behavior of other JVMs is not known but they probably enforce the signature
# as well.

# javadoc
install -d -m 0755 %{buildroot}%{_javadocdir}/%{name}-%{version}
cp -rp dist/jssdoc/* %{buildroot}%{_javadocdir}/%{name}-%{version}
rm %{buildroot}%{_javadocdir}/%{name}-%{version}/index.html.bak
%fdupes -s %{buildroot}%{_javadocdir}/%{name}-%{version}

# No ldconfig is required since this library is loaded by Java itself.
%files
%defattr(-,root,root,-)
%doc jss/jss.html MPL-1.1.txt GPL-2.0.txt LGPL-2.1.txt
%dir %{_jnidir}
%{_jnidir}/*
%{_libdir}/lib*.so

%files javadoc
%defattr(-,root,root,-)
%dir %{_javadocdir}
%dir %{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}-%{version}/*

%changelog
