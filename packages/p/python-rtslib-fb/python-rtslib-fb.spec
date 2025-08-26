#
# spec file for package python-rtslib-fb
#
# Copyright (c) 2025 SUSE LLC and contributors
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
%define oldpython python
%define cpkg %{oldpython}-rtslib-fb-common
%if 0%{?suse_version} > 1500
%bcond_without libalternatives
%else
%bcond_with libalternatives
%endif
%{?sle15_python_module_pythons}
Name:           python-rtslib-fb
Version:        2.2.2
Release:        0%{?dist}
Summary:        API for Linux kernel SCSI target (aka LIO)
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/open-iscsi/rtslib-fb.git
Source:         python-rtslib-fb-v%{version}.tar.xz
Patch1:         rtslib-target-service-for-suse.patch
Patch2:         Install-targetctl-as-an-entrypoint.patch
Patch3:         Remove-use-of-usr-bin-python.patch
Patch4:         Fix-issue-with-Path-open-needs-parenthesis.patch
Patch5:         fabric-fix-search-path-for-SRPT-wwn.patch
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module hatch_vcs}
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pyudev}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  git
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros >= 20210929
BuildRequires:  pkgconfig(systemd)
Requires:       %{cpkg}
Requires:       python-pyudev
Provides:       python-rtslib = %{version}-%{release}
Obsoletes:      python-rtslib < %{version}
BuildArch:      noarch
%if %{with libalternatives}
BuildRequires:  alts
Requires:       alts
%else
Requires(post): update-alternatives
Requires(postun): update-alternatives
%endif
%python_subpackages

%description
rtslib-fb is an object-based Python library for configuring the LIO generic
SCSI target, present in 3.x Linux kernel versions. rtslib-fb is licensed under
the Apache 2.0 license. Contributions are welcome

%package -n %{cpkg}
Summary:        Common python-rtslib-fb subpackage for all Python 3 versions
Group:          Development/Languages/Python
Obsoletes:      %{name} < %{version}-%{release}

%description -n %{cpkg}
python-rtslib-fb-common is the invariant base package needed by all
version of python3*-rtslib-fb.

%prep
%autosetup -p1 -n python-rtslib-fb-v%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}/%{_bindir}/targetctl
install -d -m755 %{buildroot}%{_mandir}/man5
install -m644 doc/saveconfig.json.5 %{buildroot}%{_mandir}/man5
install -d -m755 %{buildroot}%{_mandir}/man8
install -m644 doc/targetctl.8 %{buildroot}%{_mandir}/man8
install -d -m755 %{buildroot}/%{dbdir}
install -d -m755 %{buildroot}/%{dbdir}/pr
install -d -m755 %{buildroot}/%{dbdir}/alua
mkdir -p %{buildroot}/%{_unitdir}/
install -m644 systemd/target.service %{buildroot}/%{_unitdir}
install -d -m755 %{buildroot}%{_sbindir}
%fdupes %{buildroot}
ln -s %{_sbindir}/service %{buildroot}/%{_sbindir}/rctarget

%post
%python_install_alternative targetctl
%{service_add_post target.service}

%postun
%python_uninstall_alternative targetctl
%{service_del_postun target.service}

%pre
%python_libalternatives_reset_alternative targetctl
%{service_add_pre target.service}

%preun
%{stop_on_removal target}
%{service_del_preun target.service}

%post -n %{cpkg}
%{service_add_post target.service}

%postun -n %{cpkg}
%{service_del_postun target.service}

%pre -n %{cpkg}
%{service_add_pre target.service}

%preun -n %{cpkg}
%{service_del_preun target.service}

%files %{python_files}
%python_alternative %{_bindir}/targetctl
%{python_sitelib}/rtslib*
%pycache_only %{python_sitelib}/__pycache__

%files -n %{cpkg}
%license COPYING
%doc README.md
%dir %{dbdir}
%dir %{dbdir}/pr
%dir %{dbdir}/alua
%{_unitdir}/target.service
%{_sbindir}/rctarget
%{_mandir}/man5/saveconfig.json.5%{?ext_man}
%{_mandir}/man8/targetctl.8%{?ext_man}

%changelog
