#
# spec file for package python-avocado-plugins-vt
#
# Copyright (c) 2021 SUSE LLC
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define pythons python3
Name:           python-avocado-plugins-vt
Version:        88.0
Release:        0
Summary:        Avocado Virt Test Plugin
License:        GPL-2.0-only
URL:            https://avocado-framework.readthedocs.org/
Source0:        https://github.com/avocado-framework/avocado-vt/archive/%{version}.tar.gz#/avocado-vt-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       attr
Requires:       bridge-utils
# Requires:     autotest-framework
Requires:       gcc
Requires:       git-core
Requires:       glibc-devel
Requires:       iproute
Requires:       iputils
Requires:       make
Requires:       netcat-openbsd
Requires:       openvswitch
Requires:       python-aexpect > 1.5.0
Requires:       python-avocado >= 68.0
Requires:       python-netaddr >= 0.7.18
Requires:       python-netifaces >= 0.10.5
Requires:       python-simplejson >= 3.5.3
Requires:       python-six
Requires:       qemu-kvm
Requires:       systemtap
Requires:       tcpdump
Requires:       xz
Recommends:     libvirt
Recommends:     policycoreutils-python
BuildArch:      noarch
%ifpython2
Requires:       python-devel
%else
Requires:       python3-dbm
Requires:       python3-devel
%endif
%python_subpackages

%description
Avocado Virt Test is a plugin that executes virt-tests with all the avocado
features, such as HTML report and Xunit output, among others.

%prep
%setup -q -n avocado-vt-%{version}
sed -E -i "1{s|^#\!\s*/usr/bin/env python$|#\!%{_bindir}/python3|}" \
    scripts/*py \
    scripts/github/*py \
    virttest/remote_commander/*py \
    virttest/shared/deps/run_autotest/boottool.py
sed -E -i "1s/env //" virttest/shared/scripts/pmsocat/pmsocat36.py
sed -E -i "1s|^(#\!/usr/bin/python)$|\13|" \
    virttest/*py \
    virttest/shared/deps/serial/*py \
    virttest/shared/scripts/*py \
    virttest/staging/*py

%build
%python_build

%install
%python_install

# Reduce duplicities
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%fdupes %{buildroot}%{_datadir}/avocado-plugins-vt

%files %{python_files}
%license LICENSE
%doc README.rst
%dir %{python_sitelib}/avocado_vt
%dir %{python_sitelib}/avocado_vt/conf.d
%dir %{python_sitelib}/avocado_vt/plugins
%dir %{python_sitelib}/avocado_vt/__pycache__
%config(noreplace)%{python_sitelib}/avocado_vt/conf.d/vt.conf
%config(noreplace)%{python_sitelib}/avocado_vt/conf.d/vt_joblock.conf
%{python_sitelib}/avocado_framework_plugin_vt*egg-info
%{python_sitelib}/avocado_vt/*py
%{python_sitelib}/avocado_vt/__pycache__/*
%{python_sitelib}/avocado_vt/plugins/*
%{python_sitelib}/virttest*

%changelog
