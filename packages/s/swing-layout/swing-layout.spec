#
# spec file for package swing-layout
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           swing-layout
Version:        1.0.3
Release:        0
Summary:        Natural layout for Swing panels
License:        LGPL-2.1+
Group:          Development/Languages/Java
Url:            https://swing-layout.dev.java.net/
Source0:        %{name}-%{version}-src.tar.bz2
BuildRequires:  ant
BuildRequires:  fdupes
BuildRequires:  java-devel
BuildRequires:  javapackages-tools
BuildRequires:  xml-commons-apis
BuildRequires:  xml-commons-resolver
Requires:       jre >= 1.5
BuildArch:      noarch

%description
Swing Layout Extensions goal is to make it easy to create
   professional cross platform layouts with Swing. This project has
   an eye towards the needs of GUI builders, such as NetBeans. This
   project consists of the following pieces: * Ability to get the
   baseline for components.

* Ability to get the preferred gap between components.

A new LayoutManager that utilizes both of these concepts and is tuned
toward a free-form drag and drop layout model as can be provided by GUI
builders.

%package javadoc
Summary:        Natural layout for Swing panels
Group:          Development/Languages/Java

%description javadoc
Swing Layout Extensions goal is to make it easy to create
   professional cross platform layouts with Swing. This project has
   an eye towards the needs of GUI builders, such as NetBeans. This
   project consists of the following pieces: * Ability to get the
   baseline for components.

* Ability to get the preferred gap between components.

A new LayoutManager that utilizes both of these concepts and is tuned
toward a free-form drag and drop layout model as can be provided by GUI
builders.

%prep
%setup -q
# wrong end of line encoding
sed -i -e 's/.$//' releaseNotes.txt COPYING

%build
ant -Djavac.source=1.6 -Djavac.target=1.6 jar javadoc

%install
# jars
install -dm 755 %{buildroot}%{_javadir}
install -m 644 dist/%{name}.jar \
	%{buildroot}%{_javadir}/%{name}-%{version}.jar
pushd %{buildroot}%{_javadir}
	for jar in *-%{version}*; do
		ln -sf ${jar} `echo $jar| sed "s|-%{version}||g"`
	done
popd
# javadoc
install -dm 755 %{buildroot}%{_javadocdir}/%{name}
cp -pr dist/javadoc/* \
	%{buildroot}%{_javadocdir}/%{name}
%fdupes -s %{buildroot}%{_javadocdir}/%{name}

%files
%doc releaseNotes.txt COPYING
%{_javadir}/%{name}*.jar

%files javadoc
%doc %{_javadocdir}/%{name}

%changelog
