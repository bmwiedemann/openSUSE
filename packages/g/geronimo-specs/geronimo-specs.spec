#
# spec file for package geronimo-specs
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


%define bname geronimo
Name:           geronimo-specs
Version:        1.2
Release:        0
Summary:        Geronimo J2EE server J2EE specifications
License:        Apache-2.0
Group:          Development/Languages/Java
URL:            http://geronimo.apache.org
Source0:        %{name}-%{version}-src.tar.bz2
# STEPS TO CREATE THE SOURCE FILE
# mkdir geronimo-specs-1.2
# cd geronimo-specs-1.2
# svn export http://svn.apache.org/repos/asf/geronimo/specs/tags/geronimo-activation_1.0.2_spec-1.2/
# svn export http://svn.apache.org/repos/asf/geronimo/specs/tags/geronimo-activation_1.1_spec-1.0/
# svn export http://svn.apache.org/repos/asf/geronimo/specs/tags/geronimo-annotation_1.0_spec-1.1.0/
# svn export http://svn.apache.org/repos/asf/geronimo/specs/tags/geronimo-ejb_2.1_spec-1.1/
# svn export http://svn.apache.org/repos/asf/geronimo/specs/tags/geronimo-ejb_3.0_spec-1.0/
# svn export http://svn.apache.org/repos/asf/geronimo/specs/tags/geronimo-el_1.0_spec-1.0/
# svn export http://svn.apache.org/repos/asf/geronimo/specs/tags/geronimo-interceptor_3.0_spec-1.0/
# svn export http://svn.apache.org/repos/asf/geronimo/specs/tags/geronimo-j2ee-connector_1.5_spec-1.1.1/
# svn export http://svn.apache.org/repos/asf/geronimo/specs/tags/geronimo-j2ee-deployment_1.1_spec-1.1/
# svn export http://svn.apache.org/repos/asf/geronimo/specs/tags/geronimo-j2ee-jacc_1.0_spec-1.1/
# svn export http://svn.apache.org/repos/asf/geronimo/specs/tags/geronimo-j2ee-management_1.0_spec-1.1/
# svn export http://svn.apache.org/repos/asf/geronimo/specs/tags/geronimo-j2ee-management_1.1_spec-1.0/
# svn export http://svn.apache.org/repos/asf/geronimo/specs/tags/geronimo-jacc_1.1_spec-1.0/
# svn export http://svn.apache.org/repos/asf/geronimo/specs/tags/geronimo-javaee-deployment_1.1MR3_spec-1.0/
# svn export http://svn.apache.org/repos/asf/geronimo/specs/tags/geronimo-javamail_1.3.1_spec-1.3/
# svn export http://svn.apache.org/repos/asf/geronimo/specs/tags/geronimo-javamail_1.4_spec-1.1/
# svn export http://svn.apache.org/repos/asf/geronimo/specs/tags/geronimo-jaxr_1.0_spec-1.1/
# svn export http://svn.apache.org/repos/asf/geronimo/specs/tags/geronimo-jaxrpc_1.1_spec-1.1/
# svn export http://svn.apache.org/repos/asf/geronimo/specs/tags/geronimo-jms_1.1_spec-1.1/
# svn export http://svn.apache.org/repos/asf/geronimo/specs/tags/geronimo-jpa_3.0_spec-1.1.0/
# svn export http://svn.apache.org/repos/asf/geronimo/specs/tags/geronimo-jsp_2.0_spec-1.1/
# svn export http://svn.apache.org/repos/asf/geronimo/specs/tags/geronimo-jsp_2.1_spec-1.0/
# svn export http://svn.apache.org/repos/asf/geronimo/specs/tags/geronimo-jta_1.0.1B_spec-1.1.1/
# svn export http://svn.apache.org/repos/asf/geronimo/specs/tags/geronimo-jta_1.1_spec-1.1.0/
# svn export http://svn.apache.org/repos/asf/geronimo/specs/tags/geronimo-qname_1.1_spec-1.1/
# svn export http://svn.apache.org/repos/asf/geronimo/specs/tags/geronimo-saaj_1.1_spec-1.1/
# svn export http://svn.apache.org/repos/asf/geronimo/specs/tags/geronimo-servlet_2.4_spec-1.1.1/
# svn export http://svn.apache.org/repos/asf/geronimo/specs/tags/geronimo-servlet_2.5_spec-1.1/
# svn export http://svn.apache.org/repos/asf/geronimo/specs/tags/geronimo-stax-api_1.0_spec-1.0/
# svn export http://svn.apache.org/repos/asf/geronimo/specs/tags/geronimo-ws-metadata_2.0_spec-1.1.1/
# # AND FOR COMPLETENESS
# svn export http://svn.apache.org/repos/asf/geronimo/specs/tags/1_1_1/geronimo-spec-commonj/
# svn export http://svn.apache.org/repos/asf/geronimo/specs/tags/1_1_1/geronimo-spec-corba/
# svn export http://svn.apache.org/repos/asf/geronimo/specs/tags/1_1_1/geronimo-spec-corba-2.3/
# svn export http://svn.apache.org/repos/asf/geronimo/specs/tags/1_1_1/geronimo-spec-corba-3.0/
# # AS WELL AS
# svn export http://svn.apache.org/repos/asf/geronimo/specs/trunk/geronimo-jaspi_1.0_spec/
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
BuildRequires:  javapackages-local
BuildRequires:  junit >= 3.8.1
BuildConflicts: java-devel >= 11
BuildArch:      noarch

%description
Geronimo is Apache's ASF-licenced J2EE server project. These are the
J2EE-Specifications Note: You should use the subpackages for the
Specifications that you actually need.	The ones installed by the main
package are deprecated and will disapear in future releases.

%package -n geronimo-commonj-1_1-apis
Summary:        Geronimo J2EE server J2EE specifications
Group:          Development/Languages/Java
Provides:       commonj_1_1_apis = %{version}
Provides:       commonj_apis = 1.1
Obsoletes:      %{name}-poms

%description -n geronimo-commonj-1_1-apis
Geronimo is Apache's ASF-licenced J2EE server project. These are the
J2EE-Specifications: CommonJ Spec

%package -n geronimo-jaf-1_0_2-api
Summary:        Geronimo J2EE server J2EE specifications
# Don't obsolete jaf, classpathx-jaf provides it
# Don't even obsolete it versioned, as sun-jaf is at 1.1
#Obsoletes:    jaf
Group:          Development/Languages/Java
Requires(pre):  update-alternatives
Provides:       jaf = 1.0.2
# TODO: drop asap
Provides:       activation_1_0_2_api = %{version}
Provides:       activation_api = 1.0.2
Provides:       jaf_1_0_2_api = %{version}
Provides:       jaf_api = 1.0.2
Obsoletes:      %{name}-poms

%description -n geronimo-jaf-1_0_2-api
Geronimo is Apache's ASF-licenced J2EE server project. These are the
J2EE-Specifications: Java Activation Framework

%package -n geronimo-jaf-1_1-api
Summary:        Geronimo J2EE server J2EE specifications
# Don't obsolete jaf, classpathx-jaf provides it
# Don't even obsolete it versioned, as sun-jaf is at 1.1
#Obsoletes:    jaf
Group:          Development/Languages/Java
Requires(pre):  update-alternatives
Provides:       jaf = 1.1
# TODO: drop asap
Provides:       activation_1_1_api = %{version}
Provides:       activation_api = 1.1
Provides:       jaf_1_1_api = %{version}
Provides:       jaf_api = 1.1
Obsoletes:      %{name}-poms

%description -n geronimo-jaf-1_1-api
Geronimo is Apache's ASF-licenced J2EE server project. These are the
J2EE-Specifications Note: You should use the subpackages for the
Specifications that you actually need.	The ones installed by the main
package are deprecated and will disapear in future releases.

%package -n geronimo-annotation-1_0-api
Summary:        Geronimo J2EE server J2EE specifications
Group:          Development/Languages/Java
Requires(pre):  update-alternatives
Provides:       annotation_1_0_api
Provides:       annotation_api = 1.0
Obsoletes:      %{name}-poms

%description -n geronimo-annotation-1_0-api
Geronimo is Apache's ASF-licenced J2EE server project. These are the
J2EE-Specifications Note: You should use the subpackages for the
Specifications that you actually need.	The ones installed by the main
package are deprecated and will disapear in future releases.

%package -n geronimo-corba-1_0-apis
Summary:        Geronimo J2EE server J2EE specifications
Group:          Development/Languages/Java
Provides:       corba_1_0_apis = %{version}
Provides:       corba_apis = 1.0
Obsoletes:      %{name}-poms

