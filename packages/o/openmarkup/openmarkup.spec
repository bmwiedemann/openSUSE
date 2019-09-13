#
# spec file for package openmarkup
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


Name:           openmarkup
Version:        1.1
Release:        0
Summary:        Open Markup Interface for object realizers and XML object realization
License:        LGPL-2.1+
Group:          Development/Languages/Java
Url:            https://openmarkup.dev.java.net/
#Source:         om_1_1.zip
Source0:        %{name}-%{version}.tar.bz2
Source1:        AsyncClients.pdf
Source2:        XMLContentHandlers.pdf
Patch0:         openmarkup-1.1-nosource.patch
BuildRequires:  ant
BuildRequires:  fdupes
BuildRequires:  java-devel
BuildArch:      noarch

%description
The Open Markup project defines an open API called Open Markup
Interface for object realizers and XML object realization.

Object realization is a process by which software objects are created,
configured, and processed according to machine-readable descriptions of
those objects. It includes post-instantiation tasks, such as
configuring objects with additional attributes or properties,
connecting them with other objects to create complex object
compositions, or otherwise manipulating them according to control
information embedded in the object descriptions.

%package javadoc
Summary:        Open Markup Interface for object realizers and XML object realization
Group:          Development/Languages/Java

%description javadoc
The Open Markup project defines an open API called Open Markup
Interface for object realizers and XML object realization.

Object realization is a process by which software objects are created,
configured, and processed according to machine-readable descriptions of
those objects. It includes post-instantiation tasks, such as
configuring objects with additional attributes or properties,
connecting them with other objects to create complex object
compositions, or otherwise manipulating them according to control
information embedded in the object descriptions.

%package manual
Summary:        Open Markup Interface for object realizers and XML object realization
Group:          Development/Languages/Java

%description manual
The Open Markup project defines an open API called Open Markup
Interface for object realizers and XML object realization.

Object realization is a process by which software objects are created,
configured, and processed according to machine-readable descriptions of
those objects. It includes post-instantiation tasks, such as
configuring objects with additional attributes or properties,
connecting them with other objects to create complex object
compositions, or otherwise manipulating them according to control
information embedded in the object descriptions.

%prep
%setup -q
cp %{SOURCE1} %{SOURCE2} .
# wrong end of line encoding
sed -i -e 's/.$//' doc/javadoc/stylesheet.css doc/javadoc/package-list Copyright.txt LICENSE.txt
%patch0 -p1

%build
ant \
    -f make/build.xml -Djavaws.dir=%{java_home}/bin \
    -Dant.build.javac.source=1.6 -Dant.build.javac.target=1.6

%install
install -d -m 755 %{buildroot}/%{_javadir}
install -m 644 dist/bin/om.jar %{buildroot}/%{_javadir}
# javadoc
install -d -m 755 %{buildroot}/%{_javadocdir}/%{name}-%{version}
cp -pr doc/javadoc/* %{buildroot}/%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} %{buildroot}/%{_javadocdir}/%{name}
%fdupes -s %{buildroot}/%{_javadocdir}/%{name}

%files
%doc Copyright.txt LICENSE.txt
%{_javadir}/*jar

%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

%files manual
%doc AsyncClients.pdf XMLContentHandlers.pdf

%changelog
