#
# spec file for package xpp3
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


Name:           xpp3
Version:        1.1.4c
Release:        0
Summary:        XML Pull Parser
License:        Apache-1.1
Group:          Development/Libraries/Java
# The http://www.extreme.indiana.edu/ does not exist anymore
URL:            https://web.archive.org/web/20201024082744/http://www.extreme.indiana.edu/xgws/xsoap/xpp/mxp1/index.html
Source0:        https://web.archive.org/web/20201024082744/http://www.extreme.indiana.edu/dist/java-repository/xpp3/distributions/xpp3-%{version}_src.tgz
Source1:        https://repo1.maven.org/maven2/xpp3/xpp3/%{version}/xpp3-%{version}.pom
Source2:        https://repo1.maven.org/maven2/xpp3/xpp3_min/%{version}/xpp3_min-%{version}.pom
Source3:        https://repo1.maven.org/maven2/xpp3/xpp3_xpath/%{version}/xpp3_xpath-%{version}.pom
Source4:        %{name}-%{version}-OSGI-MANIFEST.MF
Patch0:         xpp3-sourcetarget.patch
BuildRequires:  ant >= 1.6
BuildRequires:  java-devel >= 1.8
BuildRequires:  javapackages-local >= 6
BuildRequires:  junit
BuildRequires:  perl
BuildRequires:  xml-commons-apis
BuildArch:      noarch

%description
Xml Pull Parser 3rd Edition (XPP3) MXP1 is a new XmlPull parsing engine
that is based on ideas from XPP and in particular XPP2 but completely
revised and rewritten to take best advantage of latest JIT JVMs such as
Hotspot in JDK 1.4.

%package minimal
Summary:        XML Pull Parser
Group:          Development/Libraries/Java

%description minimal
Xml Pull Parser 3rd Edition (XPP3) MXP1 is a new XmlPull parsing engine
that is based on ideas from XPP and in particular XPP2 but completely
revised and rewritten to take best advantage of latest JIT JVMs such as
Hotspot in JDK 1.4.

%package javadoc
Summary:        XML Pull Parser
Group:          Development/Libraries/Java

%description javadoc
Xml Pull Parser 3rd Edition (XPP3) MXP1 is a new XmlPull parsing engine
that is based on ideas from XPP and in particular XPP2 but completely
revised and rewritten to take best advantage of latest JIT JVMs such as
Hotspot in JDK 1.4.

%prep
%setup -q
%patch -P 0 -p1
# remove all binary libs
find . -name "*.jar" -exec rm -f {} \;
# "src/java/addons_tests" does not exist
sed -i 's|depends="junit_main,junit_addons"|depends="junit_main"|' build.xml

%build
export CLASSPATH=$(build-classpath xml-commons-apis junit)
ant xpp3 junit apidoc

# Add OSGi metadata
jar ufm build/%{name}-%{version}.jar %{SOURCE4}

%install
# jars
install -d -m 0755 %{buildroot}%{_javadir}
install -p -m 0644 build/%{name}-%{version}.jar \
  %{buildroot}%{_javadir}/%{name}.jar
install -p -m 0644 build/%{name}_min-%{version}.jar \
  %{buildroot}%{_javadir}/%{name}-minimal.jar
install -p -m 0644 build/%{name}_xpath-%{version}.jar \
  %{buildroot}%{_javadir}/%{name}-xpath.jar
# javadoc
install -d -m 0755 %{buildroot}%{_javadocdir}/%{name}
cp -pr doc/api/* %{buildroot}%{_javadocdir}/%{name}
rm -rf doc/{build.txt,api}

# Install pom file
install -d -m 755 %{buildroot}%{_mavenpomdir}
%{mvn_install_pom} %{SOURCE1} %{buildroot}%{_mavenpomdir}/%{name}.pom
%{mvn_install_pom} %{SOURCE2} %{buildroot}%{_mavenpomdir}/%{name}-minimal.pom
%{mvn_install_pom} %{SOURCE3} %{buildroot}%{_mavenpomdir}/%{name}-xpath.pom
%add_maven_depmap %{name}.pom %{name}.jar
%add_maven_depmap %{name}-minimal.pom %{name}-minimal.jar -f minimal
%add_maven_depmap %{name}-xpath.pom %{name}-xpath.jar

%files -f .mfiles
%license LICENSE.txt
%doc README.html doc/*

%files minimal -f .mfiles-minimal

%files javadoc
%defattr(0644,root,root,0755)
%{_javadocdir}/%{name}

%changelog
