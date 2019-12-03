#
# spec file for package sbt
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


%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "bootstrap"
%bcond_without bootstrap
%else
%bcond_with bootstrap
%endif
%global short_name sbt
# build non-bootstrap packages with tests, cross-referenced sources, etc
%global do_proper 0
%global scala_version 2.10.7
%global scala_short_version 2.10
%global sbt_bootstrap_version 0.13.1
%global sbt_major 0
%global sbt_minor 13
%global sbt_patch 1
%global sbt_build %{nil}
%global sbt_short_version %{sbt_major}.%{sbt_minor}
%global sbt_version %{sbt_major}.%{sbt_minor}.%{sbt_patch}
%global sbt_full_version %{sbt_version}%{sbt_build}
%global typesafe_repo http://repo.typesafe.com/typesafe/ivy-releases

%global ivy_local_dir ivy-local

%global installed_ivy_local %{_datadir}/%{short_name}/%{ivy_local_dir}

%global generic_ivy_artifact() %{1}/%{2}/%{3}/%{4}/jars/%{5}.jar
%global generic_ivy_descriptor() %{1}/%{2}/%{3}/%{4}/ivys/ivy.xml#/%{5}-%{4}-ivy.xml

%global sbt_ivy_artifact() %{typesafe_repo}/org.scala-sbt/%{1}/%{sbt_bootstrap_version}/jars/%{1}.jar
%global sbt_ivy_descriptor() %{typesafe_repo}/org.scala-sbt/%{1}/%{sbt_bootstrap_version}/ivys/ivy.xml#/%{1}-%{sbt_bootstrap_version}-ivy.xml

%global sbt_ghpages_version 0.5.1
%global sbt_git_version 0.6.3
%global sbt_site_version 0.6.2
%global sbt_site_jar_version 0.6.2

%global want_sxr 1
%global want_specs2 0
%global want_scalacheck 1
%global want_dispatch_http 1

%global sxr_version 0.3.0
%global sbinary_version 0.4.2
%global scalacheck_version 1.11.0
%global specs2_version 1.12.3
%global testinterface_version 1.0
%global dispatch_http_version 0.8.9

%if %{with bootstrap}
Name:           sbt-bootstrap
%else
Name:           sbt
%endif
Version:        %{sbt_version}
Release:        0
Summary:        The simple build tool for Scala and Java projects
License:        BSD-3-Clause
Group:          Development/Libraries/Java

BuildArch:      noarch

URL:            http://www.scala-sbt.org
Source0:        https://github.com/sbt/sbt/archive/v%{version}%{sbt_build}.tar.gz

Patch0:         sbt-0.13.1-sbt-scala.patch 
Patch1:         sbt-0.13.1-RC3-release-scala.patch 
Patch2:         sbt-0.13.1-ivy-2.3.0.patch
Patch3:         sbt-0.13.1-ivy-docs.patch
Patch4:         sbt-0.13.1-sxr.patch
Patch5:         sbt-0.13.1-ivy-2.4.0.patch

# sbt-ghpages plugin
Source1:        https://github.com/sbt/sbt-ghpages/archive/v%{sbt_ghpages_version}.tar.gz

# sbt-git plugin
Source2:        https://github.com/sbt/sbt-git/archive/v%{sbt_git_version}.tar.gz

# sbt-site plugin
Source3:        https://github.com/sbt/sbt-site/archive/%{sbt_site_version}.tar.gz

# sxr
Source4:        https://github.com/harrah/browse/archive/v%{sxr_version}.tar.gz

# scalacheck
%if %{?want_scalacheck}
Source6:        https://github.com/rickynils/scalacheck/archive/%{scalacheck_version}.tar.gz
%endif

# specs 
Source7:        https://github.com/etorreborre/specs2/archive/SPECS2-%{specs2_version}.tar.gz	

Source16:       https://raw.github.com/willb/climbing-nemesis/master/climbing-nemesis.py
Source17:       https://raw.github.com/willb/rpm-packaging/master/sbt-packaging/sbt.boot.properties
Source15:       https://raw.github.com/willb/rpm-packaging/master/sbt-packaging/rpmbuild-sbt.boot.properties

# Ivy POM
# necessary for bootstrapping with sbt 0.13.1
Source18:       http://repo1.maven.org/maven2/org/apache/ivy/ivy/2.3.0-rc1/ivy-2.3.0-rc1.pom
# Ivy 2.3.0-rc1 jar (necessary for bootstrapping with sbt 0.13.1)
Source19:       http://repo1.maven.org/maven2/org/apache/ivy/ivy/2.3.0-rc1/ivy-2.3.0-rc1.jar

# sbt script (to be obsoleted in future releases)
# https://raw.github.com/willb/rpm-packaging/master/sbt-packaging/sbt
# modified to correspond to openSUSE jline versions
Source21:       sbt

%if %{with bootstrap}
# include bootstrap libraries

Source32:       %sbt_ivy_artifact ivy 

Source132:      %sbt_ivy_descriptor ivy

Source33:       %sbt_ivy_artifact task-system 

