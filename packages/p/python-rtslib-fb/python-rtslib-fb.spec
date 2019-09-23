#
# spec file for package python-rtslib-fb
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


%define dbdir %{_sysconfdir}/target
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-rtslib-fb
Version:        2.1.70
Release:        0%{?dist}
Summary:        API for Linux kernel SCSI target (aka LIO)
License:        Apache-2.0
Group:          Development/Languages/Python
Url:            https://github.com/open-iscsi/rtslib-fb.git
Source:         %{name}-v%{version}.tar.xz
Patch1:         rbd-support.patch
BuildRequires:  %{python_module pyudev}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-pyudev
Requires(post): update-alternatives
Requires(postun): update-alternatives
Provides:       python-rtslib = %{version}-%{release}
Obsoletes:      python-rtslib < %{version}
%if 0%{?sle_version} >= 150000
# explicit Provides advertising RBD support
Provides:       python-rtslib-rbd = %{version}
Obsoletes:      python-rtslib-rbd < %{version}
%endif
BuildArch:      noarch
%python_subpackages

%description
rtslib-fb is an object-based Python library for configuring the LIO generic
SCSI target, present in 3.x Linux kernel versions. rtslib-fb is licensed under
the Apache 2.0 license. Contributions are welcome

%prep
%setup -q -n %{name}-v%{version}
%if 0%{?sle_version} >= 150000
# RBD support is dependent on LIO changes present in the SLE/Leap kernel
%patch1 -p1
%endif

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}/%{_bindir}/targetctl
%fdupes %{buildroot}
install -d -m755 %{buildroot}%{_mandir}/man5
install -m644 doc/saveconfig.json.5 %{buildroot}%{_mandir}/man5
%python_clone -a %{buildroot}%{_mandir}/man5/saveconfig.json.5
install -d -m755 %{buildroot}%{_mandir}/man8
install -m644 doc/targetctl.8 %{buildroot}%{_mandir}/man8
%python_clone -a %{buildroot}%{_mandir}/man8/targetctl.8
install -d -m755 %{buildroot}/%{dbdir}
install -d -m755 %{buildroot}/%{dbdir}/pr
install -d -m755 %{buildroot}/%{dbdir}/alua

%post
%python_install_alternative targetctl targetctl.8 saveconfig.json.5

%postun
%python_uninstall_alternative targetctl

%files %{python_files}
%python_alternative %{_bindir}/targetctl
%{python_sitelib}/*
%doc COPYING README.md
%doc %python_alternative %{_mandir}/man5/saveconfig.json.5.gz
%doc %python_alternative %{_mandir}/man8/targetctl.8.gz
%dir %{dbdir}
%dir %{dbdir}/pr
%dir %{dbdir}/alua

%changelog
