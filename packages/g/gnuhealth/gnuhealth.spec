#
# spec file for package gnuhealth
#
# Copyright (c) 2024 SUSE LLC
# Copyright (c) 2014-2024 Dr. Axel Braun
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


%bcond_with tests 1
%define         skip_python2 1

%if 0%{?suse_version} >= 1550
%define pythons python3
%define mypython python3
%define mysitelib %python3_sitelib
%else
%{?sle15_python_module_pythons}
%define mypython %pythons
%define mysitelib %{expand:%%%{mypython}_sitelib}
%endif

%define         t_version %(rpm -q --qf '%%{VERSION}' trytond)
%define         majorver 4.4

Name:           gnuhealth

Version:        %{majorver}.1
Release:        0
URL:            https://health.gnu.org
Summary:        A Health and Hospital Information System
License:        GPL-3.0-or-later
Group:          Productivity/Office/Management

Source0:        https://ftp.gnu.org/gnu/health/%{name}-%{version}.tar.gz
## Source0:        %{name}-%{version}.tar.gz
Source1:        GNUHealth.README.openSUSE
Source2:        gnuhealth-control
Source3:        gnuhealth.service
Source4:        gnuhealth-webdav@.service
Source5:        openSUSE-gnuhealth-setup
Source6:        gnuhealth
Source7:        gnuhealth-rpmlintrc
Source8:        https://ftp.gnu.org/gnu/health/%{name}-%{version}.tar.gz.sig
Source9:        https://savannah.gnu.org/project/memberlist-gpgkeys.php?group=health&download=1#/%{name}.keyring

## BuildRequires:  %{python_module pytest}
BuildRequires:  %{mypython}-pip
BuildRequires:  %{mypython}-devel
BuildRequires:  %{mypython}-setuptools
BuildRequires:  %{mypython}-wheel
BuildRequires:  fdupes
BuildRequires:  python-rpm-generators
BuildRequires:  python-rpm-macros

# For the tests:
BuildRequires:  trytond
BuildRequires:  trytond_company
BuildRequires:  trytond_currency
BuildRequires:  trytond_party
BuildRequires:  trytond_product

# new fonts for the forms:
Requires:       gnu-free-fonts
Requires:       %{mypython}-Pillow
Requires:       %{mypython}-PyWebDAV3-GNUHealth
Requires:       %{mypython}-caldav
Requires:       %{mypython}-hl7apy
Requires:       %{mypython}-ldap3
Requires:       %{mypython}-matplotlib
Requires:       %{mypython}-passlib
Requires:       %{mypython}-python-barcode
Requires:       %{mypython}-qrcode
Requires:       %{mypython}-simpleeval
Requires:       %{mypython}-six
Requires:       %{mypython}-vobject
Requires:       bsdtar
Requires:       proteus
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
BuildArch:      noarch

# additional suggestion for a useable editor
Suggests:       nano
# you may need a frontend to work with
Suggests:       gnuhealth-client

BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%{?systemd_ordering}

%description
GNU Health is the Hospital Information System adopted by the United
Nations University, International Institute for Global Health, for
the implementations and trainings.

This is the server component of GNU Health.
You would need the GNU Health Client as well, on the same or a different machine.
You may use the Tryton Client either
See https://en.opensuse.org/GNUHealth_on_openSUSE for instructions

%package -n %{name}-orthanc
Summary:        Integration module for Orthanc
Group:          Productivity/Office/Management
Requires:       %{mypython}-beren
Requires:       %{mypython}-pendulum
Requires:       %{mypython}-pydicom
Requires:       gnuhealth

%description -n %{name}-orthanc
This package provides the interface to Orthanc

%prep
%setup -q -n %{name}-%{version}
## %%patch -P 0 -p1
cp %{S:1} .
cp %{S:2} .

#shebag ersetzen
find . -iname "*.py" -exec sed -i "s/env python/%{mypython}/" '{}' \;

%build
for i in h*; do
  pushd $i
  %pyproject_wheel
  popd
done

%install
for i in h*; do
  pushd $i
  %pyproject_install
  popd
done

mkdir -p -m 755 %{buildroot}%{_bindir}
install -p -m 755 gnuhealth-control %{buildroot}%{_bindir}/gnuhealth-control
install -p -m 755 %{S:5} %{buildroot}%{_bindir}/openSUSE-gnuhealth-setup
install -p -m 755 %{S:6} %{buildroot}%{_bindir}/gnuhealth
install -p -m 755 scripts/demodb/install_demo_database.sh %{buildroot}%{_bindir}/install_demo_database.sh

#delete empty demo directory
rm -rf scripts/demodb

mkdir -p %{buildroot}%{_unitdir}
install -p -m 644 %{SOURCE3} %{buildroot}%{_unitdir}/%{name}.service
install -p -m 644 %{SOURCE4} %{buildroot}%{_unitdir}/%{name}-webdav@.service

mkdir -p %{buildroot}%{_sysconfdir}/tryton

#remove double license file:
## rm backend/fhir/client/COPYING

#Move FHIR server to examples directory
mkdir -p -m 755 %{buildroot}%{_docdir}/%{name}/examples/
mv doc/* %{buildroot}%{_docdir}/%{name}/examples/.
rmdir doc

%python_expand %fdupes %{buildroot}%{mysitelib}

%if %{with tests}
%check
cd %{buildroot}%{mysitelib}/trytond/modules
for i in h*; do
  pushd $i
    %pytest -rs tests
  popd
done
%endif

%pre
#Write environment changes to /etc/bash.bashrc.local
cat > /etc/bash.bashrc.local << "EOF"
alias cdlogs='cd /var/log/tryton'
alias cdexe='cd %python3_sitelib/trytond'
alias cdconf='cd /etc/tryton'
alias cdmods='cd %python3_sitelib/trytond/modules'
alias editconf='${EDITOR} /etc/tryton/trytond.conf'
alias cdutil='cd /usr/bin'
export EDITOR=nano
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
%{mysitelib}/%{name}_orthanc*
%{mysitelib}/trytond/modules/health_orthanc*

%files
%defattr(-,root,root)
%{_bindir}/gnuhealth
%{_bindir}/gnuhealth-control
%{_bindir}/gnuhealth-webdav-server
%{_bindir}/openSUSE-gnuhealth-setup
%{_bindir}/install_demo_database.sh
%{_unitdir}/%{name}.service
%{_unitdir}/%{name}-webdav@.service
%doc README.rst Changelog gnuhealth-setup version gnuhealthrc GNUHealth.README.openSUSE scripts/* config/*
%{_docdir}/%{name}/examples*
%dir %{_sysconfdir}/tryton
%license COPYING LICENSES/*
%exclude %{mysitelib}/%{name}_orthanc*
%exclude %{mysitelib}/trytond/modules/health_orthanc*
%{mysitelib}/trytond*
%{mysitelib}/gnuhealth*

%changelog
