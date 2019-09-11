#
# spec file for package sac
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           sac
Version:        1.3
Release:        0
Summary:        Java standard interface for CSS parser
License:        W3C
Group:          Development/Libraries/Java
Url:            http://www.w3.org/Style/CSS/SAC/
#Original source: http://www.w3.org/2002/06/%{name}java-%{version}.zip
#unzip, find . -name "*.jar" -exec rm {} \;
#to simplify the licensing
Source0:        %{name}java-%{version}-jarsdeleted.zip
Source1:        %{name}-build.xml
Source2:        %{name}-MANIFEST.MF
Source3:        http://mirrors.ibiblio.org/pub/mirrors/maven2/org/w3c/css/sac/1.3/sac-1.3.pom
BuildRequires:  ant
BuildRequires:  java-devel >= 1.6.0
BuildRequires:  javapackages-local
BuildRequires:  javapackages-tools
BuildRequires:  unzip
BuildRequires:  zip
Requires:       java
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
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
    -Dant.build.javac.source=1.6 -Dant.build.javac.target=1.6 \
    jar javadoc

%install
# inject OSGi manifests
mkdir -p META-INF
cp -p %{SOURCE2} META-INF/MANIFEST.MF
touch META-INF/MANIFEST.MF
zip -u build/lib/sac.jar META-INF/MANIFEST.MF

mkdir -p %{buildroot}%{_javadir}
cp -p ./build/lib/sac.jar %{buildroot}%{_javadir}/sac.jar

install -d -m 755 %{buildroot}%{_javadocdir}/%{name}
cp -pr build/api/* %{buildroot}%{_javadocdir}/%{name}

# poms
install -d -m 755 %{buildroot}%{_mavendepmapfragdir}
install -d -m 755 %{buildroot}%{_mavenpomdir}
install -pm 644 %{SOURCE3} \
    %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom

%add_maven_depmap JPP-%{name}.pom %{name}.jar

%files
%defattr(-,root,root)
%doc COPYRIGHT.html
%{_javadir}/%{name}.jar
%{_mavenpomdir}/*
%if 0%{?suse_version} > 1320
%{_datadir}/maven-metadata/%{name}.xml*
%else
%{_mavendepmapfragdir}/*
%endif

%files javadoc
%defattr(-,root,root)
%doc COPYRIGHT.html
%{_javadocdir}/%{name}

%changelog
