#
# spec file for package pentaho-reporting-flow-engine
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


Name:           pentaho-reporting-flow-engine
Version:        0.9.4
Release:        0
Summary:        Pentaho Flow Reporting Engine
License:        LGPL-2.1-or-later
Group:          Development/Libraries/Java
URL:            http://reporting.pentaho.org/
Source:         http://downloads.sourceforge.net/jfreereport/flow-engine-%{version}.zip
Source99:       %{name}-rpmlintrc
BuildRequires:  ant
BuildRequires:  flute
BuildRequires:  java-devel >= 1.8
BuildRequires:  jpackage-utils
BuildRequires:  libbase
BuildRequires:  libfonts
BuildRequires:  libformula
BuildRequires:  liblayout
BuildRequires:  libloader
BuildRequires:  librepository
BuildRequires:  libserializer
BuildRequires:  pentaho-libxml
BuildRequires:  sac
BuildRequires:  unzip
BuildRequires:  xml-commons-apis
Requires:       flute
Requires:       java
Requires:       jpackage-utils
Requires:       libbase >= 1.1.3
Requires:       libfonts >= 1.1.3
Requires:       libformula >= 1.1.3
Requires:       liblayout >= 0.2.10
Requires:       librepository >= 1.1.3
Requires:       libserializer
Requires:       pentaho-libxml
Requires:       sac
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
Pentaho Reporting Flow Engine is a free Java report library, formerly
known as 'JFreeReport'

%package javadoc
Summary:        Javadoc for %{name}
Group:          Documentation/HTML

%description javadoc
Javadoc for %{name}.

%prep
%setup -q -c
mkdir -p lib
find . -name "*.jar" -exec rm -f {} \;
build-jar-repository -s -p lib commons-logging-api libbase libloader \
    libfonts libxml jaxp libformula librepository sac flute liblayout \
    libserializer

%build
%ant \
    -Dant.build.javac.source=1.8 -Dant.build.javac.target=1.8 \
    jar javadoc

%install

mkdir -p %{buildroot}%{_javadir}
cp -p build/lib/flow-engine.jar %{buildroot}%{_javadir}/flow-engine.jar

mkdir -p %{buildroot}%{_javadocdir}/%{name}
cp -rp build/api %{buildroot}%{_javadocdir}/%{name}

%files
%defattr(0644,root,root,0755)
%doc licence-LGPL.txt README.txt ChangeLog.txt
%{_javadir}/*.jar

%files javadoc
%defattr(0644,root,root,0755)
%{_javadocdir}/%{name}

%changelog
