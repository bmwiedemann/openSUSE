#
# spec file for package python3-azurectl
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           python3-azurectl
Version:        3.0.4
Release:        0
Url:            https://github.com/SUSE/azurectl
Summary:        Command Line Interface to manage Microsoft Azure services
License:        Apache-2.0
Group:          Development/Languages/Python
Source:         python3-azurectl-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
Requires:       man
Requires:       openssl
Requires:       python3-APScheduler
Requires:       python3-azure-servicemanagement-legacy
Requires:       python3-azure-storage >= 0.30.0
Requires:       python3-cryptography
Requires:       python3-docopt
Requires:       python3-pyOpenSSL
Requires:       python3-python-dateutil
Requires:       python3-setuptools
BuildArch:      noarch

# Package renamed in SLE 12, do not remove Provides, Obsolete directives
# until after SLE 12 EOL
Provides:       python-azurectl = %{version}
Obsoletes:      python-azurectl < %{version}

%description
Management tool for the Microsoft Azure public cloud service.
It allows uploading, registering and maintaining OS images for
multiple Azure Account Subscriptions.

%prep
%setup -q -n azurectl-%{version}

%build
python3 setup.build.py build

%install
python3 setup.build.py install --prefix=%{_prefix} --root=%{buildroot}
mkdir -p %{buildroot}/etc/bash_completion.d
cp completion/azurectl.sh %{buildroot}/etc/bash_completion.d

mkdir -p %{buildroot}/%{_mandir}/man1
for i in doc/man/*.gz; do \
    install -m 644 $i %{buildroot}/usr/share/man/man1 ;\
done

%files
%defattr(-,root,root,-)
%{_bindir}/azurectl
%{python3_sitelib}/*
%config /etc/bash_completion.d/azurectl.sh
%doc %{_mandir}/man1/*

%changelog
