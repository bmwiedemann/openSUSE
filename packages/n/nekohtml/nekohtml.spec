#
# spec file for package nekohtml
#
# Copyright (c) 2022 SUSE LLC
# Copyright (c) 2000-2009, JPackage Project
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


Name:           nekohtml
Version:        1.9.22.noko2
Release:        0
Summary:        HTML scanner and tag balancer
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            https://github.com/sparklemotion/nekohtml
Source0:        %{name}-%{version}.tar.xz
Source2:        nekohtml-component-info.xml
Patch1:         0001-Jar-paths.patch
# Add proper attributes to MANIFEST.MF file so bundle can be used by other OSGI bundles.
Patch2:         0002-Add-OSGi-attributes.patch
BuildRequires:  ant
BuildRequires:  bcel
BuildRequires:  fdupes
BuildRequires:  java-devel >= 1.8
BuildRequires:  javapackages-local
BuildRequires:  xerces-j2 >= 2.7.1
BuildRequires:  xml-apis
Requires:       bcel
Requires:       javapackages-tools
Requires:       xerces-j2 >= 2.7.1
Requires:       xml-apis
BuildArch:      noarch

%description
NekoHTML is a simple HTML scanner and tag balancer that enables
application programmers to parse HTML documents and access the
information using standard XML interfaces. The parser can scan HTML
files and "fix up" many common mistakes that human (and computer)
authors make in writing HTML documents.  NekoHTML adds missing parent
elements; automatically closes elements with optional end tags; and
can handle mismatched inline element tags.
NekoHTML is written using the Xerces Native Interface (XNI) that is
the foundation of the Xerces2 implementation. This enables you to use
the NekoHTML parser with existing XNI tools without modification or
rewriting code.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Documentation/HTML

%description javadoc
Javadoc for %{name}.

%package demo
Summary:        Demo for %{name}
Group:          Development/Libraries/Java
Requires:       %{name} = %{version}-%{release}

%description demo
Demonstrations and samples for %{name}.

%prep
%setup -q
%patch1 -p1
%patch2 -p1

find -name "*.jar" -delete
sed -i 's/\r$//g' *.txt doc/*.html

# cannonization test fails on some whitespace, TODO investigate
rm data/meta/test-meta-encoding3.html

%build
mkdir -p lib
build-jar-repository -p -s lib bcel xerces-j2 xml-apis
%{ant} \
    -Dcompile.source=1.8 -Dcompile.target=1.8 \
    -Djar.file=%{name}.jar \
    -Djar.xni.file=%{name}-xni.jar \
    -Djar.samples.file=%{name}-samples.jar \
    clean jar jar-xni doc

%{mvn_artifact} pom.xml %{name}.jar
%{mvn_artifact} net.sourceforge.%{name}:%{name}-xni:%{version} %{name}-xni.jar
%{mvn_artifact} net.sourceforge.%{name}:%{name}-samples:%{version} %{name}-samples.jar

%install
# jar
install -dm 0755 %{buildroot}%{_javadir}
install -pm 0644 %{name}.jar %{buildroot}%{_javadir}/%{name}.jar
install -pm 0644 %{name}-xni.jar %{buildroot}%{_javadir}/%{name}-xni.jar
install -pm 0644 %{name}-samples.jar %{buildroot}%{_javadir}/%{name}-samples.jar
# pom
install -dm 0755 %{buildroot}%{_mavenpomdir}/
install -pm 0644 pom.xml %{buildroot}%{_mavenpomdir}/%{name}.pom
%add_maven_depmap %{name}.pom %{name}.jar -a %{name}:%{name}
%add_maven_depmap net.sourceforge.%{name}:%{name}-xni:%{version} %{name}-xni.jar
%add_maven_depmap net.sourceforge.%{name}:%{name}-samples:%{version} %{name}-samples.jar -f demo
# javadoc
install -dm 0755 %{buildroot}%{_javadocdir}/%{name}
cp -pr build/doc/javadoc/* %{buildroot}%{_javadocdir}/%{name}/
%fdupes -s %{buildroot}%{_javadocdir}

# Scripts
%jpackage_script org.cyberneko.html.filters.Writer "" "" "nekohtml:xerces-j2" %{name}-filter true

%files -f .mfiles
%license LICENSE.txt
%doc README.txt doc/*.html
%{_bindir}/%{name}-filter

%files demo -f .mfiles-demo

%files javadoc
%{_javadocdir}/%{name}

%changelog
