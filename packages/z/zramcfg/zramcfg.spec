#
# spec file for package zramcfg
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


%define version_unconverted 0.2

Name:           zramcfg
Version:        0.2
Release:        0
Summary:        ZRAM configuration
License:        GPL-2.0+
Group:          System/Kernel
Url:            https://github.com/hreinecke/zramcfg
Source:         %{name}-%{version}.tar.xz
BuildRequires:  python
BuildRequires:  systemd-rpm-macros
BuildArch:      noarch

%description
zramcfg is a script to configure ZRAM devices in the system. It provides
a systemd service for enabling saving and loading the ZRAM configuration
during bootup and shutdown.

%prep
%setup

%build

%install
python setup.py install --prefix=%{_prefix} --root=%{buildroot}
chmod a+x "%{buildroot}/%{python_sitelib}/%{name}.py"
mkdir -p "%{buildroot}/%{_sbindir}"
ln -sf ../..%{python_sitelib}/%{name}.py "%{buildroot}/%{_sbindir}/%{name}"

%preun
%service_del_preun %{name}.service

%postun
%service_del_postun %{name}.service

%pre
%service_add_pre %{name}.service

%post
%service_add_post %{name}.service

%files
%defattr(-,root,root,-)
%{_unitdir}/%{name}.service
%{_sbindir}/%{name}
%{_mandir}/man8/*.8*
%{python_sitelib}/*

%changelog
