#
# spec file for package bouncycastle
#
# Copyright (c) 2024 SUSE LLC
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


%global ver_major 1
%global ver_minor 79
#%%global ver_micro 1
%global gittag r%{ver_major}rv%{ver_minor}%{?ver_micro:v%{ver_micro}}
%global archivever jdk18on-%{ver_major}.%{ver_minor}%{?ver_micro:0%{ver_micro}}
%global classname org.bouncycastle.jce.provider.BouncyCastleProvider
Name:           bouncycastle
Version:        %{ver_major}.%{ver_minor}%{?ver_micro:.%{ver_micro}}
Release:        0
Summary:        Bouncy Castle Cryptography APIs for Java
License:        Apache-2.0 AND MIT
Group:          Development/Libraries/Java
URL:            https://www.bouncycastle.org
Source0:        https://github.com/bcgit/bc-java/archive/%{gittag}.tar.gz
# POMs from Maven Central
Source1:        https://repo1.maven.org/maven2/org/%{name}/bcprov-jdk18on/%{version}/bcprov-jdk18on-%{version}.pom
Source2:        https://repo1.maven.org/maven2/org/%{name}/bcpkix-jdk18on/%{version}/bcpkix-jdk18on-%{version}.pom
Source3:        https://repo1.maven.org/maven2/org/%{name}/bcpg-jdk18on/%{version}/bcpg-jdk18on-%{version}.pom
Source4:        https://repo1.maven.org/maven2/org/%{name}/bcmail-jdk18on/%{version}/bcmail-jdk18on-%{version}.pom
Source5:        https://repo1.maven.org/maven2/org/%{name}/bctls-jdk18on/%{version}/bctls-jdk18on-%{version}.pom
Source6:        https://repo1.maven.org/maven2/org/%{name}/bcutil-jdk18on/%{version}/bcutil-jdk18on-%{version}.pom
Source7:        https://repo1.maven.org/maven2/org/%{name}/bcjmail-jdk18on/%{version}/bcjmail-jdk18on-%{version}.pom
# PATCH-FIX-OPENSUSE Fix javadoc build
Patch0:         bouncycastle-javadoc.patch
# PATCH-FIX-OPENSUSE Add OSGi manifests to the distributed jars
Patch1:         bouncycastle-osgi.patch
Patch2:         bouncycastle-notests.patch
BuildRequires:  ant
BuildRequires:  ant-junit
BuildRequires:  fdupes
BuildRequires:  glassfish-activation-api
BuildRequires:  jakarta-activation
BuildRequires:  jakarta-mail
BuildRequires:  javamail
BuildRequires:  javapackages-local >= 6
Requires(post): javapackages-tools
Requires(postun): javapackages-tools
Provides:       bcprov = %{version}-%{release}
BuildArch:      noarch

%description
The Bouncy Castle Crypto package is a Java implementation of cryptographic
algorithms. This jar contains JCE provider and lightweight API for the
Bouncy Castle Cryptography APIs for JDK 1.5 to JDK 1.8.

%package pkix
Summary:        Bouncy Castle PKIX, CMS, EAC, TSP, PKCS, OCSP, CMP, and CRMF APIs
License:        MIT
Group:          Development/Libraries/Java

%description pkix
The Bouncy Castle Java APIs for CMS, PKCS, EAC, TSP, CMP, CRMF, OCSP, and
certificate generation. This jar contains APIs for JDK 1.5 to JDK 1.8. The
APIs can be used in conjunction with a JCE/JCA provider such as the one
provided with the Bouncy Castle Cryptography APIs.

%package pg
Summary:        Bouncy Castle OpenPGP API
License:        Apache-2.0 AND MIT
Group:          Development/Libraries/Java

%description pg
The Bouncy Castle Java API for handling the OpenPGP protocol.The APIs can be
used in conjunction with a JCE/JCA provider such as the one provided with the
Bouncy Castle Cryptography APIs.

%package mail
Summary:        Bouncy Castle S/MIME API
License:        MIT
Group:          Development/Libraries/Java

%description mail
The Bouncy Castle Java S/MIME APIs for handling S/MIME protocols. The APIs can
be used in conjunction with a JCE/JCA provider such as the one provided with
the Bouncy Castle Cryptography APIs. The JavaMail API and the Java activation
framework will also be needed.

%package jmail
Summary:        Bouncy Castle Jakarta S/MIME API
License:        MIT
Group:          Development/Libraries/Java
Requires:       %{name} = %{version}

%description jmail
The Bouncy Castle Java S/MIME APIs for handling S/MIME protocols. This jar
contains S/MIME APIs for JDK 1.8 and up. The APIs can be used in conjunction
with a JCE/JCA provider such as the one provided with the Bouncy Castle
Cryptography APIs. The Jakarta Mail API and the Jakarta activation framework
will also be needed.

%package tls
Summary:        Bouncy Castle JSSE provider and TLS/DTLS API
License:        MIT
Group:          Development/Libraries/Java

%description tls
The Bouncy Castle Java APIs for TLS and DTLS, including a provider for the
JSSE.

