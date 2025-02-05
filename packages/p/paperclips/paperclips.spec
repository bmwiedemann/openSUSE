#
# spec file for package paperclips
#
# Copyright (c) 2025 SUSE LLC
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


Name:           paperclips
Version:        1.0.4
Release:        0
Summary:        Simplified Java Printing Support for SWT
License:        EPL-1.0
Group:          Development/Languages/Java
URL:            https://code.google.com/archive/p/swt-paperclips/
# The link is broken
#Source:         https://swt-paperclips.googlecode.com/files/net.sf.paperclips.source_%{version}.200908120926.jar
Source:         net.sf.paperclips.source_%{version}.200908120926.jar
Patch0:         paperclips-1.0.4-javadoc.patch
BuildRequires:  ant
BuildRequires:  eclipse-swt
BuildRequires:  fdupes
BuildRequires:  java-devel >= 1.8
BuildRequires:  javapackages-tools
BuildRequires:  unzip
BuildArch:      noarch

%description
A simple, light weight, extensible Java printing plug-in for SWT.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Libraries/Java

%description javadoc
Simple, light weight, extensible Java printing plug-in for SWT. PaperClips
hides the complexity of laying out and rendering documents on the printer,
helping you focus on what to print instead of how to print it.

In a nutshell, PaperClips provides an assortment of document "building
blocks," which you can tweak and combine to form a custom document. The
assembled document is then sent to PaperClips for printing. PaperClips
includes support for printing text, images, borders, headers and footers,
column layouts and grid layouts, to name a few. It can also be extended with
your own printable classes.

With PaperClips you do not have to track cursors, calculate line breaking,
fool around with font metrics, or manage system resources--it's all handled
internally. And unlike report-generation tools, you are not constrained to a
predefined document structure (like report bands). Every document is custom
and the layout is up to you.

%prep
%setup -q -c %{name}-%{version}
%patch -P 0 -p1

%build
export CLASSPATH=$(find-jar swt)

pushd src
  javac -source 1.8 -target 1.8 -g -encoding UTF-8 $(find . -type f -name "*.java")
  jarfile="../net.sf.paperclips_%{version}.jar"
  files="$(find . -type f \( -name '*.class' -o -name '*.properties' \))"
  test ! -d classes && mf="" \
    || mf="`find classes/ -type f -name "*.mf" 2>/dev/null`"
  test -n "$mf" && jar cvfm $jarfile $mf $files \
    || jar --create --verbose \
%if %{?pkg_vcmp:%pkg_vcmp java-devel >= 17}%{!?pkg_vcmp:0}
        --date="$(date -u -d @${SOURCE_DATE_EPOCH:-$(date +%%s)} +%%Y-%%m-%%dT%%H:%%M:%%SZ)" \
%endif
        --file=$jarfile $files
popd

%{ant} \
      -f gen_javadoc.xml \
	  -Dant.build.javac.source=1.8 -Dswt.jar=$(build-classpath swt)

%install
mkdir -p %{buildroot}%{_javadir}
install net.sf.paperclips_%{version}.jar %{buildroot}%{_javadir}

mkdir -p %{buildroot}%{_javadocdir}/%{name}-%{version}
cp -r api/* %{buildroot}%{_javadocdir}/%{name}-%{version}
%fdupes -s %{buildroot}%{_javadocdir}/%{name}-%{version}

%files
%{_javadir}/net.sf.paperclips_%{version}.jar

%files javadoc
%{_javadocdir}/%{name}-%{version}

%changelog