Source133:      %sbt_ivy_descriptor task-system

Source34:       %generic_ivy_artifact %{typesafe_repo} org.scala-sbt compiler-interface %{sbt_bootstrap_version} compiler-interface-src

Source134:      %generic_ivy_descriptor %{typesafe_repo} org.scala-sbt compiler-interface %{sbt_bootstrap_version} compiler-interface-src

Source35:       %generic_ivy_artifact %{typesafe_repo} org.scala-sbt compiler-interface %{sbt_bootstrap_version} compiler-interface-bin

Source135:      %generic_ivy_descriptor %{typesafe_repo} org.scala-sbt compiler-interface %{sbt_bootstrap_version} compiler-interface-bin

Source36:       %sbt_ivy_artifact testing 

Source136:      %sbt_ivy_descriptor testing

Source37:       %sbt_ivy_artifact command 

Source137:      %sbt_ivy_descriptor command

Source38:       %sbt_ivy_artifact test-agent 

Source138:      %sbt_ivy_descriptor test-agent

Source39:       %sbt_ivy_artifact launcher-interface 

Source139:      %sbt_ivy_descriptor launcher-interface

Source40:       %sbt_ivy_artifact run 

Source140:      %sbt_ivy_descriptor run

Source41:       %sbt_ivy_artifact compiler-ivy-integration 

Source141:      %sbt_ivy_descriptor compiler-ivy-integration

Source42:       %sbt_ivy_artifact scripted-sbt 

Source142:      %sbt_ivy_descriptor scripted-sbt

Source44:       %sbt_ivy_artifact collections 

Source144:      %sbt_ivy_descriptor collections

Source45:       %sbt_ivy_artifact persist 

Source145:      %sbt_ivy_descriptor persist

Source46:       %sbt_ivy_artifact classfile 

Source146:      %sbt_ivy_descriptor classfile

Source47:       %sbt_ivy_artifact control 

Source147:      %sbt_ivy_descriptor control

Source48:       %sbt_ivy_artifact launcher 

Source148:      %sbt_ivy_descriptor launcher

Source49:       %sbt_ivy_artifact apply-macro 

Source149:      %sbt_ivy_descriptor apply-macro

Source50:       %sbt_ivy_artifact datatype-generator 

Source150:      %sbt_ivy_descriptor datatype-generator

Source51:       %sbt_ivy_artifact interface 

Source151:      %sbt_ivy_descriptor interface

Source52:       %sbt_ivy_artifact main-settings 

Source152:      %sbt_ivy_descriptor main-settings

Source53:       %sbt_ivy_artifact incremental-compiler 

Source153:      %sbt_ivy_descriptor incremental-compiler

Source54:       %sbt_ivy_artifact cache 

Source154:      %sbt_ivy_descriptor cache

Source55:       %sbt_ivy_artifact compiler-integration 

Source155:      %sbt_ivy_descriptor compiler-integration

Source56:       %sbt_ivy_artifact api 

Source156:      %sbt_ivy_descriptor api

Source57:       %sbt_ivy_artifact main 

Source157:      %sbt_ivy_descriptor main

Source58:       %sbt_ivy_artifact classpath 

Source158:      %sbt_ivy_descriptor classpath

Source59:       %sbt_ivy_artifact logging 

Source159:      %sbt_ivy_descriptor logging

Source60:       %sbt_ivy_artifact compile 

Source160:      %sbt_ivy_descriptor compile

Source61:       %sbt_ivy_artifact process 

Source161:      %sbt_ivy_descriptor process

Source62:       %sbt_ivy_artifact actions

Source162:      %sbt_ivy_descriptor actions

Source63:       %sbt_ivy_artifact sbt-launch 

Source163:      %sbt_ivy_descriptor sbt-launch

Source64:       %sbt_ivy_artifact scripted-plugin 

Source164:      %sbt_ivy_descriptor scripted-plugin

Source65:       %sbt_ivy_artifact tracking 

Source165:      %sbt_ivy_descriptor tracking

Source66:       %sbt_ivy_artifact tasks 

Source166:      %sbt_ivy_descriptor tasks

Source67:       %sbt_ivy_artifact completion 

Source167:      %sbt_ivy_descriptor completion

Source68:       %sbt_ivy_artifact cross 

Source168:      %sbt_ivy_descriptor cross

Source69:       %sbt_ivy_artifact relation 

Source169:      %sbt_ivy_descriptor relation

Source70:       %sbt_ivy_artifact io 

Source170:      %sbt_ivy_descriptor io

Source71:       %sbt_ivy_artifact sbt 

Source171:      %sbt_ivy_descriptor sbt

Source72:       %sbt_ivy_artifact scripted-framework 

Source172:      %sbt_ivy_descriptor scripted-framework

