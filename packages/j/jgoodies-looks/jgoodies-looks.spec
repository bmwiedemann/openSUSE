#
# spec file for package jgoodies-looks
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


%define _shortname looks
%define real_ver 2_3_1
Name:           jgoodies-looks
Version:        2.3.1
Release:        0
Summary:        JGoodies Windows l&f and Plastic l&f family
License:        BSD-3-Clause
Group:          Development/Libraries/Java
Url:            http://www.jgoodies.com
Source0:        http://www.jgoodies.com/download/libraries/%{_shortname}/%{_shortname}-%{real_ver}.zip
Source1000:     jgoodies-looks-rpmlintrc
Patch0:         jgoodies-looks-default.properties.patch
BuildRequires:  ant
BuildRequires:  fdupes
BuildRequires:  java-devel
BuildRequires:  javapackages-tools
BuildRequires:  jgoodies-forms >= 1.0.5
BuildRequires:  unzip
BuildRequires:  xml-commons-apis
BuildRequires:  xml-commons-resolver
BuildConflicts: java-devel >= 10
Requires:       jgoodies-forms >= 1.0.5
Requires:       jre >= 1.5
BuildArch:      noarch

%description
The JGoodies Looks make your Swing applications and applets look
better. The package consists of a Windows look&feel and the Plastic
look&feel family.

These have been optimized for readability, precise micro-design and
usability.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Libraries/Java

%description javadoc
The JGoodies Looks make your Swing applications and applets look
better. The package consists of a Windows look&feel and the Plastic
look&feel family.

This package contains a javadoc API documentation

%package manual
Summary:        Documentation for %{name}
Group:          Development/Languages/Java

%description manual
The JGoodies Looks make your Swing applications and applets look
better. The package consists of a Windows look&feel and the Plastic
look&feel family.

This package contains a documentation for %{name}

%package demo
Summary:        JGoodies Windows l&f and Plastic l&f family
Group:          Development/Libraries/Java
Requires:       %{name} = %{version}

%description demo
The JGoodies Looks make your Swing applications and applets look
better. The package consists of a Windows look&feel and the Plastic
look&feel family.

This package contains a demo files for %{name}

%prep
%setup -q -n %{_shortname}-%{version}
%patch0 -p1
mkdir -p src/plastic
mkdir -p src/windows

# remove a third party jars
find BUILD/ -iname '*jar' | xargs rm -rf

# wrong end of line encoding
sed -i -e 's/.$//' LICENSE.txt README.html RELEASE-NOTES.txt
find docs -iname '*.html' -or -iname '*.css' | xargs sed -i -e 's/.$//'

mkdir -p conf/service_descriptors

%build
ant compile jar javadoc

%install
# jars
install -dm 755 %{buildroot}%{_javadir}
install -pm 644 build/%{_shortname}.jar \
	%{buildroot}%{_javadir}/%{_shortname}-%{version}.jar
pushd %{buildroot}%{_javadir}
	for jar in *-%{version}*; do
		ln -sf ${jar} `echo $jar| sed "s|-%{version}||g"`
	done
popd
# javadoc
install -dm 755 %{buildroot}%{_javadocdir}/%{name}
cp -pr build/docs/api/* %{buildroot}%{_javadocdir}/%{name}
%fdupes -s %{buildroot}%{_javadocdir}/%{name}
# demo
install -dm 755 %{buildroot}%{_datadir}/%{name}
install -pm 644 build/demo.jar %{buildroot}%{_datadir}/%{name}
install -pm 644 build/tiny.jar %{buildroot}%{_datadir}/%{name}

%files
%{_javadir}/%{_shortname}*.jar
%doc LICENSE.txt README.html RELEASE-NOTES.txt

%files javadoc
%doc %{_javadocdir}/%{name}

%files manual
%doc docs/examples.html docs/guide/ docs/images/ docs/quickstart.html docs/style.css docs/tips.html

%files demo
%{_datadir}/%{name}

%changelog
