#
# spec file for package jcsp
#
# Copyright (c) 2019 SUSE LLC
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


%global base_version 1.1
%global namedreltag rc5
%global namedversion %{base_version}-%{namedreltag}
Name:           jcsp
Version:        %{base_version}~%{namedreltag}
Release:        0
Summary:        Communicating Sequential Processes for Java (JCSP)
License:        LGPL-2.1-or-later
Group:          Development/Libraries/Java
URL:            https://github.com/codehaus/jcsp
# sh jcsp-create-tarball.sh < VERSION-TAG >
Source0:        %{name}-%{namedversion}-clean.tar.xz
Source1:        %{name}-create-tarball.sh
BuildRequires:  fdupes
BuildRequires:  maven-local
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.osgi:osgi.core)
BuildArch:      noarch

%description
JCSP (Communication Sequential Processes for Java) is a
library providing a concurrency model that is a combination
of ideas from Hoare's CSP and Milner's pi-calculus.

Communicating Sequential Processes (CSP) is a mathematical
theory for specifying and verifying complex patterns of
behavior arising from interactions between concurrent
objects.

JCSP provides a base range of CSP primitives plus a rich set of
extensions. Also included is a package providing CSP process
wrappers giving a channel interface to all Java AWT widgets
and graphics operations.  It is extensively (java/documented)
and includes much teaching.

JCSP is an alternative concurrency model to the threads and
mechanisms built into Java. It is also compatible with
it since it is implemented on top of it.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Documentation/HTML

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{name}-%{namedversion}

%pom_remove_plugin :cobertura-maven-plugin
%pom_remove_plugin :findbugs-maven-plugin
%pom_remove_plugin :jdepend-maven-plugin
%pom_remove_plugin :rat-maven-plugin
%pom_remove_plugin :taglist-maven-plugin

# Use modern osgi implementation
%pom_change_dep :org.osgi.core org.osgi:osgi.core

# remove wagon-webdav
%pom_xpath_remove "pom:project/pom:build/pom:extensions"
# fix resouce directory and filter these ones
%pom_xpath_inject "pom:project/pom:build" "
<resources>
  <resource>
    <directory>src</directory>
    <excludes>
      <exclude>**/*.java</exclude>
      <exclude>**/doc-files/**</exclude>
      <exclude>**/win32/*Services.txt</exclude>
      <exclude>**/package.html</exclude>
    </excludes>
  </resource>
</resources>"

%pom_xpath_remove "pom:project/pom:reporting/pom:plugins/pom:plugin[pom:artifactId='maven-javadoc-plugin']/pom:configuration/pom:excludePackageNames"

%pom_xpath_remove "pom:project/pom:build/pom:plugins/pom:plugin[pom:artifactId='maven-bundle-plugin']/pom:configuration/pom:instructions/pom:Export-Package"
%pom_xpath_inject "pom:project/pom:build/pom:plugins/pom:plugin[pom:artifactId='maven-bundle-plugin']/pom:configuration/pom:instructions" '
<Export-Package>org.jcsp.*;version="${project.version}"</Export-Package>'

%pom_xpath_set "pom:project/pom:build/pom:plugins/pom:plugin[pom:artifactId='maven-compiler-plugin']/pom:configuration/pom:source" 6
%pom_xpath_set "pom:project/pom:build/pom:plugins/pom:plugin[pom:artifactId='maven-compiler-plugin']/pom:configuration/pom:target" 6

%pom_xpath_set "pom:project/pom:reporting/pom:plugins/pom:plugin[pom:artifactId='maven-javadoc-plugin']/pom:configuration/pom:source" 6

rm -f src/org/jcsp/test/TestExtendedRendezvous.java

sed -i 's|${name}|${project.name}|' pom.xml

sed -i "s|59 Temple Place, Suite 330, Boston, MA 02111-1307 USA|51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA|" pom.xml

for d in LICENCE README ; do
  iconv -f iso8859-1 -t utf-8 $d.txt > $d.txt.conv && mv -f $d.txt.conv $d.txt
  sed -i 's/\r//' $d.txt
done

rm -r src/org/jcsp/win32 \
 src/org/jcsp/net/remote/SpawnerServiceNT.java \
 src/org/jcsp/net/tcpip/TCPIPCNSServerNT.java

%{mvn_file} : %{name}

%build

%{mvn_build} -f -- -Dproject.build.sourceEncoding=UTF-8 \
%if %{?pkg_vcmp:%pkg_vcmp java-devel >= 9}%{!?pkg_vcmp:0}
	-Dmaven.compiler.release=6
%endif

%install
%mvn_install
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%doc README.txt
%license LICENCE.txt

%files javadoc -f .mfiles-javadoc
%license LICENCE.txt

%changelog
