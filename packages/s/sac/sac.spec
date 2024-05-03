#
# spec file for package sac
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


Name:           sac
Version:        1.3
Release:        0
Summary:        Java standard interface for CSS parser
License:        W3C
Group:          Development/Libraries/Java
URL:            https://www.w3.org/Style/CSS/SAC/
#Original source: http://www.w3.org/2002/06/%{name}java-%{version}.zip
#unzip, find . -name "*.jar" -exec rm {} \;
#to simplify the licensing
Source0:        %{name}java-%{version}-jarsdeleted.zip
Source1:        %{name}-build.xml
Source2:        %{name}-MANIFEST.MF
Source3:        https://repo1.maven.org/maven2/org/w3c/css/sac/%{version}/%{name}-%{version}.pom
BuildRequires:  ant
BuildRequires:  fdupes
BuildRequires:  java-devel >= 1.8
BuildRequires:  javapackages-local >= 6
BuildRequires:  unzip
BuildRequires:  zip
Requires:       java
BuildArch:      noarch

%description
SAC is a standard interface for CSS parsers, intended to work with CSS1, CSS2,
CSS3 and other CSS derived languages.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Documentation/HTML

%description javadoc
Javadoc for %{name}.

%prep
%setup -q
install -m 644 %{SOURCE1} build.xml
find . -name "*.jar" -exec rm -f {} \;

%build
ant \
    -Dant.build.javac.source=1.8 -Dant.build.javac.target=1.8 \
    jar javadoc

%install
# inject OSGi manifest
jar -umf %{SOURCE2} build/lib/sac.jar

install -d -m 0755 %{buildroot}%{_javadir}
install -p -m 0644 ./build/lib/sac.jar %{buildroot}%{_javadir}/%{name}.jar

# poms
install -d -m 0755 %{buildroot}%{_mavenpomdir}
%{mvn_install_pom} %{SOURCE3} %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom
%add_maven_depmap JPP-%{name}.pom %{name}.jar

# javadoc
install -d -m 0755 %{buildroot}%{_javadocdir}/%{name}
cp -pr build/api/* %{buildroot}%{_javadocdir}/%{name}
%fdupes %{buildroot}%{_javadocdir}/%{name}

%files -f .mfiles
%doc COPYRIGHT.html

%files javadoc
%doc COPYRIGHT.html
%{_javadocdir}/%{name}

%changelog
