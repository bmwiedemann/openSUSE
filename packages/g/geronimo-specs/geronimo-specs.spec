#
# spec file for package geronimo-specs
#
# Copyright (c) 2023 SUSE LLC
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


%define bname geronimo
Name:           geronimo-specs
Version:        1.2
Release:        0
Summary:        Geronimo J2EE server J2EE specifications
License:        Apache-2.0
Group:          Development/Languages/Java
URL:            https://geronimo.apache.org
Source0:        %{name}-%{version}-src.tar.xz
# STEPS TO CREATE THE SOURCE FILE
# mkdir geronimo-specs-1.2
# cd geronimo-specs-1.2
# svn export http://svn.apache.org/repos/asf/geronimo/specs/tags/geronimo-activation_1.0.2_spec-1.2/
# svn export http://svn.apache.org/repos/asf/geronimo/specs/tags/geronimo-activation_1.1_spec-1.0/
# svn export http://svn.apache.org/repos/asf/geronimo/specs/tags/geronimo-annotation_1.0_spec-1.1.0/
# svn export http://svn.apache.org/repos/asf/geronimo/specs/tags/geronimo-j2ee-connector_1.5_spec-1.1.1/
# svn export http://svn.apache.org/repos/asf/geronimo/specs/tags/geronimo-jaxrpc_1.1_spec-1.1/
# svn export http://svn.apache.org/repos/asf/geronimo/specs/tags/geronimo-jms_1.1_spec-1.1/
# svn export http://svn.apache.org/repos/asf/geronimo/specs/tags/geronimo-jpa_3.0_spec-1.1.0/
# svn export http://svn.apache.org/repos/asf/geronimo/specs/tags/geronimo-jta_1.0.1B_spec-1.1.1/
# svn export http://svn.apache.org/repos/asf/geronimo/specs/tags/geronimo-jta_1.1_spec-1.1.0/
# svn export http://svn.apache.org/repos/asf/geronimo/specs/tags/geronimo-qname_1.1_spec-1.1/
# svn export http://svn.apache.org/repos/asf/geronimo/specs/tags/geronimo-saaj_1.1_spec-1.1/
# svn export http://svn.apache.org/repos/asf/geronimo/specs/tags/geronimo-servlet_2.4_spec-1.1.1/
# svn export http://svn.apache.org/repos/asf/geronimo/specs/tags/geronimo-servlet_2.5_spec-1.1/
# # AND
# curl -O http://svn.apache.org/repos/asf/geronimo/specs/trunk/pom.xml
# curl -O http://svn.apache.org/repos/asf/geronimo/specs/trunk/LICENSE.txt
# curl -O http://svn.apache.org/repos/asf/geronimo/specs/trunk/NOTICE.txt
# curl -O http://svn.apache.org/repos/asf/geronimo/specs/trunk/README.txt
#
Source1000:     geronimo-specs.build.xml
Source1001:     undot.py
BuildRequires:  ant
BuildRequires:  fdupes
BuildRequires:  java-devel >= 1.8
BuildRequires:  javapackages-local >= 6
BuildArch:      noarch

%description
Geronimo is Apache's ASF-licenced J2EE server project. These are the
J2EE-Specifications Note: You should use the subpackages for the
Specifications that you actually need.	The ones installed by the main
package are deprecated and will disapear in future releases.

%package -n geronimo-jaf-1_0_2-api
Summary:        Geronimo Activation 1.0.2 Specification
Group:          Development/Languages/Java
Obsoletes:      %{name}-poms

%description -n geronimo-jaf-1_0_2-api
Geronimo is Apache's ASF-licenced J2EE server project. These are the
J2EE-Specifications: Java Activation Framework

%package -n geronimo-jaf-1_1-api
Summary:        Geronimo Activation 1.1 Specification
Group:          Development/Languages/Java
Obsoletes:      %{name}-poms