%description -n geronimo-corba-1_0-apis
Geronimo is Apache's ASF-licenced J2EE server project. These are the
J2EE-Specifications: CORBA 1.0 Spec

%package -n geronimo-corba-2_3-apis
Summary:        Geronimo J2EE server J2EE specifications
Group:          Development/Languages/Java
Provides:       corba_2_3_apis = %{version}
Provides:       corba_apis = 2.3
Obsoletes:      %{name}-poms

%description -n geronimo-corba-2_3-apis
Geronimo is Apache's ASF-licenced J2EE server project. These are the
J2EE-Specifications: CORBA 2.3 Spec

%package -n geronimo-ejb-2_1-api
Summary:        Geronimo J2EE server J2EE specifications
Group:          Development/Languages/Java
Requires:       jta_1_0_1B_api
Requires(pre):  update-alternatives
Provides:       ejb = 2.1
# TODO: drop asap
Provides:       ejb_2_1_api = %{version}
Provides:       ejb_api = 2.1
# drop the following asap
Obsoletes:      %{name}-poms
Obsoletes:      ejb

%description -n geronimo-ejb-2_1-api
Geronimo is Apache's ASF-licenced J2EE server project. These are the
J2EE-Specifications: Enterprise JavaBeans Specification

%package -n geronimo-ejb-3_0-api
Summary:        Geronimo J2EE server J2EE specifications
Group:          Development/Languages/Java
Requires:       annotation_1_0_api
Requires:       interceptor_3_0_api
Requires:       jta_1_1_api
Requires(pre):  update-alternatives
Provides:       ejb = 3.0
# TODO: drop asap
Provides:       ejb_3_0_api = %{version}
Provides:       ejb_api = 3.0
Obsoletes:      %{name}-poms
Obsoletes:      ejb

%description -n geronimo-ejb-3_0-api
Geronimo is Apache's ASF-licenced J2EE server project. These are the
J2EE-Specifications Note: You should use the subpackages for the
Specifications that you actually need.	The ones installed by the main
package are deprecated and will disapear in future releases.

%package -n geronimo-el-1_0-api
Summary:        Geronimo J2EE server J2EE specifications
Group:          Development/Languages/Java
Requires(pre):  update-alternatives
Provides:       el_1_0_api = %{version}
Provides:       el_api = 1.0
Obsoletes:      %{name}-poms

%description -n geronimo-el-1_0-api
Geronimo is Apache's ASF-licenced J2EE server project. These are the
J2EE-Specifications Note: You should use the subpackages for the
Specifications that you actually need.	The ones installed by the main
package are deprecated and will disapear in future releases.

%package -n geronimo-interceptor-3_0-api
Summary:        Geronimo J2EE server J2EE specifications
Group:          Development/Languages/Java
Requires(pre):  update-alternatives
Provides:       interceptor_3_0_api = %{version}
Provides:       interceptor_api = 3.0
Obsoletes:      %{name}-poms

%description -n geronimo-interceptor-3_0-api
Geronimo is Apache's ASF-licenced J2EE server project. These are the
J2EE-Specifications Note: You should use the subpackages for the
Specifications that you actually need.	The ones installed by the main
package are deprecated and will disapear in future releases.

%package -n geronimo-j2ee-1_4-apis
Summary:        Geronimo J2EE server J2EE specifications
# Do not provide it as this is just the API (is it?) and
# our 'javamail' alternative means the providers as well
# all in a single jar file called 'javamail.jar'
#Provides:      javamail = 1.3.1
#
Group:          Development/Languages/Java
Requires(pre):  update-alternatives
Provides:       commonj_1_1_apis = %{version}
Provides:       commonj_apis = 1.1
Provides:       corba_2_3_apis = %{version}
Provides:       corba_apis = 2.3
Provides:       ejb_2_1_api = %{version}
Provides:       ejb_api = 2.1
Provides:       j2ee_connector_1_5_api = %{version}
Provides:       j2ee_connector_api = 1.5
Provides:       j2ee_deployment_1_1_api = %{version}
Provides:       j2ee_deployment_api = 1.1
Provides:       j2ee_management_1_0_api = %{version}
Provides:       j2ee_management_api = 1.0
Provides:       jacc_1_0_api = %{version}
Provides:       jacc_api = 1.0
Provides:       jaf_1_0_2_api = %{version}
Provides:       jaf_api = 1.0.2
Provides:       javamail_1_3_1_api = %{version}
Provides:       javamail_api = 1.3.1
Provides:       jaxr_1_0_api = %{version}
Provides:       jaxr_api = 1.0
Provides:       jaxrpc_1_1_api = %{version}
Provides:       jaxrpc_api = 1.1
Provides:       jms_1_1_api = %{version}
Provides:       jms_api = 1.1
Provides:       jsp_2_0_api = %{version}
Provides:       jsp_api = 2.0
Provides:       jta_1_0_1B_api = %{version}
Provides:       jta_api = 1.0.1B
Provides:       qname_1_1_api = %{version}
Provides:       qname_api = 1.1
Provides:       saaj_1_1_api = %{version}
Provides:       saaj_api = 1.1
Provides:       servlet_2_4_api = %{version}
Provides:       servlet_api = 2.4
# XXX: (dwalluck): section added for backwards compatibility with Fedora 9
#
# Provides:  commonj = 1.1
Provides:       ejb = 2.1
# Provides:  corba = 2.3
Provides:       j2ee-connector = 1.5
Provides:       j2ee-deployment = 1.1
Provides:       j2ee-management = 1.0
Provides:       jacc = 1.0
Provides:       jaf = 1.0.2
Provides:       javamail = 1.3.1
Provides:       jaxr = 1.0
Provides:       jaxrpc = 1.1
Provides:       jms = 1.1
Provides:       jsp = 2.0
Provides:       jta = 1.0.1B
# Provides:  qname = 1.1
Provides:       saaj = 1.1
Provides:       servlet = 2.4
# added Epoch
Provides:       geronimo-corba-2_3-apis = %{version}
# added Epoch
Provides:       geronimo-qname-1_1-api = %{version}
Obsoletes:      %{name}-poms

%description -n geronimo-j2ee-1_4-apis
Geronimo is Apache's ASF-licenced J2EE server project. These are the
J2EE-Specifications: J2EE Specification (the complete set in one jar)

%package -n geronimo-j2ee-connector-1_5-api
Summary:        Geronimo J2EE server J2EE specifications
Group:          Development/Languages/Java
Requires:       jta_1_0_1B_api
Requires(pre):  update-alternatives
Provides:       j2ee_connector_1_5_api = %{version}
Provides:       j2ee_connector_api = 1.5
# drop the following asap
Provides:       j2ee-connector = 1.5
Obsoletes:      %{name}-poms
Obsoletes:      j2ee-connector

%description -n geronimo-j2ee-connector-1_5-api
Geronimo is Apache's ASF-licenced J2EE server project. These are the
J2EE-Specifications: J2EE Connector Architecture Specification

%package -n geronimo-j2ee-deployment-1_1-api
Summary:        Geronimo J2EE server J2EE specifications
Group:          Development/Languages/Java
Requires(pre):  update-alternatives
Provides:       j2ee_deployment_1_1_api = %{version}
Provides:       j2ee_deployment_api = 1.1
# drop the following asap
Provides:       j2ee-deployment = 1.1
Obsoletes:      %{name}-poms
Obsoletes:      j2ee-deployment

%description -n geronimo-j2ee-deployment-1_1-api
Geronimo is Apache's ASF-licenced J2EE server project. These are the
J2EE-Specifications: J2EE Application Deployment Specification

%package -n geronimo-javaee-deployment-1_1-api
Summary:        Geronimo J2EE server J2EE specifications
Group:          Development/Languages/Java
Requires(pre):  update-alternatives
Provides:       javaee_deployment_1_1_api = %{version}
Provides:       javaee_deployment_api = 1.1
Obsoletes:      %{name}-poms

%description -n geronimo-javaee-deployment-1_1-api
Geronimo is Apache's ASF-licenced J2EE server project. These are the
J2EE-Specifications Note: You should use the subpackages for the
Specifications that you actually need.	The ones installed by the main
package are deprecated and will disapear in future releases.

%package -n geronimo-jacc-1_0-api
Summary:        Geronimo J2EE server J2EE specifications
Group:          Development/Languages/Java
Requires:       servlet_2_4_api
Requires(pre):  update-alternatives
Provides:       jacc = 1.0
# TODO: drop asap
Provides:       jacc_1_0_api = %{version}
Provides:       jacc_api = 1.0
Obsoletes:      %{name}-poms

%description -n geronimo-jacc-1_0-api
Geronimo is Apache's ASF-licenced J2EE server project. These are the
J2EE-Specifications: Java Authorization Contract for Containers
Specification

