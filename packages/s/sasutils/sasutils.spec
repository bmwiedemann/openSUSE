#
# spec file for package sasutils
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


Name:           sasutils
Version:        0.5.0
Release:        1
Summary:        Serial Attached SCSI (SAS) utilities
License:        Apache-2.0
Group:          Hardware/Other
URL:            https://github.com/stanford-rc/sasutils
Source0:        https://files.pythonhosted.org/packages/source/s/%{name}/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  fdupes
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
Requires:       python3-setuptools
Requires:       sg3_utils
Requires:       smp_utils

%description
sasutils is a set of command-line tools, udev scripts and a Python
library to ease the administration of Serial Attached SCSI (SAS)
storage devices.

%prep
%setup -q

%build
%py3_build

%install
%py3_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
install -d %{buildroot}/%{_mandir}/man1
install -p -m 0644 doc/man/man1/sas_counters.1 %{buildroot}/%{_mandir}/man1/
install -p -m 0644 doc/man/man1/sas_devices.1 %{buildroot}/%{_mandir}/man1/
install -p -m 0644 doc/man/man1/sas_discover.1 %{buildroot}/%{_mandir}/man1/
install -p -m 0644 doc/man/man1/ses_report.1 %{buildroot}/%{_mandir}/man1/

%files
%{_bindir}/sas_counters
%{_bindir}/sas_devices
%{_bindir}/sas_discover
%{_bindir}/sas_mpath_snic_alias
%{_bindir}/sas_sd_snic_alias
%{_bindir}/sas_st_snic_alias
%{_bindir}/ses_report
%{python3_sitelib}/sasutils/
%{python3_sitelib}/sasutils-*
%{_mandir}/man1/sas_counters.1*
%{_mandir}/man1/sas_devices.1*
%{_mandir}/man1/sas_discover.1*
%{_mandir}/man1/ses_report.1*
%doc README.rst
%license LICENSE.txt

%changelog
