#
# spec file for package qpid-tools
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           qpid-tools
Version:        0.32
Release:        0
Summary:        Management and diagostic tools for Apache Qpid
License:        Apache-2.0
Group:          Productivity/Networking/Other
Url:            http://qpid.apache.org
Source0:        http://www.apache.org/dist/qpid/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  python
BuildRequires:  python-devel
Requires:       python-qpid
Requires:       python-qpid-qmf
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Management and diagnostic tools for Apache Qpid brokers and clients.

%files
%defattr(-,root,root,-)
%{_bindir}/qpid-config
%{_bindir}/qpid-ha
%{_bindir}/qpid-printevents
%{_bindir}/qpid-queue-stats
%{_bindir}/qpid-route
%{_bindir}/qpid-stat
%{_bindir}/qpid-tool
%{python_sitelib}
%doc LICENSE.txt NOTICE.txt

%prep
%setup -q

%build
python setup.py build

%install
python setup.py install \
	--skip-build \
    --prefix %{_prefix} \
	--install-purelib %{python_sitelib} \
	--root %{buildroot}

# clean up items we're not installing
rm -f  %{buildroot}/%{_bindir}/qmf*
rm -rf %{buildroot}/%{_datadir}/qpid-tools
rm -rf %{buildroot}/%{_prefix}/libexec/qpid-qls-analyze

%fdupes -s %{buildroot}

%changelog