%package -n geronimo-jacc-1_1-api
Summary:        Geronimo J2EE server J2EE specifications
Group:          Development/Languages/Java
Requires:       servlet_2_5_api
Requires(pre):  update-alternatives
Provides:       jacc_1_1_api = %{version}
Provides:       jacc_api = 1.1
Obsoletes:      %{name}-poms

%description -n geronimo-jacc-1_1-api
Geronimo is Apache's ASF-licenced J2EE server project. These are the
J2EE-Specifications Note: You should use the subpackages for the
Specifications that you actually need.	The ones installed by the main
package are deprecated and will disapear in future releases.

%package -n geronimo-j2ee-management-1_0-api
Summary:        Geronimo J2EE server J2EE specifications
Group:          Development/Languages/Java
Requires:       ejb_2_1_api
Requires(pre):  update-alternatives
Provides:       j2ee_management_1_0_api = %{version}
Provides:       j2ee_management_api = 1.0
# drop the following asap
Provides:       j2ee-management = 1.0
Obsoletes:      %{name}-poms
Obsoletes:      j2ee-management

%description -n geronimo-j2ee-management-1_0-api
Geronimo is Apache's ASF-licenced J2EE server project. These are the
J2EE-Specifications: J2EE Application Management Specification

%package -n geronimo-j2ee-management-1_1-api
Summary:        Geronimo J2EE server J2EE specifications
Group:          Development/Languages/Java
Requires:       ejb_3_0_api
Requires(pre):  update-alternatives
Provides:       j2ee_management_1_1_api = %{version}
Provides:       j2ee_management_api = 1.1
# drop the following asap
Provides:       j2ee-management = 1.1
Obsoletes:      %{name}-poms
Obsoletes:      j2ee-management

%description -n geronimo-j2ee-management-1_1-api
Geronimo is Apache's ASF-licenced J2EE server project. These are the
J2EE-Specifications Note: You should use the subpackages for the
Specifications that you actually need.	The ones installed by the main
package are deprecated and will disapear in future releases.

%package -n geronimo-javamail-1_3_1-api
Summary:        Geronimo J2EE server J2EE specifications
Group:          Development/Languages/Java
Requires:       jaf_1_0_2_api
Requires(pre):  update-alternatives
Provides:       javamail_1_3_1_api = %{version}
Provides:       javamail_api = 1.3.1
# Do not provide javamail as this is just the API (is it?) and
# our 'javamail' alternative means the providers as well
# all in a single jar file called 'javamail.jar'
#Provides:    javamail = 1.3.1
Obsoletes:      %{name}-poms

%description -n geronimo-javamail-1_3_1-api
Geronimo is Apache's ASF-licenced J2EE server project. These are the
J2EE-Specifications: JavaMail API

%package -n geronimo-javamail-1_4-api
Summary:        Geronimo J2EE server J2EE specifications
Group:          Development/Languages/Java
Requires:       jaf_1_1_api
Requires(pre):  update-alternatives
Provides:       javamail_1_4_api = %{version}
Provides:       javamail_api = 1.4
# Do not provide javamail as this is just the API (is it?) and
# our 'javamail' alternative means the providers as well
# all in a single jar file called 'javamail.jar'
#Provides:    javamail = 1.4
Obsoletes:      %{name}-poms

%description -n geronimo-javamail-1_4-api
Geronimo is Apache's ASF-licenced J2EE server project. These are the
J2EE-Specifications Note: You should use the subpackages for the
Specifications that you actually need.	The ones installed by the main
package are deprecated and will disapear in future releases.

%package -n geronimo-jaxr-1_0-api
Summary:        Geronimo J2EE server J2EE specifications
Group:          Development/Languages/Java
Requires:       jaf_1_0_2_api
Requires(pre):  update-alternatives
Provides:       jaxr_1_0_api = %{version}
Provides:       jaxr_api = 1.0
# drop the following asap
Provides:       jaxr = 1.0
Obsoletes:      %{name}-poms
Obsoletes:      jaxr-api

%description -n geronimo-jaxr-1_0-api
Geronimo is Apache's ASF-licenced J2EE server project. These are the
J2EE-Specifications: Java API for XML Registries (JAXR)

%package -n geronimo-jaxrpc-1_1-api
Summary:        Geronimo J2EE server J2EE specifications
Group:          Development/Languages/Java
Requires:       qname_1_1_api
Requires:       saaj_1_1_api
Requires:       servlet_2_4_api
Requires(pre):  update-alternatives
Provides:       jaxrpc = 1.1
# TODO: drop asap
Provides:       jaxrpc_1_1_api = %{version}
Provides:       jaxrpc_api = 1.1
Obsoletes:      %{name}-poms

%description -n geronimo-jaxrpc-1_1-api
Geronimo is Apache's ASF-licenced J2EE server project. These are the
J2EE-Specifications: Java API for XML-Based RPC (JAXRPC)

%package -n geronimo-jms-1_1-api
Summary:        Geronimo J2EE server J2EE specifications
Group:          Development/Languages/Java
Requires(pre):  update-alternatives
Provides:       jms_1_1_api = %{version}
Provides:       jms_api = 1.1
# drop the following asap
Provides:       jms = 1.1
Obsoletes:      %{name}-poms
Obsoletes:      jms

%description -n geronimo-jms-1_1-api
Geronimo is Apache's ASF-licenced J2EE server project. These are the
J2EE-Specifications: JMS Specification

%package -n geronimo-jpa-3_0-api
Summary:        Geronimo J2EE server J2EE specifications
Group:          Development/Languages/Java
Requires(pre):  update-alternatives
Provides:       jpa_3_0_api = %{version}
Provides:       jpa_api = 3.0
Obsoletes:      %{name}-poms

%description -n geronimo-jpa-3_0-api
Geronimo is Apache's ASF-licenced J2EE server project. These are the
J2EE-Specifications Note: You should use the subpackages for the
Specifications that you actually need.	The ones installed by the main
package are deprecated and will disapear in future releases.

%package -n geronimo-jsp-2_0-api
Summary:        Geronimo J2EE server J2EE specifications
Group:          Development/Languages/Java
Requires:       servlet_2_4_api
Requires(pre):  update-alternatives
Provides:       jsp = 2.0
# TODO: drop asap
Provides:       jsp_2_0_api = %{version}
Provides:       jsp_api = 2.0
Obsoletes:      %{name}-poms

%description -n geronimo-jsp-2_0-api
Geronimo is Apache's ASF-licenced J2EE server project. These are the
J2EE-Specifications: JavaServer Pages Specification

%package -n geronimo-jsp-2_1-api
Summary:        Geronimo J2EE server J2EE specifications
Group:          Development/Languages/Java
Requires:       el_1_0_api
Requires:       servlet_2_5_api
Requires(pre):  update-alternatives
Provides:       jsp = 2.1
# TODO: drop asap
Provides:       jsp_2_1_api = %{version}
Provides:       jsp_api = 2.1
Obsoletes:      %{name}-poms

%description -n geronimo-jsp-2_1-api
Geronimo is Apache's ASF-licenced J2EE server project. These are the
J2EE-Specifications Note: You should use the subpackages for the
Specifications that you actually need.	The ones installed by the main
package are deprecated and will disapear in future releases.

%package -n geronimo-jta-1_0_1B-api
Summary:        Geronimo J2EE server J2EE specifications
# Don't obsolete jta, as this is provided by java-1.4.2-gcj-compat
#Obsoletes:    jta
Group:          Development/Languages/Java
Requires(pre):  update-alternatives
Provides:       jta_1_0_1B_api = %{version}
Provides:       jta_api = 1.0.1B
# drop the following asap
Provides:       jta = 1.0.1B
Obsoletes:      %{name}-poms

%description -n geronimo-jta-1_0_1B-api
Geronimo is Apache's ASF-licenced J2EE server project. These are the
J2EE-Specifications: Java Transaction API Specification

%package -n geronimo-jta-1_1-api
Summary:        Geronimo J2EE server J2EE specifications
# Don't obsolete jta, as this is provided by java-1.4.2-gcj-compat
#Obsoletes:    jta
Group:          Development/Languages/Java
Requires(pre):  update-alternatives
Provides:       jta_1_1_api = %{version}
Provides:       jta_api = 1.1
# drop the following asap
Provides:       jta = 1.1
Obsoletes:      %{name}-poms

%description -n geronimo-jta-1_1-api
Geronimo is Apache's ASF-licenced J2EE server project. These are the
J2EE-Specifications Note: You should use the subpackages for the
Specifications that you actually need.	The ones installed by the main
package are deprecated and will disapear in future releases.

