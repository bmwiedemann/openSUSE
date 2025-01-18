#
# spec file for package jarjar
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


%define section free
Name:           jarjar
Version:        1.4
Release:        0
Summary:        Tool to repackage Java libraries
License:        GPL-2.0-or-later
Group:          Development/Libraries/Java
URL:            http://tonicsystems.com/products/jarjar/
Source0:        https://storage.googleapis.com/google-code-archive-downloads/v2/code.google.com/%{name}/%{name}-src-%{version}.zip
Source1:        jarjar.pom
Source2:        jarjar-util.pom
Patch0:         do-not-embed-asm.patch
Patch1:         jarjar-1.4-asm5.patch
BuildRequires:  ant >= 1.6
BuildRequires:  ant-junit >= 1.6
BuildRequires:  fdupes
BuildRequires:  java-devel >= 1.8
BuildRequires:  javapackages-local
BuildRequires:  junit
BuildRequires:  objectweb-asm >= 5
BuildRequires:  unzip
Requires:       gnu-regexp
Requires:       objectweb-anttask
Requires:       objectweb-asm >= 5
Requires(post): javapackages-tools
Requires(postun): javapackages-tools
BuildArch:      noarch

%description
Jar Jar Links is a utility that makes it easy to repackage Java
libraries and embed them into your own distribution. This is useful for
two reasons: You can easily ship a single jar file with no external
dependencies. You can avoid problems where your library depends on a
specific version of a library, which may conflict with the dependencies
of another library.

%package javadoc
Summary:        Tool to repackage Java libraries
Group:          Development/Libraries/Java

%description javadoc
Jar Jar Links is a utility that repackages Java libraries and embeds
them into a distribution of its own. This is useful for two reasons:
You can easily ship a single jar file with no external dependencies.
You can avoid problems where your library depends on a specific
version of a library, which may conflict with the dependencies of
another library.

%prep
%setup -q
%patch -P 0
%patch -P 1 -p1
# remove all binary libs
rm -f lib/*.jar
# maven plugin
find . -name JarJarMojo.java -delete

%build
pushd lib
ln -sf $(build-classpath objectweb-asm/asm) asm-4.0.jar
ln -sf $(build-classpath objectweb-asm/asm-commons) asm-commons-4.0.jar
ln -sf $(build-classpath ant) ant.jar
popd
export OPT_JAR_LIST="ant/ant-junit junit"
%{ant} \
    -Dcompile.source=8 -Dcompile.target=8 \
    jar jar-util javadoc

%install
# jars
install -dm 0755 %{buildroot}%{_javadir}
install -pm 0644 dist/%{name}-%{version}.jar \
  %{buildroot}%{_javadir}/%{name}.jar
install -pm 0644 dist/%{name}-util-%{version}.jar \
  %{buildroot}%{_javadir}/%{name}-util.jar

# poms
install -dm 0755 %{buildroot}/%{_mavenpomdir}
%{mvn_install_pom} %{SOURCE1} \
  %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom
%{mvn_install_pom} %{SOURCE2} \
  %{buildroot}%{_mavenpomdir}/JPP-%{name}-util.pom

# depmaps
%add_maven_depmap JPP-%{name}.pom %{name}.jar -a "jarjar:%{name},com.tonicsystems:%{name},com.googlecode.jarjar:%{name},org.gradle.jarjar:%{name}"
%add_maven_depmap JPP-%{name}-util.pom %{name}-util.jar -a "jarjar:%{name}-util,com.tonicsystems:%{name}-util"

# ant config
install -dm 0755 %{buildroot}%{_sysconfdir}/ant.d
echo %{name} %{name} objectweb-asm/asm{,-commons} > %{buildroot}%{_sysconfdir}/ant.d/%{name}

# javadoc
mkdir -p %{buildroot}%{_javadocdir}/%{name}
cp -pr dist/javadoc/* %{buildroot}%{_javadocdir}/%{name}
%fdupes -s %{buildroot}%{_javadocdir}/%{name}

%files -f .mfiles
%config(noreplace) %{_sysconfdir}/ant.d/%{name}
%license COPYING

%files javadoc
%{_javadocdir}/%{name}

%changelog
