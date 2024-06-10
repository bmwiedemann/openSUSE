#
# spec file for package virtme
#
# Copyright (c) 2024 SUSE LLC
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


%if 0%{?suse_version} >= 1600
%global pythons python3
%else
%global pythons python311
%endif
Name:           virtme
Version:        1.25
Release:        0
Summary:        Tools for virtualize the running distro or a rootfs
License:        GPL-2.0-only
Group:          Development/Tools/Other
URL:            https://github.com/arighi/virtme-ng
Source0:        %{name}-ng-%{version}.tar.xz
Patch0:         0001-virtme-ng-fix-virtiofsd-search-path-on-openSUSE.patch
BuildRequires:  %{pythons}-argcomplete
BuildRequires:  %{pythons}-requests
BuildRequires:  %{pythons}-setuptools
BuildRequires:  python-rpm-macros
Requires:       %{pythons}-argcomplete
Requires:       %{pythons}-requests
Requires:       %{pythons}-setuptools
Requires:       busybox-static
Requires:       qemu
%if 0%{?suse_version} == 1500 && 0%{?sle_version} <= 150500
Requires:       qemu-tools
%else
Requires:       virtiofsd
%endif
BuildArch:      noarch

%description
Virtme is a set of tools to run a virtualized Linux kernel that
uses the host Linux distribution or a rootfs instead of a whole
disk image.

%prep
%autosetup -n %{name}-ng-%{version} -p1

%build
%python_build
# remove pycache directories
find . -name __pycache__ -type d -exec rm -fr {} +

%install
export PYTHONDONTWRITEBYTECODE=1 %python_install

%files
%{_bindir}/virtme-configkernel
%{_bindir}/virtme-ng
%{_bindir}/virtme-mkinitramfs
%{_bindir}/virtme-prep-kdir-mods
%{_bindir}/virtme-run
%{_bindir}/vng
%{python_sitelib}/%{name}
%{python_sitelib}/%{name}_ng
%{python_sitelib}/%{name}_ng-%{version}-py*.egg-info
%{_datadir}/bash-completion
%config(noreplace) %{_sysconfdir}/%{name}-ng.conf

%changelog
