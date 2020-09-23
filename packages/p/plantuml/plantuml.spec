#
# spec file for package plantuml
#
# Copyright (c) 2020 SUSE LLC
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
Version:        1.2020.17
Release:        0
Summary:        Java UML Tool
License:        GPL-3.0-or-later
Group:          Productivity/Publishing/Other
URL:            http://plantuml.sourceforge.net
Source0:        https://github.com/plantuml/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        %{name}.script
Source2:        %{name}.xml
Source10:       example01.uml
Source11:       example02.uml
Source20:       http://pdf.plantuml.net/PlantUML_Language_Reference_Guide_en.pdf
BuildRequires:  ant
BuildRequires:  docbook-xsl-stylesheets
BuildRequires:  java-devel >= 1.5
BuildRequires:  jpackage-utils
BuildRequires:  libxslt
BuildRequires:  unzip
Requires:       dejavu-fonts
Requires:       java >= 1.8.0
Requires:       jpackage-utils
Conflicts:      java-1_5_0-gcj-compat
BuildArch:      noarch

%description
PlantUML is a program allowing to draw UML diagrams, using a simple human readable text description.

PlantUML supports the following diagram types:
   - sequence diagram
   - use case diagram
   - class diagram
   - activity diagram
   - component diagram
   - state diagram

Output images can be generated in PNG, in SVG or LaTeX format.  PlantUML also supports generation of ASCII art diagrams (only for sequence diagrams).

%prep
%setup -q
# Replace placeholder strings:
cp %{SOURCE1} %{name}
cp %{SOURCE2} .
cp %{SOURCE10} %{SOURCE11} .
cp %{SOURCE20} .

%build
%{ant} \
  -Dant.build.javac.source=1.6 \
  -Dant.build.javac.target=1.6

# Building Manpages and HTML:
DB=%{_datadir}/xml/docbook/stylesheet/nwalsh/current/
xsltproc $DB/manpages/docbook.xsl %{name}.xml
xsltproc --output %{name}.html $DB/html/docbook.xsl %{name}.xml

%install
install -m 755 -d %{buildroot}%{_bindir}/
install -m 755 -d %{buildroot}%{_javadir}
install -m 755 -d %{buildroot}%{_mandir}/man1
install -m 755 %{name} %{buildroot}%{_bindir}/%{name}
install -m 644 %{name}.1  %{buildroot}%{_mandir}/man1/

# Install jar file
cp %{name}.jar %{buildroot}%{_javadir}/%{name}-%{version}.jar
(cd %{buildroot}%{_javadir} && for jar in *-%{version}.jar; do ln -sf ${jar} `echo $jar| sed "s|-%{version}||g"`; done)

%files
%license license.txt
%doc example*.uml *.pdf *.html
%{_javadir}/%{name}.jar
%{_javadir}/%{name}-%{version}.jar
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1%{?ext_man}

%changelog