%package -n geronimo-qname-1_1-api
Summary:        Geronimo J2EE server J2EE specifications
Group:          Development/Languages/Java
Requires(pre):  update-alternatives
Provides:       qname_1_1_api = %{version}
Provides:       qname_api = 1.1
Obsoletes:      %{name}-poms

%description -n geronimo-qname-1_1-api
Geronimo is Apache's ASF-licenced J2EE server project. These are the
J2EE-Specifications: javax.xml.namespace.QName API

%package -n geronimo-saaj-1_1-api
Summary:        Geronimo J2EE server J2EE specifications
Group:          Development/Languages/Java
Requires:       jaf_1_0_2_api
Requires(pre):  update-alternatives
Provides:       saaj = 1.1
# TODO: drop asap
Provides:       saaj_1_1_api = %{version}
Provides:       saaj_api = 1.1
Obsoletes:      %{name}-poms

%description -n geronimo-saaj-1_1-api
Geronimo is Apache's ASF-licenced J2EE server project. These are the
J2EE-Specifications: SOAP with Attachments API for Java (SAAJ)

%package -n geronimo-servlet-2_4-api
Summary:        Geronimo J2EE server J2EE specifications
Group:          Development/Languages/Java
Requires(pre):  update-alternatives
Provides:       servlet = 2.4
# TODO: drop asap
Provides:       servlet_2_4_api = %{version}
Provides:       servlet_api = 2.4
Obsoletes:      %{name}-poms

%description -n geronimo-servlet-2_4-api
Geronimo is Apache's ASF-licenced J2EE server project. These are the
J2EE-Specifications: J2EE Servlet v2.4 API

%package -n geronimo-servlet-2_5-api
Summary:        Geronimo J2EE server J2EE specifications
Group:          Development/Languages/Java
Requires(pre):  update-alternatives
Provides:       servlet = 2.5
# TODO: drop asap
Provides:       servlet_2_5_api = %{version}
Provides:       servlet_api = 2.5
Obsoletes:      %{name}-poms

%description -n geronimo-servlet-2_5-api
Geronimo is Apache's ASF-licenced J2EE server project. These are the
J2EE-Specifications Note: You should use the subpackages for the
Specifications that you actually need.	The ones installed by the main
package are deprecated and will disapear in future releases.

%package -n geronimo-stax-1_0-api
Summary:        Geronimo J2EE server J2EE specifications
Group:          Development/Languages/Java
Requires(pre):  update-alternatives
Provides:       stax_1_0_api = %{version}
Provides:       stax_api = 1.0
Obsoletes:      %{name}-poms

%description -n geronimo-stax-1_0-api
Geronimo is Apache's ASF-licenced J2EE server project. These are the
J2EE-Specifications Note: You should use the subpackages for the
Specifications that you actually need.	The ones installed by the main
package are deprecated and will disapear in future releases.

%package -n geronimo-ws-metadata-2_0-api
Summary:        Geronimo J2EE server J2EE specifications
Group:          Development/Languages/Java
Requires(pre):  update-alternatives
Provides:       ws_metadata_2_0_api = %{version}
Provides:       ws_metadata_api = 2.0
Obsoletes:      %{name}-poms

%description -n geronimo-ws-metadata-2_0-api
Geronimo is Apache's ASF-licenced J2EE server project. These are the
J2EE-Specifications Note: You should use the subpackages for the
Specifications that you actually need.	The ones installed by the main
package are deprecated and will disapear in future releases.

%prep
%setup -q
chmod -R go=u-w *
mkdir etc
cp LICENSE.txt etc
mkdir external_repo
ln -s %{_javadir} external_repo/JPP
cp %{SOURCE1000} build.xml
for i in */pom.xml; do
  %pom_remove_parent ${i}
  %pom_xpath_inject "pom:project" "<groupId>org.apache.geronimo.specs</groupId>" ${i}
done
%pom_add_dep logkit:logkit:1.2.2 geronimo-spec-corba-2.3

%build
ant -Dant.build.javac.source=8 -Dant.build.javac.target=8 \
    -Didlj=%{java_home}/bin/idlj

%install
set +x
# Directory for poms
install -d -m 0755 %{buildroot}/%{_mavenpomdir}
# subpackage jars
install -d -m 755 %{buildroot}%{_javadir}
install -m 0644 \
  geronimo-activation_1.0.2_spec-1.2/target/geronimo-activation_1.0.2_spec-1.2.jar \
  %{buildroot}%{_javadir}/geronimo-jaf-1.0.2-api.jar
install -m 0644 geronimo-activation_1.0.2_spec-1.2/pom.xml \
  %{buildroot}/%{_mavenpomdir}/JPP-geronimo-jaf-1.0.2-api.pom
%add_maven_depmap JPP-geronimo-jaf-1.0.2-api.pom geronimo-jaf-1.0.2-api.jar -f jaf-1.0.2-api

install -m 0644 \
  geronimo-activation_1.1_spec-1.0/target/geronimo-activation_1.1_spec-1.0.jar \
  %{buildroot}%{_javadir}/geronimo-jaf-1.1-api.jar
install -m 0644 geronimo-activation_1.1_spec-1.0/pom.xml \
  %{buildroot}/%{_mavenpomdir}/JPP-geronimo-jaf-1.1-api.pom
%add_maven_depmap JPP-geronimo-jaf-1.1-api.pom geronimo-jaf-1.1-api.jar -f jaf-1.1-api

install -m 0644 \
  geronimo-annotation_1.0_spec-1.1.0/target/geronimo-annotation_1.0_spec-1.1.jar \
  %{buildroot}%{_javadir}/geronimo-annotation-1.0-api.jar
install -m 0644 geronimo-annotation_1.0_spec-1.1.0/pom.xml \
  %{buildroot}/%{_mavenpomdir}/JPP-geronimo-annotation-1.0-api.pom
%add_maven_depmap JPP-geronimo-annotation-1.0-api.pom geronimo-annotation-1.0-api.jar -a "javax.annotation:jsr250-api,org.eclipse.jetty.orbit:javax.annotation" -f annotation-1.0-api

install -m 0644 \
  geronimo-spec-corba-2.3/target/geronimo-corba_2.3_spec-null.jar \
  %{buildroot}%{_javadir}/geronimo-corba-2.3-apis.jar
install -m 0644 geronimo-spec-corba-2.3/pom.xml \
  %{buildroot}/%{_mavenpomdir}/JPP-geronimo-corba-2.3-apis.pom
%add_maven_depmap JPP-geronimo-corba-2.3-apis.pom geronimo-corba-2.3-apis.jar -f corba-2.3-apis

install -m 0644 \
  geronimo-spec-corba/target/geronimo-spec-corba-null.jar \
  %{buildroot}%{_javadir}/geronimo-corba-1.0-apis.jar
install -m 0644 geronimo-spec-corba/pom.xml \
  %{buildroot}/%{_mavenpomdir}/JPP-geronimo-corba-1.0-apis.pom
%add_maven_depmap JPP-geronimo-corba-1.0-apis.pom geronimo-corba-1.0-apis.jar -f corba-1.0-apis

install -m 0644 \
  geronimo-ejb_2.1_spec-1.1/target/geronimo-ejb_2.1_spec-1.1.jar \
  %{buildroot}%{_javadir}/geronimo-ejb-2.1-api.jar
install -m 0644 geronimo-ejb_2.1_spec-1.1/pom.xml \
  %{buildroot}/%{_mavenpomdir}/JPP-geronimo-ejb-2.1-api.pom
%add_maven_depmap JPP-geronimo-ejb-2.1-api.pom geronimo-ejb-2.1-api.jar -f ejb-2.1-api

install -m 0644 \
  geronimo-ejb_3.0_spec-1.0/target/geronimo-ejb_3.0_spec-1.0.jar \
  %{buildroot}%{_javadir}/geronimo-ejb-3.0-api.jar
install -m 0644 geronimo-ejb_3.0_spec-1.0/pom.xml \
  %{buildroot}/%{_mavenpomdir}/JPP-geronimo-ejb-3.0-api.pom
%add_maven_depmap JPP-geronimo-ejb-3.0-api.pom geronimo-ejb-3.0-api.jar -f ejb-3.0-api

install -m 0644 \
  geronimo-el_1.0_spec-1.0/target/geronimo-el_1.0_spec-1.0.jar \
  %{buildroot}%{_javadir}/geronimo-el-1.0-api.jar
install -m 0644 geronimo-el_1.0_spec-1.0/pom.xml \
  %{buildroot}/%{_mavenpomdir}/JPP-geronimo-el-1.0-api.pom
%add_maven_depmap JPP-geronimo-el-1.0-api.pom geronimo-el-1.0-api.jar -f el-1.0-api

