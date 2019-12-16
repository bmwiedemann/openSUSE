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
%global sbt_bootstrap_version 0.13.18
%global sbt_major 0
%global sbt_minor 13
%global sbt_patch 18
%global sbt_build %{nil}
%global sbt_short_version %{sbt_major}.%{sbt_minor}
%global sbt_version %{sbt_major}.%{sbt_minor}.%{sbt_patch}
%global sbt_full_version %{sbt_version}%{sbt_build}
%global typesafe_repo http://repo.typesafe.com/typesafe/ivy-releases

%global ivy_local_dir ivy-local

%global installed_ivy_local %{_datadir}/%{short_name}/%{ivy_local_dir}

%global generic_ivy_artifact() %{1}/%{2}/%{3}/%{4}/jars/%{5}.jar#/%{5}-%{4}.jar
%global generic_ivy_descriptor() %{1}/%{2}/%{3}/%{4}/ivys/ivy.xml#/%{5}-%{4}-ivy.xml

%global sbt_ivy_artifact() %{typesafe_repo}/org.scala-sbt/%{1}/%{sbt_bootstrap_version}/jars/%{1}.jar#/%{1}-%{sbt_bootstrap_version}.jar
%global sbt_ivy_descriptor() %{typesafe_repo}/org.scala-sbt/%{1}/%{sbt_bootstrap_version}/ivys/ivy.xml#/%{1}-%{sbt_bootstrap_version}-ivy.xml

%global sbt_launcher_version 1.0.1
%global sbt_bootstrap_ivy_version 2.3.0-sbt-b18f59ea3bc914a297bb6f1a4f7fb0ace399e310
%global sbt_serialization_version 0.1.2
%global scala_pickling_version 0.10.1
%global template_resolver_version 0.1
%global quasiquotes_version 2.0.1
%global jline_version 2.14.5
%global jansi_version 1.12
%global sbt_ghpages_version 0.5.4
%global sbt_git_version 0.8.5
%global sbt_site_version 0.8.2
%global sbt_jvcheck_version 0.1.0
%global sbt_doge_version 0.1.5
%global sbt_assembly_version 0.14.2
%global sbt_bintray_version 0.5.1
%global scalariform_version 0.1.4
%global sbt_scalariform_version 1.3.0
%global sbt_pgp_version 1.0.0
%global sxr_version 0.3.0
%global sbinary_version 0.4.2
%global scalacheck_version 1.11.4
%global specs2_version 2.3.11
%global testinterface_version 1.0
%global dispatch_http_version 0.8.9

%global want_sxr 0
%global want_specs2 0
%global want_scalacheck 0
%global want_dispatch_http 0

%if %{with bootstrap}
Name:           %{short_name}-bootstrap
%else
Name:           %{short_name}
%endif
Version:        %{sbt_version}
Release:        0
Summary:        The simple build tool for Scala and Java projects
License:        BSD-3-Clause
URL:            http://www.scala-sbt.org
Patch0:         sbt-%{sbt_version}-build-sbt.patch
Patch2:         sbt-0.13.17-lines.patch

Patch4:         sbt-0.13.13-sxr.patch

Source0:        https://github.com/sbt/sbt/archive/v%{version}%{sbt_build}.tar.gz

# sbt-ghpages plugin
Source1:        https://github.com/sbt/sbt-ghpages/archive/v%{sbt_ghpages_version}.tar.gz
# sbt-git plugin
Source2:        https://github.com/sbt/sbt-git/archive/v%{sbt_git_version}.tar.gz
# sbt-site plugin
Source3:        https://github.com/sbt/sbt-site/archive/v%{sbt_site_version}.tar.gz

# sxr
Source4:        https://github.com/harrah/browse/archive/v%{sxr_version}.tar.gz

# scalacheck
%if %{?want_scalacheck}
Source6:        https://github.com/rickynils/scalacheck/archive/%{scalacheck_version}.tar.gz
%endif

# specs 
Source7:        https://github.com/etorreborre/specs2/archive/SPECS2-%{specs2_version}.tar.gz	

Source15:       https://raw.github.com/willb/climbing-nemesis/master/climbing-nemesis.py
Source16:       https://raw.github.com/willb/rpm-packaging/master/sbt-packaging/rpmbuild-sbt.boot.properties
Source17:       https://raw.github.com/willb/rpm-packaging/master/sbt-packaging/sbt.boot.properties

# sbt script (to be obsoleted in future releases)
# https://raw.github.com/willb/rpm-packaging/master/sbt-packaging/sbt
# modified to correspond to openSUSE jline versions
Source21:       sbt

Source34:       http://dl.bintray.com/typesafe/ivy-releases/org.scala-sbt/compiler-interface/%{sbt_bootstrap_version}/srcs/compiler-interface-sources.jar#/compiler-interface-%{sbt_bootstrap_version}-sources.jar
Source134:      %{sbt_ivy_descriptor compiler-interface}

%if %{with bootstrap}
# include bootstrap libraries

Source57:       %{sbt_ivy_artifact main}
Source157:      %{sbt_ivy_descriptor main}

Source62:       %{sbt_ivy_artifact actions}
Source162:      %{sbt_ivy_descriptor actions}

Source51:       %{sbt_ivy_artifact interface}
Source151:      %{sbt_ivy_descriptor interface}

Source52:       %{sbt_ivy_artifact main-settings}
Source152:      %{sbt_ivy_descriptor main-settings}

