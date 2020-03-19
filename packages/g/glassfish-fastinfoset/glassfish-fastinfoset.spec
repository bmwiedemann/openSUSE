#
# spec file for package glassfish-fastinfoset
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


Name:           glassfish-fastinfoset
Version:        1.2.15
Release:        0
Summary:        Fast Infoset
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            https://fi.java.net
Source0:        https://github.com/javaee/metro-fi/archive/%{version}-RELEASE.tar.gz
# add xmlstreambuffer 1.5.x support
Patch0:         %{name}-1.2.12-utilities-FastInfosetWriterSAXBufferProcessor.patch
BuildRequires:  fdupes
BuildRequires:  java-devel >= 9
BuildRequires:  maven-local
BuildRequires:  mvn(com.sun.xml.stream.buffer:streambuffer)
BuildRequires:  mvn(com.sun.xsom:xsom)
BuildRequires:  mvn(net.java:jvnet-parent:pom:)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildArch:      noarch

%description
Fast Infoset specifies a standardized binary encoding for the XML Information
Set. An XML infoset (such as a DOM tree, StAX events or SAX events in
programmatic representations) may be serialized to an XML 1.x document or, as
specified by the Fast Infoset standard, may be serialized to a fast infoset
document.  Fast infoset documents are generally smaller in size and faster to
parse and serialize than equivalent XML documents.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Documentation/HTML

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n metro-fi-%{version}-RELEASE
%patch0

pushd code

# Remove wagon-webdav
%pom_xpath_remove "pom:build/pom:extensions"

%pom_remove_plugin :findbugs-maven-plugin
%pom_remove_plugin :maven-antrun-extended-plugin
#%pom_remove_plugin org.sonatype.plugins:nexus-staging-maven-plugin
%pom_remove_plugin org.codehaus.mojo:buildnumber-maven-plugin
%pom_remove_plugin :maven-javadoc-plugin

%pom_disable_module roundtrip-tests
%pom_disable_module samples

# Disable default-jar execution of maven-jar-plugin, which is causing
# problems with version 3.0.0 of the plugin.
%pom_xpath_inject "pom:plugin[pom:artifactId='maven-jar-plugin']/pom:executions" "
 <execution>
  <id>default-jar</id>
  <phase>skip</phase>
 </execution>" fastinfoset

%{mvn_file} :FastInfoset %{name}
%{mvn_file} :FastInfosetUtilities %{name}-utilities
popd

%build
pushd code
%{mvn_build} -f -j
popd

%install
pushd code
%mvn_install
%fdupes -s %{buildroot}%{_javadocdir}
popd

%files -f code/.mfiles
%license code/copyright.txt LICENSE

%if 0
%files javadoc -f code/.mfiles-javadoc
%license code/copyright.txt LICENSE
%endif

%changelog