install -m 0644 \
  geronimo-interceptor_3.0_spec-1.0/target/geronimo-interceptor_3.0_spec-1.0.jar \
  %{buildroot}%{_javadir}/geronimo-interceptor-3.0-api.jar
install -m 0644 geronimo-interceptor_3.0_spec-1.0/pom.xml \
  %{buildroot}/%{_mavenpomdir}/JPP-geronimo-interceptor-3.0-api.pom
%add_maven_depmap JPP-geronimo-interceptor-3.0-api.pom geronimo-interceptor-3.0-api.jar -f interceptor-3.0-api

install -m 0644 \
  geronimo-j2ee-connector_1.5_spec-1.1.1/target/geronimo-j2ee-connector_1.5_spec-1.1.1.jar \
  %{buildroot}%{_javadir}/geronimo-j2ee-connector-1.5-api.jar
install -m 0644 geronimo-j2ee-connector_1.5_spec-1.1.1/pom.xml \
  %{buildroot}/%{_mavenpomdir}/JPP-geronimo-j2ee-connector-1.5-api.pom
%add_maven_depmap JPP-geronimo-j2ee-connector-1.5-api.pom geronimo-j2ee-connector-1.5-api.jar -f j2ee-connector-1.5-api

install -m 0644 \
  geronimo-j2ee-deployment_1.1_spec-1.1/target/geronimo-j2ee-deployment_1.1_spec-1.1.jar \
  %{buildroot}%{_javadir}/geronimo-j2ee-deployment-1.1-api.jar
install -m 0644 geronimo-j2ee-deployment_1.1_spec-1.1/pom.xml \
  %{buildroot}/%{_mavenpomdir}/JPP-geronimo-j2ee-deployment-1.1-api.pom
%add_maven_depmap JPP-geronimo-j2ee-deployment-1.1-api.pom geronimo-j2ee-deployment-1.1-api.jar -f j2ee-deployment-1.1-api

install -m 0644 \
  geronimo-javaee-deployment_1.1MR3_spec-1.0/target/geronimo-javaee-deployment_1.1MR3_spec-1.0.jar \
  %{buildroot}%{_javadir}/geronimo-javaee-deployment-1.1-api.jar
install -m 0644 geronimo-javaee-deployment_1.1MR3_spec-1.0/pom.xml \
  %{buildroot}/%{_mavenpomdir}/JPP-geronimo-javaee-deployment-1.1-api.pom
%add_maven_depmap JPP-geronimo-javaee-deployment-1.1-api.pom geronimo-javaee-deployment-1.1-api.jar -f javaee-deployment-1.1-api

install -m 0644 \
  geronimo-j2ee-jacc_1.0_spec-1.1/target/geronimo-j2ee-jacc_1.0_spec-1.1.jar \
  %{buildroot}%{_javadir}/geronimo-jacc-1.0-api.jar
install -m 0644 geronimo-j2ee-jacc_1.0_spec-1.1/pom.xml \
  %{buildroot}/%{_mavenpomdir}/JPP-geronimo-jacc-1.0-api.pom
%add_maven_depmap JPP-geronimo-jacc-1.0-api.pom geronimo-jacc-1.0-api.jar -f jacc-1.0-api

install -m 0644 \
  geronimo-jacc_1.1_spec-1.0/target/geronimo-jacc_1.1_spec-1.0.jar \
  %{buildroot}%{_javadir}/geronimo-jacc-1.1-api.jar
install -m 0644 geronimo-jacc_1.1_spec-1.0/pom.xml \
  %{buildroot}/%{_mavenpomdir}/JPP-geronimo-jacc-1.1-api.pom
%add_maven_depmap JPP-geronimo-jacc-1.1-api.pom geronimo-jacc-1.1-api.jar -f jacc-1.1-api

install -m 0644 \
  geronimo-j2ee-management_1.0_spec-1.1/target/geronimo-j2ee-management_1.0_spec-1.1.jar \
  %{buildroot}%{_javadir}/geronimo-j2ee-management-1.0-api.jar
install -m 0644 geronimo-j2ee-management_1.0_spec-1.1/pom.xml \
  %{buildroot}/%{_mavenpomdir}/JPP-geronimo-j2ee-management-1.0-api.pom
%add_maven_depmap JPP-geronimo-j2ee-management-1.0-api.pom geronimo-j2ee-management-1.0-api.jar -f j2ee-management-1.0-api

install -m 0644 \
  geronimo-j2ee-management_1.1_spec-1.0/target/geronimo-j2ee-management_1.1_spec-1.0.jar \
  %{buildroot}%{_javadir}/geronimo-j2ee-management-1.1-api.jar
install -m 0644 geronimo-j2ee-management_1.1_spec-1.0/pom.xml \
  %{buildroot}/%{_mavenpomdir}/JPP-geronimo-j2ee-management-1.1-api.pom
%add_maven_depmap JPP-geronimo-j2ee-management-1.1-api.pom geronimo-j2ee-management-1.1-api.jar -f j2ee-management-1.1-api

install -m 0644 \
  geronimo-javamail_1.3.1_spec-1.3/target/geronimo-javamail_1.3.1_spec-1.3.jar \
  %{buildroot}%{_javadir}/geronimo-javamail-1.3.1-api.jar
install -m 0644 geronimo-javamail_1.3.1_spec-1.3/pom.xml \
  %{buildroot}/%{_mavenpomdir}/JPP-geronimo-javamail-1.3.1-api.pom
%add_maven_depmap JPP-geronimo-javamail-1.3.1-api.pom geronimo-javamail-1.3.1-api.jar -f javamail-1.3.1-api

install -m 0644 \
  geronimo-javamail_1.4_spec-1.1/target/geronimo-javamail_1.4_spec-1.1.jar \
  %{buildroot}%{_javadir}/geronimo-javamail-1.4-api.jar
install -m 0644 geronimo-javamail_1.4_spec-1.1/pom.xml \
  %{buildroot}/%{_mavenpomdir}/JPP-geronimo-javamail-1.4-api.pom
%add_maven_depmap JPP-geronimo-javamail-1.4-api.pom geronimo-javamail-1.4-api.jar -f javamail-1.4-api

install -m 0644 \
  geronimo-jaxr_1.0_spec-1.1/target/geronimo-jaxr_1.0_spec-1.1.jar \
  %{buildroot}%{_javadir}/geronimo-jaxr-1.0-api.jar
install -m 0644 geronimo-jaxr_1.0_spec-1.1/pom.xml \
  %{buildroot}/%{_mavenpomdir}/JPP-geronimo-jaxr-1.0-api.pom
%add_maven_depmap JPP-geronimo-jaxr-1.0-api.pom geronimo-jaxr-1.0-api.jar -f jaxr-1.0-api

install -m 0644 \
  geronimo-jaxrpc_1.1_spec-1.1/target/geronimo-jaxrpc_1.1_spec-1.1.jar \
  %{buildroot}%{_javadir}/geronimo-jaxrpc-1.1-api.jar
install -m 0644 geronimo-jaxrpc_1.1_spec-1.1/pom.xml \
  %{buildroot}/%{_mavenpomdir}/JPP-geronimo-jaxrpc-1.1-api.pom
%add_maven_depmap JPP-geronimo-jaxrpc-1.1-api.pom geronimo-jaxrpc-1.1-api.jar -f jaxrpc-1.1-api

install -m 0644 \
  geronimo-spec-j2ee/target/geronimo-j2ee_1.4_spec-1.2-jar-with-dependencies.jar \
  %{buildroot}%{_javadir}/geronimo-j2ee-1.4-apis.jar
install -m 0644 geronimo-spec-j2ee/pom.xml \
  %{buildroot}/%{_mavenpomdir}/JPP-geronimo-j2ee-1.4-apis.pom
%add_maven_depmap JPP-geronimo-j2ee-1.4-apis.pom geronimo-j2ee-1.4-apis.jar -f j2ee-1.4-apis

install -m 0644 \
  geronimo-jms_1.1_spec-1.1/target/geronimo-jms_1.1_spec-1.1.jar \
  %{buildroot}%{_javadir}/geronimo-jms-1.1-api.jar
install -m 0644 geronimo-jms_1.1_spec-1.1/pom.xml \
  %{buildroot}/%{_mavenpomdir}/JPP-geronimo-jms-1.1-api.pom
%add_maven_depmap JPP-geronimo-jms-1.1-api.pom geronimo-jms-1.1-api.jar -f jms-1.1-api -a javax.jms:jms

install -m 0644 \
  geronimo-jpa_3.0_spec-1.1.0/target/geronimo-jpa_3.0_spec-1.1.jar \
  %{buildroot}%{_javadir}/geronimo-jpa-3.0-api.jar
install -m 0644 geronimo-jpa_3.0_spec-1.1.0/pom.xml \
  %{buildroot}/%{_mavenpomdir}/JPP-geronimo-jpa-3.0-api.pom