%description -n geronimo-jaf-1_1-api
Geronimo is Apache's ASF-licenced J2EE server project. These are the
J2EE-Specifications Note: You should use the subpackages for the
Specifications that you actually need.	The ones installed by the main
package are deprecated and will disapear in future releases.

%package -n geronimo-annotation-1_0-api
Summary:        Geronimo Annotation 1.0 Specification
Group:          Development/Languages/Java
Obsoletes:      %{name}-poms

%description -n geronimo-annotation-1_0-api
Geronimo is Apache's ASF-licenced J2EE server project. These are the
J2EE-Specifications Note: You should use the subpackages for the
Specifications that you actually need.	The ones installed by the main
package are deprecated and will disapear in future releases.

%package -n geronimo-j2ee-connector-1_5-api
Summary:        Geronimo J2EE server J2EE specifications
Group:          Development/Languages/Java
Requires:       geronimo-jta-1_0_1B-api
Obsoletes:      %{name}-poms
Obsoletes:      j2ee-connector

%description -n geronimo-j2ee-connector-1_5-api
Geronimo is Apache's ASF-licenced J2EE server project. These are the
J2EE-Specifications: J2EE Connector Architecture Specification

%package -n geronimo-jaxrpc-1_1-api
Summary:        Geronimo JAXRPC 1.1 Specification
Group:          Development/Languages/Java
Requires:       geronimo-qname-1_1-api
Requires:       geronimo-saaj-1_1-api
Requires:       geronimo-servlet-2_4-api
Obsoletes:      %{name}-poms

%description -n geronimo-jaxrpc-1_1-api
Geronimo is Apache's ASF-licenced J2EE server project. These are the
J2EE-Specifications: Java API for XML-Based RPC (JAXRPC)

%package -n geronimo-jms-1_1-api
Summary:        Geronimo JMS 1.1 Specification
Group:          Development/Languages/Java
Obsoletes:      %{name}-poms
Obsoletes:      jms

%description -n geronimo-jms-1_1-api
Geronimo is Apache's ASF-licenced J2EE server project. These are the
J2EE-Specifications: JMS Specification

%package -n geronimo-jpa-3_0-api
Summary:        Geronimo JPA 1.0 Specification
Group:          Development/Languages/Java
Obsoletes:      %{name}-poms

%description -n geronimo-jpa-3_0-api
Geronimo is Apache's ASF-licenced J2EE server project. These are the
J2EE-Specifications Note: You should use the subpackages for the
Specifications that you actually need.	The ones installed by the main
package are deprecated and will disapear in future releases.

%package -n geronimo-jta-1_0_1B-api
Summary:        Geronimo JTA 1.0.1B Specification
Group:          Development/Languages/Java
Obsoletes:      %{name}-poms

%description -n geronimo-jta-1_0_1B-api
Geronimo is Apache's ASF-licenced J2EE server project. These are the
J2EE-Specifications: Java Transaction API Specification

%package -n geronimo-jta-1_1-api
Summary:        Geronimo JTA 1.1 Specification
Group:          Development/Languages/Java
Obsoletes:      %{name}-poms

%description -n geronimo-jta-1_1-api
Geronimo is Apache's ASF-licenced J2EE server project. These are the
J2EE-Specifications Note: You should use the subpackages for the
Specifications that you actually need.	The ones installed by the main
package are deprecated and will disapear in future releases.

%package -n geronimo-qname-1_1-api
Summary:        Geronimo QName 1.1 Specification
Group:          Development/Languages/Java
Obsoletes:      %{name}-poms

%description -n geronimo-qname-1_1-api
Geronimo is Apache's ASF-licenced J2EE server project. These are the
J2EE-Specifications: javax.xml.namespace.QName API

%package -n geronimo-saaj-1_1-api
Summary:        Geronimo SAAJ 1.1 Specification
Group:          Development/Languages/Java
Requires:       geronimo-jaf-1_0_2-api
Obsoletes:      %{name}-poms

