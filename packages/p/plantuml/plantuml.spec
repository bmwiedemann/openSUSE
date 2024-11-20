#
# spec file for package plantuml
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


Name:           plantuml
Version:        1.2024.8
Release:        0
Summary:        Java UML Tool
License:        GPL-3.0-or-later
Group:          Productivity/Publishing/Other
URL:            https://plantuml.com/
Source0:        https://github.com/plantuml/plantuml/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source10:       http://pdf.plantuml.net/PlantUML_Language_Reference_Guide_en.pdf
Patch0:         build-with-javac-utf8-encoding.patch
BuildRequires:  ant
BuildRequires:  fdupes
BuildRequires:  javapackages-local
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
%setup -q
%patch -P 0 -p1
cp %{SOURCE10} .

%build
ant

# build javadoc
export CLASSPATH=$(build-classpath ant):plantuml.jar
javadoc \
    -source 1.8 \
    -encoding UTF-8 \
    -notimestamp \
    -Xdoclint:none \
    -d javadoc \
    -windowtitle "PlantUML %{version}" \
    $(find src -name "*.java")

%install
# Set jar location
install -dm 0755 %{buildroot}%{_javadir}
install -pm 0644 %{name}.jar %{buildroot}%{_javadir}/%{name}.jar
# Configure maven depmap
%add_maven_depmap  net.sourceforge.%{name}:%{name}:%{version} %{name}.jar
# javadoc
install -dm 0755 %{buildroot}%{_javadocdir}/%{name}
cp -r javadoc/* %{buildroot}%{_javadocdir}/%{name}/
%fdupes %{buildroot}%{_datadir}
# launcher script
%jpackage_script net.sourceforge.plantuml.Run "" "" %{name} %{name}

%files -f .mfiles
%{_bindir}/%{name}
%license COPYING

%files javadoc
%{_javadocdir}/%{name}
%license COPYING

%changelog