# sbt plugins
Source73:       https://dl.bintray.com/sbt/sbt-plugin-releases/com.typesafe.sbt/sbt-ghpages/scala_%{scala_short_version}/sbt_%{sbt_short_version}/%{sbt_ghpages_version}/jars/sbt-ghpages.jar
Source74:       https://dl.bintray.com/sbt/sbt-plugin-releases/com.typesafe.sbt/sbt-site/scala_%{scala_short_version}/sbt_%{sbt_short_version}/%{sbt_site_jar_version}/jars/sbt-site.jar
Source75:       https://dl.bintray.com/sbt/sbt-plugin-releases/com.typesafe.sbt/sbt-git/scala_%{scala_short_version}/sbt_%{sbt_short_version}/%{sbt_git_version}/jars/sbt-git.jar

%if %{?want_sxr}
# sxr
Source76:       http://repo.typesafe.com/typesafe/ivy-releases/org.scala-sbt.sxr/sxr_%{scala_short_version}/%{sxr_version}/jars/sxr_%{scala_short_version}.jar
%endif

# scalacheck
%if %{?want_scalacheck}
Source78:       http://oss.sonatype.org/content/repositories/releases/org/scalacheck/scalacheck_%{scala_short_version}/%{scalacheck_version}/scalacheck_%{scala_short_version}-%{scalacheck_version}.jar
%endif

%if %{?want_specs2}
# specs
Source79:       http://oss.sonatype.org/content/repositories/releases/org/specs2/specs2_%{scala_short_version}/%{specs2_version}/specs2_%{scala_short_version}-%{specs2_version}.jar
%endif

%if %{?want_dispatch_http}
# dispatch-http
Source81:       http://oss.sonatype.org/content/repositories/releases/net/databinder/dispatch-http_%{scala_short_version}/%{dispatch_http_version}/dispatch-http_%{scala_short_version}-%{dispatch_http_version}.jar
%endif

# precompiled (need only for bootstrapping)

Source82:       http://repo.typesafe.com/typesafe/ivy-releases/org.scala-sbt/precompiled-2_8_2/%{sbt_bootstrap_version}/jars/compiler-interface-bin.jar#/compiler-interface-bin-2_8_2.jar

Source182:      %sbt_ivy_descriptor precompiled-2_8_2

Source83:       http://repo.typesafe.com/typesafe/ivy-releases/org.scala-sbt/precompiled-2_9_2/%{sbt_bootstrap_version}/jars/compiler-interface-bin.jar#/compiler-interface-bin-2_9_2.jar

Source183:      %sbt_ivy_descriptor precompiled-2_9_2

Source84:       http://repo.typesafe.com/typesafe/ivy-releases/org.scala-sbt/precompiled-2_9_3/%{sbt_bootstrap_version}/jars/compiler-interface-bin.jar#/compiler-interface-bin-2_9_3.jar

Source184:      %sbt_ivy_descriptor precompiled-2_9_3

%endif

BuildRequires:  fdupes
BuildRequires:  java-devel
BuildConflicts: java-devel >= 9 java-headless >= 9 java >= 9
BuildRequires:  python
BuildRequires:  mvn(org.scala-lang:scala-compiler)

BuildRequires:  javapackages-local
BuildRequires:  xmvn-resolve

BuildRequires:  hawtjni
BuildRequires:  jline >= 2
BuildRequires:  proguard
BuildRequires:  mvn(org.bouncycastle:bcpg-jdk16)
BuildRequires:  mvn(org.bouncycastle:bcprov-jdk16)
BuildRequires:  mvn(org.fusesource.jansi:jansi)

BuildRequires:  javapackages-tools
Requires:       javapackages-tools

BuildRequires:  apache-ivy
BuildRequires:  mvn(com.jcraft:jsch)
BuildRequires:  mvn(commons-httpclient:commons-httpclient)
BuildRequires:  mvn(org.jsoup:jsoup)
BuildRequires:  mvn(org.scala-lang:scala-compiler)
BuildRequires:  mvn(org.scala-lang:scala-library)
BuildRequires:  mvn(org.scala-lang:scala-reflect)
BuildRequires:  mvn(oro:oro)

Requires:       apache-ivy
Requires:       proguard
Requires:       mvn(com.jcraft:jsch)
Requires:       mvn(commons-httpclient:commons-httpclient)
Requires:       mvn(org.jsoup:jsoup)
Requires:       mvn(org.scala-lang:scala-compiler)
Requires:       mvn(org.scala-lang:scala-library)
Requires:       mvn(org.scala-lang:scala-reflect)
Requires:       mvn(oro:oro)

Requires:       jline >= 2
Requires:       mvn(org.bouncycastle:bcpg-jdk16)
Requires:       mvn(org.bouncycastle:bcprov-jdk16)
Requires:       mvn(org.fusesource.jansi:jansi)

BuildRequires:  sbinary = %{sbinary_version}
BuildRequires:  test-interface = %{testinterface_version}

Requires:       sbinary = %{sbinary_version}
Requires:       test-interface = %{testinterface_version}

%if %{without bootstrap}
BuildRequires:  sbt-bootstrap
Obsoletes:      sbt-bootstrap

%if %{do_proper}
BuildRequires:  sbt-ghpages = %{sbt_ghpages_version}
BuildRequires:  sbt-git = %{sbt_git_version}
BuildRequires:  sbt-site = %{sbt_site_version}