%description -n geronimo-saaj-1_1-api
Geronimo is Apache's ASF-licenced J2EE server project. These are the
J2EE-Specifications: SOAP with Attachments API for Java (SAAJ)

%package -n geronimo-servlet-2_4-api
Summary:        Geronimo Servlet 2.4 Specification
Group:          Development/Languages/Java
Obsoletes:      %{name}-poms

%description -n geronimo-servlet-2_4-api
Geronimo is Apache's ASF-licenced J2EE server project. These are the
J2EE-Specifications: J2EE Servlet v2.4 API

%package -n geronimo-servlet-2_5-api
Summary:        Geronimo Servlet 2.5 Specification
Group:          Development/Languages/Java
Obsoletes:      %{name}-poms

%description -n geronimo-servlet-2_5-api
Geronimo is Apache's ASF-licenced J2EE server project. These are the
J2EE-Specifications Note: You should use the subpackages for the
Specifications that you actually need.	The ones installed by the main
package are deprecated and will disapear in future releases.

%prep
%setup -q
chmod -R go=u-w *
cp %{SOURCE1000} build.xml

%build
%{ant} -Dant.build.javac.source=8 -Dant.build.javac.target=8

%install
set +x
# Directory for poms
install -d -m 0755 %{buildroot}/%{_mavenpomdir}
# subpackage jars
install -d -m 755 %{buildroot}%{_javadir}
install -m 0644 \
  geronimo-activation_1.0.2_spec-1.2/target/geronimo-activation_1.0.2_spec-1.2.jar \
  %{buildroot}%{_javadir}/geronimo-jaf-1.0.2-api.jar
%{mvn_install_pom} geronimo-activation_1.0.2_spec-1.2/pom.xml \
  %{buildroot}/%{_mavenpomdir}/JPP-geronimo-jaf-1.0.2-api.pom
%add_maven_depmap JPP-geronimo-jaf-1.0.2-api.pom geronimo-jaf-1.0.2-api.jar -f jaf-1.0.2-api

install -m 0644 \
  geronimo-activation_1.1_spec-1.0/target/geronimo-activation_1.1_spec-1.0.jar \
  %{buildroot}%{_javadir}/geronimo-jaf-1.1-api.jar
%{mvn_install_pom} geronimo-activation_1.1_spec-1.0/pom.xml \
  %{buildroot}/%{_mavenpomdir}/JPP-geronimo-jaf-1.1-api.pom
%add_maven_depmap JPP-geronimo-jaf-1.1-api.pom geronimo-jaf-1.1-api.jar -f jaf-1.1-api

install -m 0644 \
  geronimo-annotation_1.0_spec-1.1.0/target/geronimo-annotation_1.0_spec-1.1.jar \
  %{buildroot}%{_javadir}/geronimo-annotation-1.0-api.jar
%{mvn_install_pom} geronimo-annotation_1.0_spec-1.1.0/pom.xml \
  %{buildroot}/%{_mavenpomdir}/JPP-geronimo-annotation-1.0-api.pom
%add_maven_depmap JPP-geronimo-annotation-1.0-api.pom geronimo-annotation-1.0-api.jar -a "javax.annotation:jsr250-api,org.eclipse.jetty.orbit:javax.annotation" -f annotation-1.0-api

install -m 0644 \
  geronimo-j2ee-connector_1.5_spec-1.1.1/target/geronimo-j2ee-connector_1.5_spec-1.1.1.jar \
  %{buildroot}%{_javadir}/geronimo-j2ee-connector-1.5-api.jar
%{mvn_install_pom} geronimo-j2ee-connector_1.5_spec-1.1.1/pom.xml \
  %{buildroot}/%{_mavenpomdir}/JPP-geronimo-j2ee-connector-1.5-api.pom
%add_maven_depmap JPP-geronimo-j2ee-connector-1.5-api.pom geronimo-j2ee-connector-1.5-api.jar -f j2ee-connector-1.5-api

