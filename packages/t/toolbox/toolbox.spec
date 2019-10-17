#
# spec file for package toolbox
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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
Version:        1.0+git20191014.3034fbc
Release:        0
Summary:        Script to start a toolbox container for system debugging
License:        Apache-2.0
URL:            https://github.com/thkukuk/microos-toolbox
Source:         microos-toolbox-%{version}.tar.xz
Requires:       podman
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

%build

%install
mkdir -p %{buildroot}%{_bindir}
install -m 755 toolbox %{buildroot}%{_bindir}/toolbox

%files
%license LICENSE
%doc README.md
%{_bindir}/toolbox

%changelog
