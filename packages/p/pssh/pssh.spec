#
# spec file for package pssh
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           pssh
Version:        2.3.1
Release:        0
Summary:        Parallel SSH to control large numbers of Machines simultaneously
License:        BSD-3-Clause
Group:          Productivity/Clustering/Computing
Url:            http://code.google.com/p/parallel-ssh/
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
# PATCH-FIX-UPSTREAM 0007-test-Teardown-code-was-never-called.patch kgronlund@suse.com -- test:
# Teardown code was never called
Patch4:         0004-test-Teardown-code-was-never-called.patch
# PATCH-FEATURE-UPSTREAM 0005-Add-an-explicit-API-entrypoint.patch kgronlund@suse.com -- Add
# an explicit API entrypoint
Patch5:         0005-Add-an-explicit-API-entrypoint.patch
# PATCH-FIX-OPENSUSE 0006-openSUSE-Adjust-man-pages-destination.patch dejan@suse.de -- adjust
# man pages destination
Patch6:         0006-openSUSE-Adjust-man-pages-destination.patch
# PATCH-FIX-OPENSUSE 0007-openSUSE-Add-openSUSE-specific-pssh-askpass-location.patch dejan@suse.de -- add
# openSUSE specific pssh-askpass location
Patch7:         0007-openSUSE-Add-openSUSE-specific-pssh-askpass-location.patch
# PATCH-FEATURE-UPSTREAM 0008-openSUSE-add-C-pcmk_nodes-option-to-get-list-of-node.patch dejan@suse.de -- add
# -C/--pcmk_nodes option to get list of nodes from Pacemaker
Patch8:         0008-openSUSE-add-C-pcmk_nodes-option-to-get-list-of-node.patch
# PATCH-FEATURE-UPSTREAM Prepend hostname on each line when -P is set
Patch9:         0001-Prepend-hostname-on-each-line-when-P-is-set.patch
# PATCH-FIX-UPSTREAM Fix quiet option after API patch
Patch10:        0002-Fix-quiet-option-after-API-patch.patch
BuildRequires:  python-devel
BuildRequires:  python-setuptools
Requires:       python-pssh = %{version}-%{release}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
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
%setup -q
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1

%build
python setup.py build

%install
python setup.py install \
	 --prefix="%{_prefix}" \
	 --root=%{buildroot} \
	 --record-rpm=files.lst

# remove files under bin/ and man/ from rpmfiles.lst to include them in the main package
sed -i '/.*\/bin\/.*/d;/.*\/man\/.*/d' files.lst

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog COPYING
%{_mandir}/man1/pssh.1%{ext_man}
%{_mandir}/man1/pnuke.1%{ext_man}
%{_mandir}/man1/pscp.1%{ext_man}
%{_mandir}/man1/pslurp.1%{ext_man}
%{_mandir}/man1/prsync.1%{ext_man}
%{_bindir}/pnuke
%{_bindir}/prsync
%{_bindir}/pscp
%{_bindir}/pslurp
%{_bindir}/pssh
%{_bindir}/pssh-askpass

%files -n python-pssh -f files.lst
%defattr(-,root,root)
%doc AUTHORS ChangeLog COPYING

%changelog
