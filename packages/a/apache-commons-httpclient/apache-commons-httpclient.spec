#
# spec file for package apache-commons-httpclient
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


%define short_name commons-httpclient
Name:           apache-commons-httpclient
Version:        3.1
Release:        0
Summary:        Feature rich package for accessing resources via HTTP
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            https://hc.apache.org/httpclient-3.x/
Source0:        https://archive.apache.org/dist/httpcomponents/%{short_name}/source/%{short_name}-%{version}-src.tar.gz
Source1:        https://repo1.maven.org/maven2/%{short_name}/%{short_name}/%{version}/%{short_name}-%{version}.pom
Patch0:         %{name}-disablecryptotests.patch
# Add OSGi MANIFEST.MF bits
Patch1:         %{name}-addosgimanifest.patch
Patch2:         %{name}-encoding.patch
#PATCH-FIX-UPSTREAM: bnc#803332
#https://issues.apache.org/jira/secure/attachment/12560251/CVE-2012-5783-2.patch
Patch3:         %{short_name}-CVE-2012-5783-2.patch
#PATCH-FIX-UPSTREAM bsc#1178171 CVE-2014-3577 MITM security vulnerability
Patch4:         apache-commons-httpclient-CVE-2014-3577.patch
#PATCH-FIX-UPSTREAM bsc#945190 CVE-2015-5262 Missing HTTPS connection timeout
Patch5:         apache-commons-httpclient-CVE-2015-5262.patch
BuildRequires:  ant
BuildRequires:  ant-junit
BuildRequires:  commons-codec
BuildRequires:  commons-logging >= 1.0.3
BuildRequires:  fdupes
BuildRequires:  java-devel >= 1.8
BuildRequires:  javapackages-local >= 6
BuildRequires:  junit
Provides:       %{short_name} = %{version}
Provides:       jakarta-%{short_name} = %{version}
Obsoletes:      jakarta-%{short_name} < %{version}
Provides:       jakarta-%{short_name}3 = %{version}
Obsoletes:      jakarta-%{short_name}3 < %{version}
BuildArch:      noarch

%description
Although the java.net  package provides basic functionality for
accessing resources via HTTP, it doesn't provide the full flexibility
or functionality needed by many applications. The Apache Commons
HttpClient component provides a package implementing the client side
of the most recent HTTP standards and recommendations.

The HttpClient component may be of interest to anyone building
HTTP-aware client applications such as web browsers, web service
clients, or systems that leverage or extend the HTTP protocol for
distributed communication.

%package        javadoc
Summary:        Developer documentation for %{name}
Group:          Development/Libraries/Java

%description    javadoc
Developer documentation for %{name} in JavaDoc
format.

%{summary}.

%package        demo
Summary:        Demonstration files for %{name}
Group:          Development/Libraries/Java
Requires:       %{name} = %{version}

%description    demo
Demonstration files for %{name}. NOTE: It is
possible that some demonstration files are specially prepared for SUN
Java runtime environment. If they fail with IBM or BEA Java, the
package itself does not need to be broken.

%{summary}.

%package        manual
Summary:        Manual for %{name}
Group:          Development/Libraries/Java

%description    manual
Manual for %{name}

%{summary}.

%prep
%setup -q -n %{short_name}-%{version}
mkdir lib # duh
rm -rf docs/apidocs docs/*.patch docs/*.orig docs/*.rej

%patch -P 0

pushd src/conf
sed -i 's/\r//' MANIFEST.MF
%patch -P 1
popd

%patch -P 2
%patch -P 3 -p1
%patch -P 4 -p1
%patch -P 5 -p1

# Use javax classes, not com.sun ones
# assume no filename contains spaces
pushd src
    for j in $(find . -name "*.java" -exec grep -l 'com\.sun\.net\.ssl' {} \;); do
        sed -e 's|com\.sun\.net\.ssl|javax.net.ssl|' $j > tempf
        cp tempf $j
    done
    rm tempf
popd

sed -i 's/\r//' RELEASE_NOTES.txt
sed -i 's/\r//' README.txt
sed -i 's/\r//' LICENSE.txt

%build
ant \
  -Dant.build.javac.source=8 -Dant.build.javac.target=8 \
  -Dbuild.sysclasspath=first \
  -Djavadoc.j2sdk.link=%{_javadocdir}/java \
  -Djavadoc.logging.link=%{_javadocdir}/apache-commons-logging \
  -Dtest.failonerror=false \
  -Dlib.dir=%{_javadir} \
  -Djavac.encoding=UTF-8 \
  dist test

%install
# jars
mkdir -p %{buildroot}%{_javadir}
cp -p dist/%{short_name}.jar \
  %{buildroot}%{_javadir}/%{name}.jar
# compat symlink
pushd %{buildroot}%{_javadir}
ln -s %{name}.jar %{name}3.jar
ln -s %{name}.jar %{short_name}3.jar
ln -s %{name}.jar %{short_name}.jar
ln -s %{name}.jar jakarta-%{short_name}.jar
ln -s %{name}.jar jakarta-%{short_name}3.jar
popd

# pom
install -d -m 0755 %{buildroot}%{_mavenpomdir}
%{mvn_install_pom} %{SOURCE1} %{buildroot}%{_mavenpomdir}/%{name}.pom
%add_maven_depmap %{name}.pom %{name}.jar -a apache:commons-httpclient

# javadoc
install -d -m 0755 %{buildroot}%{_javadocdir}
mv dist/docs/api %{buildroot}%{_javadocdir}/%{name}
%fdupes -s %{buildroot}%{_javadocdir}/%{name}

# demo
install -d -m 0755 %{buildroot}%{_datadir}/%{name}
cp -pr src/examples src/contrib %{buildroot}%{_datadir}/%{name}
%fdupes -s %{buildroot}%{_datadir}/%{name}

# manual and docs
rm -f dist/docs/{BUILDING,TESTING}.txt
ln -s %{_javadocdir}/%{name} dist/docs/apidocs
%fdupes -s dist/docs

%files -f .mfiles
%defattr(0644,root,root,0755)
%license LICENSE.txt
%doc README.txt RELEASE_NOTES.txt
%{_javadir}/%{name}3.jar
%{_javadir}/%{short_name}3.jar
%{_javadir}/%{short_name}.jar
%{_javadir}/jakarta-%{short_name}3.jar
%{_javadir}/jakarta-%{short_name}.jar

%files javadoc
%defattr(0644,root,root,0755)
%doc %{_javadocdir}/%{name}

%files demo
%defattr(0644,root,root,0755)
%{_datadir}/%{name}

%files manual
%defattr(0644,root,root,0755)
%doc dist/docs/*

%changelog
