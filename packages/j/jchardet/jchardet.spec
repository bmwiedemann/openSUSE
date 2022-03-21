#
# spec file for package jchardet
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


Name:           jchardet
Version:        1.1
Release:        0
Summary:        Java port of Mozilla's automatic character set detection algorithm
License:        GPL-2.0-or-later OR MPL-1.1 OR LGPL-2.1-or-later
URL:            https://jchardet.sourceforge.net/
Source0:        https://download.sourceforge.net/jchardet/%{version}/jchardet-%{version}.zip
Source1:        https://repo1.maven.org/maven2/net/sourceforge/%{name}/%{name}/1.0/%{name}-1.0.pom
BuildRequires:  ant
BuildRequires:  fdupes
BuildRequires:  java-devel >= 1.8
BuildRequires:  javapackages-local
BuildRequires:  unzip
BuildArch:      noarch

%description
jchardet is a java port of the source from Mozilla's automatic charset
detection algorithm. The original author is Frank Tang. What is available
here is the java port of that code. The original source in C++ can be found
from http://lxr.mozilla.org/mozilla/source/intl/chardet/. More information can
be found at http://www.mozilla.org/projects/intl/chardet.html.

%package javadoc
Summary:        API documentation for %{name}

%description javadoc
%{summary}.

%prep
%setup -q
find -name '*.class' -exec rm -f '{}' \;
find -name '*.jar' -exec rm -f '{}' \;

cp %{SOURCE1} pom.xml

# fix up the provided version
%pom_xpath_set /pom:project/pom:version %{version}

# remove distributionManagement.status from pom
%pom_xpath_remove pom:distributionManagement

%build
# Build the jar file
%{ant} -Dant.build.javac.source=1.8 -Dant.build.javac.target=1.8 dist
# Generate the javadoc
mkdir -p dist/javadoc
javadoc -notimestamp -d dist/javadoc $(find src -name \*.java | xargs)

%install
# jar
install -dm 0755 %{buildroot}%{_javadir}/%{name}
install -pm 0644 dist/lib/chardet.jar %{buildroot}%{_javadir}/%{name}/%{name}.jar
# pom
install -dm 0755 %{buildroot}%{_mavenpomdir}/%{name}
install -pm 0644 pom.xml %{buildroot}%{_mavenpomdir}/%{name}/%{name}.pom
%add_maven_depmap %{name}/%{name}.pom %{name}/%{name}.jar
# javadoc
install -dm 0755 %{buildroot}%{_javadocdir}
cp -r dist/javadoc %{buildroot}%{_javadocdir}/%{name}
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%license LICENSE

%files javadoc
%{_javadocdir}/%{name}
%license LICENSE

%changelog
