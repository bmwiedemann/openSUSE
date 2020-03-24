#
# spec file for package log4j12
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


%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "bootstrap"
%bcond_without bootstrap
%else
%bcond_with bootstrap
%endif
%define real log4j12
Version:        1.2.17
Release:        0
Summary:        Java logging tool
License:        Apache-2.0
URL:            https://logging.apache.org/log4j/
Source0:        http://www.apache.org/dist/logging/log4j/%{version}/log4j-%{version}.tar.gz
# Converted from src/java/org/apache/log4j/lf5/viewer/images/lf5_small_icon.gif
Source1:        log4j-logfactor5.png
Source2:        log4j-logfactor5.sh
Source3:        log4j-logfactor5.desktop
# Converted from docs/images/logo.jpg
Source4:        log4j-chainsaw.png
Source5:        log4j-chainsaw.sh
Source6:        log4j-chainsaw.desktop
Source7:        log4j.catalog
Patch0:         log4j-logfactor5-userdir.patch
Patch1:         log4j-javadoc-xlink.patch
Patch2:         log4j-mx4j-tools.patch
# PATCH-FIX-OPENSUSE -- Drop javadoc timestamp
Patch3:         log4j-reproducible.patch
# PATCH-FIX-UPSTREAM bsc#1159646 CVE-2019-17571 deserialization of untrusted data in SocketServer
Patch4:         log4j-CVE-2019-17571.patch
# PATCH-FIX-OPENSUSE -- add bundle manifest
Patch5:         log4j12-bundle_manifest.patch
BuildRequires:  ant
BuildRequires:  fdupes
BuildRequires:  java-devel >= 1.8
BuildRequires:  javapackages-local
BuildRequires:  jndi
BuildRequires:  perl
BuildRequires:  update-desktop-files
Requires:       javapackages-tools
Requires:       jaxp_parser_impl
Requires:       xml-apis
Requires(pre):  coreutils
Obsoletes:      log4j < 1.3
Obsoletes:      log4j-mini < 1.3
BuildArch:      noarch
%if %{with bootstrap}
Name:           %{real}-mini
Provides:       %{real} = %{version}-%{release}
%else
Name:           %{real}
BuildRequires:  geronimo-jaf-1_0_2-api
BuildRequires:  geronimo-jms-1_1-api
BuildRequires:  javamail
BuildRequires:  mx4j
#!BuildIgnore:  apache-commons-discovery
#!BuildIgnore:  apache-commons-logging
#!BuildIgnore:  axis
Provides:       %{real}-mini
Obsoletes:      %{real}-mini
#!BuildRequires: %{real}-mini
%endif

%description
Log4j is a tool to help the programmer output log statements to a
variety of output targets.

%if %{without bootstrap}
%package        manual
Summary:        Java logging tool (Manual)
# Manual's api directory is a symlink to javadoc
Requires:       %{name}-javadoc

%description    manual
Documentation manual for Java logging tool log4j.

%package        javadoc
Summary:        Java logging tool (Documentation)

%description    javadoc
Documentation javadoc for Java logging tool log4j.
%endif

%prep
%setup -q -n apache-log4j-%{version}
%patch0
%patch1
%patch2
%patch3 -p1
%patch4 -p1
%if %{without bootstrap}
%patch5 -p1
%endif

