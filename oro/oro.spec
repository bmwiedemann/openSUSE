#
# spec file for package oro
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define full_name	jakarta-%{name}
Name:           oro
Version:        2.0.8
Release:        0
Summary:        Full regular expressions API
License:        Apache-2.0
Group:          Development/Libraries/Java
Url:            http://jakarta.apache.org/oro/
Source0:        http://archive.apache.org/dist/jakarta/oro/%{full_name}-%{version}.tar.gz
Source1:        http://repo1.maven.org/maven2/%{name}/%{name}/%{version}/%{name}-%{version}.pom
BuildRequires:  ant
BuildRequires:  fdupes
BuildRequires:  javapackages-local
BuildRequires:  xml-commons-apis
Provides:       %{full_name} = %{version}-%{release}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
The Jakarta-ORO Java classes are a set of text-processing Java classes
that provide Perl5 compatible regular expressions, AWK-like regular
expressions, glob expressions, and utility classes for performing
substitutions, splits, filtering filenames, etc. This library is the
successor to the OROMatcher, AwkTools, PerlTools, and TextTools
libraries from ORO, Inc. (www.oroinc.com). They have been donated to
the Jakarta Project by Daniel Savarese (www.savarese.org), the
copyright holder of the ORO libraries. Daniel will continue to
participate in their development under the Jakarta Project.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Libraries/Java

%description javadoc
Javadoc for %{name}.

%prep
%setup -q -n %{full_name}-%{version}
# remove all binary libs
find . -name "*.jar" -exec rm -f {} \;
# remove all CVS files
for dir in `find . -type d -name CVS`; do rm -rf $dir; done
for file in `find . -type f -name .cvsignore`; do rm -rf $file; done

%build
ant \
	-Dant.build.javac.source=1.6 -Dant.build.javac.target=1.6 \
	-Dfinal.name=%{name} jar javadocs

%install
# jar
install -dm 0755 %{buildroot}%{_javadir}
install -pm 0644 %{name}.jar %{buildroot}%{_javadir}/
ln -sf %{name}.jar %{buildroot}%{_javadir}/%{full_name}.jar
# pom
install -dm 0755 %{buildroot}%{_mavenpomdir}
install -pm 0644 %{SOURCE1} %{buildroot}%{_mavenpomdir}/%{name}.pom
%add_maven_depmap %{name}.pom %{name}.jar
# javadoc
install -dm 0755 %{buildroot}%{_javadocdir}/%{name}
cp -pr docs/api/* %{buildroot}%{_javadocdir}/%{name}/
%fdupes %{buildroot}%{_javadocdir}

%files -f .mfiles
%doc COMPILE ISSUES README TODO CHANGES CONTRIBUTORS STYLE
%license LICENSE
%{_javadir}/%{full_name}.jar

%files javadoc
%license LICENSE
%{_javadocdir}/%{name}

%changelog