BuildRequires:  scalacheck = %{scalacheck_version}
BuildRequires:  specs2 = %{specs2_version}
BuildRequires:  sxr = %{sxr_version}
%endif

%endif

%description
sbt is the simple build tool for Scala and Java projects.

%prep
%setup -q -n %{short_name}-%{sbt_version}%{sbt_build}

%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%if !%{do_proper}
%patch4 -p1
%endif

%patch5

sed -i -e '/% "test"/d' project/Util.scala

cp %{SOURCE16} .
cp %{SOURCE15} .
chmod 755 climbing-nemesis.py

cp %{SOURCE17} .

%if %{with bootstrap}
cp %{SOURCE63} .
%endif

sed -i -e '/dispatch-http/d' project/p.sbt
sed -i -e '/sbt-site/d' project/p.sbt
sed -i -e '/sbt-ghpages/d' project/p.sbt

sed -i -e 's/0.7.1/0.6.2/g' project/p.sbt

for props in rpmbuild-sbt.boot.properties sbt.boot.properties ; do
    sed -i -e 's/FEDORA_SCALA_VERSION/%{scala_version}/g' $props
    sed -i -e 's/FEDORA_SBT_VERSION/%{sbt_version}/g' $props
done

sed -i -e 's/0.13.0/%{sbt_bootstrap_version}/g' project/build.properties

######################################################################
# Here we're going to use the climbing-nemesis script to populate a local
# Ivy repository.  sbt needs these dependencies to be resolvable by Ivy
# and not merely on the classpath.  When we build a package, we'll be taking
# this repository and installing it alongside the sbt jars so our sbt binary
# can use it.
######################################################################

./climbing-nemesis.py org.jsoup jsoup %{ivy_local_dir} --version 1.7.1

# fake on F19
./climbing-nemesis.py com.jcraft jsch %{ivy_local_dir} --version 0.1.46

# scala compiler; nb; we may need to treat the compiler specially to remove the spurious jline dependency
./climbing-nemesis.py org.scala-lang scala-library %{ivy_local_dir} --version %{scala_version}
./climbing-nemesis.py org.scala-lang scala-compiler %{ivy_local_dir} --version %{scala_version}
./climbing-nemesis.py org.scala-lang scala-reflect %{ivy_local_dir} --version %{scala_version}

./climbing-nemesis.py jline jline %{ivy_local_dir} --version 2.11
./climbing-nemesis.py org.fusesource.jansi jansi %{ivy_local_dir} --version 1.12
./climbing-nemesis.py org.fusesource.jansi jansi-native %{ivy_local_dir} --version 1.8
./climbing-nemesis.py org.fusesource.hawtjni hawtjni-runtime %{ivy_local_dir} --version 1.16

%if %{with bootstrap}
# we need to use the bundled ivy in the bootstrap build because 2.3.0
# is source and binary incompatible with 2.3.0-rc1 (which upstream sbt
# 0.13.1 is built against)

./climbing-nemesis.py org.apache.ivy ivy %{ivy_local_dir} --version 2.3.0-rc1 --pomfile %{SOURCE18} --jarfile %{SOURCE19} # --extra-dep org.bouncycastle:bcpg-jdk16:1.46 --extra-dep org.bouncycastle:bcprov-jdk16:1.46
%endif

# we're building against Ivy 2.3.0, though
./climbing-nemesis.py org.apache.ivy ivy %{ivy_local_dir} --version 2.3.0 --pomfile %{_mavenpomdir}/JPP-ivy.pom --jarfile %{_javadir}/ivy.jar # --extra-dep org.bouncycastle:bcpg-jdk16:1.46 --extra-dep org.bouncycastle:bcprov-jdk16:1.46

## BEGIN OPTIONAL IVY DEPS

# bouncycastle pgp signature generator
# ./climbing-nemesis.py org.bouncycastle bcpg-jdk16 %{ivy_local_dir} --version 1.46
# ./climbing-nemesis.py org.bouncycastle bcprov-jdk16 %{ivy_local_dir} --version 1.46

# ORO (blast from the past)
./climbing-nemesis.py oro oro  %{ivy_local_dir} --version 2.0.8

# JSCH
./climbing-nemesis.py com.jcraft jsch  %{ivy_local_dir} --version 0.1.31

# commons-httpclient
./climbing-nemesis.py commons-httpclient commons-httpclient %{ivy_local_dir} --version 3.0

## END OPTIONAL IVY DEPS

./climbing-nemesis.py net.sf.proguard proguard-base %{ivy_local_dir} --version 4.8 --jarfile %{_javadir}/proguard/proguard.jar

%if %{with bootstrap}
cp %{SOURCE132} org.scala-sbt.ivy-%{sbt_bootstrap_version}.ivy.xml
cp %{SOURCE171} org.scala-sbt.sbt-%{sbt_bootstrap_version}.ivy.xml

sed -i -e '/precompiled/d' org.scala-sbt.ivy-%{sbt_bootstrap_version}.ivy.xml
sed -i -e '/precompiled/d' org.scala-sbt.sbt-%{sbt_bootstrap_version}.ivy.xml

