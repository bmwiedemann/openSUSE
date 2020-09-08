#
# spec file for package javapackages-tools
#
# Copyright (c) 2020 SUSE LLC
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


%{!?_rpmmacrodir:%global _rpmmacrodir %{_rpmconfigdir}/macros.d}
%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "extras"
%bcond_without python
%else
%bcond_with python
%endif
%if %{with python}
Name:           javapackages-tools-%{flavor}
%else
Name:           javapackages-tools
%endif
Version:        5.3.1
Release:        0
Summary:        Macros and scripts for Java packaging support
License:        BSD-3-Clause
Group:          Development/Languages/Java
URL:            https://github.com/fedora-java/javapackages
Source0:        https://github.com/fedora-java/javapackages/archive/%{version}.tar.gz
#PATCH-FIX-SUSE: SUSE does store jvm related things in libdir - ie /usr/lib64 on 64bits
#                where Fedora use jpackage convention - usr/lib everywhere
Patch0:         suse-use-libdir.patch
#PATCH-FIX-SUSE: allow building without python to reduce depgraph
Patch1:         python-optional.patch
#PATCH-FIX-SUSE: SUSE did not bump epoch of openjdk packages, whereas Fedora did
#               Avoid generating unresolvable requires
Patch2:         suse-no-epoch.patch
BuildRequires:  asciidoc
BuildRequires:  fdupes
BuildRequires:  perl
BuildRequires:  rpm
BuildRequires:  xmlto
%if %{with python}
BuildRequires:  javapackages-filesystem
%else
Requires:       javapackages-filesystem = %{version}-%{release}
%endif
# Used on too many places
Provides:       jpackage-utils = %{version}
Obsoletes:      %{name}-doc
Obsoletes:      jpackage-utils < %{version}
%if %{with python}
BuildRequires:  python3-lxml
BuildRequires:  python3-nose
BuildRequires:  python3-setuptools
BuildRequires:  python3-six
BuildArch:      noarch
%else
Provides:       mvn(com.sun:tools) = SYSTEM
Provides:       mvn(sun.jdk:jconsole) = SYSTEM
%endif

%description
This package provides macros and scripts to support Java packaging.

%package -n javapackages-filesystem
Summary:        Java packages filesystem layout
Group:          Development/Languages/Java

%description -n javapackages-filesystem
This package provides some basic directories into which Java packages
install their content.

%if %{with python}
%package -n javapackages-gradle
Summary:        Local mode for Gradle (files)
Group:          Development/Languages/Java
Requires:       javapackages-local = %{version}
Requires:       javapackages-tools = %{version}

%description -n javapackages-gradle
This package contains files needed by local mode for Gradle, which
allows artifact resolution using XMvn resolver.


%package -n javapackages-ivy
Summary:        Local mode for Apache Ivy (files)
Group:          Development/Languages/Java
Requires:       javapackages-local = %{version}
Requires:       javapackages-tools = %{version}

%description -n javapackages-ivy
This package contains files needed by local mode fow Apache Ivy, which
allows artifact resolution using XMvn resolver.

%package -n python3-javapackages
Summary:        Module for handling various files for Java packaging
Group:          Development/Languages/Java
Requires:       python3-lxml
Requires:       python3-six
Obsoletes:      python-javapackages < %{version}-%{release}
Provides:       python-javapackages = %{version}-%{release}

%description -n python3-javapackages
Module for handling, querying and manipulating of various files for Java
packaging in Linux distributions

%package -n javapackages-local
Summary:        Non-essential macros and scripts for Java packaging support
Group:          Development/Languages/Java
Requires:       java-devel
Requires:       javapackages-tools = %{version}
Requires:       python3-javapackages = %{version}

%description -n javapackages-local
This package provides non-essential macros and scripts to support Java packaging.
%endif

%prep
%setup -q -n javapackages-%{version}
%autopatch -p1

# The usr/lib is hardcoded in configuration files too
new_dir=$(echo %{_libdir} | sed 's#/##')
perl -pi -e "s#usr/lib#${new_dir}#g" configs/*.xml

%build
%configure \
%if %{with python}
    --pyinterpreter=%{_bindir}/python3
%else
    --pyinterpreter=%{nil}
%endif
./build
%if %{with python}
pushd python
python3 setup.py build
popd
%endif

%install
./install
sed -e 's/.[17]$/&.gz/' -e 's/.py$/&*/' -i files-*

%if %{with python}
pushd python
python3 setup.py install --root %{buildroot}
popd
# kill all the common files
files="
%{_bindir}/build-classpath
%{_bindir}/build-classpath-directory
%{_bindir}/build-jar-repository
%{_bindir}/check-binary-files
%{_bindir}/clean-binary-files
%{_bindir}/create-jar-links
%{_bindir}/diff-jars
%{_bindir}/find-jar
%{_bindir}/rebuild-jar-repository
%{_bindir}/shade-jar
%{_sysconfdir}/java/font.properties
%{_sysconfdir}/java/java.conf
%{_sysconfdir}/java/eclipse.conf
%{_datadir}/java-utils/java-functions
%{_datadir}/java-utils/java-wrapper
%{_datadir}/java-utils/scl-enable
%{_rpmmacrodir}/macros.jpackage
%{_rpmmacrodir}/macros.javapackages-filesystem
%{_mandir}/man1/build-classpath.1
%{_mandir}/man1/build-jar-repository.1
%{_mandir}/man1/diff-jars.1
%{_mandir}/man1/rebuild-jar-repository.1
%{_mandir}/man1/shade-jar.1
%{_mandir}/man1/find-jar.1
%{_datadir}/maven-metadata/javapackages-metadata.xml
%{_datadir}/xmvn/configuration.xml
"
for i in $files; do
    rm -rf %{buildroot}/$i
done
%endif

rm -rf %{buildroot}%{_datadir}/fedora-review/

%fdupes %{buildroot}/%{_prefix}

%check
./check

%if !%{with python}
%files -f files-tools
%license LICENSE

%files -n javapackages-filesystem -f files-filesystem

%else
%files -n javapackages-local -f files-local
%dir %{_datadir}/java-utils

%files -n javapackages-gradle -f files-gradle
%dir %{_datadir}/gradle-local

%files -n javapackages-ivy -f files-ivy
%dir %{_sysconfdir}/ant.d

%files -n python3-javapackages
%license LICENSE
%{python3_sitelib}/javapackages*
%endif

%changelog