sed -i 's/\r//g' LICENSE NOTICE src/site/resources/css/*.css

# remove all the stuff we'll build ourselves
find . \( -name "*.jar" -o -name "*.class" \) -exec rm -f {} \;
rm -rf docs/api

# fix encoding of mailbox files
for i in contribs/JimMoore/mail*;do
    iconv --from=ISO-8859-1 --to=UTF-8 "$i" > new
    mv new "$i"
done

%build
%{ant} \
        -Djavamail.jar=$(build-classpath javamail/mailapi) \
        -Dactivation.jar=$(build-classpath jaf) \
        -Djaxp.jaxp.jar.jar=$(build-classpath jaxp_parser_impl) \
        -Djms.jar=$(build-classpath jms) \
        -Djmx.jar=$(build-classpath mx4j/mx4j) \
        -Djmx-extra.jar=$(build-classpath mx4j/mx4j-tools) \
        -Djndi.jar=$(build-classpath jndi) \
        -Djavac.source=1.6 -Djavac.target=1.6 \
        -Djdk.javadoc=%{_javadocdir}/java \
        jar \
%if %{without bootstrap}
        javadoc
%endif

%install
# jars
mkdir -p %{buildroot}%{_javadir}/%{real}
cp -a dist/lib/log4j-%{version}.jar %{buildroot}%{_javadir}/%{real}/log4j.jar

#pom
install -d -m 755 %{buildroot}%{_mavenpomdir}/%{real}
install -pm 644 pom.xml %{buildroot}%{_mavenpomdir}/%{real}/log4j.pom
%add_maven_depmap %{real}/log4j.pom %{real}/log4j.jar -v "1.2.17,1.2.16,1.2.15,1.2.14,1.2.13,1.2.12,12"

%if %{without bootstrap}
# javadoc
mkdir -p %{buildroot}%{_javadocdir}/%{name}
cp -a docs/api/* %{buildroot}%{_javadocdir}/%{name}
%fdupes -s %{buildroot}%{_javadocdir}/%{name}
rm -rf docs/api
ln -s %{_javadocdir}/%{name} docs/api
%endif
# scripts
mkdir -p %{buildroot}%{_bindir}
install -p -m 755 %{SOURCE2} %{buildroot}%{_bindir}/logfactor5
install -p -m 755 %{SOURCE5} %{buildroot}%{_bindir}/chainsaw
# freedesktop.org menu entries and icons
mkdir -p %{buildroot}%{_datadir}/{applications,pixmaps}
cp -a %{SOURCE1} \
  %{buildroot}%{_datadir}/pixmaps/logfactor5.png
cp -a %{SOURCE3} \
  %{buildroot}%{_datadir}/applications/jpackage-logfactor5.desktop
cp -a %{SOURCE4} \
  %{buildroot}%{_datadir}/pixmaps/chainsaw.png
cp -a %{SOURCE6} \
  %{buildroot}%{_datadir}/applications/jpackage-chainsaw.desktop
# DTD and the SGML catalog (XML catalog handled in scriptlets)
mkdir -p %{buildroot}%{_datadir}/sgml/%{name}
cp -a src/main/resources/org/apache/log4j/xml/log4j.dtd \
  %{buildroot}%{_datadir}/sgml/%{name}
cp -a %{SOURCE7} \
  %{buildroot}%{_datadir}/sgml/%{name}/catalog
# fix perl location
perl -p -i -e 's|/opt/perl5/bin/perl|perl|' \
contribs/KitchingSimon/udpserver.pl
%suse_update_desktop_file jpackage-chainsaw Development Debugger
%suse_update_desktop_file jpackage-logfactor5 Development Debugger

%post
# Note that we're using versioned catalog, so this is always ok.
if [ -x %{_bindir}/install-catalog -a -d %{_sysconfdir}/sgml ]; then
  %{_bindir}/install-catalog --add \
    %{_sysconfdir}/sgml/%{name}-%{version}-%{release}.cat \
    %{_datadir}/sgml/%{name}/catalog > /dev/null || :
fi
if [ -x %{_bindir}/xmlcatalog -a -w %{_sysconfdir}/xml/catalog ]; then
  %{_bindir}/xmlcatalog --noout --add system log4j.dtd \
    file://%{_datadir}/sgml/%{name}/log4j.dtd %{_sysconfdir}/xml/catalog \
    > /dev/null || :
fi

%preun
if [ $1 -eq 0 ]; then
  if [ -x %{_bindir}/xmlcatalog -a -w %{_sysconfdir}/xml/catalog ]; then
    %{_bindir}/xmlcatalog --noout --del log4j.dtd \
      %{_sysconfdir}/xml/catalog > /dev/null || :
  fi
fi

%postun
# Note that we're using versioned catalog, so this is always ok.
if [ -x %{_bindir}/install-catalog -a -d %{_sysconfdir}/sgml ]; then
  %{_bindir}/install-catalog --remove \
    %{_sysconfdir}/sgml/%{name}-%{version}-%{release}.cat \
    %{_datadir}/sgml/%{name}/catalog > /dev/null || :
fi

%files -f .mfiles
%license LICENSE
%doc NOTICE
%{_bindir}/*
%{_javadir}/*
%{_datadir}/applications/*
%{_datadir}/pixmaps/*
%{_datadir}/sgml/%{name}

%if %{without bootstrap}
%files manual
%doc docs/* contribs

%files javadoc
%dir %{_javadocdir}/%{name}
%{_javadocdir}/%{name}/*
%endif

%changelog
