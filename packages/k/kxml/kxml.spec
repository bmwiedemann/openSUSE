#
# spec file for package kxml
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2000-2008, JPackage Project
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


Name:           kxml
Version:        2.3.0
Release:        17%{?dist}
Summary:        Small XML pull parser
License:        MIT
Group:          Development/Libraries/Java
URL:            http://kxml.sourceforge.net/
# ./create-tarball.sh %%{version}
Source0:        %{name}-%{version}-clean.tar.gz
Source1:        http://repo1.maven.org/maven2/net/sf/kxml/kxml2/%{version}/kxml2-%{version}.pom
Source2:        http://repo1.maven.org/maven2/net/sf/kxml/kxml2-min/%{version}/kxml2-min-%{version}.pom
Source3:        %{name}-%{version}-OSGI-MANIFEST.MF
Source100:      create-tarball.sh
Patch0:         0001-Unbundle-xpp3-classes.patch
Patch1:         kxml-2.3.0-fix_build.patch
BuildRequires:  ant
BuildRequires:  fdupes
BuildRequires:  javapackages-local
BuildRequires:  xmvn-install
BuildRequires:  xmvn-resolve
BuildRequires:  xpp3 >= 1.1.3.1
Requires:       xpp3 >= 1.1.3.1
BuildArch:      noarch

%description
kXML is a small XML pull parser, specially designed for constrained
environments such as Applets, Personal Java or MIDP devices.

%package        javadoc
Summary:        Javadoc for %{name}
Group:          Documentation/HTML

%description    javadoc
API documentation for %{name}.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
mkdir -p lib
build-jar-repository -s lib xpp3
%{ant}

jar ufm dist/%{name}2-%{version}.jar %{SOURCE3}

%{mvn_artifact} %{SOURCE1} dist/%{name}2-%{version}.jar
%{mvn_artifact} %{SOURCE2} dist/%{name}2-min-%{version}.jar

# Compat symlinks
%{mvn_file} :kxml2 kxml/kxml2 kxml
%{mvn_file} :kxml2-min kxml/kxml2-min kxml-min

%install
%mvn_install -J www/kxml2/javadoc
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%license license.txt

%files javadoc -f .mfiles-javadoc
%license license.txt

%changelog
