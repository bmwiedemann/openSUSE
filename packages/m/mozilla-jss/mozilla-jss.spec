#
# spec file for package mozilla-jss
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


Name:           mozilla-jss
Summary:        Java Security Services (JSS)
License:        GPL-2.0-only OR MPL-1.1 OR LGPL-2.1-only
Group:          Development/Libraries/Java
URL:            http://www.dogtagpki.org/wiki/JSS
Version:        5.0.0
Release:        0
Source0:        https://github.com/dogtagpki/jss/archive/v%{version}/jss-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  git
BuildRequires:  make
BuildRequires:  unzip
BuildRequires:  zip

BuildRequires:  apache-commons-lang3
BuildRequires:  gcc-c++
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
Requires:       java-headless
Requires:       jpackage-utils
Requires:       mozilla-nss >= 3.44
Requires:       slf4j
Requires:       slf4j-jdk14

Conflicts:      idm-console-framework < 1.2
Conflicts:      ldapjdk < 4.20
Conflicts:      pki-base < 10.6.5
Conflicts:      tomcatjss < 7.3.4

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
export JAVA_HOME=%{java_home}

# Enable compiler optimizations
export BUILD_OPT=1

# Generate symbolic info for debuggers
CFLAGS="-g $RPM_OPT_FLAGS"
export CFLAGS

# Check if we're in FIPS mode
modutil -dbdir /etc/pki/nssdb -chkfips true | grep -q enabled && export FIPS_ENABLED=1

./build.sh \
    %{?_verbose:-v} \
    --work-dir=%{_vpath_builddir} \
    --java-lib-dir=%{_jnidir} \
    --jss-lib-dir=%{_libdir}/jss \
    --version=%{version} \
    %{!?with_javadoc:--without-javadoc} \
    %{!?with_test:--without-test} \
    dist

%install

./build.sh \
    %{?_verbose:-v} \
    --work-dir=%{_vpath_builddir} \
    --install-dir=%{buildroot} \
    install

%files

%defattr(-,root,root,-)
%doc jss.html
%license MPL-1.1.txt gpl.txt lgpl.txt
%{_libdir}/jss
%{_jnidir}/*

%if %{with javadoc}

%files javadoc

%defattr(-,root,root,-)
%{_javadocdir}/%{name}/
%endif

%changelog
