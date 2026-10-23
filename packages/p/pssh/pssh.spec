#
# spec file for package pssh
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%define pythons python3
%if ! %{defined python3_sitelib}
%define python3_sitelib %{_prefix}/lib/python3.6/site-packages/
%endif
Name:           pssh
Version:        2.3.6
Release:        0
Summary:        Parallel SSH to control large numbers of Machines simultaneously
License:        BSD-3-Clause
URL:            https://github.com/lilydjwg/pssh
Source:         https://github.com/lilydjwg/pssh/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
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
# setup.cfg (2.3.5+) no longer installs the man pages
install -Dpm 0644 -t %{buildroot}%{_mandir}/man1 man/man1/*.1
%fdupes %{buildroot}%{python3_sitelib}

%check
# upstream's test/test.py needs live ssh hosts: smoke-test the CLIs only
export PYTHONPATH=%{buildroot}%{python3_sitelib}
for t in pssh pscp prsync pslurp pnuke; do
  %{buildroot}%{_bindir}/$t --version
done

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
%{python3_sitelib}/%{name}-%{version}.dist-info
%{python3_sitelib}/%{name}lib

%changelog