./climbing-nemesis.py --jarfile %{SOURCE32} --ivyfile org.scala-sbt.ivy-%{sbt_bootstrap_version}.ivy.xml org.scala-sbt ivy %{ivy_local_dir} --version %{sbt_bootstrap_version}
./climbing-nemesis.py --jarfile %{SOURCE33} --ivyfile %{SOURCE133} org.scala-sbt task-system %{ivy_local_dir} --version %{sbt_bootstrap_version}
./climbing-nemesis.py --jarfile %{SOURCE34} --ivyfile %{SOURCE134} org.scala-sbt compiler-interface-src %{ivy_local_dir} --version %{sbt_bootstrap_version} --override org.scala-sbt:compiler-interface --override-dir-only
./climbing-nemesis.py --jarfile %{SOURCE35} --ivyfile %{SOURCE135} org.scala-sbt compiler-interface-bin %{ivy_local_dir} --version %{sbt_bootstrap_version} --override org.scala-sbt:compiler-interface --override-dir-only
./climbing-nemesis.py --jarfile %{SOURCE36} --ivyfile %{SOURCE136} org.scala-sbt testing %{ivy_local_dir} --version %{sbt_bootstrap_version}
./climbing-nemesis.py --jarfile %{SOURCE37} --ivyfile %{SOURCE137} org.scala-sbt command %{ivy_local_dir} --version %{sbt_bootstrap_version}
./climbing-nemesis.py --jarfile %{SOURCE38} --ivyfile %{SOURCE138} org.scala-sbt test-agent %{ivy_local_dir} --version %{sbt_bootstrap_version}
./climbing-nemesis.py --jarfile %{SOURCE39} --ivyfile %{SOURCE139} org.scala-sbt launcher-interface %{ivy_local_dir} --version %{sbt_bootstrap_version}
./climbing-nemesis.py --jarfile %{SOURCE40} --ivyfile %{SOURCE140} org.scala-sbt run %{ivy_local_dir} --version %{sbt_bootstrap_version}
./climbing-nemesis.py --jarfile %{SOURCE41} --ivyfile %{SOURCE141} org.scala-sbt compiler-ivy-integration %{ivy_local_dir} --version %{sbt_bootstrap_version}
./climbing-nemesis.py --jarfile %{SOURCE42} --ivyfile %{SOURCE142} org.scala-sbt scripted-sbt %{ivy_local_dir} --version %{sbt_bootstrap_version}
./climbing-nemesis.py --jarfile %{SOURCE44} --ivyfile %{SOURCE144} org.scala-sbt collections %{ivy_local_dir} --version %{sbt_bootstrap_version}
./climbing-nemesis.py --jarfile %{SOURCE45} --ivyfile %{SOURCE145} org.scala-sbt persist %{ivy_local_dir} --version %{sbt_bootstrap_version}
./climbing-nemesis.py --jarfile %{SOURCE46} --ivyfile %{SOURCE146} org.scala-sbt classfile %{ivy_local_dir} --version %{sbt_bootstrap_version}
./climbing-nemesis.py --jarfile %{SOURCE47} --ivyfile %{SOURCE147} org.scala-sbt control %{ivy_local_dir} --version %{sbt_bootstrap_version}
./climbing-nemesis.py --jarfile %{SOURCE48} --ivyfile %{SOURCE148} org.scala-sbt launcher %{ivy_local_dir} --version %{sbt_bootstrap_version}
./climbing-nemesis.py --jarfile %{SOURCE49} --ivyfile %{SOURCE149} org.scala-sbt apply-macro %{ivy_local_dir} --version %{sbt_bootstrap_version}
./climbing-nemesis.py --jarfile %{SOURCE50} --ivyfile %{SOURCE150} org.scala-sbt datatype-generator %{ivy_local_dir} --version %{sbt_bootstrap_version}
./climbing-nemesis.py --jarfile %{SOURCE51} --ivyfile %{SOURCE151} org.scala-sbt interface %{ivy_local_dir} --version %{sbt_bootstrap_version}
./climbing-nemesis.py --jarfile %{SOURCE52} --ivyfile %{SOURCE152} org.scala-sbt main-settings %{ivy_local_dir} --version %{sbt_bootstrap_version}
./climbing-nemesis.py --jarfile %{SOURCE53} --ivyfile %{SOURCE153} org.scala-sbt incremental-compiler %{ivy_local_dir} --version %{sbt_bootstrap_version}
./climbing-nemesis.py --jarfile %{SOURCE54} --ivyfile %{SOURCE154} org.scala-sbt cache %{ivy_local_dir} --version %{sbt_bootstrap_version}
./climbing-nemesis.py --jarfile %{SOURCE55} --ivyfile %{SOURCE155} org.scala-sbt compiler-integration %{ivy_local_dir} --version %{sbt_bootstrap_version}
./climbing-nemesis.py --jarfile %{SOURCE56} --ivyfile %{SOURCE156} org.scala-sbt api %{ivy_local_dir} --version %{sbt_bootstrap_version}
./climbing-nemesis.py --jarfile %{SOURCE57} --ivyfile %{SOURCE157} org.scala-sbt main %{ivy_local_dir} --version %{sbt_bootstrap_version}
./climbing-nemesis.py --jarfile %{SOURCE58} --ivyfile %{SOURCE158} org.scala-sbt classpath %{ivy_local_dir} --version %{sbt_bootstrap_version}
./climbing-nemesis.py --jarfile %{SOURCE59} --ivyfile %{SOURCE159} org.scala-sbt logging %{ivy_local_dir} --version %{sbt_bootstrap_version}
./climbing-nemesis.py --jarfile %{SOURCE60} --ivyfile %{SOURCE160} org.scala-sbt compile %{ivy_local_dir} --version %{sbt_bootstrap_version}
./climbing-nemesis.py --jarfile %{SOURCE61} --ivyfile %{SOURCE161} org.scala-sbt process %{ivy_local_dir} --version %{sbt_bootstrap_version}
./climbing-nemesis.py --jarfile %{SOURCE62} --ivyfile %{SOURCE162} org.scala-sbt actions %{ivy_local_dir} --version %{sbt_bootstrap_version}
./climbing-nemesis.py --jarfile %{SOURCE63} --ivyfile %{SOURCE163} org.scala-sbt sbt-launch %{ivy_local_dir} --version %{sbt_bootstrap_version}
./climbing-nemesis.py --jarfile %{SOURCE64} --ivyfile %{SOURCE164} org.scala-sbt scripted-plugin %{ivy_local_dir} --version %{sbt_bootstrap_version}
./climbing-nemesis.py --jarfile %{SOURCE65} --ivyfile %{SOURCE165} org.scala-sbt tracking %{ivy_local_dir} --version %{sbt_bootstrap_version}
./climbing-nemesis.py --jarfile %{SOURCE66} --ivyfile %{SOURCE166} org.scala-sbt tasks %{ivy_local_dir} --version %{sbt_bootstrap_version}
./climbing-nemesis.py --jarfile %{SOURCE67} --ivyfile %{SOURCE167} org.scala-sbt completion %{ivy_local_dir} --version %{sbt_bootstrap_version}
./climbing-nemesis.py --jarfile %{SOURCE68} --ivyfile %{SOURCE168} org.scala-sbt cross %{ivy_local_dir} --version %{sbt_bootstrap_version}
./climbing-nemesis.py --jarfile %{SOURCE69} --ivyfile %{SOURCE169} org.scala-sbt relation %{ivy_local_dir} --version %{sbt_bootstrap_version}
./climbing-nemesis.py --jarfile %{SOURCE70} --ivyfile %{SOURCE170} org.scala-sbt io %{ivy_local_dir} --version %{sbt_bootstrap_version}
./climbing-nemesis.py --jarfile %{SOURCE71} --ivyfile org.scala-sbt.sbt-%{sbt_bootstrap_version}.ivy.xml org.scala-sbt sbt %{ivy_local_dir} --version %{sbt_bootstrap_version}
./climbing-nemesis.py --jarfile %{SOURCE72} --ivyfile %{SOURCE172} org.scala-sbt scripted-framework %{ivy_local_dir} --version %{sbt_bootstrap_version}

