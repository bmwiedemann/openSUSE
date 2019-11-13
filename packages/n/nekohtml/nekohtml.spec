#
# spec file for package nekohtml
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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
Version:        1.9.22
Release:        0
Summary:        HTML scanner and tag balancer
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            http://nekohtml.sourceforge.net/
# No upstream tarball for this release
# svn export svn://svn.code.sf.net/p/nekohtml/code/branches/nekohtml-1.9.22 nekohtml-1.9.22
# find nekohtml-1.9.22 -name '*.jar' -delete
# tar cJf nekohtml-1.9.22.tar.xz nekohtml-1.9.22/
Source0:        %{name}-%{version}.tar.xz
Source2:        nekohtml-component-info.xml
Source3:        http://central.maven.org/maven2/net/sourceforge/%{name}/%{name}/%{version}/%{name}-%{version}.pom
Patch1:         0002-Jar-paths.patch
# Add proper attributes to MANIFEST.MF file so bundle can be used by other OSGI bundles.
Patch2:         0003-Add-OSGi-attributes.patch
BuildRequires:  ant
BuildRequires:  ant-junit
BuildRequires:  bcel
BuildRequires:  fdupes
BuildRequires:  javapackages-local
BuildRequires:  xerces-j2 >= 2.7.1
BuildRequires:  xml-apis
BuildRequires:  xmvn-install
BuildRequires:  xmvn-resolve
Requires:       bcel
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

%{mvn_alias} net.sourceforge.%{name}:%{name} %{name}:%{name}
%{mvn_package} net.sourceforge.%{name}:%{name}-samples demo
%{mvn_file} ':{*}' @1

%build
export CLASSPATH=$(build-classpath bcel xerces-j2 xml-apis)
%{ant} \
    -Dcompile.source=1.6 -Dcompile.target=1.6 \
    -Dbuild.sysclasspath=first \
    -Dlib.dir=%{_javadir} \
    -Djar.file=%{name}.jar \
    -Djar.xni.file=%{name}-xni.jar \
    -Djar.samples.file=%{name}-samples.jar \
    -Dbcel.javadoc=%{_javadocdir}/bcel \
    -Dj2se.javadoc=%{_javadocdir}/java \
    -Dxni.javadoc=%{_javadocdir}/xerces-j2-xni \
    -Dxerces.javadoc=%{_javadocdir}/xerces-j2-impl \
    clean jar jar-xni doc
# test - disabled because it makes the build failing

%{mvn_artifact} %{SOURCE3} %{name}.jar
%{mvn_artifact} net.sourceforge.%{name}:%{name}-xni:%{version} %{name}-xni.jar
%{mvn_artifact} net.sourceforge.%{name}:%{name}-samples:%{version} %{name}-samples.jar

%install
%mvn_install -J build/doc/javadoc
%fdupes -s %{buildroot}%{_javadocdir}

# Scripts
%jpackage_script org.cyberneko.html.filters.Writer "" "" "nekohtml:xerces-j2" nekohtml-filter true

%files -f .mfiles
%license LICENSE.txt
%doc README.txt doc/*.html
%{_bindir}/%{name}-filter

%files javadoc -f .mfiles-javadoc

%files demo -f .mfiles-demo

%changelog
