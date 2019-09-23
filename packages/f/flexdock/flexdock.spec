#
# spec file for package flexdock
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           flexdock
Version:        1.2.4
Release:        0
Summary:        Swing windowing and docking framework
License:        MIT
Group:          Development/Libraries/Java
Url:            http://forge.scilab.org/index.php/p/flexdock/
Source0:        http://forge.scilab.org/index.php/p/flexdock/downloads/get/%{name}-%{version}.tar.gz
# PATCH-FIX-OPENSUSE flexdock-nojmf.patch
Patch1:         flexdock-nojmf.patch
# PATCH-FIX-OPENSUSE flexdock-build.patch
Patch2:         flexdock-build.patch
Patch3:         flexdock-1.2.4-jdk9.patch
BuildRequires:  ant
BuildRequires:  java-devel >= 1.8
BuildRequires:  jgoodies-looks
BuildRequires:  jpackage-utils
BuildRequires:  skinlf
Requires:       jakarta-commons-logging
Requires:       java >= 1.8
Requires:       jgoodies-looks
Requires:       jpackage-utils
Requires:       skinlf
BuildArch:      noarch

%description
FlexDock is a Java docking framework for use in cross-platform Swing
applications. It offers features you'd expect in any desktop docking
framework such as:

* Tabbed and Split Layouts
* Drag-n-Drop capability (native drag rubber band painting on some platforms)
* Floating windows
* Collapsible Containers to Save Real Estate
* Layout Persistence

It is released using the MIT license.

%prep
%setup -q

%patch1 -p1
%patch2 -p1
%patch3 -p1

# fix wrong-file-end-of-line-encoding
sed -i 's/\r$//' README

# remove build in jars
find . -name '*.jar' -type f -delete -print
build-jar-repository -s -p lib skinlf looks

#Override the build file's default hard-coded paths
echo "sdk.home=%{java_home}" > workingcopy.properties

#Remove the jmf-using demo files
rm src/java/demo/org/flexdock/demos/raw/jmf/MediaPanel.java
rm src/java/demo/org/flexdock/demos/raw/jmf/JMFDemo.java

%build
%{ant} jar

%install
# jars
install -Dm 644 build/%{name}-%{version}.jar %{buildroot}%{_javadir}/%{name}-%{version}.jar
ln -sf %{name}-%{version}.jar %{buildroot}%{_javadir}/%{name}.jar

%files
%doc LICENSE.txt README release-notes.txt
%{_javadir}/*.jar

%changelog
