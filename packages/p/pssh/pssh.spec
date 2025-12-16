#
# spec file for package pssh
#
# Copyright (c) 2025 SUSE LLC
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


%define pkg_version 2.3.4
%define pythons python3
%if ! %{defined python3_sitelib}
%define python3_sitelib /usr/lib/python3.6/site-packages/
%endif

Name:           pssh
Version:        2.3.4+git10.d4909c9
Release:        0
Summary:        Parallel SSH to control large numbers of Machines simultaneously
License:        BSD-3-Clause
Group:          Productivity/Clustering/Computing
URL:            https://github.com/lilydjwg/pssh
Source:         pssh-%{version}.tar.xz
# PATCH-FIX-OPENSUSE 0001-Remove-shebangs-from-library-files.patch dejan@suse.de -- remove
# shebangs from library files
Patch1:         0001-Remove-shebangs-from-library-files.patch
# PATCH-FEATURE-UPSTREAM 0002-Add-quiet-option.patch dejan@suse.de -- add
# the -q (quiet) option
Patch2:         0002-Add-quiet-option.patch
# PATCH-FIX-UPSTREAM 0003-Fix-order-of-command-statuses-returned-by-the-Manage.patch bnc#828897 dejan@suse.de -- Fix
# order of command statuses returned by the Manager
Patch3:         0003-Fix-order-of-command-statuses-returned-by-the-Manage.patch
# PATCH-FIX-OPENSUSE 0007-openSUSE-Add-openSUSE-specific-pssh-askpass-location.patch dejan@suse.de -- add
# openSUSE specific pssh-askpass location
Patch7:         0007-openSUSE-Add-openSUSE-specific-pssh-askpass-location.patch
# PATCH-FEATURE-UPSTREAM 0008-openSUSE-add-C-pcmk_nodes-option-to-get-list-of-node.patch dejan@suse.de -- add
# -C/--pcmk_nodes option to get list of nodes from Pacemaker
Patch8:         0008-openSUSE-add-C-pcmk_nodes-option-to-get-list-of-node.patch
# PATCH-FEATURE-UPSTREAM Prepend hostname on each line when -P is set
Patch9:         0001-Prepend-hostname-on-each-line-when-P-is-set.patch
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-pssh = %{version}-%{release}
BuildArch:      noarch

%description
pssh provides parallel versions of the OpenSSH tools that are useful for
controlling large numbers of machines simultaneously. It includes parallel
versions of ssh, scp, and rsync, as well as a parallel kill command.

%package -n python-pssh
Summary:        Python Module for Parallel SSH
Group:          Development/Libraries/Python
Requires:       openssh
Requires:       rsync

%description -n python-pssh
pssh provides parallel versions of the OpenSSH tools that are useful for
controlling large numbers of machines simultaneously. It includes parallel
versions of ssh, scp, and rsync, as well as a parallel kill command.

This package contains the pssh Python module.

%prep
%autosetup -p1

%build
%pyproject_wheel

%install
%pyproject_install
%fdupes %{buildroot}%{python3_sitelib}

%files
%doc AUTHORS ChangeLog
%license COPYING
%if 0%{?centos_version} || 0%{?centos} || 0%{?rhel_version} || 0%{?rhel}
%{!?ext_man: %define ext_man .gz}
%endif
%{_mandir}/man1/pssh.1%{?ext_man}
%{_mandir}/man1/pnuke.1%{?ext_man}
%{_mandir}/man1/pscp.1%{?ext_man}
%{_mandir}/man1/pslurp.1%{?ext_man}
%{_mandir}/man1/prsync.1%{?ext_man}
%{_bindir}/pnuke
%{_bindir}/prsync
%{_bindir}/pscp
%{_bindir}/pslurp
%{_bindir}/pssh
%{_bindir}/pssh-askpass

%files -n python-pssh
%license COPYING
%doc AUTHORS ChangeLog
%{python3_sitelib}/%{name}-%{pkg_version}.dist-info
%{python3_sitelib}/%{name}lib

%changelog