# plugins

./climbing-nemesis.py --jarfile %{SOURCE73} com.typesafe.sbt sbt-ghpages %{ivy_local_dir} --version %{sbt_ghpages_version} --meta e:scalaVersion=%{scala_short_version} --meta e:sbtVersion=%{sbt_short_version}
./climbing-nemesis.py --jarfile %{SOURCE74} com.typesafe.sbt sbt-site %{ivy_local_dir} --version %{sbt_site_version} --meta e:scalaVersion=%{scala_short_version} --meta e:sbtVersion=%{sbt_short_version}
./climbing-nemesis.py --jarfile %{SOURCE75} com.typesafe.sbt sbt-git %{ivy_local_dir} --version %{sbt_git_version} --meta e:scalaVersion=%{scala_short_version} --meta e:sbtVersion=%{sbt_short_version}

# SXR
%if %{?want_sxr}
./climbing-nemesis.py --jarfile %{SOURCE76} org.scala-sbt.sxr sxr %{ivy_local_dir} --version %{sxr_version} --scala %{scala_short_version}
%endif

# test-interface
./climbing-nemesis.py org.scala-sbt test-interface %{ivy_local_dir} --version 1.0

# sbinary
./climbing-nemesis.py org.scala-tools.sbinary sbinary_%{scala_short_version} %{ivy_local_dir} # --scala %{scala_short_version}

# scalacheck
%if %{?want_scalacheck}
./climbing-nemesis.py --jarfile %{SOURCE78} org.scalacheck scalacheck %{ivy_local_dir} --version %{scalacheck_version} --scala %{scala_short_version}
%endif

# specs2
%if %{?want_specs2}
./climbing-nemesis.py --jarfile %{SOURCE79} org.specs2 specs2 %{ivy_local_dir} --version %{specs2_version} --scala %{scala_short_version}
%endif

