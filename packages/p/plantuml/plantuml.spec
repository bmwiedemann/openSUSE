#
# spec file for package plantuml
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


Name:           plantuml
Version:        1.2023.0
Release:        0
Summary:        Java UML Tool
License:        GPL-3.0-or-later
Group:          Productivity/Publishing/Other
URL:            http://plantuml.com/
Source0:        http://downloads.sourceforge.net/plantuml/%{name}-lgpl-%{version}.tar.gz
Source1:        %{name}.script
Source10:       http://pdf.plantuml.net/PlantUML_Language_Reference_Guide_en.pdf
Patch0:         build-with-javac-utf8-encoding.patch
BuildRequires:  ant
BuildRequires:  fdupes
BuildRequires:  javapackages-local
BuildRequires:  xmvn-install
Requires:       java >= 1.8.0
Requires:       javapackages-tools
BuildArch:      noarch

%description
PlantUML is a program allowing to draw UML diagrams, using a simple
and human readable text description. It is extremely useful for code
documenting, sketching project architecture during team conversations
and so on.

PlantUML supports the following diagram types
  - sequence diagram
  - use case diagram
  - class diagram
  - activity diagram
  - component diagram
  - state diagram

%package javadoc
Summary:        Javadoc for %{name}
Group:          Productivity/Publishing/Other

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -c -n plantuml
%patch0 -p1
cp %{SOURCE1} %{name}
cp %{SOURCE10} .
# only contains a single line pointing to website
rm README

%build
ant

# build javadoc
export CLASSPATH=$(build-classpath ant):plantuml.jar
%javadoc -source 1.8 -encoding UTF-8 -Xdoclint:none -d javadoc $(find src -name "*.java") -windowtitle "PlantUML %{version}"

%install
# Set jar location
%mvn_file net.sourceforge.%{name}:%{name} %{name}
# Configure maven depmap
%mvn_artifact net.sourceforge.%{name}:%{name}:%{version} %{name}.jar
%mvn_install -J javadoc

install -m 755 -d %{buildroot}%{_bindir}/
install -m 755 -d %{buildroot}%{_javadir}
install -m 755 %{name} %{buildroot}%{_bindir}/%{name}

# Install jar file
cp %{name}.jar %{buildroot}%{_javadir}/%{name}-%{version}.jar
(cd %{buildroot}%{_javadir} && for jar in *-%{version}.jar; do ln -sf ${jar} `echo $jar| sed "s|-%{version}||g"`; done)

%fdupes %{buildroot}%{_datadir}

%files -f .mfiles
%{_bindir}/plantuml
%{_javadir}/%{name}-%{version}.jar
%license COPYING

%files javadoc -f .mfiles-javadoc
%license COPYING

%changelog
