#
# spec file for package jtidy
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


Name:           jtidy
Version:        1.0.4
Release:        0
Summary:        HTML syntax checker and pretty printer
License:        HTMLTIDY
Group:          Development/Libraries/Java
URL:            https://github.com/jtidy/jtidy
Source0:        https://github.com/jtidy/jtidy/archive/refs/tags/jtidy-1.0.4.tar.gz
Source1:        %{name}-build.xml
Source100:      %{name}-rpmlintrc
BuildRequires:  ant >= 1.6
BuildRequires:  ant-junit
BuildRequires:  fdupes
BuildRequires:  javapackages-local >= 6
BuildRequires:  xerces-j2
BuildRequires:  xml-apis
Requires:       xerces-j2
Requires:       xml-apis
BuildArch:      noarch

%description
JTidy is a Java port of HTML Tidy, a HTML syntax checker and pretty
printer. Like its non-Java cousin, JTidy can be used as a tool for
cleaning up malformed and faulty HTML. In addition, JTidy provides a
DOM parser for real-world HTML.

%package javadoc
Summary:        HTML syntax checker and pretty printer
Group:          Development/Libraries/Java

%description javadoc
JTidy is a Java port of HTML Tidy, a HTML syntax checker and pretty
printer. Like its non-Java cousin, JTidy can be used as a tool for
cleaning up malformed and faulty HTML. In addition, JTidy provides a
DOM parser for real-world HTML.

%package scripts
Summary:        HTML syntax checker and pretty printer
Group:          Development/Libraries/Java
Requires:       %{name} = %{version}
Requires:       javapackages-tools

%description scripts
JTidy is a Java port of HTML Tidy, a HTML syntax checker and pretty
printer. Like its non-Java cousin, JTidy can be used as a tool for
cleaning up malformed and faulty HTML. In addition, JTidy provides a
DOM parser for real-world HTML.

%prep
%setup -q -n %{name}-%{name}-%{version}
cp -p %{SOURCE1} build.xml

%build
mkdir -p lib
build-jar-repository -s lib xerces-j2 xml-apis
%{ant} \
    package javadoc

%install

# jar
install -d -m 0755 %{buildroot}%{_javadir}
install -m 644 target/%{name}-%{version}.jar %{buildroot}%{_javadir}/%{name}.jar

# pom
install -d -m 755 %{buildroot}%{_mavenpomdir}
%{mvn_install_pom} pom.xml %{buildroot}%{_mavenpomdir}/%{name}.pom
%add_maven_depmap %{name}.pom %{name}.jar -a net.sf.jtidy:%{name}

# javadoc
install -d -m 0755 %{buildroot}%{_javadocdir}/%{name}
cp -aL target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}
%fdupes -s %{buildroot}%{_javadocdir}/%{name}

# shell script
%jpackage_script org.w3c.tidy.Tidy "" "" %{name}:xerces-j2:xml-apis %{name} true

# ant.d
install -d -m 0755 %{buildroot}%{_sysconfdir}/ant.d
cat > %{buildroot}%{_sysconfdir}/ant.d/%{name} << EOF
jtidy xerces-j2 xml-apis
EOF

%files -f .mfiles
%license LICENSE.txt
%{_javadir}/%{name}.jar
%config(noreplace) %{_sysconfdir}/ant.d/%{name}

%files javadoc
%defattr(0644,root,root,0755)
%doc %{_javadocdir}/%{name}

%files scripts
%defattr(0755,root,root,0755)
%{_bindir}/*

%changelog
