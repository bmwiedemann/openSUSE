#
# spec file for package nvmetcli
#
# Copyright (c) 2022 SUSE LLC
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


Name:           nvmetcli
Version:        0.7
Release:        1%{?dist}
Summary:        Command line interface for the kernel NVMe nvmet
License:        Apache-2.0
Group:          System/Management
URL:            http://git.infradead.org/users/hch/nvmetcli.git
Source:         nvmetcli-v%{version}.tar.gz
Patch1:         %{name}-update-python-to-python3.patch
Patch2:         0001-nvmetcli-don-t-remove-ANA-Group-1-on-clear.patch
Patch3:         harden_nvmet.service.patch
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
Requires:       python3-configshell-fb
Requires:       python3-kmod
Requires(post): systemd
Requires(postun):systemd
Requires(preun):systemd
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
This package contains the command line interface to the NVMe over
Fabrics target in the Linux kernel. It allows configuring the NVMe
target interactively as well as saving / restoring the configuration
to / from a json file.

%prep
%setup -q -n nvmetcli-v%{version}
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
python3 setup.py build

%install
python3 setup.py install --skip-build --root=%{buildroot} --prefix=usr
mkdir -p %{buildroot}%{_sysconfdir}/nvmet
mkdir -p %{buildroot}%{_prefix}/sbin
install -m 755 nvmetcli %{buildroot}%{_sbindir}/nvmetcli
mkdir -p %{buildroot}%{_prefix}/usr/sbin
ln -s /usr/sbin/service %{buildroot}/usr/sbin/rcnvmet
mkdir -p %{buildroot}%{_unitdir}
install -m 644 nvmet.service %{buildroot}%{_unitdir}/nvmet.service

%post
%service_add_post nvmet.service

%pre
%service_add_pre nvmet.service

%preun
%service_del_preun nvmet.service

%postun
%service_del_postun nvmet.service

%files
%defattr(-,root,root,-)
%{python3_sitelib}
%dir %{_sysconfdir}/nvmet
%{_sbindir}/nvmetcli
/usr/sbin/rcnvmet
%{_unitdir}/nvmet.service
%doc COPYING README

%changelog
