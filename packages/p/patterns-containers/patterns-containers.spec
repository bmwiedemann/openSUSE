#
# spec file for package patterns-containers
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


Name:           patterns-containers
Version:        5.1
Release:        0
Summary:        Patterns for container technologies
License:        MIT
Group:          Metapackages
URL:            https://github.com/openSUSE/patterns
Source0:        %{name}-rpmlintrc
ExclusiveArch:  x86_64 %{arm} aarch64 ppc64le s390x riscv64

%description
This is an internal package that is used to create the patterns as part
of the installation source setup. Installation of this package does
not make sense.

%package container_runtime
Summary:        Container Runtime for non-clustered systems
Group:          Metapackages
Provides:       pattern() = container_runtime
Provides:       pattern-category() = Containers
Provides:       pattern-icon() = pattern-kubic
Provides:       pattern-order() = 9030
Provides:       pattern-visible()
Requires:       containers-systemd
Requires:       podman
Requires:       (distrobox if patterns-microos-desktop-common else toolbox)
Suggests:       toolbox
Requires:       pattern() = basesystem
#Obsolete CaaSP Patterns
Provides:       patterns-caasp-container-runtime
Obsoletes:      patterns-caasp-container-runtime <= 4.0

%description container_runtime
This pattern installs the default container runtime packages for non-clustered systems.

%prep
# empty on purpose

%build
# empty on purpose

%install
mkdir -p %{buildroot}%{_docdir}/patterns-containers/
echo 'This file marks the pattern container_runtime to be installed.' >%{buildroot}%{_docdir}/patterns-containers/container_runtime.txt

%files container_runtime
%dir %{_docdir}/patterns-containers
%{_docdir}/patterns-containers/container_runtime.txt

%changelog
