#
# spec file for package bouncycastle
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


%global ver  1.60
%global shortver 160
%global gittag r1v60
%global archivever jdk15on-%{shortver}
%global classname org.bouncycastle.jce.provider.BouncyCastleProvider
Name:           bouncycastle
Version:        %{ver}
Release:        0
Summary:        Bouncy Castle Cryptography APIs for Java
License:        MIT AND Apache-2.0
Group:          Development/Libraries/Java
URL:            http://www.bouncycastle.org
Source0:        https://github.com/bcgit/bc-java/archive/%{gittag}.tar.gz
# POMs from Maven Central
Source1:        http://repo1.maven.org/maven2/org/bouncycastle/bcprov-jdk15on/%{version}/bcprov-jdk15on-%{version}.pom
Source2:        http://repo1.maven.org/maven2/org/bouncycastle/bcpkix-jdk15on/%{version}/bcpkix-jdk15on-%{version}.pom
Source3:        http://repo1.maven.org/maven2/org/bouncycastle/bcpg-jdk15on/%{version}/bcpg-jdk15on-%{version}.pom
Source4:        http://repo1.maven.org/maven2/org/bouncycastle/bcmail-jdk15on/%{version}/bcmail-jdk15on-%{version}.pom
Source5:        http://repo1.maven.org/maven2/org/bouncycastle/bctls-jdk15on/%{version}/bctls-jdk15on-%{version}.pom
Patch0:         bouncycastle-javadoc.patch
BuildRequires:  ant
BuildRequires:  ant-junit
BuildRequires:  fdupes
BuildRequires:  javamail
BuildRequires:  javapackages-local
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
Requires:       %{name} = %{version}

%description pkix
The Bouncy Castle Java APIs for CMS, PKCS, EAC, TSP, CMP, CRMF, OCSP, and
certificate generation. This jar contains APIs for JDK 1.5 to JDK 1.8. The
APIs can be used in conjunction with a JCE/JCA provider such as the one
provided with the Bouncy Castle Cryptography APIs.

%package pg
Summary:        Bouncy Castle OpenPGP API
License:        MIT AND Apache-2.0
Group:          Development/Libraries/Java
Requires:       %{name} = %{version}

%description pg
The Bouncy Castle Java API for handling the OpenPGP protocol. This jar
contains the OpenPGP API for JDK 1.5 to JDK 1.8. The APIs can be used in
conjunction with a JCE/JCA provider such as the one provided with the
Bouncy Castle Cryptography APIs.

%package mail
Summary:        Bouncy Castle S/MIME API
License:        MIT
Group:          Development/Libraries/Java
Requires:       %{name} = %{version}
Requires:       %{name}-pkix = %{version}

%description mail
The Bouncy Castle Java S/MIME APIs for handling S/MIME protocols. This jar
contains S/MIME APIs for JDK 1.5 to JDK 1.8. The APIs can be used in
conjunction with a JCE/JCA provider such as the one provided with the Bouncy
Castle Cryptography APIs. The JavaMail API and the Java activation framework
will also be needed.

%package tls
Summary:        Bouncy Castle JSSE provider and TLS/DTLS API
License:        MIT
Group:          Development/Libraries/Java
Requires:       %{name} = %{version}

%description tls
The Bouncy Castle Java APIs for TLS and DTLS, including a provider for the
JSSE.

%package javadoc
Summary:        Javadoc for %{name}
License:        MIT
Group:          Development/Libraries/Java

%description javadoc
API documentation for the Bouncy Castle Cryptography APIs.

%prep
%setup -q -n bc-java-%{gittag}
%patch0 -p1

# Remove provided binaries
find . -type f -name "*.class" -exec rm -f {} \;
find . -type f -name "*.jar" -exec rm -f {} \;

%build
ant -f ant/jdk15+.xml \
  -Dbc.javac.source=6 -Dbc.javac.target=6 \
  -Djunit.jar.home=$(build-classpath junit) \
  -Dmail.jar.home=$(build-classpath javax.mail) \
  -Dactivation.jar.home= \
  -Drelease.debug=true \
  clean build-provider build

# Not shipping the "lcrypto" jar, so don't ship the javadoc for it
rm -rf build/artifacts/jdk1.5/javadoc/lcrypto

%install
install -dm 755 %{buildroot}%{_sysconfdir}/java/security/security.d
touch %{buildroot}%{_sysconfdir}/java/security/security.d/2000-%{classname}

install -dm 0755 %{buildroot}%{_javadir}
install -dm 0755 %{buildroot}%{_mavenpomdir}
for bc in bcprov bcpkix bcpg bcmail bctls ; do
  install -pm 0644 build/artifacts/jdk1.5/jars/$bc-%{archivever}.jar %{buildroot}%{_javadir}/$bc.jar
  install -pm 0644 %{_sourcedir}/$bc-jdk15on-%{version}.pom %{buildroot}%{_mavenpomdir}/$bc.pom
  %add_maven_depmap $bc.pom $bc.jar -a "org.bouncycastle:$bc-jdk16,org.bouncycastle:$bc-jdk15" -f $bc
done

install -dm 0755 %{buildroot}%{_javadocdir}/%{name}
cp -r build/artifacts/jdk1.5/javadoc/* %{buildroot}%{_javadocdir}/%{name}/
%fdupes -s %{buildroot}%{_javadocdir}

%post
{
  # Rebuild the list of security providers in classpath.security
  suffix=security/classpath.security
  secfiles="%{_libexecdir}/$suffix %{_libdir}/$suffix"

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
    secfiles="%{_libexecdir}/$suffix %{_libdir}/$suffix"

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
%license build/artifacts/jdk1.5/bcprov-jdk15on-*/LICENSE.html
%doc docs/ core/docs/ *.html
%config(noreplace) %{_sysconfdir}/java/security/security.d/2000-%{classname}

%files pkix -f .mfiles-bcpkix
%license build/artifacts/jdk1.5/bcpkix-jdk15on-*/LICENSE.html

%files pg -f .mfiles-bcpg
%license build/artifacts/jdk1.5/bcpg-jdk15on-*/LICENSE.html

%files mail -f .mfiles-bcmail
%license build/artifacts/jdk1.5/bcmail-jdk15on-*/LICENSE.html

%files tls -f .mfiles-bctls
%license build/artifacts/jdk1.5/bctls-jdk15on-*/LICENSE.html

%files javadoc
%{_javadocdir}/%{name}
%license LICENSE.html

%changelog