%package util
Summary:        Bouncy Castle ASN.1 Extension and Utility APIs
License:        MIT
Group:          Development/Libraries/Java

%description util
The Bouncy Castle Java APIs for ASN.1 extension and utility APIs used to
support bcpkix and bctls.

%package javadoc
Summary:        Javadoc for %{name}
License:        MIT
Group:          Development/Libraries/Java

%description javadoc
API documentation for the Bouncy Castle Cryptography APIs.

%prep
%autosetup -p1 -n bc-java-%{gittag}

# Remove provided binaries
find . -type f -name "*.class" -exec rm -f {} \;
find . -type f -name "*.jar" -exec rm -f {} \;

%build
echo "package.version:\ %{version}" >> bc-build.properties
echo "bundle.version:\ %{version}.0" >> bc-build.properties
ant -f ant/jdk18+.xml \
  -Dbc.javac.source=8 -Dbc.javac.target=8 \
  -Djunit.jar.home=$(build-classpath junit) \
  -Dmail.jar.home=$(build-classpath javax.mail) \
  -Djmail.jar.home=$(build-classpath jakarta-mail) \
  -Dactivation.jar.home=$(build-classpath glassfish-activation-api) \
  -Djactivation.jar.home=$(build-classpath jakarta-activation) \
  -Drelease.debug=true \
  clean build-provider build

# Not shipping the "lcrypto" jar, so don't ship the javadoc for it
rm -rf build/artifacts/jdk1.8/javadoc/lcrypto

%install
install -dm 755 %{buildroot}%{_sysconfdir}/java/security/security.d
touch %{buildroot}%{_sysconfdir}/java/security/security.d/2000-%{classname}

install -dm 0755 %{buildroot}%{_javadir}
install -dm 0755 %{buildroot}%{_mavenpomdir}

for bc in bcprov bcpkix bcpg bcmail bctls bcutil bcjmail ; do
  install -pm 0644 build/artifacts/jdk1.8/jars/$bc-%{archivever}.jar %{buildroot}%{_javadir}/$bc.jar
  %{mvn_install_pom} %{_sourcedir}/$bc-jdk18on-%{version}.pom %{buildroot}%{_mavenpomdir}/$bc.pom
  %add_maven_depmap $bc.pom $bc.jar -a "org.bouncycastle:$bc-jdk18,org.bouncycastle:$bc-jdk16,org.bouncycastle:$bc-jdk15on,org.bouncycastle:$bc-jdk15,org.bouncycastle:$bc-jdk15to18" -f $bc
done

install -dm 0755 %{buildroot}%{_javadocdir}/%{name}
cp -r build/artifacts/jdk1.8/javadoc/* %{buildroot}%{_javadocdir}/%{name}/
%fdupes -s %{buildroot}%{_javadocdir}

%post
{
  # Rebuild the list of security providers in classpath.security
  suffix=security/classpath.security
  secfiles="%{_prefix}/lib/$suffix %{_libdir}/$suffix"

  for secfile in $secfiles
  do
    # check if this classpath.security file exists
    [ -f "$secfile" ] || continue

    sed -i '/^security\.provider\./d' "$secfile"

    count=0
    for provider in $(ls %{_sysconfdir}/java/security/security.d)
    do
      count=$((count + 1))
      echo "security.provider.${count}=${provider#*-}" >> "$secfile"
    done
  done
} || :

%postun
if [ $1 -eq 0 ] ; then

  {
    # Rebuild the list of security providers in classpath.security
    suffix=security/classpath.security
    secfiles="%{_prefix}/lib/$suffix %{_libdir}/$suffix"

    for secfile in $secfiles
    do
      # check if this classpath.security file exists
      [ -f "$secfile" ] || continue

      sed -i '/^security\.provider\./d' "$secfile"

      count=0
      for provider in $(ls %{_sysconfdir}/java/security/security.d)
      do
        count=$((count + 1))
        echo "security.provider.${count}=${provider#*-}" >> "$secfile"
      done
    done
  } || :

fi

%files -f .mfiles-bcprov
%license build/artifacts/jdk1.8/bcprov-jdk18on-*/LICENSE.html
%doc docs/ *.html
%config(noreplace) %{_sysconfdir}/java/security/security.d/2000-%{classname}

%files pkix -f .mfiles-bcpkix
%license build/artifacts/jdk1.8/bcpkix-jdk18on-*/LICENSE.html

%files pg -f .mfiles-bcpg
%license build/artifacts/jdk1.8/bcpg-jdk18on-*/LICENSE.html

%files mail -f .mfiles-bcmail
%license build/artifacts/jdk1.8/bcmail-jdk18on-*/LICENSE.html

%files jmail -f .mfiles-bcjmail
%license build/artifacts/jdk1.8/bcjmail-jdk18on-*/LICENSE.html

%files tls -f .mfiles-bctls
%license build/artifacts/jdk1.8/bctls-jdk18on-*/LICENSE.html

%files util -f .mfiles-bcutil
%license build/artifacts/jdk1.8/bcutil-jdk18on-*/LICENSE.html

%files javadoc
%{_javadocdir}/%{name}
%license LICENSE.html

%changelog
