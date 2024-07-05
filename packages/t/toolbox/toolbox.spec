#
# spec file for package toolbox
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


Name:           toolbox
Version:        2.3+git20240704.84ec25e
Release:        0
Summary:        Script to start a toolbox container for system debugging
License:        Apache-2.0
Group:          System/Management
URL:            https://github.com/openSUSE/microos-toolbox
Source:         microos-toolbox-%{version}.tar.xz
Requires:       (podman or docker)
Suggests:       podman
BuildArch:      noarch

%description
On systems using transactional-update it is not really possible due to
the read-only root filesystem to install tools to analyze problems in the
currently running system, a reboot is always required. Which makes it next
to impossible to debug such problems. toolbox is a small script that launches
a container to let you bring in your favorite debugging or admin tools in
such a system. The root filesystem can be found at /media/root.

%prep
%setup -q -n microos-toolbox-%{version}
%if 0%{?sle_version}
%if !0%{?is_opensuse}
sed -i -e 's,registry.opensuse.org,registry.suse.com,' toolbox
sed -i -e 's,opensuse/toolbox,suse/sle-micro/5.4/toolbox,' toolbox
%else
sed -i -e 's,opensuse/toolbox,opensuse/leap-micro/5.4/toolbox,' toolbox
%endif
%endif

%build

%install
mkdir -p %{buildroot}%{_bindir}
install -m 755 toolbox %{buildroot}%{_bindir}/toolbox

%files
%license LICENSE
%doc README.md
%{_bindir}/toolbox
%ghost %config %{_sysconfdir}/toolboxrc

%changelog