%add_maven_depmap JPP-geronimo-jpa-3.0-api.pom geronimo-jpa-3.0-api.jar -f jpa-3.0-api -a javax.persistence:persistence-api

install -m 0644 \
  geronimo-jsp_2.0_spec-1.1/target/geronimo-jsp_2.0_spec-1.1.jar \
  %{buildroot}%{_javadir}/geronimo-jsp-2.0-api.jar
install -m 0644 geronimo-jsp_2.0_spec-1.1/pom.xml \
  %{buildroot}/%{_mavenpomdir}/JPP-geronimo-jsp-2.0-api.pom
%add_maven_depmap JPP-geronimo-jsp-2.0-api.pom geronimo-jsp-2.0-api.jar -f jsp-2.0-api

install -m 0644 \
  geronimo-jsp_2.1_spec-1.0/target/geronimo-jsp_2.1_spec-1.0.jar \
  %{buildroot}%{_javadir}/geronimo-jsp-2.1-api.jar
install -m 0644 geronimo-jsp_2.1_spec-1.0/pom.xml \
  %{buildroot}/%{_mavenpomdir}/JPP-geronimo-jsp-2.1-api.pom
%add_maven_depmap JPP-geronimo-jsp-2.1-api.pom geronimo-jsp-2.1-api.jar -f jsp-2.1-api

install -m 0644 \
  geronimo-jta_1.0.1B_spec-1.1.1/target/geronimo-jta_1.0.1B_spec-1.1.1.jar \
  %{buildroot}%{_javadir}/geronimo-jta-1.0.1B-api.jar
install -m 0644 geronimo-jta_1.0.1B_spec-1.1.1/pom.xml \
  %{buildroot}/%{_mavenpomdir}/JPP-geronimo-jta-1.0.1B-api.pom
%add_maven_depmap JPP-geronimo-jta-1.0.1B-api.pom geronimo-jta-1.0.1B-api.jar -f jta-1.0.1B-api

install -m 0644 \
  geronimo-jta_1.1_spec-1.1.0/target/geronimo-jta_1.1_spec-1.1.jar \
  %{buildroot}%{_javadir}/geronimo-jta-1.1-api.jar
install -m 0644 geronimo-jta_1.1_spec-1.1.0/pom.xml \
  %{buildroot}/%{_mavenpomdir}/JPP-geronimo-jta-1.1-api.pom
%add_maven_depmap JPP-geronimo-jta-1.1-api.pom geronimo-jta-1.1-api.jar -f jta-1.1-api -a "javax.transaction:jta,org.eclipse.jetty.orbit:javax.transaction"

install -m 0644 \
  geronimo-qname_1.1_spec-1.1/target/geronimo-qname_1.1_spec-1.1.jar \
  %{buildroot}%{_javadir}/geronimo-qname-1.1-api.jar
install -m 0644 geronimo-qname_1.1_spec-1.1/pom.xml \
  %{buildroot}/%{_mavenpomdir}/JPP-geronimo-qname-1.1-api.pom
%add_maven_depmap JPP-geronimo-qname-1.1-api.pom geronimo-qname-1.1-api.jar -f qname-1.1-api

install -m 0644 \
  geronimo-saaj_1.1_spec-1.1/target/geronimo-saaj_1.1_spec-1.1.jar \
  %{buildroot}%{_javadir}/geronimo-saaj-1.1-api.jar
install -m 0644 geronimo-saaj_1.1_spec-1.1/pom.xml \
  %{buildroot}/%{_mavenpomdir}/JPP-geronimo-saaj-1.1-api.pom
%add_maven_depmap JPP-geronimo-saaj-1.1-api.pom geronimo-saaj-1.1-api.jar -f saaj-1.1-api

install -m 0644 \
  geronimo-servlet_2.4_spec-1.1.1/target/geronimo-servlet_2.4_spec-1.1.1.jar \
  %{buildroot}%{_javadir}/geronimo-servlet-2.4-api.jar
install -m 0644 geronimo-servlet_2.4_spec-1.1.1/pom.xml \
  %{buildroot}/%{_mavenpomdir}/JPP-geronimo-servlet-2.4-api.pom
%add_maven_depmap JPP-geronimo-servlet-2.4-api.pom geronimo-servlet-2.4-api.jar -f servlet-2.4-api

install -m 0644 \
  geronimo-servlet_2.5_spec-1.1/target/geronimo-servlet_2.5_spec-1.1.jar \
  %{buildroot}%{_javadir}/geronimo-servlet-2.5-api.jar
install -m 0644 geronimo-servlet_2.5_spec-1.1/pom.xml \
  %{buildroot}/%{_mavenpomdir}/JPP-geronimo-servlet-2.5-api.pom
%add_maven_depmap JPP-geronimo-servlet-2.5-api.pom geronimo-servlet-2.5-api.jar -f servlet-2.5-api

install -m 0644 \
  geronimo-stax-api_1.0_spec-1.0/target/geronimo-stax-api_1.0_spec-1.0.jar \
  %{buildroot}%{_javadir}/geronimo-stax-1.0-api.jar
install -m 0644 geronimo-stax-api_1.0_spec-1.0/pom.xml \
  %{buildroot}/%{_mavenpomdir}/JPP-geronimo-stax-1.0-api.pom
%add_maven_depmap JPP-geronimo-stax-1.0-api.pom geronimo-stax-1.0-api.jar -f stax-1.0-api

install -m 0644 \
  geronimo-ws-metadata_2.0_spec-1.1.1/target/geronimo-ws-metadata_2.0_spec-1.1.1.jar \
  %{buildroot}%{_javadir}/geronimo-ws-metadata-2.0-api.jar
install -m 0644 geronimo-ws-metadata_2.0_spec-1.1.1/pom.xml \
  %{buildroot}/%{_mavenpomdir}/JPP-geronimo-ws-metadata-2.0-api.pom
%add_maven_depmap JPP-geronimo-ws-metadata-2.0-api.pom geronimo-ws-metadata-2.0-api.jar -f ws-metadata-2.0-api

install -m 0644 \
  geronimo-spec-commonj/target/geronimo-commonj_1.1_spec-null.jar \
  %{buildroot}%{_javadir}/geronimo-commonj-1.1-apis.jar
install -m 0644 geronimo-spec-commonj/pom.xml \
  %{buildroot}/%{_mavenpomdir}/JPP-geronimo-commonj-1.1-apis.pom
%add_maven_depmap JPP-geronimo-commonj-1.1-apis.pom geronimo-commonj-1.1-apis.jar -f commonj-1.1-apis

%pre -n geronimo-commonj-1_1-apis
update-alternatives --remove commonj_apis %{_javadir}/geronimo-commonj-1.1-apis.jar
update-alternatives --remove commonj_1_1_apis %{_javadir}/geronimo-commonj-1.1-apis.jar

%pre -n geronimo-jaf-1_0_2-api
update-alternatives --remove jaf %{_javadir}/geronimo-jaf-1.0.2-api.jar
update-alternatives --remove jaf_api %{_javadir}/geronimo-jaf-1.0.2-api.jar
update-alternatives --remove jaf_1_0_2_api %{_javadir}/geronimo-jaf-1.0.2-api.jar

%pre -n geronimo-jaf-1_1-api
update-alternatives --remove jaf %{_javadir}/geronimo-jaf-1.1-api.jar
update-alternatives --remove jaf_api %{_javadir}/geronimo-jaf-1.1-api.jar
update-alternatives --remove jaf_1_1_api %{_javadir}/geronimo-jaf-1.1-api.jar

%pre -n geronimo-annotation-1_0-api
update-alternatives --remove annotation_api %{_javadir}/geronimo-annotation-1.0-api.jar
update-alternatives --remove annotation_1_0_api %{_javadir}/geronimo-annotation-1.0-api.jar

%pre -n geronimo-corba-1_0-apis
update-alternatives --remove corba_apis %{_javadir}/geronimo-corba-1.0-apis.jar
update-alternatives --remove corba_1_0_apis %{_javadir}/geronimo-corba-1.0-apis.jar

%pre -n geronimo-corba-2_3-apis
update-alternatives --remove corba_apis %{_javadir}/geronimo-corba-2.3-apis.jar
update-alternatives --remove corba_2_3_apis %{_javadir}/geronimo-corba-2.3-apis.jar

%pre -n geronimo-ejb-2_1-api
update-alternatives --remove ejb %{_javadir}/geronimo-ejb-2.1-api.jar
update-alternatives --remove ejb_api %{_javadir}/geronimo-ejb-2.1-api.jar
update-alternatives --remove ejb_2_1_api %{_javadir}/geronimo-ejb-2.1-api.jar

