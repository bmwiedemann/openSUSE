#
# spec file for package patterns-containers
#
# Copyright (c) 2026 SUSE LLC and contributors
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
# SLFO package was named patterns-container
Obsoletes:      patterns-container < %{version}
Provides:       patterns-container = %{version}

%description
This is an internal package that is used to create the patterns as part
of the installation source setup. Installation of this package does
not make sense.

%package runtime_podman
Summary:        Podman Container Runtime for non-clustered systems
Group:          Metapackages
Provides:       pattern() = container_runtime
Provides:       pattern() = container_runtime_podman
Provides:       pattern-category() = Containers
Provides:       pattern-icon() = pattern-kubic
Provides:       pattern-order() = 9030
Provides:       pattern-visible()
Requires:       podman
Requires:       (distrobox if patterns-microos-desktop-common else toolbox)
Suggests:       toolbox
Requires:       pattern() = basesystem
Obsoletes:      patterns-containers-container_runtime < %{version}
Provides:       patterns-containers-container_runtime = %{version}
Obsoletes:      patterns-microos-container_runtime
Provides:       patterns-microos-container_runtime

# upgrade path from the old SLFO package (patterns-container (singular))
Obsoletes:      patterns-container-runtime_podman < %{version}
Provides:       patterns-container-runtime_podman = %{version}

%description runtime_podman
This pattern installs Podman as the container runtime for non-clustered systems.

%package runtime_docker
Summary:        Docker Container Runtime
Group:          Metapackages
Provides:       pattern() = container_runtime_docker
Provides:       pattern-category() = Containers
Provides:       pattern-icon() = pattern-kubic
Provides:       pattern-order() = 9040
Provides:       pattern-visible()
Requires:       docker
Requires:       pattern() = basesystem
Obsoletes:      patterns-container-runtime_docker < %{version}
Provides:       patterns-container-runtime_docker = %{version}

%description runtime_docker
This pattern installs Docker as the container runtime.

%prep
# empty on purpose

%build
# empty on purpose

%install
mkdir -p %{buildroot}%{_docdir}/patterns-containers/
for pattern in runtime_podman runtime_docker; do
    echo "This file marks the pattern $pattern to be installed." \
        >%{buildroot}%{_docdir}/patterns-containers/${pattern}.txt
done

%files runtime_podman
%dir %{_docdir}/patterns-containers
%{_docdir}/patterns-containers/runtime_podman.txt

%files runtime_docker
%dir %{_docdir}/patterns-containers
%{_docdir}/patterns-containers/runtime_docker.txt

%changelog