%if %{?want_dispatch_http}
# dispatch-http
./climbing-nemesis.py --jarfile %{SOURCE81} net.databinder dispatch-http_%{scala_short_version} %{ivy_local_dir} --version %{dispatch_http_version}
%endif

%else
# If we aren't bootstrapping, copy installed jars into local ivy cache
# dir.  In the future, we'll use Mikołaj's new xmvn Ivy resolver.

# sbt components
for jar in actions api apply-macro cache classfile classpath collections command compile compiler-integration compiler-ivy-integration completion control cross datatype-generator incremental-compiler interface io ivy launcher launcher-interface logging main main-settings persist process relation run sbt scripted-framework scripted-plugin scripted-sbt tasks task-system test-agent testing tracking; do
    ./climbing-nemesis.py --jarfile %{_javadir}/%{short_name}/${jar}.jar --ivyfile %{installed_ivy_local}/org.scala-sbt/${jar}/%{sbt_bootstrap_version}/ivy.xml org.scala-sbt ${jar} %{ivy_local_dir}
done

./climbing-nemesis.py --jarfile %{_javadir}/%{short_name}/compiler-interface-src.jar --ivyfile %{installed_ivy_local}/org.scala-sbt/compiler-interface/%{sbt_bootstrap_version}/ivy.xml org.scala-sbt compiler-interface-src %{ivy_local_dir} --version %{sbt_bootstrap_version} --override org.scala-sbt:compiler-interface --override-dir-only

./climbing-nemesis.py --jarfile %{_javadir}/%{short_name}/compiler-interface-bin.jar --ivyfile %{installed_ivy_local}/org.scala-sbt/compiler-interface/%{sbt_bootstrap_version}/ivy.xml org.scala-sbt compiler-interface-bin %{ivy_local_dir} --version %{sbt_bootstrap_version} --override org.scala-sbt:compiler-interface --override-dir-only

# test-interface
./climbing-nemesis.py org.scala-sbt test-interface %{ivy_local_dir} --version 1.0

# sbinary
./climbing-nemesis.py org.scala-tools.sbinary sbinary_%{scala_short_version} %{ivy_local_dir} # --scala %{scala_short_version}

%endif

# better not to try and compile the docs project
rm -f project/Docs.scala

mkdir sbt-boot-dir

%if %{with bootstrap}
mkdir -p sbt-boot-dir/scala-%{scala_version}/org.scala-sbt/%{short_name}/%{sbt_bootstrap_version}/
mkdir -p sbt-boot-dir/scala-%{scala_version}/lib

for jar in $(find %{ivy_local_dir}/ -name \*.jar | grep fusesource) ; do 
   cp --symbolic-link $(readlink $jar) sbt-boot-dir/scala-%{scala_version}/lib
done

# this is a hack, obvs
for jar in $(find %{ivy_local_dir}/ -name \*.jar | grep bouncycastle) ; do 
   cp --symbolic-link $(readlink $jar) sbt-boot-dir/scala-%{scala_version}/lib
done

