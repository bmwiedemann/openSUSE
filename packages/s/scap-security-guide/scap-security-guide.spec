#
# spec file for package scap-security-guide
#
# Copyright (c) 2024 SUSE LLC
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


%if ! (0%{?fedora} || 0%{?rhel} > 5)
%if "%{_vendor}" == "debbuild"
%global __python /usr/bin/python3
%endif
%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}
%{!?python_sitearch: %global python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib(1))")}
%endif

%if 0%{?fedora} || 0%{?rhel} >= 8
%{!?pylint_check: %global pylint_check 0}
%endif

%if 0%{?fedora} || 0%{?suse_version} > 1320 || 0%{?rhel} >= 8 || "%{_vendor}" == "debbuild"
%global build_py3   1
%if "%{_vendor}" != "debbuild"
%global python_sitelib %{python3_sitelib}
%endif
%endif

%if 0%{?fedora} || 0%{?rhel} >= 8
%global python2prefix python2
%else
%global python2prefix python
%endif

Name:           scap-security-guide
Version:        0.1.73
Release:        0
Summary:        XCCDF files for SUSE Linux and openSUSE
License:        BSD-3-Clause
Group:          Productivity/Security
URL:            https://github.com/ComplianceAsCode/content
%if "%{_vendor}" == "debbuild"
Packager:       SUSE Security Team <security@suse.de>
%endif
Source:         https://github.com/ComplianceAsCode/content/archive/v%{version}.tar.gz

# explicit require what is needed by the detection logic in the scripts
Requires:       coreutils
Requires:       findutils
Requires:       gawk
Requires:       grep
Requires:       sed
Requires:       sudo
Requires:       zypper

BuildRequires:  cmake

%if "%{_vendor}" == "debbuild"
%{!?_licensedir:%global license %%doc}
BuildRequires:  libopenscap8
BuildRequires:  libxml2-utils
BuildRequires:  libxslt1.1
BuildRequires:  xsltproc
%else
BuildRequires:  libxslt
BuildRequires:  openscap-utils
%endif

%if 0%{?rhel} == 7
BuildRequires:  python-setuptools
%else
BuildRequires:  python3-setuptools
%endif

%if 0%{?rhel} == 8
BuildRequires:  python3
%endif

%if 0%{?suse_version}
BuildRequires:  python3-xml
%endif

%if 0%{?rhel} == 7
BuildRequires:  PyYAML
%else
%if 0%{?rhel} == 8
BuildRequires:  python3-pyyaml
%else
%if "%{_vendor}" == "debbuild"
BuildRequires:  python3-yaml
%else
BuildRequires:  python3-PyYAML
%endif
%endif
%endif

%if 0%{?rhel} == 7
BuildRequires:  python-jinja2
%else
%if 0%{?rhel} >= 8
BuildRequires:  python3-jinja2
%else
%if "%{_vendor}" == "debbuild"
BuildRequires:  python3-jinja2
%else
BuildRequires:  python3-Jinja2
%endif
%endif
%endif

BuildRequires:  expat
BuildRequires:  libxml2
# not on SLES currently
%if 0%{?is_opensuse} || 0%{?fedora} || "%{_vendor}" == "debbuild"
BuildRequires:  ansible
%endif
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
Security Content Automation Protocol (SCAP) Security Guide for SUSE Linux.

This package contains XCCDF (Extensible Configuration Checklist
Description Format), OVAL (Open Vulnerability and Assessment
Language), CPE (Common Platform Enumeration) and DS (Data Stream)
files to run a compliance test on SLE12, SLE15 and openSUSE

SUSE supported in this version of scap-security-guide:

- DISA STIG profile for SUSE Linux Enterprise Server 12 and 15
- ANSSI-BP-028 profile for SUSE Linux Enterprise Server 12 and 15
- PCI-DSS profile for SUSE Linux Enterprise Server 12 and 15
- HIPAA profile for SUSE Linux Enterprise Server 12 and 15
- CIS profile for SUSE Linux Enterprise Server 12 and 15
- Hardening for Public Cloud Image of SUSE Linux Enterprise Server for SAP Applications 15
- Public Cloud Hardening for SUSE Linux Enterprise 15

Other profiles, like the Standard System Security Profile for SUSE Linux Enterprise 12 and 15,
are community supplied and not officially supported by SUSE.

%package redhat
Summary:        XCCDF files for RHEL, CentOS, Fedora and ScientificLinux
Group:          Productivity/Security
%if 0%{?fedora} || 0%{?rhel}
Conflicts:      scap-security-guide
%endif

%description redhat
Security Content Automation Protocol (SCAP) Security Guide for Redhat/Fedora/CentOS/OracleLinux/ScientificLinux.