install -m 0644 \
  geronimo-jaxrpc_1.1_spec-1.1/target/geronimo-jaxrpc_1.1_spec-1.1.jar \
  %{buildroot}%{_javadir}/geronimo-jaxrpc-1.1-api.jar
%{mvn_install_pom} geronimo-jaxrpc_1.1_spec-1.1/pom.xml \
  %{buildroot}/%{_mavenpomdir}/JPP-geronimo-jaxrpc-1.1-api.pom
%add_maven_depmap JPP-geronimo-jaxrpc-1.1-api.pom geronimo-jaxrpc-1.1-api.jar -f jaxrpc-1.1-api

install -m 0644 \
  geronimo-jms_1.1_spec-1.1/target/geronimo-jms_1.1_spec-1.1.jar \
  %{buildroot}%{_javadir}/geronimo-jms-1.1-api.jar
%{mvn_install_pom} geronimo-jms_1.1_spec-1.1/pom.xml \
  %{buildroot}/%{_mavenpomdir}/JPP-geronimo-jms-1.1-api.pom
%add_maven_depmap JPP-geronimo-jms-1.1-api.pom geronimo-jms-1.1-api.jar -f jms-1.1-api -a javax.jms:jms

install -m 0644 \
  geronimo-jpa_3.0_spec-1.1.0/target/geronimo-jpa_3.0_spec-1.1.jar \
  %{buildroot}%{_javadir}/geronimo-jpa-3.0-api.jar
%{mvn_install_pom} geronimo-jpa_3.0_spec-1.1.0/pom.xml \
  %{buildroot}/%{_mavenpomdir}/JPP-geronimo-jpa-3.0-api.pom
%add_maven_depmap JPP-geronimo-jpa-3.0-api.pom geronimo-jpa-3.0-api.jar -f jpa-3.0-api -a javax.persistence:persistence-api

install -m 0644 \
  geronimo-jta_1.0.1B_spec-1.1.1/target/geronimo-jta_1.0.1B_spec-1.1.1.jar \
  %{buildroot}%{_javadir}/geronimo-jta-1.0.1B-api.jar
%{mvn_install_pom} geronimo-jta_1.0.1B_spec-1.1.1/pom.xml \
  %{buildroot}/%{_mavenpomdir}/JPP-geronimo-jta-1.0.1B-api.pom
%add_maven_depmap JPP-geronimo-jta-1.0.1B-api.pom geronimo-jta-1.0.1B-api.jar -f jta-1.0.1B-api

install -m 0644 \
  geronimo-jta_1.1_spec-1.1.0/target/geronimo-jta_1.1_spec-1.1.jar \
  %{buildroot}%{_javadir}/geronimo-jta-1.1-api.jar
%{mvn_install_pom} geronimo-jta_1.1_spec-1.1.0/pom.xml \
  %{buildroot}/%{_mavenpomdir}/JPP-geronimo-jta-1.1-api.pom
%add_maven_depmap JPP-geronimo-jta-1.1-api.pom geronimo-jta-1.1-api.jar -f jta-1.1-api -a "javax.transaction:jta,org.eclipse.jetty.orbit:javax.transaction"

install -m 0644 \
  geronimo-qname_1.1_spec-1.1/target/geronimo-qname_1.1_spec-1.1.jar \
  %{buildroot}%{_javadir}/geronimo-qname-1.1-api.jar
%{mvn_install_pom} geronimo-qname_1.1_spec-1.1/pom.xml \
  %{buildroot}/%{_mavenpomdir}/JPP-geronimo-qname-1.1-api.pom
%add_maven_depmap JPP-geronimo-qname-1.1-api.pom geronimo-qname-1.1-api.jar -f qname-1.1-api

install -m 0644 \
  geronimo-saaj_1.1_spec-1.1/target/geronimo-saaj_1.1_spec-1.1.jar \
  %{buildroot}%{_javadir}/geronimo-saaj-1.1-api.jar
