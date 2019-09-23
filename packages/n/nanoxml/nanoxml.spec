#
# spec file for package nanoxml
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


Name:           nanoxml
Version:        2.2.3
Release:        0
Summary:        Small non-validating XML parser for Java
License:        Zlib
Group:          Development/Libraries/Java
Url:            http://nanoxml.sourceforge.net/orig/
Source0:        NanoXML-2.2.3.tar.bz2
Source1:        %{name}-java-1.4.2-package-list
Patch0:         %{name}-build.patch
Patch1:         %{name}-%{version}_build.patch
Patch2:         %{name}-%{version}_enum.patch
BuildRequires:  fdupes
BuildRequires:  java-devel
BuildRequires:  jpackage-utils >= 1.6
BuildRequires:  unzip
Requires:       java
Recommends:     %{name}-manual = %{version}
BuildArch:      noarch

%description
NanoXML is a small non-validating parser for Java.
The full parser with builder fits in a JAR file of about 32K.

%package        lite
Summary:        Lite version of %{name}
Group:          Development/Libraries/Java
Recommends:     %{name}-manual-lite = %{version}

%description    lite
NanoXML/Lite is the successor of NanoXML 1.x. It is still small (only
6KB) and features a much faster algorithm. It is recommended if you
are currently using NanoXML 1.x and do not want to adapt your code
for the new API or if you are coding applications that have to be
very small (like applets or embedded code). Please note that
NanoXML/Lite has only limited functionality (no mixed content, DTD is
ignored...).

%package        manual
Summary:        Manual for %{name}
Group:          Documentation/Other
Recommends:     %{name} = %{version}

%description    manual
Documentation for %{name}, a small non-validating XML parser.

%package        manual-lite
Summary:        Manual for the lite version of %{name}
Group:          Documentation/Other
Recommends:     %{name}-lite = %{version}

%description    manual-lite
Documentation for the lite version of %{name}.

%package        javadoc
Summary:        Javadoc for %{name}
Group:          Documentation/Other

%description    javadoc
Java documentation for %{name}.

%prep
%setup -q -n NanoXML-%{version}
%patch0
%patch1
%patch2
cp %{SOURCE1} package-list
find . -name "*.jar" -delete

%build
sh ./build.sh

%install
# jars
install -dm 755 %{buildroot}%{_javadir}
install -pm 644 Output/%{name}-lite.jar \
  %{buildroot}%{_javadir}/%{name}-lite-%{version}.jar
install -pm 644 Output/%{name}-sax.jar \
  %{buildroot}%{_javadir}/%{name}-sax-%{version}.jar
install -pm 644 Output/%{name}.jar \
  %{buildroot}%{_javadir}/%{name}-%{version}.jar
(cd %{buildroot}%{_javadir} && for jar in *-%{version}*; do ln -sf ${jar} `echo $jar| sed "s|-%{version}||g"`; done)

# javadoc
install -dm 755 %{buildroot}%{_javadocdir}/%{name}
cp -pr Documentation/JavaDoc/* %{buildroot}%{_javadocdir}/%{name}
%fdupes -s %{buildroot}%{_javadocdir}/%{name}

%files
%{_javadir}/%{name}-%{version}.jar
%{_javadir}/%{name}.jar
%{_javadir}/%{name}-sax-%{version}.jar
%{_javadir}/%{name}-sax.jar

%files lite
%{_javadir}/%{name}-lite-%{version}.jar
%{_javadir}/%{name}-lite.jar

%files manual
%doc Documentation/NanoXML-Java/*

%files manual-lite
%doc Documentation/NanoXML-Lite/*

%files javadoc
%{_javadocdir}/%{name}

%changelog