This package contains XCCDF (Extensible Configuration Checklist
Description Format), OVAL (Open Vulnerability and Assessment
Language), CPE (Common Platform Enumeration) and DS (Data Stream)
files to run a compliance test on various Redhat products, CentOS, Oracle Linux, Fedora and ScientificLinux.

Note that the included profiles are community supplied and not officially supported by SUSE..

%package debian
Summary:        XCCDF files for Debian
Group:          Productivity/Security

%description debian
Security Content Automation Protocol (SCAP) Security Guide for Debian.

This package contains XCCDF (Extensible Configuration Checklist
Description Format), OVAL (Open Vulnerability and Assessment
Language), CPE (Common Platform Enumeration) and DS (Data Stream)
files to run a compliance test on Debian.

Note that the included profiles are community supplied and not officially supported by SUSE..

%package ubuntu
Summary:        XCCDF files for Ubuntu
Group:          Productivity/Security

%description ubuntu
Security Content Automation Protocol (SCAP) Security Guide for Ubuntu.

This package contains XCCDF (Extensible Configuration Checklist
Description Format), OVAL (Open Vulnerability and Assessment
Language), CPE (Common Platform Enumeration) and DS (Data Stream)
files to run a compliance test on Ubuntu.

Note that the included profiles are community supplied and not officially supported by SUSE..

%prep
%setup -q -n content-%version

%build
cd build
cmake -DCMAKE_INSTALL_PREFIX=%{_prefix} \
      -DCMAKE_INSTALL_MANDIR=%{_mandir} \
      -DSSG_PRODUCT_CHROMIUM=OFF \
	 -DSSG_PRODUCT_ALINUX2=OFF \
	 -DSSG_PRODUCT_ALINUX3=OFF \
	 -DSSG_PRODUCT_DEBIAN9=ON \
	 -DSSG_PRODUCT_DEBIAN10=ON \
	 -DSSG_PRODUCT_DEFAULT=ON \
	 -DSSG_PRODUCT_EXAMPLE=OFF \
	 -DSSG_PRODUCT_FEDORA=ON \
	 -DSSG_PRODUCT_FIREFOX=OFF \
	 -DSSG_PRODUCT_FUSE6=OFF \
	 -DSSG_PRODUCT_JRE=OFF \
	 -DSSG_PRODUCT_MACOS1015=OFF \
	 -DSSG_PRODUCT_OCP4=OFF \
	 -DSSG_PRODUCT_OL7=ON \
	 -DSSG_PRODUCT_OL8=ON \
	 -DSSG_PRODUCT_OL9=ON \
	 -DSSG_PRODUCT_OPENSUSE=ON \
	 -DSSG_PRODUCT_OPENEMBEDDED=OFF \
	 -DSSG_PRODUCT_RHCOS4=ON \
	 -DSSG_PRODUCT_RHEL7=ON \
	 -DSSG_PRODUCT_RHEL8=ON \
	 -DSSG_PRODUCT_RHEL9=ON \
	 -DSSG_PRODUCT_RHOSP10=ON \
	 -DSSG_PRODUCT_RHOSP13=ON \
	 -DSSG_PRODUCT_RHV4=ON \
	 -DSSG_PRODUCT_SLE12=ON \
	 -DSSG_PRODUCT_SLE15=ON \
	 -DSSG_PRODUCT_UBUNTU1604=ON \
	 -DSSG_PRODUCT_UBUNTU1804=ON \
	 -DSSG_PRODUCT_UBUNTU2004=ON \
	 -DSSG_PRODUCT_UBUNTU2204=ON \
	 -DSSG_PRODUCT_UOS20=OFF \
         -DSSG_PRODUCT_VSEL=OFF \
         -DSSG_PRODUCT_EKS=OFF \
         -DSSG_PRODUCT_WRLINUX8=OFF \
         -DSSG_PRODUCT_WRLINUX1019=OFF \
         -DSSG_PRODUCT_ANOLIS8=OFF \
         -DSSG_PRODUCT_ANOLIS23=OFF \
         ../
make

%install
cd build/
make install DESTDIR=%buildroot

