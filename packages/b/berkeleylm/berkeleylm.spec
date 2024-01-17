#
# spec file for package berkeleylm
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


Name:           berkeleylm
Version:        1.1.6
Release:        0
Summary:        Berkeley Language Model library
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            https://github.com/adampauls/berkeleylm
Source0:        %{name}-%{version}.tar.xz
Source1:        pom.xml
BuildRequires:  ant
BuildRequires:  fdupes
BuildRequires:  java-devel >= 1.8
BuildRequires:  javapackages-local
BuildArch:      noarch

%description
Berkeleylm is a library for estimating storing large n-gram language models in
memory and accessing them efficiently. It is described in
http://nlp.cs.berkeley.edu/pubs/Pauls-Klein_2011_LM_paper.pdf

%package javadoc
Summary:        API documentation for %{name}
Group:          Documentation/HTML

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q

%build
%{ant} \
	-Dant.build.javac.source=1.8 -Dant.build.javac.target=1.8 \
	-Dtest.skip=true \
	jar javadoc

%install
install -dm 0755 %{buildroot}%{_javadir}
install -pm 0644 jar/%{name}.jar %{buildroot}%{_javadir}/%{name}.jar
# pom
install -dm 0755 %{buildroot}%{_mavenpomdir}
install -pm 0644 %{SOURCE1} %{buildroot}%{_mavenpomdir}/%{name}.pom
%add_maven_depmap %{name}.pom %{name}.jar
# javadoc
install -dm 0755 %{buildroot}%{_javadocdir}/%{name}
cp -pr doc/* %{buildroot}%{_javadocdir}/%{name}/
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%{_javadir}/%{name}.jar

%files javadoc
%{_javadocdir}/%{name}

%changelog
