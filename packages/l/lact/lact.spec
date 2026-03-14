#
# spec file for package lact
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


%define flavor @BUILD_FLAVOR@%{nil}
%global sname lact

# Define package name based on build flavor
%if "%{?flavor}" == "headless"
%global pname %{sname}-headless
%bcond_without headless
%else
%global pname %{sname}
%bcond_with headless
%endif

Name:           %{pname}
Version:        0.8.4
Release:        0
Summary:        Linux GPU Configuration And Monitoring Tool
License:        MIT
URL:            https://github.com/ilya-zlobintsev/LACT
Group:          Hardware/Other

# Get the source from tar_scm
Source0:        %{sname}-%{version}.tar.xz
# Additional sources for rust vendor and sysusers configuration
Source1:        vendor.tar.xz
# Sysusers configuration for creating the "lact" system user and group to manage the daemon's permissions
Source2:        system-user-%{sname}.conf
# Handle exclusions
Source3:        %{sname}.rpmlintrc
# LACT configuration file
# The LACT config file is located in /etc/lact/config.yaml,
# and contains all of the GPU settings that are typically edited in the GUI,
# as well as a few settings specifying the behaviour of the daemon.
# LACT listens for config file changes and reloads all GPU settings automatically,
# but daemon-related settings such as the logging level or permissions require a service restart (systemctl restart lactd).
# This configuration file provides a specific setting for the admin user and group that the daemon will use for permissions management.
# Instead of using "wheel" or "sudo", it creates a dedicated "lact" system user and group for this purpose, and specify them in the config file.
Source4:        %{sname}.config.yaml
# Post-installation/unistallation guide for users
Source5:        install-guide.txt
Source6:        uninstall-guide.txt

# Rust is only available on these architectures
ExclusiveArch:  x86_64 aarch64

# LACT BuildDeps for both build flavors
BuildRequires:  (rust1.92 or rust >= 1.92)
BuildRequires:  (cargo1.92 or cargo >= 1.92)
BuildRequires:  cargo-packaging
BuildRequires:  clang-devel
BuildRequires:  pkgconfig(hwdata)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(vulkan)
BuildRequires:  pkgconfig(OpenCL)
BuildRequires:  systemd-rpm-macros
BuildRequires:  desktop-file-utils
BuildRequires:  hicolor-icon-theme
BuildRequires:  appstream-glib
BuildRequires:  sysuser-tools
%{?sysusers_requires}

# GUI-specific for full build flavor
%if %{without headless}
BuildRequires:  pkgconfig(gtk4) >= 4.6
BuildRequires:  pkgconfig(libadwaita-1) >= 1.2
%endif

# Runtime dependencies
Requires:       hwdata
%{?systemd_ordering}

# GUI-specific for full build runtime dependencies
%if %{without headless}
Requires:       gtk4 >= 4.6
Requires:       libadwaita >= 1.2
%endif

# Mutual exclusion between build flavors
%if %{with headless}
Provides:       lact-daemon = %{version}-%{release}
Conflicts:      lact
%else
Provides:       lact-daemon = %{version}-%{release}
Conflicts:      lact-headless
%endif

%description
%if %{with headless}
LACT (Linux GPU Configuration And Monitoring Tool) is a daemon and CLI
utility for GPU configuration and monitoring. This headless variant includes
only the daemon and CLI, suitable for servers and minimal installations
without graphical dependencies.
%else
LACT (Linux GPU Configuration And Monitoring Tool) provides comprehensive
GPU control with a graphical interface. Features include power management,
fan curve configuration, overclocking, and detailed monitoring with
historical graphs.
%endif

Post-installation/uninstallation steps can be found in:
/usr/share/doc/packages/lact

DISCLAIMER, none of the SUSE maintainers are responsible if you mess up
your GPU by using this tool, especially the overclocking features.
Please be careful and understand the risks before using it.

%prep
# Unpack the source and apply any necessary patches or modifications
%autosetup -p1 -n %{sname}-%{version} -a1

# Version 0.8.4 has a bug in lact-daemon/Cargo.toml missing the "socket" feature
%if "%{version}" == "0.8.4"
sed -i 's/features = \["user", "fs", "ioctl"\]/features = ["user", "fs", "ioctl", "socket"]/' lact-daemon/Cargo.toml
cargo update --offline -p lact-daemon --precise 0.8.4
%endif

# Configure cargo to use vendored dependencies
mkdir -p .cargo
cat > .cargo/config.toml <<EOF
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"
EOF

%build
# Copy the post-installation/uninstallation guides
cp %_sourcedir/*install-guide.txt .

%if %{with headless}
# Build headless flavor (daemon + CLI only)
%{cargo_build} -p lact --no-default-features --features nvidia
%else
# Build full flavor (daemon + CLI + GUI)
%{cargo_build} -p lact --features adw
%endif

# Generate system user pre-install scriptlet
%sysusers_generate_pre %{SOURCE2} %{sname} %{sname}-user.conf

%install
# Install the built binaries and resources to the appropriate locations in the buildroot
%make_install PREFIX="%{_prefix}"

# Install sysusers configuration
install -Dpm 0644 %{SOURCE2} %{buildroot}%{_sysusersdir}/%{sname}-user.conf
install -d -m 0750 %{buildroot}%{_sharedstatedir}/lact

# Configuration for lact
mkdir -p %{buildroot}%{_sysconfdir}/lact
install -Dpm 0644 %{SOURCE4} %{buildroot}%{_sysconfdir}/lact/config.yaml

%pre -f %{sname}.pre
# System user is created by the pre-scriptlet of sysusers_generate_pre, handle pre-installation tasks for the systemd service
%service_add_pre lactd.service

%post
# Handle post-installation tasks for the systemd service
%service_add_post lactd.service

%preun
# Stop and disable systemd service before uninstall
%service_del_preun lactd.service

%postun
# Clean up after service removal
%service_del_postun lactd.service

%check
# Validate desktop files and appstream metadata
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/*.xml

%files
# License and documentation
%license LICENSE
%doc README.md install-guide.txt uninstall-guide.txt

# Core binaries
%{_bindir}/lact

# Systemd integration
%{_unitdir}/lactd.service

# System user configuration
%{_sysusersdir}/%{sname}-user.conf
%dir %attr(0750,lact,lact) %{_sharedstatedir}/lact

# Desktop files and appstream metadata
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/apps/io.github.ilya_zlobintsev.LACT.*
%{_datadir}/metainfo/*.xml

# LACT Configuration file
%dir %attr(0755,root,lact) %{_sysconfdir}/lact
%config(noreplace) %attr(0644,root,lact) %{_sysconfdir}/lact/config.yaml

%changelog