Source56:       %{sbt_ivy_artifact api}
Source156:      %{sbt_ivy_descriptor api}

Source58:       %{sbt_ivy_artifact classpath}
Source158:      %{sbt_ivy_descriptor classpath}

Source67:       %{sbt_ivy_artifact completion}
Source167:      %{sbt_ivy_descriptor completion}

Source41:       %{sbt_ivy_artifact compiler-ivy-integration}
Source141:      %{sbt_ivy_descriptor compiler-ivy-integration}

Source55:       %{sbt_ivy_artifact compiler-integration}
Source155:      %{sbt_ivy_descriptor compiler-integration}

Source70:       %{sbt_ivy_artifact io}
Source170:      %{sbt_ivy_descriptor io}

Source61:       %{sbt_ivy_artifact process}
Source161:      %{sbt_ivy_descriptor process}

Source40:       %{sbt_ivy_artifact run}
Source140:      %{sbt_ivy_descriptor run}

Source69:       %{sbt_ivy_artifact relation}
Source169:      %{sbt_ivy_descriptor relation}

Source33:       %{sbt_ivy_artifact task-system}
Source133:      %{sbt_ivy_descriptor task-system}

Source66:       %{sbt_ivy_artifact tasks}
Source166:      %{sbt_ivy_descriptor tasks}

Source65:       %{sbt_ivy_artifact tracking}
Source165:      %{sbt_ivy_descriptor tracking}

Source73:       %{sbt_ivy_artifact logic}
Source173:      %{sbt_ivy_descriptor logic}

Source36:       %{sbt_ivy_artifact testing}
Source136:      %{sbt_ivy_descriptor testing}

Source49:       %{sbt_ivy_artifact apply-macro}
Source149:      %{sbt_ivy_descriptor apply-macro}

Source37:       %{sbt_ivy_artifact command}
Source137:      %{sbt_ivy_descriptor command}

Source32:       %{sbt_ivy_artifact ivy}
Source132:      %{sbt_ivy_descriptor ivy}

Source47:       %{sbt_ivy_artifact control}
Source147:      %{sbt_ivy_descriptor control}

Source68:       %{sbt_ivy_artifact cross}
Source168:      %{sbt_ivy_descriptor cross}

Source46:       %{sbt_ivy_artifact classfile}
Source146:      %{sbt_ivy_descriptor classfile}

Source38:       %{sbt_ivy_artifact test-agent}
Source138:      %{sbt_ivy_descriptor test-agent}

Source45:       %{sbt_ivy_artifact persist}
Source145:      %{sbt_ivy_descriptor persist}

Source53:       %{sbt_ivy_artifact incremental-compiler}
Source153:      %{sbt_ivy_descriptor incremental-compiler}

Source54:       %{sbt_ivy_artifact cache}
Source154:      %{sbt_ivy_descriptor cache}

Source59:       %{sbt_ivy_artifact logging}
Source159:      %{sbt_ivy_descriptor logging}

Source60:       %{sbt_ivy_artifact compile}
Source160:      %{sbt_ivy_descriptor compile}

Source44:       %{sbt_ivy_artifact collections}
Source144:      %{sbt_ivy_descriptor collections}

Source63:       %{sbt_ivy_artifact sbt-launch}
Source163:      %{sbt_ivy_descriptor sbt-launch}

%if %{?want_specs2}
# specs
Source79:       https://oss.sonatype.org/content/repositories/releases/org/specs2/specs2_%{scala_short_version}/%{specs2_version}/specs2_%{scala_short_version}-%{specs2_version}.jar
%endif

%if %{do_proper}
# sbt plugins
Source74:       http://repo.scala-sbt.org/scalasbt/sbt-plugin-releases/com.typesafe.sbt/sbt-ghpages/scala_%{scala_short_version}/sbt_%{sbt_short_version}/%{sbt_ghpages_version}/jars/sbt-ghpages.jar
Source75:       http://repo.scala-sbt.org/scalasbt/sbt-plugin-releases/com.typesafe.sbt/sbt-site/scala_%{scala_short_version}/sbt_%{sbt_short_version}/%{sbt_site_version}/jars/sbt-site.jar
Source76:       http://repo.scala-sbt.org/scalasbt/sbt-plugin-releases/com.typesafe.sbt/sbt-git/scala_%{scala_short_version}/sbt_%{sbt_short_version}/%{sbt_git_version}/jars/sbt-git.jar
%endif # do_proper

