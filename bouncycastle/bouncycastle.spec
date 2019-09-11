#
# spec file for package bouncycastle
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%define ver  1.60
%define shortver 160
%define archivever jdk15on-%{shortver}
%define classname org.bouncycastle.jce.provider.BouncyCastleProvider
Name:           bouncycastle
Version:        %{ver}
Release:        0
Summary:        Bouncy Castle Crypto Package for Java
License:        MIT
Group:          Development/Libraries/Java
Url:            http://www.bouncycastle.org/
Source0:        http://www.bouncycastle.org/download/bcprov-%{archivever}.tar.gz
Source1:        http://repo1.maven.org/maven2/org/bouncycastle/bcprov-jdk15on/%{ver}/bcprov-jdk15on-%{ver}.pom
BuildRequires:  java-devel >= 1.8
BuildRequires:  javapackages-local
BuildRequires:  javapackages-tools
BuildRequires:  junit
#FIXME: this is needed for initialize of NSS crypto backend, will be required (not required(post) by openjdk)
BuildRequires:  mozilla-nss
BuildRequires:  unzip
Requires:       java
Provides:       bcprov = %{version}-%{release}
BuildArch:      noarch

%description
The Bouncy Castle Crypto package is a Java implementation of cryptographic
algorithms. The package is organised so that it contains a light-weight API
suitable for use in any environment (including the newly released J2ME) with
the additional infrastructure to conform the algorithms to the JCE framework.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Libraries/Java
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch

%description javadoc
API documentation for the %{name} package.

%prep
%setup -q -n bcprov-%{archivever}

# Remove provided binaries
find . -type f -name "*.class" -exec rm -f {} \;
find . -type f -name "*.jar" -exec rm -f {} \;

mkdir src
unzip -qq src.zip -d src/

%build
pushd src
  export CLASSPATH=$(build-classpath junit)
  %javac -g -source 8 -target 8 -encoding UTF-8 $(find . -type f -name "*.java")
  jarfile="../bcprov-%{version}.jar"
  # Exclude all */test/* files except org.bouncycastle.util.test, cf. upstream
  files="$(find . -type f \( -name '*.class' -o -name '*.properties' \) -not -path '*/test/*')"
  files="$files $(find . -type f -path '*/org/bouncycastle/util/test/*.class')"
  files="$files $(find . -type f -path '*/org/bouncycastle/jce/provider/test/*.class')"
  files="$files $(find . -type f -path '*/org/bouncycastle/ocsp/test/*.class')"
  test ! -d classes && mf="" \
    || mf="`find classes/ -type f -name "*.mf" 2>/dev/null`"
  test -n "$mf" && jar cvfm $jarfile $mf $files \
    || %jar cvf $jarfile $files
popd

%install
install -dm 755 %{buildroot}%{_sysconfdir}/java/security/security.d
touch %{buildroot}%{_sysconfdir}/java/security/security.d/2000-%{classname}

# install bouncy castle provider
install -dm 755 %{buildroot}%{_javadir}
install -pm 644 bcprov-%{version}.jar \
  %{buildroot}%{_javadir}/bcprov-%{version}.jar
pushd %{buildroot}%{_javadir}
  ln -sf bcprov-%{version}.jar bcprov.jar
popd

# javadoc
mkdir -p %{buildroot}%{_javadocdir}/%{name}
cp -pr docs/* %{buildroot}%{_javadocdir}/%{name}

# maven pom
install -dm 755 %{buildroot}%{_mavenpomdir}
install -pm 644 %{SOURCE1} %{buildroot}%{_mavenpomdir}/JPP-bcprov.pom
%add_maven_depmap -a "bouncycastle:bcprov-jdk15,org.bouncycastle:bcprov-jdk16" JPP-bcprov.pom bcprov.jar

%check
# Tests hang in obs, run them localy when bumping
#pushd src
#  export CLASSPATH=$PWD:$(build-classpath junit)
#  for test in $(find . -name AllTests.class) ; do
#    test=${test#./} ; test=${test%.class} ; test=${test//\//.}
#    # TODO: failures; get them fixed and remove || :
#    %java org.junit.runner.JUnitCore $test || :
#  done
#popd

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

%files
%doc *.html
%{_javadir}/bcprov.jar
%{_javadir}/bcprov-%{version}.jar
%{_javadir}/*
%config(noreplace) %{_sysconfdir}/java/security/security.d/2000-%{classname}
%{_mavenpomdir}/JPP-bcprov.pom
%{_datadir}/maven-metadata/%{name}.xml

%files javadoc
%{_javadocdir}/%{name}/

%changelog