%pre -n geronimo-ejb-3_0-api
update-alternatives --remove ejb %{_javadir}/geronimo-ejb-3.0-api.jar
update-alternatives --remove ejb_api %{_javadir}/geronimo-ejb-3.0-api.jar
update-alternatives --remove ejb_3_0_api %{_javadir}/geronimo-ejb-3.0-api.jar

%pre -n geronimo-el-1_0-api
update-alternatives --remove el_api %{_javadir}/geronimo-el-1.0-api.jar
update-alternatives --remove el_1_0_api %{_javadir}/geronimo-el-1.0-api.jar

%pre -n geronimo-interceptor-3_0-api
update-alternatives --remove interceptor_api %{_javadir}/geronimo-interceptor-3.0-api.jar
update-alternatives --remove interceptor_3_0_api %{_javadir}/geronimo-interceptor-3.0-api.jar

%pre -n geronimo-j2ee-connector-1_5-api
update-alternatives --remove j2ee-connector %{_javadir}/geronimo-j2ee-connector-1.5-api.jar
update-alternatives --remove j2ee_connector_api %{_javadir}/geronimo-j2ee-connector-1.5-api.jar
update-alternatives --remove j2ee_connector_1_5_api %{_javadir}/geronimo-j2ee-connector-1.5-api.jar

%pre -n geronimo-j2ee-deployment-1_1-api
update-alternatives --remove j2ee-deployment %{_javadir}/geronimo-j2ee-deployment-1.1-api.jar
update-alternatives --remove j2ee_deployment_api %{_javadir}/geronimo-j2ee-deployment-1.1-api.jar
update-alternatives --remove j2ee_deployment_1_1_api %{_javadir}/geronimo-j2ee-deployment-1.1-api.jar

%pre -n geronimo-javaee-deployment-1_1-api
update-alternatives --remove javaee_deployment_api %{_javadir}/geronimo-javaee-deployment-1.1-api.jar
update-alternatives --remove javaee_deployment_1_1MR3_api %{_javadir}/geronimo-javaee-deployment-1.1-api.jar

%pre -n geronimo-jacc-1_0-api
update-alternatives --remove jacc %{_javadir}/geronimo-jacc-1.0-api.jar
update-alternatives --remove jacc_api %{_javadir}/geronimo-jacc-1.0-api.jar
update-alternatives --remove jacc_1_0_api %{_javadir}/geronimo-jacc-1.0-api.jar

%pre -n geronimo-jacc-1_1-api
update-alternatives --remove jacc_api %{_javadir}/geronimo-jacc-1.1-api.jar
update-alternatives --remove jacc_1_1_api %{_javadir}/geronimo-jacc-1.1-api.jar

%pre -n geronimo-j2ee-management-1_0-api
update-alternatives --remove j2ee-management %{_javadir}/geronimo-j2ee-management-1.0-api.jar
update-alternatives --remove j2ee_management_api %{_javadir}/geronimo-j2ee-management-1.0-api.jar
update-alternatives --remove j2ee_management_1_0_api %{_javadir}/geronimo-j2ee-management-1.0-api.jar

%pre -n geronimo-j2ee-management-1_1-api
update-alternatives --remove j2ee-management %{_javadir}/geronimo-j2ee-management-1.1-api.jar
update-alternatives --remove j2ee_management_api %{_javadir}/geronimo-j2ee-management-1.1-api.jar
update-alternatives --remove j2ee_management_1_1_api %{_javadir}/geronimo-j2ee-management-1.1-api.jar

%pre -n geronimo-javamail-1_3_1-api
update-alternatives --remove javamail_api %{_javadir}/geronimo-javamail-1.3.1-api.jar
update-alternatives --remove javamail_1_3_1_api %{_javadir}/geronimo-javamail-1.3.1-api.jar

%pre -n geronimo-javamail-1_4-api
update-alternatives --remove javamail_api %{_javadir}/geronimo-javamail-1.4-api.jar
update-alternatives --remove javamail_1_4_api %{_javadir}/geronimo-javamail-1.4-api.jar

%pre -n geronimo-jaxr-1_0-api
update-alternatives --remove jaxr %{_javadir}/geronimo-jaxr-1.0-api.jar
update-alternatives --remove jaxr_api %{_javadir}/geronimo-jaxr-1.0-api.jar
update-alternatives --remove jaxr_1_0_api %{_javadir}/geronimo-jaxr-1.0-api.jar

%pre -n geronimo-jaxrpc-1_1-api
update-alternatives --remove jaxrpc %{_javadir}/geronimo-jaxrpc-1.1-api.jar
update-alternatives --remove jaxrpc_api %{_javadir}/geronimo-jaxrpc-1.1-api.jar
update-alternatives --remove jaxrpc_1_1_api %{_javadir}/geronimo-jaxrpc-1.1-api.jar

%pre -n geronimo-jms-1_1-api
update-alternatives --remove jms %{_javadir}/geronimo-jms-1.1-api.jar
update-alternatives --remove jms_api %{_javadir}/geronimo-jms-1.1-api.jar
update-alternatives --remove jms_1_1_api %{_javadir}/geronimo-jms-1.1-api.jar

%pre -n geronimo-jpa-3_0-api
update-alternatives --remove jpa_api %{_javadir}/geronimo-jpa-3.0-api.jar
update-alternatives --remove jpa_3_0_api %{_javadir}/geronimo-jpa-3.0-api.jar

%pre -n geronimo-jsp-2_0-api
update-alternatives --remove jsp %{_javadir}/geronimo-jsp-2.0-api.jar
update-alternatives --remove jsp_api %{_javadir}/geronimo-jsp-2.0-api.jar
update-alternatives --remove jsp_2_0_api %{_javadir}/geronimo-jsp-2.0-api.jar

%pre -n geronimo-jsp-2_1-api
update-alternatives --remove jsp %{_javadir}/geronimo-jsp-2.1-api.jar
update-alternatives --remove jsp_api %{_javadir}/geronimo-jsp-2.1-api.jar
update-alternatives --remove jsp_2_1_api %{_javadir}/geronimo-jsp-2.1-api.jar

%pre -n geronimo-jta-1_0_1B-api
update-alternatives --remove jta %{_javadir}/geronimo-jta-1.0.1B-api.jar
update-alternatives --remove jta_api %{_javadir}/geronimo-jta-1.0.1B-api.jar
update-alternatives --remove jta_1_0_1B_api %{_javadir}/geronimo-jta-1.0.1B-api.jar

%pre -n geronimo-jta-1_1-api
update-alternatives --remove jta %{_javadir}/geronimo-jta-1.1-api.jar
update-alternatives --remove jta_api %{_javadir}/geronimo-jta-1.1-api.jar
update-alternatives --remove jta_1_1_api %{_javadir}/geronimo-jta-1.1-api.jar

%pre -n geronimo-qname-1_1-api
update-alternatives --remove qname_api %{_javadir}/geronimo-qname-1.1-api.jar
update-alternatives --remove qname_1_1_api %{_javadir}/geronimo-qname-1.1-api.jar

%pre -n geronimo-saaj-1_1-api
update-alternatives --remove saaj %{_javadir}/geronimo-saaj-1.1-api.jar
update-alternatives --remove saaj_api %{_javadir}/geronimo-saaj-1.1-api.jar
update-alternatives --remove saaj_1_1_api %{_javadir}/geronimo-saaj-1.1-api.jar

%pre -n geronimo-servlet-2_4-api
update-alternatives --remove servlet %{_javadir}/geronimo-servlet-2.4-api.jar
update-alternatives --remove servlet_api %{_javadir}/geronimo-servlet-2.4-api.jar
update-alternatives --remove servlet_2_4_api %{_javadir}/geronimo-servlet-2.4-api.jar

%pre -n geronimo-servlet-2_5-api
update-alternatives --remove servlet %{_javadir}/geronimo-servlet-2.5-api.jar
update-alternatives --remove servlet_api %{_javadir}/geronimo-servlet-2.5-api.jar
update-alternatives --remove servlet_2_5_api %{_javadir}/geronimo-servlet-2.5-api.jar

%pre -n geronimo-stax-1_0-api
update-alternatives --remove stax_api %{_javadir}/geronimo-stax-1.0-api.jar
update-alternatives --remove stax_1_0_api %{_javadir}/geronimo-stax-1.0-api.jar

%pre -n geronimo-ws-metadata-2_0-api
update-alternatives --remove ws_metadata_api %{_javadir}/geronimo-ws-metadata-2.0-api.jar
update-alternatives --remove ws_metadata_2_0_api %{_javadir}/geronimo-ws-metadata-2.0-api.jar

