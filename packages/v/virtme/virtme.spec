#
# spec file
#
# Copyright (c) 2023 SUSE LLC
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


%define name virtme
%define version 0.1.2
%define skip_python2 1

Name:           %{name}
Version:        %{version}
Release:        0
Summary:        Tools for virtualize the running distro or a rootfs
License:        GPL-2.0-only
Group:          Development/Tools/Other
URL:            https://github.com/arighi/virtme
Source0:        https://github.com/arighi/virtme/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  python-rpm-macros
Requires:       busybox-static
Requires:       qemu
BuildArch:      noarch

%description
Virtme is a set of tools to run a virtualized Linux kernel that
uses the host Linux distribution or a rootfs instead of a whole
disk image.

Right now it is not really configurable enough for being useful as a
sort of sandbox.

%prep
%autosetup -n %{name}-%{version} -p1

%build
%py3_build
# remove pycache directories
find . -name __pycache__ -type d -exec rm -fr {} +

%install
export PYTHONDONTWRITEBYTECODE=1 %py3_install

%files
%{_bindir}/virtme-configkernel
%{_bindir}/virtme-mkinitramfs
%{_bindir}/virtme-prep-kdir-mods
%{_bindir}/virtme-run
%{python_sitelib}/%{name}
%{python_sitelib}/%{name}-%{version}-py*.egg-info

%changelog