%if %{?want_sxr}
Source77:       %{generic_ivy_artifact http://repo.typesafe.com/typesafe/ivy-releases org.scala-sbt.sxr sxr_%{scala_short_version} %{sxr_version} sxr_%{scala_short_version}}
%endif # want_sxr

# scalacheck
%if %{?want_scalacheck}
Source78:       http://oss.sonatype.org/content/repositories/releases/org/scalacheck/scalacheck_%{scala_short_version}/%{scalacheck_version}/scalacheck_%{scala_short_version}-%{scalacheck_version}.jar
%endif

%if %{?want_dispatch_http}
# dispatch-http
Source81:       http://oss.sonatype.org/content/repositories/releases/net/databinder/dispatch-http_%{scala_short_version}/%{dispatch_http_version}/dispatch-http_%{scala_short_version}-%{dispatch_http_version}.jar
%endif # want_dispatch_http

%if %{do_proper}
# more plugins
Source90:       http://repo.scala-sbt.org/scalasbt/sbt-plugin-releases/com.eed3si9n/sbt-doge/scala_%{scala_short_version}/sbt_%{sbt_short_version}/%{sbt_doge_version}/jars/sbt-doge.jar
Source190:      http://repo.scala-sbt.org/scalasbt/sbt-plugin-releases/com.eed3si9n/sbt-doge/scala_%{scala_short_version}/sbt_%{sbt_short_version}/%{sbt_doge_version}/ivys/ivy.xml#/sbt-doge-%{sbt_doge_version}-ivy.xml

Source91:       http://repo.scala-sbt.org/scalasbt/sbt-plugin-releases/com.typesafe.sbt/sbt-javaversioncheck/scala_%{scala_short_version}/sbt_%{sbt_short_version}/%{sbt_jvcheck_version}/jars/sbt-javaversioncheck.jar
Source191:      http://repo.scala-sbt.org/scalasbt/sbt-plugin-releases/com.typesafe.sbt/sbt-javaversioncheck/scala_%{scala_short_version}/sbt_%{sbt_short_version}/%{sbt_jvcheck_version}/ivys/ivy.xml#/sbt-javaversioncheck-%{sbt_jvcheck_version}-ivy.xml

Source92:       http://repo.scala-sbt.org/scalasbt/sbt-plugin-releases/com.typesafe.sbt/sbt-scalariform/scala_%{scala_short_version}/sbt_%{sbt_short_version}/%{sbt_scalariform_version}/jars/sbt-scalariform.jar
Source192:      http://repo.scala-sbt.org/scalasbt/sbt-plugin-releases/com.typesafe.sbt/sbt-scalariform/scala_%{scala_short_version}/sbt_%{sbt_short_version}/%{sbt_scalariform_version}/ivys/ivy.xml#/sbt-scalariform-%{sbt_scalariform_version}-ivy.xml

Source93:       http://repo.scala-sbt.org/scalasbt/sbt-plugin-releases/com.jsuereth/sbt-pgp/scala_%{scala_short_version}/sbt_%{sbt_short_version}/%{sbt_pgp_version}/jars/sbt-pgp.jar
Source193:      http://repo.scala-sbt.org/scalasbt/sbt-plugin-releases/com.jsuereth/sbt-pgp/scala_%{scala_short_version}/sbt_%{sbt_short_version}/%{sbt_pgp_version}/ivys/ivy.xml#/sbt-pgp-%{sbt_pgp_version}-ivy.xml

Source94:       http://repo.scala-sbt.org/scalasbt/sbt-plugin-releases/com.eed3si9n/sbt-assembly/scala_%{scala_short_version}/sbt_%{sbt_short_version}/%{sbt_assembly_version}/jars/sbt-assembly.jar
Source194:      http://repo.scala-sbt.org/scalasbt/sbt-plugin-releases/com.eed3si9n/sbt-assembly/scala_%{scala_short_version}/sbt_%{sbt_short_version}/%{sbt_assembly_version}/ivys/ivy.xml#/sbt-assembly-%{sbt_assembly_version}-ivy.xml

Source95:       http://repo.scala-sbt.org/scalasbt/sbt-plugin-releases/org.foundweekends/sbt-bintray/scala_%{scala_short_version}/sbt_%{sbt_short_version}/%{sbt_bintray_version}/jars/sbt-bintray.jar
Source195:      http://repo.scala-sbt.org/scalasbt/sbt-plugin-releases/org.foundweekends/sbt-bintray/scala_%{scala_short_version}/sbt_%{sbt_short_version}/%{sbt_bintray_version}/ivys/ivy.xml#/sbt-bintray-%{sbt_bintray_version}-ivy.xml

Source96:       https://repo1.maven.org/maven2/org/scalariform/scalariform_%{scala_short_version}/%{scalariform_version}/scalariform_%{scala_short_version}-%{scalariform_version}.jar
Source196:      https://repo1.maven.org/maven2/org/scalariform/scalariform_%{scala_short_version}/%{scalariform_version}/scalariform_%{scala_short_version}-%{scalariform_version}.pom
%endif # do_proper

%endif # with bootstrap

Source71:       %{sbt_ivy_artifact sbt}
Source171:      %{sbt_ivy_descriptor sbt}

#Source650:  https://oss.sonatype.org/service/local/repositories/releases/content/org/scala-sbt/sbt-giter8-resolver/sbt-giter8-resolver_%{scala_short_version}/0.1.0/sbt-giter8-resolver_%{scala_short_version}-0.1.0.jar
#Source660:  https://oss.sonatype.org/service/local/repositories/releases/content/org/foundweekends/giter8/giter8_%{scala_short_version}/0.7.1/giter8_%{scala_short_version}-0.7.1.jar

BuildRequires:  ivy-local
BuildRequires:  java-devel
BuildRequires:  jline
BuildRequires:  jsch
BuildRequires:  json4s-core
BuildRequires:  junit
BuildRequires:  maven-lib
BuildRequires:  proguard
BuildRequires:  python
BuildRequires:  sbinary
BuildRequires:  sbt-launcher
BuildRequires:  sbt-launcher-interface
BuildRequires:  serialization
BuildRequires:  template-resolver
BuildRequires:  xmvn-resolve
BuildRequires:  xmvn-subst
BuildRequires:  mvn(com.google.guava:guava)
BuildRequires:  mvn(javax.inject:javax.inject)
BuildRequires:  mvn(org.bouncycastle:bcpg-jdk16)
BuildRequires:  mvn(org.bouncycastle:bcprov-jdk16)
BuildRequires:  mvn(org.codehaus.plexus:plexus-classworlds)
BuildRequires:  mvn(org.codehaus.plexus:plexus-component-annotations)
BuildRequires:  mvn(org.codehaus.plexus:plexus-interpolation)
BuildRequires:  mvn(org.codehaus.plexus:plexus-utils)
BuildRequires:  mvn(org.eclipse.aether:aether-api)
BuildRequires:  mvn(org.eclipse.aether:aether-connector-basic)
BuildRequires:  mvn(org.eclipse.aether:aether-impl)
BuildRequires:  mvn(org.eclipse.aether:aether-spi)
BuildRequires:  mvn(org.eclipse.aether:aether-util)
BuildRequires:  mvn(org.eclipse.sisu:org.eclipse.sisu.inject)
BuildRequires:  mvn(org.eclipse.sisu:org.eclipse.sisu.plexus)
BuildRequires:  mvn(org.fusesource.jansi:jansi) mvn(org.apache.commons:commons-lang3)

BuildRequires:  javapackages-tools
Requires:       javapackages-tools

BuildRequires:  apache-ivy
BuildRequires:  mvn(commons-httpclient:commons-httpclient)
BuildRequires:  mvn(org.jsoup:jsoup)
BuildRequires:  mvn(oro:oro)

BuildRequires:  scala

BuildRequires:  test-interface

Requires:       apache-commons-lang3
Requires:       apache-ivy
Requires:       atinject
Requires:       guava
Requires:       hamcrest-core
Requires:       hawtjni-runtime
Requires:       jansi
Requires:       jansi-native
Requires:       jawn-json4s
Requires:       jawn-parser
Requires:       jawn-util
Requires:       jline
Requires:       jsch
Requires:       json4s-ast
Requires:       json4s-core
Requires:       jsr-305
Requires:       junit
Requires:       maven-lib
Requires:       maven-resolver-api
Requires:       maven-resolver-connector-basic
Requires:       maven-resolver-impl
Requires:       maven-resolver-spi
Requires:       maven-resolver-util
Requires:       paranamer
Requires:       plexus-classworlds
Requires:       plexus-containers-component-annotations
Requires:       plexus-interpolation
Requires:       plexus-utils
Requires:       quasiquotes
Requires:       sbinary
Requires:       sbt-launcher
Requires:       sbt-launcher-interface
Requires:       scala
Requires:       scala-pickling
Requires:       serialization
Requires:       sisu-inject
Requires:       sisu-plexus
Requires:       slf4j
Requires:       template-resolver
Requires:       test-interface

%if %{without bootstrap}
BuildRequires:  %{short_name}-bootstrap
Obsoletes:      %{short_name}-bootstrap

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

%if !%{do_proper}
%patch0 -p1
%endif

%patch2 -p1

%if !%{do_proper}
%patch4 -p1
%endif

sed -i -e '/% "test"/d' project/Util.scala

cp %{SOURCE15} .
chmod 755 climbing-nemesis.py

cp %{SOURCE16} .
cp %{SOURCE17} .

mkdir %{ivy_local_dir}

%if %{with bootstrap}
cp %{SOURCE63} .
%endif

./climbing-nemesis.py org.scala-lang scala-library %{ivy_local_dir} --version %{scala_version}
./climbing-nemesis.py org.scala-lang scala-compiler %{ivy_local_dir} --version %{scala_version}
./climbing-nemesis.py org.scala-lang scala-reflect %{ivy_local_dir} --version %{scala_version}

./climbing-nemesis.py org.scala-tools.sbinary sbinary_%{scala_short_version} %{ivy_local_dir} --version 0.4.2
./climbing-nemesis.py jline jline %{ivy_local_dir} --version %{jline_version}
./climbing-nemesis.py com.jcraft jsch %{ivy_local_dir} --version 0.1.50
./climbing-nemesis.py junit junit %{ivy_local_dir} --version 4.11
./climbing-nemesis.py org.hamcrest hamcrest-core %{ivy_local_dir} --version 1.3
./climbing-nemesis.py org.apache.commons commons-lang3 %{ivy_local_dir} --version 3.8.1

./climbing-nemesis.py org.fusesource.jansi jansi %{ivy_local_dir} --version %{jansi_version}
./climbing-nemesis.py org.scala-sbt serialization_%{scala_short_version} %{ivy_local_dir} --version %{sbt_serialization_version}
./climbing-nemesis.py org.json4s json4s-core_%{scala_short_version} %{ivy_local_dir} --version 3.2.10
./climbing-nemesis.py org.json4s json4s-ast_%{scala_short_version} %{ivy_local_dir} --version 3.2.7
./climbing-nemesis.py org.json4s json4s-ast_%{scala_short_version} %{ivy_local_dir} --version 3.2.10
./climbing-nemesis.py org.json4s json4s-ast_%{scala_short_version} %{ivy_local_dir} --version 3.6.3
./climbing-nemesis.py org.typelevel jawn-parser_%{scala_short_version} %{ivy_local_dir} --version 0.14.1
./climbing-nemesis.py org.typelevel jawn-json4s_%{scala_short_version} %{ivy_local_dir} --version 0.14.1
./climbing-nemesis.py org.typelevel jawn-util_%{scala_short_version} %{ivy_local_dir} --version 0.14.1
./climbing-nemesis.py org.fusesource.jansi jansi-native %{ivy_local_dir} --version 1.8
./climbing-nemesis.py org.fusesource.hawtjni hawtjni-runtime %{ivy_local_dir} --version 1.16
./climbing-nemesis.py org.apache.ivy ivy %{ivy_local_dir} --version 2.4.0

./climbing-nemesis.py org.scala-sbt launcher-interface %{ivy_local_dir} --version %{sbt_launcher_version}
./climbing-nemesis.py org.scala-sbt launcher-implementation %{ivy_local_dir} --version %{sbt_launcher_version}

./climbing-nemesis.py org.scala-lang.modules scala-pickling_%{scala_short_version} %{ivy_local_dir} --version %{scala_pickling_version}
./climbing-nemesis.py com.thoughtworks.paranamer paranamer %{ivy_local_dir} --version 2.6
./climbing-nemesis.py org.scalamacros quasiquotes_%{scala_short_version} %{ivy_local_dir} --version 2.0.1

./climbing-nemesis.py org.scala-sbt template-resolver %{ivy_local_dir} --version %{template_resolver_version}

./climbing-nemesis.py org.codehaus.plexus plexus-component-annotations %{ivy_local_dir} --version 1.6
./climbing-nemesis.py org.codehaus.plexus plexus-classworlds %{ivy_local_dir} --version 2.5.2
./climbing-nemesis.py org.codehaus.plexus plexus-utils %{ivy_local_dir} --version 3.0.22
./climbing-nemesis.py org.codehaus.plexus plexus-utils %{ivy_local_dir} --version 3.2.1
./climbing-nemesis.py org.eclipse.aether aether-api %{ivy_local_dir} --version 1.3.1
./climbing-nemesis.py org.apache.maven.resolver maven-resolver-api %{ivy_local_dir} --version 1.4.1
./climbing-nemesis.py org.eclipse.aether aether-spi %{ivy_local_dir} --version 1.3.1
./climbing-nemesis.py org.apache.maven.resolver maven-resolver-spi %{ivy_local_dir} --version 1.4.1
./climbing-nemesis.py org.eclipse.aether aether-util %{ivy_local_dir} --version 1.3.1
./climbing-nemesis.py org.apache.maven.resolver maven-resolver-util %{ivy_local_dir} --version 1.4.1
./climbing-nemesis.py org.apache.maven maven-model %{ivy_local_dir}  --version 3.2.3
./climbing-nemesis.py org.apache.maven maven-model %{ivy_local_dir}  --version 3.6.2
./climbing-nemesis.py org.apache.maven maven-model-builder %{ivy_local_dir} --version 3.2.3
./climbing-nemesis.py org.apache.maven maven-model-builder %{ivy_local_dir} --version 3.6.2
./climbing-nemesis.py org.apache.maven maven-repository-metadata %{ivy_local_dir} --version 3.2.3
./climbing-nemesis.py org.apache.maven maven-repository-metadata %{ivy_local_dir} --version 3.6.2
./climbing-nemesis.py org.apache.maven maven-builder-support %{ivy_local_dir} --version 3.6.2
./climbing-nemesis.py org.apache.maven maven-artifact %{ivy_local_dir} --version 3.6.2
./climbing-nemesis.py org.codehaus.plexus plexus-utils %{ivy_local_dir} --version 3.0.17
./climbing-nemesis.py org.codehaus.plexus plexus-interpolation %{ivy_local_dir} --version 1.25
./climbing-nemesis.py org.eclipse.sisu org.eclipse.sisu.inject %{ivy_local_dir} --version 0.3.0.M1
./climbing-nemesis.py org.eclipse.sisu org.eclipse.sisu.inject %{ivy_local_dir} --version 0.3.3

./climbing-nemesis.py org.slf4j slf4j-api %{ivy_local_dir} --version 1.7.25

./climbing-nemesis.py com.google.guava guava %{ivy_local_dir} --version 18.0 --ignore "jsr305"
./climbing-nemesis.py com.google.code.findbugs jsr305 %{ivy_local_dir} --version 1.3.9
./climbing-nemesis.py javax.inject javax.inject %{ivy_local_dir} --version 1
./climbing-nemesis.py org.eclipse.sisu org.eclipse.sisu.plexus %{ivy_local_dir} --version 0.3.0.M1
./climbing-nemesis.py org.eclipse.aether aether-impl %{ivy_local_dir} --version 1.0.1.v20141111
./climbing-nemesis.py org.apache.maven.resolver maven-resolver-impl %{ivy_local_dir} --version 1.4.1
./climbing-nemesis.py org.eclipse.aether aether-connector-basic %{ivy_local_dir} --version 1.0.1.v20141111
./climbing-nemesis.py org.apache.maven maven-aether-provider %{ivy_local_dir} --version 3.2.3

# test-interface
./climbing-nemesis.py org.scala-sbt test-interface %{ivy_local_dir} --version %{testinterface_version}

./climbing-nemesis.py --jarfile %{SOURCE34} --ivyfile %{SOURCE134} org.scala-sbt compiler-interface %{ivy_local_dir} --version %{sbt_bootstrap_version}

%if %{with bootstrap}
cp %{SOURCE171} org.scala-sbt.sbt-%{sbt_bootstrap_version}.ivy.xml
sed -i -e '/precompiled/d' org.scala-sbt.sbt-%{sbt_bootstrap_version}.ivy.xml

./climbing-nemesis.py --jarfile %{SOURCE71} --ivyfile org.scala-sbt.sbt-%{sbt_bootstrap_version}.ivy.xml org.scala-sbt sbt %{ivy_local_dir} --version %{sbt_bootstrap_version}
./climbing-nemesis.py --jarfile %{SOURCE57} --ivyfile %{SOURCE157} org.scala-sbt main %{ivy_local_dir} --version %{sbt_bootstrap_version}
./climbing-nemesis.py --jarfile %{SOURCE62} --ivyfile %{SOURCE162} org.scala-sbt actions %{ivy_local_dir} --version %{sbt_bootstrap_version}
./climbing-nemesis.py --jarfile %{SOURCE52} --ivyfile %{SOURCE152} org.scala-sbt main-settings %{ivy_local_dir} --version %{sbt_bootstrap_version}
./climbing-nemesis.py --jarfile %{SOURCE32} --ivyfile %{SOURCE132} org.scala-sbt ivy %{ivy_local_dir} --version %{sbt_bootstrap_version}
./climbing-nemesis.py --jarfile %{SOURCE33} --ivyfile %{SOURCE133} org.scala-sbt task-system %{ivy_local_dir} --version %{sbt_bootstrap_version}
./climbing-nemesis.py --jarfile %{SOURCE36} --ivyfile %{SOURCE136} org.scala-sbt testing %{ivy_local_dir} --version %{sbt_bootstrap_version}
./climbing-nemesis.py --jarfile %{SOURCE37} --ivyfile %{SOURCE137} org.scala-sbt command %{ivy_local_dir} --version %{sbt_bootstrap_version}
./climbing-nemesis.py --jarfile %{SOURCE40} --ivyfile %{SOURCE140} org.scala-sbt run %{ivy_local_dir} --version %{sbt_bootstrap_version}
./climbing-nemesis.py --jarfile %{SOURCE41} --ivyfile %{SOURCE141} org.scala-sbt compiler-ivy-integration %{ivy_local_dir} --version %{sbt_bootstrap_version}
./climbing-nemesis.py --jarfile %{SOURCE55} --ivyfile %{SOURCE155} org.scala-sbt compiler-integration %{ivy_local_dir} --version %{sbt_bootstrap_version}
./climbing-nemesis.py --jarfile %{SOURCE56} --ivyfile %{SOURCE156} org.scala-sbt api %{ivy_local_dir} --version %{sbt_bootstrap_version}
./climbing-nemesis.py --jarfile %{SOURCE58} --ivyfile %{SOURCE158} org.scala-sbt classpath %{ivy_local_dir} --version %{sbt_bootstrap_version}
./climbing-nemesis.py --jarfile %{SOURCE61} --ivyfile %{SOURCE161} org.scala-sbt process %{ivy_local_dir} --version %{sbt_bootstrap_version}
./climbing-nemesis.py --jarfile %{SOURCE65} --ivyfile %{SOURCE165} org.scala-sbt tracking %{ivy_local_dir} --version %{sbt_bootstrap_version}
./climbing-nemesis.py --jarfile %{SOURCE66} --ivyfile %{SOURCE166} org.scala-sbt tasks %{ivy_local_dir} --version %{sbt_bootstrap_version}
./climbing-nemesis.py --jarfile %{SOURCE67} --ivyfile %{SOURCE167} org.scala-sbt completion %{ivy_local_dir} --version %{sbt_bootstrap_version}
./climbing-nemesis.py --jarfile %{SOURCE69} --ivyfile %{SOURCE169} org.scala-sbt relation %{ivy_local_dir} --version %{sbt_bootstrap_version}
./climbing-nemesis.py --jarfile %{SOURCE73} --ivyfile %{SOURCE173} org.scala-sbt logic %{ivy_local_dir} --version %{sbt_bootstrap_version}

./climbing-nemesis.py --jarfile %{SOURCE51} --ivyfile %{SOURCE151} org.scala-sbt interface %{ivy_local_dir} --version %{sbt_bootstrap_version}
./climbing-nemesis.py --jarfile %{SOURCE70} --ivyfile %{SOURCE170} org.scala-sbt io %{ivy_local_dir} --version %{sbt_bootstrap_version}
./climbing-nemesis.py --jarfile %{SOURCE68} --ivyfile %{SOURCE168} org.scala-sbt cross %{ivy_local_dir} --version %{sbt_bootstrap_version}
./climbing-nemesis.py --jarfile %{SOURCE47} --ivyfile %{SOURCE147} org.scala-sbt control %{ivy_local_dir} --version %{sbt_bootstrap_version}

./climbing-nemesis.py --jarfile %{SOURCE46} --ivyfile %{SOURCE146} org.scala-sbt classfile %{ivy_local_dir} --version %{sbt_bootstrap_version}
./climbing-nemesis.py --jarfile %{SOURCE53} --ivyfile %{SOURCE153} org.scala-sbt incremental-compiler %{ivy_local_dir} --version %{sbt_bootstrap_version}
./climbing-nemesis.py --jarfile %{SOURCE60} --ivyfile %{SOURCE160} org.scala-sbt compile %{ivy_local_dir} --version %{sbt_bootstrap_version}
./climbing-nemesis.py --jarfile %{SOURCE45} --ivyfile %{SOURCE145} org.scala-sbt persist %{ivy_local_dir} --version %{sbt_bootstrap_version}
./climbing-nemesis.py --jarfile %{SOURCE59} --ivyfile %{SOURCE159} org.scala-sbt logging %{ivy_local_dir} --version %{sbt_bootstrap_version}
./climbing-nemesis.py --jarfile %{SOURCE54} --ivyfile %{SOURCE154} org.scala-sbt cache %{ivy_local_dir} --version %{sbt_bootstrap_version}
./climbing-nemesis.py --jarfile %{SOURCE38} --ivyfile %{SOURCE138} org.scala-sbt test-agent %{ivy_local_dir} --version %{sbt_bootstrap_version}

./climbing-nemesis.py --jarfile %{SOURCE44} --ivyfile %{SOURCE144} org.scala-sbt collections %{ivy_local_dir} --version %{sbt_bootstrap_version}

./climbing-nemesis.py --jarfile %{SOURCE49} --ivyfile %{SOURCE149} org.scala-sbt apply-macro %{ivy_local_dir} --version %{sbt_bootstrap_version}

./climbing-nemesis.py --jarfile %{SOURCE51} --ivyfile %{SOURCE151} org.scala-sbt interface %{ivy_local_dir} --version %{sbt_bootstrap_version}
./climbing-nemesis.py --jarfile %{SOURCE70} --ivyfile %{SOURCE170} org.scala-sbt io %{ivy_local_dir} --version %{sbt_bootstrap_version}

./climbing-nemesis.py org.apache.ivy ivy %{ivy_local_dir} --version %{sbt_bootstrap_ivy_version} --override org.scala-sbt.ivy:ivy

%if %{?want_specs2}
./climbing-nemesis.py org.specs2 specs2_%{scala_short_version} %{ivy_local_dir} --version %{specs2_version} --jarfile %{SOURCE79}
%endif # want_specs2

# scalacheck
%if %{?want_scalacheck}
./climbing-nemesis.py --jarfile %{SOURCE78} org.scalacheck scalacheck %{ivy_local_dir} --version %{scalacheck_version} --scala %{scala_short_version}
%endif # want_scalacheck

%if %{?want_sxr}
./climbing-nemesis.py --jarfile %{SOURCE77} org.scala-sbt.sxr sxr %{ivy_local_dir} --version %{sxr_version} --scala %{scala_short_version}
./climbing-nemesis.py --jarfile %{SOURCE77} org.scala-sbt sxr %{ivy_local_dir} --version %{sxr_version} --scala %{scala_short_version}
%endif # want_sxr

%if %{do_proper}
./climbing-nemesis.py --jarfile %{SOURCE74} com.typesafe.sbt sbt-ghpages %{ivy_local_dir} --version %{sbt_ghpages_version} --meta e:scalaVersion=%{scala_short_version} --meta e:sbtVersion=%{sbt_short_version}
./climbing-nemesis.py --jarfile %{SOURCE75} com.typesafe.sbt sbt-site %{ivy_local_dir} --version %{sbt_site_version} --meta e:scalaVersion=%{scala_short_version} --meta e:sbtVersion=%{sbt_short_version}
./climbing-nemesis.py --jarfile %{SOURCE76} com.typesafe.sbt sbt-git %{ivy_local_dir} --version %{sbt_git_version} --meta e:scalaVersion=%{scala_short_version} --meta e:sbtVersion=%{sbt_short_version}

./climbing-nemesis.py --jarfile %{SOURCE90} --ivyfile %{SOURCE190} com.eed3si9n sbt-doge %{ivy_local_dir} --version %{sbt_doge_version}
./climbing-nemesis.py --jarfile %{SOURCE91} --ivyfile %{SOURCE191} com.typesafe.sbt sbt-javaversioncheck %{ivy_local_dir} --version %{sbt_jvcheck_version}
./climbing-nemesis.py --jarfile %{SOURCE92} --ivyfile %{SOURCE192} com.typesafe.sbt sbt-scalariform %{ivy_local_dir} --version %{sbt_scalariform_version}
./climbing-nemesis.py --jarfile %{SOURCE93} --ivyfile %{SOURCE193} com.jsuereth sbt-pgp %{ivy_local_dir} --version %{sbt_pgp_version}
./climbing-nemesis.py --jarfile %{SOURCE94} --ivyfile %{SOURCE194} com.eed3si9n sbt-assembly %{ivy_local_dir} --version %{sbt_assembly_version}
./climbing-nemesis.py --jarfile %{SOURCE95} --ivyfile %{SOURCE195} org.foundweekends sbt-bintray %{ivy_local_dir} --version %{sbt_bintray_version}
%endif

# dispatch-http
%if %{?want_dispatch_http}
./climbing-nemesis.py --jarfile %{SOURCE81} net.databinder dispatch-http_%{scala_short_version} %{ivy_local_dir} --version %{dispatch_http_version}
%endif

%else
# If we aren't bootstrapping, copy installed jars into local ivy cache
# dir.  In the future, we'll use Mikołaj's new xmvn Ivy resolver.

# sbt components
for jar in actions api apply-macro cache classfile classpath collections command compile compiler-integration compiler-ivy-integration completion control cross datatype-generator incremental-compiler interface io ivy logging logic main main-settings persist process relation run sbt scripted-framework scripted-plugin scripted-sbt tasks task-system test-agent testing tracking; do
    ./climbing-nemesis.py --jarfile %{_javadir}/%{short_name}/${jar}.jar --ivyfile %{installed_ivy_local}/org.scala-sbt/${jar}/%{sbt_bootstrap_version}/ivy.xml org.scala-sbt ${jar} %{ivy_local_dir}
done

%endif # with bootstrap

%if !%{do_proper}
sed -i -e '/sbt-doge/d' project/plugins.sbt
sed -i -e '/sbt-ghpages/d' project/plugins.sbt
sed -i -e '/sbt-git/d' project/plugins.sbt
sed -i -e '/sbt-javaversioncheck/d' project/plugins.sbt
sed -i -e '/sbt-pgp/d' project/plugins.sbt
sed -i -e '/sbt-scalariform/d' project/plugins.sbt
sed -i -e '/sbt-site/d' project/plugins.sbt
sed -i -e '/sbt-bintray/d' project/plugins.sbt
sed -i -e '/sbt-assembly/d' project/plugins.sbt
rm -f main/src/main/scala/sbt/plugins/Giter8ResolverPlugin.scala
sed -i '/sbt.plugins.Giter8TemplatePlugin/d' main/src/main/scala/sbt/PluginDiscovery.scala 
sed -i 's/sbt.plugins.JUnitXmlReportPlugin,/sbt.plugins.JUnitXmlReportPlugin/' main/src/main/scala/sbt/PluginDiscovery.scala
#sed -i "/templateResolverApi/d" project/Dependencies.scala 
#sed -i "/templateResolverApi/d" build.sbt
%endif

for props in rpmbuild-sbt.boot.properties sbt.boot.properties ; do
    sed -i -e 's/FEDORA_SCALA_VERSION/%{scala_version}/g' $props
    sed -i -e 's/FEDORA_SBT_VERSION/%{sbt_version}/g' $props
done

sed -i -e 's/0[.]13[.]17/%{sbt_bootstrap_version}/g' project/build.properties

sed -i -e 's/["]2[.]10[.][23456]["]/\"%{scala_version}\"/g' $(find . -name \*.sbt -type f) $(find . -name \*.xml) $(find . -name \*.scala)

sed -i -e 's#org\.scala-sbt\.ivy#org.apache.ivy#g' project/Dependencies.scala
sed -i -e 's#2[.]3[.]0-sbt-.*["]#2.4.0\"#g' project/Dependencies.scala

%if !%{do_proper}
rm -f project/Docs.scala
rm -f project/Formatting.scala
rm -f project/NightlyPlugin.scala
rm -f project/Release.scala
rm -f project/SiteMap.scala
rm -f project/StatusPlugin.scala
%endif

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

%build

%if %{with bootstrap}
java \
  -Xms512M -Xmx1536M -Xss1M -XX:+CMSClassUnloadingEnabled \
  -Dfedora.sbt.ivy.dir=$PWD/%{ivy_local_dir} -Dfedora.sbt.boot.dir=$PWD/sbt-boot-dir/ \
  -Divy.checksums='""' -Dsbt.boot.properties=$PWD/rpmbuild-sbt.boot.properties -Dsbt.log.noformat=true \
  -jar sbt-launch-%{sbt_bootstrap_version}.jar package "set publishTo in Global := Some(Resolver.file(\"published\", file(\"published\"))(Resolver.ivyStylePatterns) ivys \"$(pwd)/published/[organization]/[module]/[revision]/ivy.xml\" artifacts \"$(pwd)/published/[organization]/[module]/[revision]/[artifact]-[revision].[ext]\")" publish makePom
%else
export SBT_IVY_DIR=$PWD/%{ivy_local_dir}
export SBT_BOOT_DIR=$PWD/sbt-boot-dir/
export SBT_BOOT_PROPERTIES=rpmbuild-sbt.boot.properties
sbt -Dsbt.log.noformat=true package "set publishTo in Global := Some(Resolver.file(\"published\", file(\"published\"))(Resolver.ivyStylePatterns) ivys \"$(pwd)/published/[organization]/[module]/[revision]/ivy.xml\" artifacts \"$(pwd)/published/[organization]/[module]/[revision]/[artifact]-[revision].[ext]\")" publish makePom
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

rm -f %{buildroot}/%{_javadir}/%{short_name}/sbt-launch*.jar

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

for bootjar in $(find %{buildroot}/%{installed_ivy_local}/org.scala-sbt/*/%{sbt_version}/ -name \*-%{sbt_version}.jar) ; do
rm -f $bootjar
ln -s %{_javadir}/%{short_name}/$(basename $bootjar -%{sbt_version}.jar).jar $bootjar
done

%if %{with bootstrap}

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

find %{buildroot}/%{_datadir}/%{short_name} -name \*launcher-interface\* | xargs rm -rf
./climbing-nemesis.py org.scala-sbt launcher-interface %{buildroot}/%{installed_ivy_local} --version %{sbt_launcher_version}

find %{buildroot}/%{_datadir}/%{short_name} -name \*launcher-implementation\* | xargs rm -rf
./climbing-nemesis.py org.scala-sbt launcher-implementation %{buildroot}/%{installed_ivy_local} --version %{sbt_launcher_version}

### install POM files
mkdir -p %{buildroot}/%{_mavenpomdir}
rm -f .rpm_pomfiles
touch .rpm_pomfiles
declare -a shortnames

for pom in $(find ./*/ -name \*%{sbt_full_version}.pom -a ! -name \*sbtroot\*) ; do 
    shortname=$(echo $pom | sed -e 's/^.*[/]\([a-z-]\+\)-%{sbt_full_version}.pom$/\1/g')
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
%{_sysconfdir}/%{short_name}

%doc README.md
%license LICENSE NOTICE

%changelog
