#
# spec file for package saxpath
#
# Copyright (c) 2023 SUSE LLC
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


Name:           saxpath
Version:        1.0
Release:        0
Summary:        Simple API for XPath
License:        Saxpath
URL:            https://sourceforge.net/projects/saxpath/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Source1:        https://repo1.maven.org/maven2/%{name}/%{name}/%{version}-FCS/%{name}-%{version}-FCS.pom
Source2:        LICENSE
BuildRequires:  ant
BuildRequires:  javapackages-local
Requires:       jpackage-utils
BuildArch:      noarch

%description
The SAXPath project is a Simple API for XPath. SAXPath is analogous to SAX
in that the API abstracts away the details of parsing and provides a simple
event based callback interface.

%package javadoc
Summary:        API documentation for %{name}

%description javadoc
This package contains %{summary}.

%prep
%setup -q -n %{name}-%{version}-FCS

find -name \*.jar -delete

cp %{SOURCE2} .

%build
mkdir src/conf
touch src/conf/MANIFEST.MF

%{ant}

# fix rpmlint warings: saxpath-javadoc.noarch: W: wrong-file-end-of-line-encoding /usr/share/javadoc/saxpath/**/*.css
for file in `find build/doc -type f | grep .css`; do
    sed -i 's/\r//g' $file
done

%install
# jar
install -d -m 755 %{buildroot}/%{_javadir}
install -p -m 644 build/%{name}.jar %{buildroot}/%{_javadir}/
# pom
install -d -m 755 %{buildroot}/%{_mavenpomdir}
install -p -m 644 %{SOURCE1} %{buildroot}/%{_mavenpomdir}/%{name}.pom
%add_maven_depmap %{name}.pom %{name}.jar
# javadoc
install -d -m 755 %{buildroot}/%{_javadocdir}/%{name}
cp -a build/doc/* %{buildroot}/%{_javadocdir}/%{name}/

%files -f .mfiles
%license LICENSE

%files javadoc
%license LICENSE
%{_javadocdir}/%{name}

%changelog