%endif
mkdir -p scala/lib
for jar in %{_javadir}/scala/*.jar ; do
   cp --symbolic-link $jar scala/lib
done

sed -i -e 's/["]2[.]10[.][23456]["]/\"%{scala_version}\"/g' $(find . -name \*.sbt -type f) $(find . -name \*.xml) $(find . -name \*.scala)
sed -i -e 's/["]2[.]10[.]2-RC2["]/\"%{scala_version}\"/g' $(find . -name \*.sbt -type f)

# work around proguard bugs with the Scala library
sed -i -e 's/"-dontnote",/"-dontnote", "-dontshrink", "-dontoptimize",/g' project/Proguard.scala
sed -i -e 's/mapLibraryJars.all filterNot in[.]toSet./mapLibraryJars(all.map {f => new java.io.File(f.getCanonicalPath())} filterNot in.map {f => new java.io.File(f.getCanonicalPath())}.toSet)/g' project/Proguard.scala

%build

%if %{with bootstrap}
java -Xms512M -Xmx1536M -Xss1M -XX:+CMSClassUnloadingEnabled -jar -Dfedora.sbt.ivy.dir=ivy-local -Dfedora.sbt.boot.dir=sbt-boot-dir -Divy.checksums='""' -Dsbt.boot.properties=rpmbuild-sbt.boot.properties sbt-launch.jar package "set publishTo in Global := Some(Resolver.file(\"published\", file(\"published\"))(Resolver.ivyStylePatterns) ivys \"$(pwd)/published/[organization]/[module]/[revision]/ivy.xml\" artifacts \"$(pwd)/published/[organization]/[module]/[revision]/[artifact]-[revision].[ext]\")" publish makePom
%else
export SBT_IVY_DIR=$PWD/ivy-local
export SBT_BOOT_DIR=$PWD/sbt-boot-dir
export SBT_BOOT_PROPERTIES=rpmbuild-sbt.boot.properties
sbt package "set publishTo in Global := Some(Resolver.file(\"published\", file(\"published\"))(Resolver.ivyStylePatterns) ivys \"$(pwd)/published/[organization]/[module]/[revision]/ivy.xml\" artifacts \"$(pwd)/published/[organization]/[module]/[revision]/[artifact]-[revision].[ext]\")" publish makePom
%endif

# XXX: this is a hack; we seem to get correct metadata but bogus JARs
# from "sbt publish" for some reason
for f in $(find published -name \*.jar ) ; do
    find . -ipath \*target\* -and -name $(basename $f) -exec cp '{}' $f \;
done

%install

mkdir -p %{buildroot}/%{_javadir}/%{short_name}

# collect and install SBT jars
find published -name \*.jar | grep -v sbt-launch.jar | grep %{sbt_full_version}.jar | xargs -I JAR cp JAR %{buildroot}/%{_javadir}/%{short_name}

mkdir -p %{buildroot}/%{_bindir}
cp -p %{SOURCE21} %{buildroot}/%{_bindir}/%{short_name}
chmod 755 %{buildroot}/%{_bindir}/%{short_name}

pushd %{buildroot}/%{_javadir}/%{short_name}
for jar in *.jar ; do
    mv $jar $(echo $jar | sed -e 's/-%{sbt_full_version}//g')
done
popd

rm -f %{buildroot}/%{_javadir}/%{short_name}/sbt-launch.jar

mkdir -p %{buildroot}/%{_sysconfdir}/%{short_name}

# XXXXXXX
for props in rpmbuild-sbt.boot.properties sbt.boot.properties ; do
    sed 's/debug/info/' < $props > %{buildroot}/%{_sysconfdir}/%{short_name}/$props
done

mkdir -p %{buildroot}/%{installed_ivy_local}

# remove things that we only needed for the bootstrap build

rm -rf %{ivy_local_dir}/net.databinder
rm -rf %{ivy_local_dir}/com.typesafe.sbt
rm -rf %{ivy_local_dir}/org.scalacheck
rm -rf %{ivy_local_dir}/org.scala-sbt.sxr
rm -rf %{ivy_local_dir}/cache

rm -rf %{ivy_local_dir}/org.scala-sbt/sbt-launch

(cd %{ivy_local_dir} ; tar --exclude=.md5 --exclude=.sha1 -cf - .) | (cd %{buildroot}/%{installed_ivy_local} ; tar -xf - )
(cd published ; tar --exclude=\*.md5 --exclude=\*.sha1 -cf - .) | (cd %{buildroot}/%{installed_ivy_local} ; tar -xf - )

for bootjar in $(find %{buildroot}/%{installed_ivy_local}/org.scala-sbt -type l) ; do
rm -f $bootjar
ln -s %{_javadir}/%{short_name}/$(basename $bootjar) $bootjar
done

%if %{with bootstrap}
# remove bootstrap ivy 2.3.0-rc1 jar if we're using it
find %{buildroot}/%{installed_ivy_local} -lname %{SOURCE19} | xargs dirname | xargs rm -rf

concretize() {
    src=$(readlink $1)
    rm $1 && cp $src $1
}

# copy other bootstrap dependency jars from their sources
for depjar in $(find %{buildroot}/%{installed_ivy_local} -lname %{_sourcedir}\* ) ; do
concretize $depjar
done

%endif # with bootstrap

find %{buildroot}/%{installed_ivy_local} -name \*.lock -delete

find %{buildroot}/%{_datadir}/%{short_name} -name \*test-interface\* | xargs rm -rf
./climbing-nemesis.py org.scala-sbt test-interface %{buildroot}/%{installed_ivy_local} --version %{testinterface_version}

### install POM files
mkdir -p %{buildroot}/%{_mavenpomdir}
rm -f .rpm_pomfiles
touch .rpm_pomfiles
declare -a shortnames

for pom in $(find . -name \*.pom | grep -v compiler-interface | grep -v launch-test | grep -v sbt-launch ) ; do 
    shortname=$(echo $pom | sed -e 's/^.*[/]\([a-z-]\+\)-0.13.1.pom$/\1/g')
    echo installing POM $pom to %{_mavenpomdir}/JPP.%{short_name}-${shortname}.pom
    cp $pom %{buildroot}/%{_mavenpomdir}/JPP.%{short_name}-${shortname}.pom
    echo %{_mavenpomdir}/JPP.%{short_name}-${shortname}.pom >> .rpm_pomfiles
    shortnames=( "${shortnames[@]}" $shortname )
done

echo shortnames are ${shortnames[@]}

for sub in ${shortnames[@]} ; do
    echo running add_maven_depmap JPP.%{short_name}-${sub}.pom %{short_name}/${sub}.jar
    %add_maven_depmap JPP.%{short_name}-${sub}.pom %{short_name}/${sub}.jar
done

%files -f .mfiles
%{_datadir}/%{short_name}
%{_bindir}/%{short_name}*
%{_javadir}/%{short_name}
%{_javadir}/%{short_name}/compiler-interface-src.jar
%{_javadir}/%{short_name}/compiler-interface-bin.jar

%{_sysconfdir}/%{short_name}
%doc README.md LICENSE NOTICE

%changelog