%files
%if "%{_vendor}" != "debbuild"
%license LICENSE
%endif
%dir %{_datadir}/doc/scap-security-guide/
%{_datadir}/doc/scap-security-guide/Contributors.md
%{_datadir}/doc/scap-security-guide/README.md
%{_datadir}/doc/scap-security-guide/LICENSE
%dir %{_datadir}/doc/scap-security-guide/guides/
%doc %{_datadir}/doc/scap-security-guide/guides/ssg-sle*
%doc %{_datadir}/doc/scap-security-guide/guides/ssg-opensuse*
%dir %{_datadir}/doc/scap-security-guide/tables/
%doc %{_datadir}/doc/scap-security-guide/tables/table-sle*
%doc %{_mandir}/man8/scap-security-guide.8.gz
%dir %{_datadir}/scap-security-guide/
%dir %{_datadir}/scap-security-guide/ansible/
%dir %{_datadir}/scap-security-guide/bash/
%dir %{_datadir}/scap-security-guide/kickstart/
%{_datadir}/scap-security-guide/*/opensuse*
%{_datadir}/scap-security-guide/*/sle*
%dir %{_datadir}/xml/scap/
%dir %{_datadir}/xml/scap/ssg/
%dir %{_datadir}/xml/scap/ssg/content/
%{_datadir}/xml/scap/ssg/content/*-sle*
%{_datadir}/xml/scap/ssg/content/*-opensuse*

%files redhat
%if "%{_vendor}" != "debbuild"
%license LICENSE
%endif
%dir %{_datadir}/doc/scap-security-guide/guides/
%doc %{_datadir}/doc/scap-security-guide/guides/ssg-centos*
%doc %{_datadir}/doc/scap-security-guide/guides/ssg-cs9*
%doc %{_datadir}/doc/scap-security-guide/guides/ssg-fedora*
%doc %{_datadir}/doc/scap-security-guide/guides/ssg-ol*
%doc %{_datadir}/doc/scap-security-guide/guides/ssg-openeuler*
%doc %{_datadir}/doc/scap-security-guide/guides/ssg-rh*
%doc %{_datadir}/doc/scap-security-guide/guides/ssg-sl7*
%dir %{_datadir}/doc/scap-security-guide/tables/
%doc %{_datadir}/doc/scap-security-guide/tables/table-ol*
%doc %{_datadir}/doc/scap-security-guide/tables/table-rh*
%dir %{_datadir}/doc/scap-security-guide/
%dir %{_datadir}/scap-security-guide/
%dir %{_datadir}/scap-security-guide/ansible/
%dir %{_datadir}/scap-security-guide/tailoring/
%dir %{_datadir}/scap-security-guide/bash/
%dir %{_datadir}/scap-security-guide/kickstart/
%{_datadir}/scap-security-guide/*/*centos*
%{_datadir}/scap-security-guide/*/*cs9*
%{_datadir}/scap-security-guide/*/*fedora*
%{_datadir}/scap-security-guide/*/*ol*
%{_datadir}/scap-security-guide/*/*openeuler*
%{_datadir}/scap-security-guide/*/*rh*
%{_datadir}/scap-security-guide/*/*sl7*
%dir %{_datadir}/xml/scap/
%dir %{_datadir}/xml/scap/ssg/
%dir %{_datadir}/xml/scap/ssg/content/
%{_datadir}/xml/scap/ssg/content/*-centos*
%{_datadir}/xml/scap/ssg/content/*-cs9*
%{_datadir}/xml/scap/ssg/content/*-fedora*
%{_datadir}/xml/scap/ssg/content/*-ol*
%{_datadir}/xml/scap/ssg/content/*-openeuler*
%{_datadir}/xml/scap/ssg/content/*-rh*
%{_datadir}/xml/scap/ssg/content/*-sl7*

%files debian
%if "%{_vendor}" != "debbuild"
%license LICENSE
%endif
%dir %{_datadir}/doc/scap-security-guide/guides/
%doc %{_datadir}/doc/scap-security-guide/guides/ssg-debian*
%dir %{_datadir}/doc/scap-security-guide/tables/
%dir %{_datadir}/doc/scap-security-guide/
%dir %{_datadir}/scap-security-guide/
%dir %{_datadir}/scap-security-guide/ansible/
%dir %{_datadir}/scap-security-guide/bash/
%dir %{_datadir}/scap-security-guide/kickstart/
%{_datadir}/scap-security-guide/*/*debian*
%dir %{_datadir}/xml/scap/
%dir %{_datadir}/xml/scap/ssg/
%dir %{_datadir}/xml/scap/ssg/content/
%{_datadir}/xml/scap/ssg/content/*-debian*

%files ubuntu
%if "%{_vendor}" != "debbuild"
%license LICENSE
%endif
%dir %{_datadir}/doc/scap-security-guide/guides/
%doc %{_datadir}/doc/scap-security-guide/guides/ssg-ubuntu*
%dir %{_datadir}/doc/scap-security-guide/tables/
%dir %{_datadir}/doc/scap-security-guide/
%dir %{_datadir}/scap-security-guide/
%dir %{_datadir}/scap-security-guide/ansible/
%dir %{_datadir}/scap-security-guide/bash/
%dir %{_datadir}/scap-security-guide/kickstart/
%{_datadir}/scap-security-guide/*/*ubuntu*
%dir %{_datadir}/xml/scap/
%dir %{_datadir}/xml/scap/ssg/
%dir %{_datadir}/xml/scap/ssg/content/
%{_datadir}/xml/scap/ssg/content/*-ubuntu*

%changelog
