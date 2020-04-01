#
# spec file for package gnuhealth
#
# Copyright (c) 2020 SUSE LLC
# Copyright (c) 2014-2020 Dr. Axel Braun
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


%define         t_version %(rpm -q --qf '%%{VERSION}' trytond)
%define         majorver 3.6
Name:           gnuhealth

Version:        %{majorver}.3
Release:        0

# List of additional build dependencies
BuildRequires:  fdupes
BuildRequires:  python3-rpm-macros
BuildRequires:  python3-setuptools

# For the variables:
BuildRequires:  trytond

URL:            http://health.gnu.org
Source0:        %{name}-%{version}.tar.gz
###http://ftp.gnu.org/gnu/health/%{name}-%{version}.tar.gz
Source1:        GNUHealth.README.SUSE
Source2:        gnuhealth-control
Source3:        gnuhealth.service
Source4:        gnuhealth-webdav@.service
Source5:        openSUSE-gnuhealth-setup
Source6:        gnuhealth
Source7:        gnuhealth-rpmlintrc
Patch0:         shebang.diff
##atch1:         xmlfix.diff
##atch2:         demo.diff

BuildArch:      noarch

Summary:        A Health and Hospital Information System
License:        GPL-3.0-or-later
Group:          Productivity/Office/Management

Requires:       bsdtar
Requires:       proteus
Requires:       python3-PyWebDAV3-GNUHealth
Requires:       python3-caldav
Requires:       python3-hl7apy
Requires:       python3-ldap3
Requires:       python3-passlib
Requires:       python3-pyBarcode
Requires:       python3-qrcode
Requires:       python3-simpleeval
Requires:       python3-six
Requires:       python3-vobject
Requires:       trytond
Requires:       trytond_account
Requires:       trytond_account_invoice
Requires:       trytond_account_invoice_stock
Requires:       trytond_account_product
Requires:       trytond_company
Requires:       trytond_country
Requires:       trytond_currency
Requires:       trytond_party
Requires:       trytond_product
Requires:       trytond_purchase
Requires:       trytond_purchase_request
Requires:       trytond_stock
Requires:       trytond_stock_lot
Requires:       trytond_stock_supply

# additional suggestion for a useable editor
Suggests:       nano
# you may need a frontend to work with
Suggests:       gnuhealth-client

BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
GNU Health is the Hospital Information System adopted by the United
Nations University, International Institute for Global Health, for
the implementations and trainings.

This is the server component of GNU Health. 
You would need the GNU Health Client as well, on the same or a different machine. You may use the Tryton Client either

%package -n %{name}-orthanc
Summary:        Integration module for Orthanc
Group:          Productivity/Office/Management
Requires:       gnuhealth
Requires:       python3-beren
Requires:       python3-pendulum

%description -n %{name}-orthanc
This package provides the interface to Orthanc

%prep
%setup -q -n %{name}-%{version}
%patch0 -p1
##atch1 -p1
##atch2 -p1
cp %{S:1} .
cp %{S:2} .

%build
for i in h*; do
  cd $i
  python3 setup.py build
  cd ..
done

%install
for i in h*; do
  cd $i
  python3 setup.py install --prefix=%_prefix --root=%buildroot 
  cd ..
done

mkdir -p -m 755 %{buildroot}%{_bindir}
install -p -m 755 gnuhealth-control %{buildroot}%{_bindir}/gnuhealth-control
install -p -m 755 %{S:5} %{buildroot}%{_bindir}/openSUSE-gnuhealth-setup
install -p -m 755 %{S:6} %{buildroot}%{_bindir}/gnuhealth
install -p -m 755 scripts/demo/install_demo_database.sh %{buildroot}%{_bindir}/install_demo_database.sh

#delete empty demo directory
rm -rf scripts/demo

mkdir -p %{buildroot}%{_unitdir}
install -p -m 644 %{SOURCE3} %{buildroot}%{_unitdir}/%{name}.service
install -p -m 644 %{SOURCE4} %{buildroot}%{_unitdir}/%{name}-webdav@.service

mkdir -p %{buildroot}%{_sysconfdir}/tryton

#remove double license file:
rm backend/fhir/client/COPYING

#Move FHIR serer to examples directory
mkdir -p -m 755 %{buildroot}%{_docdir}/%{name}/examples/
mv backend/fhir* %{buildroot}%{_docdir}/%{name}/examples/.
rmdir backend

%python_expand %fdupes %{buildroot}%{$python_sitelib}

%pre
#Write environment changes to /etc/bash.bashrc.local
cat > /etc/bash.bashrc.local << "EOF"
alias cdlogs='cd /var/log/tryton'
alias cdexe='cd $(ls -d /usr/lib/python3.* )/site-packages/trytond'
alias cdconf='cd /etc/tryton'
alias cdmods='cd $(ls -d /usr/lib/python3.* )/site-packages/trytond/modules'
alias editconf='${EDITOR} /etc/tryton/trytond.conf'
alias cdutil='cd /usr/bin'
EOF

#Write GH Variable /etc/tryton/gnuhealthrc 
cat > /etc/tryton/gnuhealthrc << "EOF"
GNUHEALTH_VERSION=%{version}
TRYTON_VERSION=%{t_version}
EOF

%service_add_pre gnuhealth.service
%service_add_pre gnuhealth-webdav@.service

%post
%service_add_post gnuhealth.service
%service_add_post gnuhealth-webdav@.service

%preun
%service_del_preun gnuhealth.service
%service_del_preun gnuhealth-webdav@.service

%postun
%service_del_postun gnuhealth.service
%service_del_postun gnuhealth-webdav@.service

%files -n %{name}-orthanc
%{python3_sitelib}/%{name}_orthanc*
%{python3_sitelib}/trytond/modules/health_orthanc*

%files 
%{_bindir}/gnuhealth-control
%{_bindir}/openSUSE-gnuhealth-setup
%{_bindir}/install_demo_database.sh
%{_unitdir}/%{name}.service
%{_unitdir}/%{name}-webdav@.service
%doc README Changelog gnuhealth-setup version gnuhealthrc GNUHealth.README.SUSE scripts/* config/* doc/*
%{_docdir}/%{name}/examples* 
%dir %{_sysconfdir}/tryton
%license COPYING
%exclude %{python3_sitelib}/%{name}_orthanc*
%exclude %{python3_sitelib}/trytond/modules/health_orthanc*
%{python_sitelib}/*

%changelog