%pre -n geronimo-j2ee-1_4-apis
update-alternatives --remove jaf_api %{_javadir}/geronimo-j2ee-1.4-apis.jar
update-alternatives --remove jaf_1_0_2_api %{_javadir}/geronimo-j2ee-1.4-apis.jar
update-alternatives --remove commonj_apis %{_javadir}/geronimo-j2ee-1.4-apis.jar
update-alternatives --remove commonj_1_1_apis %{_javadir}/geronimo-j2ee-1.4-apis.jar
update-alternatives --remove corba_apis %{_javadir}/geronimo-j2ee-1.4-apis.jar
update-alternatives --remove corba_2_3_apis %{_javadir}/geronimo-j2ee-1.4-apis.jar
update-alternatives --remove ejb_api %{_javadir}/geronimo-j2ee-1.4-apis.jar
update-alternatives --remove ejb_2_1_api %{_javadir}/geronimo-j2ee-1.4-apis.jar
update-alternatives --remove j2ee-connector %{_javadir}/geronimo-j2ee-connector-1.5-api.jar
update-alternatives --remove j2ee_connector_api %{_javadir}/geronimo-j2ee-1.4-apis.jar
update-alternatives --remove j2ee_connector_1_5_api %{_javadir}/geronimo-j2ee-1.4-apis.jar
update-alternatives --remove j2ee_deployment_api %{_javadir}/geronimo-j2ee-1.4-apis.jar
update-alternatives --remove j2ee_deployment_1_1_api %{_javadir}/geronimo-j2ee-1.4-apis.jar
update-alternatives --remove j2ee_management_api %{_javadir}/geronimo-j2ee-1.4-apis.jar
update-alternatives --remove j2ee_management_1_0_api %{_javadir}/geronimo-j2ee-1.4-apis.jar
update-alternatives --remove jacc_api %{_javadir}/geronimo-j2ee-1.4-apis.jar
update-alternatives --remove jacc_1_0_api %{_javadir}/geronimo-j2ee-1.4-apis.jar
update-alternatives --remove javamail_api %{_javadir}/geronimo-j2ee-1.4-apis.jar
update-alternatives --remove javamail_1_3_1_api %{_javadir}/geronimo-j2ee-1.4-apis.jar
update-alternatives --remove jaxr_api %{_javadir}/geronimo-j2ee-1.4-apis.jar
update-alternatives --remove jaxr_1_0_api %{_javadir}/geronimo-j2ee-1.4-apis.jar
update-alternatives --remove jaxrpc_api %{_javadir}/geronimo-j2ee-1.4-apis.jar
update-alternatives --remove jaxrpc_1_1_api %{_javadir}/geronimo-j2ee-1.4-apis.jar
update-alternatives --remove jms_api %{_javadir}/geronimo-j2ee-1.4-apis.jar
update-alternatives --remove jms_1_1_api %{_javadir}/geronimo-j2ee-1.4-apis.jar
update-alternatives --remove jsp_api %{_javadir}/geronimo-j2ee-1.4-apis.jar
update-alternatives --remove jsp_2_0_api %{_javadir}/geronimo-j2ee-1.4-apis.jar
update-alternatives --remove jta_api %{_javadir}/geronimo-j2ee-1.4-apis.jar
update-alternatives --remove jta_1_0_1B_api %{_javadir}/geronimo-j2ee-1.4-apis.jar
update-alternatives --remove qname_api %{_javadir}/geronimo-j2ee-1.4-apis.jar
update-alternatives --remove qname_1_1_api %{_javadir}/geronimo-j2ee-1.4-apis.jar
update-alternatives --remove saaj_api %{_javadir}/geronimo-j2ee-1.4-apis.jar
update-alternatives --remove saaj_1_1_api %{_javadir}/geronimo-j2ee-1.4-apis.jar
update-alternatives --remove servlet_api %{_javadir}/geronimo-j2ee-1.4-apis.jar
update-alternatives --remove servlet_2_4_api %{_javadir}/geronimo-j2ee-1.4-apis.jar

%files -n geronimo-commonj-1_1-apis -f .mfiles-commonj-1.1-apis
%license geronimo-spec-commonj/LICENSE.txt

%files -n geronimo-jaf-1_0_2-api -f .mfiles-jaf-1.0.2-api
%license geronimo-activation_1.0.2_spec-1.2/LICENSE.txt

%files -n geronimo-jaf-1_1-api -f .mfiles-jaf-1.1-api
%license geronimo-activation_1.1_spec-1.0/LICENSE.txt

%files -n geronimo-annotation-1_0-api -f .mfiles-annotation-1.0-api
%license geronimo-annotation_1.0_spec-1.1.0/LICENSE.txt

%files -n geronimo-corba-1_0-apis -f .mfiles-corba-1.0-apis

%files -n geronimo-corba-2_3-apis -f .mfiles-corba-2.3-apis
%license geronimo-spec-corba-2.3/LICENSE.txt

%files -n geronimo-ejb-2_1-api -f .mfiles-ejb-2.1-api
%license geronimo-ejb_2.1_spec-1.1/LICENSE.txt

%files -n geronimo-ejb-3_0-api -f .mfiles-ejb-3.0-api
%license geronimo-ejb_3.0_spec-1.0/LICENSE.txt

%files -n geronimo-el-1_0-api -f .mfiles-el-1.0-api
%license geronimo-el_1.0_spec-1.0/LICENSE.txt

%files -n geronimo-interceptor-3_0-api -f .mfiles-interceptor-3.0-api
%license geronimo-interceptor_3.0_spec-1.0/LICENSE.txt

%files -n geronimo-j2ee-1_4-apis -f .mfiles-j2ee-1.4-apis
%license geronimo-spec-j2ee/LICENSE.txt

%files -n geronimo-j2ee-connector-1_5-api -f .mfiles-j2ee-connector-1.5-api
%license geronimo-j2ee-connector_1.5_spec-1.1.1/LICENSE.txt

%files -n geronimo-j2ee-deployment-1_1-api -f .mfiles-j2ee-deployment-1.1-api
%license geronimo-j2ee-deployment_1.1_spec-1.1/LICENSE.txt

%files -n geronimo-javaee-deployment-1_1-api -f .mfiles-javaee-deployment-1.1-api
%license geronimo-javaee-deployment_1.1MR3_spec-1.0/LICENSE.txt

%files -n geronimo-jacc-1_0-api -f .mfiles-jacc-1.0-api
%license geronimo-j2ee-jacc_1.0_spec-1.1/LICENSE.txt

%files -n geronimo-jacc-1_1-api -f .mfiles-jacc-1.1-api
%license geronimo-jacc_1.1_spec-1.0/LICENSE.txt

%files -n geronimo-j2ee-management-1_0-api -f .mfiles-j2ee-management-1.0-api
%license geronimo-j2ee-management_1.0_spec-1.1/LICENSE.txt

%files -n geronimo-j2ee-management-1_1-api -f .mfiles-j2ee-management-1.1-api
%license geronimo-j2ee-management_1.1_spec-1.0/LICENSE.txt

%files -n geronimo-javamail-1_3_1-api -f .mfiles-javamail-1.3.1-api
%license geronimo-javamail_1.3.1_spec-1.3/LICENSE.txt

%files -n geronimo-javamail-1_4-api -f .mfiles-javamail-1.4-api
%license geronimo-javamail_1.4_spec-1.1/LICENSE.txt

%files -n geronimo-jaxr-1_0-api -f .mfiles-jaxr-1.0-api
%license geronimo-jaxr_1.0_spec-1.1/LICENSE.txt

%files -n geronimo-jaxrpc-1_1-api -f .mfiles-jaxrpc-1.1-api
%license geronimo-jaxrpc_1.1_spec-1.1/LICENSE.txt

%files -n geronimo-jms-1_1-api -f .mfiles-jms-1.1-api
%license geronimo-jms_1.1_spec-1.1/LICENSE.txt

%files -n geronimo-jpa-3_0-api -f .mfiles-jpa-3.0-api
%license geronimo-jpa_3.0_spec-1.1.0/LICENSE.txt

%files -n geronimo-jsp-2_0-api -f .mfiles-jsp-2.0-api
%license geronimo-jsp_2.0_spec-1.1/LICENSE.txt

%files -n geronimo-jsp-2_1-api -f .mfiles-jsp-2.1-api
%license geronimo-jsp_2.1_spec-1.0/LICENSE.txt

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

%files -n geronimo-stax-1_0-api -f .mfiles-stax-1.0-api
%license geronimo-stax-api_1.0_spec-1.0/LICENSE.txt

%files -n geronimo-ws-metadata-2_0-api -f .mfiles-ws-metadata-2.0-api
%license geronimo-ws-metadata_2.0_spec-1.1.1/LICENSE.txt

%changelog
