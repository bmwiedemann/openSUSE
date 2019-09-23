#
# spec file for package jgoodies-forms
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


%define _shortname	forms
%define tar_ver 1_3_0
Name:           jgoodies-forms
Version:        1.3.0
Release:        0
Summary:        JGoodies Forms framework
License:        BSD-3-Clause
Group:          Development/Languages/Java
URL:            http://jgoodies.com
Source0:        http://www.jgoodies.com/download/libraries/%{_shortname}/%{_shortname}-%{tar_ver}.zip
BuildRequires:  ant
BuildRequires:  fdupes
BuildRequires:  java-devel
BuildRequires:  jpackage-utils
BuildRequires:  unzip
BuildRequires:  xml-commons-apis
BuildRequires:  xml-commons-resolver
Requires:       jre >= 1.5
BuildArch:      noarch

%description
The Forms framework helps you lay out and implement elegant Swing
panels quickly and consistently. It makes simple things easy and the
hard stuff possible, the good design easy and the bad difficult.

Main Benefits: * Powerful, flexible and precise layout

* Easy to work with and quite easy to learn

* Faster UI production

* Better UI code readability

* Leads to better style guide compliance

%package javadoc
Summary:        Javadoc for JGoodies Forms framework
# FIXME: use proper Requires(pre/post/preun/...)
# FIXME: use proper Requires(pre/post/preun/...)
# FIXME: use proper Requires(pre/post/preun/...)
Group:          Development/Languages/Java
PreReq:         coreutils

%description javadoc
The Forms framework helps you lay out and implement elegant Swing
panels quickly and consistently. It makes simple things easy and the
hard stuff possible, the good design easy and the bad difficult.

Main Benefits: * Powerful, flexible and precise layout

* Easy to work with and quite easy to learn

* Faster UI production

* Better UI code readability

* Leads to better style guide compliance

%package manual
Summary:        Documentation for JGoodies Forms framework
Group:          Development/Languages/Java

%description manual
The Forms framework helps you lay out and implement elegant Swing
panels quickly and consistently. It makes simple things easy and the
hard stuff possible, the good design easy and the bad difficult.

Main Benefits: * Powerful, flexible and precise layout

* Easy to work with and quite easy to learn

* Faster UI production

* Better UI code readability

* Leads to better style guide compliance

%package demo
Summary:        Demo files for JGoodies Forms framework
Group:          Development/Languages/Java
Requires:       %{name} = %{version}

%description demo
The Forms framework helps you lay out and implement elegant Swing
panels quickly and consistently. It makes simple things easy and the
hard stuff possible, the good design easy and the bad difficult.

Main Benefits: * Powerful, flexible and precise layout

* Easy to work with and quite easy to learn

* Faster UI production

* Better UI code readability

* Leads to better style guide compliance

%prep
%setup -q -n %{_shortname}-%{version}
# clean up some files
rm -f %{_shortname}-%{version}.jar
# wrong end of line encoding and rigths
sed -i -e 's/.$//' LICENSE.txt README.html RELEASE-NOTES.txt
find docs -iname '*.html' -or -iname '*.css' | xargs sed -i -e 's/.$//'

%build
unset CLASSPATH
export CLASSPATH=%{java_home}/jre/lib/rt.jar
%{ant} \
    -Dbuild.compile.source=1.6 -Dbuild.compile.target=1.6 \
    compile jar javadoc

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
cp -pr src/tutorial/* %{buildroot}%{_datadir}/%{name}
cp -pr build/classes/tutorial/* %{buildroot}%{_datadir}/%{name}
%fdupes -s %{buildroot}%{_datadir}/%{name}
cat > %{name}.sh << EOF
#!/bin/bash
cd %{_datadir}/%{name}
java -cp .:%{_javadir}/forms.jar \
	com/jgoodies/forms/tutorial/QuickStartExample
EOF
install -dm 755 %{buildroot}%{_bindir}
install -m 755 %{name}.sh \
	%{buildroot}%{_bindir}

# PACKAGE list of authors in an AUTHORS text file
cat > AUTHORS << EOF
Karsten Lentzsch
EOF

%files
%license LICENSE.txt
%doc AUTHORS README.html RELEASE-NOTES.txt
%{_javadir}/%{_shortname}*.jar

%files javadoc
%doc %{_javadocdir}/%{name}

%files manual
%doc docs/references.html
%doc docs/tips.html
%doc docs/visualbuilders.html
%doc docs/*.pdf
%doc docs/style.css
%doc docs/reference
%doc docs/images/

%files demo
%license LICENSE.txt
%doc README.html RELEASE-NOTES.txt
%doc docs/tutorial
%{_datadir}/%{name}
%defattr(755,root,root,755)
%{_bindir}/%{name}.sh

%changelog
