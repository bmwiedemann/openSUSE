#
# spec file for package tagsoup
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2000-2005, JPackage Project
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


Name:           tagsoup
Version:        1.2.1
Release:        0
Summary:        A SAX-compliant HTML parser written in Java
License:        Apache-2.0
Group:          Productivity/Publishing/XML
URL:            http://home.ccil.org/~cowan/XML/tagsoup/
#Source0:        http://home.ccil.org/~cowan/XML/tagsoup/tagsoup-1.2.1-src.zip
Source0:        tagsoup-1.2.1-src.zip
Source1:        http://repo1.maven.org/maven2/org/ccil/cowan/tagsoup/%{name}/%{version}/%{name}-%{version}.pom
Patch0:         tagsoup-1.2.1-man.patch
Patch1:         tagsoup-1.2.1-jdk9.patch
BuildRequires:  ant
BuildRequires:  fdupes
BuildRequires:  javapackages-local
BuildRequires:  unzip
BuildRequires:  xalan-j2
Requires:       javapackages-tools
BuildArch:      noarch

%description
TagSoup is a SAX-compliant parser written in Java that, instead of
parsing well-formed or valid XML, parses HTML as it is found in the wild: nasty
and brutish, though quite often far from short. By providing a SAX interface,
it allows standard XML tools to be applied to even the worst HTML.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Documentation/HTML

%description javadoc
Javadoc package for %{name}.

%prep
%setup -q
%patch0
%patch1 -p1

find . -name '*.class' -delete
find . -name "*.jar" -delete

%build
export CLASSPATH=$(build-classpath xalan-j2-serializer xalan-j2)
ant \
  -Dant.build.javac.source=1.6 -Dant.build.javac.target=1.6 \
  -Dtagsoup.version=%{version} \
  -Dj2se.apiurl=%{_javadocdir}/java \
  -Dclasspath=$(build-classpath xalan-j2-serializer xalan-j2) \
  dist docs-api

%install
# jar
mkdir -p %{buildroot}%{_javadir}
install -m 644 dist/lib/%{name}-%{version}.jar \
  %{buildroot}%{_javadir}/%{name}.jar
# pom
mkdir -p %{buildroot}%{_mavenpomdir}
install -pm 644 %{SOURCE1} %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom
%add_maven_depmap
# javadoc
mkdir -p %{buildroot}%{_javadocdir}/%{name}
cp -pr docs/api/* %{buildroot}%{_javadocdir}/%{name}
%fdupes -s %{buildroot}%{_javadocdir}/%{name}

mkdir -p %{buildroot}%{_mandir}/man1
install -m 644 %{name}.1 %{buildroot}%{_mandir}/man1/

%files -f .mfiles
%{_mandir}/man1/%{name}.1%{?ext_man}
%license LICENSE
%doc CHANGES README TODO %{name}.txt

%files javadoc
%{_javadocdir}/%{name}

%changelog