%{mvn_install_pom} geronimo-saaj_1.1_spec-1.1/pom.xml \
  %{buildroot}/%{_mavenpomdir}/JPP-geronimo-saaj-1.1-api.pom
%add_maven_depmap JPP-geronimo-saaj-1.1-api.pom geronimo-saaj-1.1-api.jar -f saaj-1.1-api

install -m 0644 \
  geronimo-servlet_2.4_spec-1.1.1/target/geronimo-servlet_2.4_spec-1.1.1.jar \
  %{buildroot}%{_javadir}/geronimo-servlet-2.4-api.jar
%{mvn_install_pom} geronimo-servlet_2.4_spec-1.1.1/pom.xml \
  %{buildroot}/%{_mavenpomdir}/JPP-geronimo-servlet-2.4-api.pom
%add_maven_depmap JPP-geronimo-servlet-2.4-api.pom geronimo-servlet-2.4-api.jar -f servlet-2.4-api

install -m 0644 \
  geronimo-servlet_2.5_spec-1.1/target/geronimo-servlet_2.5_spec-1.1.jar \
  %{buildroot}%{_javadir}/geronimo-servlet-2.5-api.jar
%{mvn_install_pom} geronimo-servlet_2.5_spec-1.1/pom.xml \
  %{buildroot}/%{_mavenpomdir}/JPP-geronimo-servlet-2.5-api.pom
%add_maven_depmap JPP-geronimo-servlet-2.5-api.pom geronimo-servlet-2.5-api.jar -f servlet-2.5-api

%files -n geronimo-jaf-1_0_2-api -f .mfiles-jaf-1.0.2-api
%license geronimo-activation_1.0.2_spec-1.2/LICENSE.txt

%files -n geronimo-jaf-1_1-api -f .mfiles-jaf-1.1-api
%license geronimo-activation_1.1_spec-1.0/LICENSE.txt

%files -n geronimo-annotation-1_0-api -f .mfiles-annotation-1.0-api
%license geronimo-annotation_1.0_spec-1.1.0/LICENSE.txt

%files -n geronimo-j2ee-connector-1_5-api -f .mfiles-j2ee-connector-1.5-api
%license geronimo-j2ee-connector_1.5_spec-1.1.1/LICENSE.txt

%files -n geronimo-jaxrpc-1_1-api -f .mfiles-jaxrpc-1.1-api
%license geronimo-jaxrpc_1.1_spec-1.1/LICENSE.txt

%files -n geronimo-jms-1_1-api -f .mfiles-jms-1.1-api
%license geronimo-jms_1.1_spec-1.1/LICENSE.txt

%files -n geronimo-jpa-3_0-api -f .mfiles-jpa-3.0-api
%license geronimo-jpa_3.0_spec-1.1.0/LICENSE.txt

%files -n geronimo-jta-1_0_1B-api -f .mfiles-jta-1.0.1B-api
%license geronimo-jta_1.0.1B_spec-1.1.1/LICENSE.txt

%files -n geronimo-jta-1_1-api -f .mfiles-jta-1.1-api
%license geronimo-jta_1.1_spec-1.1.0/LICENSE.txt

%files -n geronimo-qname-1_1-api -f .mfiles-qname-1.1-api
%license geronimo-qname_1.1_spec-1.1/LICENSE.txt

%files -n geronimo-saaj-1_1-api -f .mfiles-saaj-1.1-api
%license geronimo-saaj_1.1_spec-1.1/LICENSE.txt

%files -n geronimo-servlet-2_4-api -f .mfiles-servlet-2.4-api
%license geronimo-servlet_2.4_spec-1.1.1/LICENSE.txt

%files -n geronimo-servlet-2_5-api -f .mfiles-servlet-2.5-api
%license geronimo-servlet_2.5_spec-1.1/LICENSE.txt

%changelog
