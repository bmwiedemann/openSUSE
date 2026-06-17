#
# spec file for package libdnf-plugin-txnupd
#
# Copyright (c) 2026 Neal Gompa.
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


# Minimum compatible version
%define libdnf5_minver 5.4.0.0
%define tukit_minver 3.6.2


Name:           libdnf-plugin-txnupd
Version:        0.3.0
Release:        0
Summary:        Plugin for libdnf5 to implement transactional updates
License:        LGPL-2.1-or-later
URL:            https://gitlab.com/VelocityLimitless/Projects/libdnf-plugin-txnupd
Source0:        %{url}/-/archive/%{version}/%{name}-%{version}.tar.gz

# Backports from upstream
Patch0001:      %{url}/-/commit/3add4c39b5506f8bfafd1daca3bf6165e55c5e18.patch

BuildRequires:  cmake
BuildRequires:  make
BuildRequires:  gcc-c++ >= 13
BuildRequires:  scdoc

BuildRequires:  dnf5-devel >= %{libdnf5_minver}
BuildRequires:  pkgconfig(libdnf5) >= %{libdnf5_minver}
BuildRequires:  pkgconfig(libdnf5-cli) >= %{libdnf5_minver}
BuildRequires:  pkgconfig(tukit) >= %{tukit_minver}

# To keep OBS and rpmlint from complaining about directory ownership
BuildRequires:  dnf-data

%description
This package contains the plugin to implement transactional updates
as a libdnf plugin. This plugin hooks into libdnf5 for DNF and
PackageKit to enable this functionality in normal use.


%package -n dnf5-plugin-txnupd
Summary:        Plugin for dnf5 to implement transactional updates

# Indicate providing dnf5 command
Provides:       dnf5-command(txnupd)

# Require correct minimum version of the CLI
%requires_ge %(rpm --qf "%%{name}" -qf "$(readlink -f %{_bindir}/dnf5)")

# Require the core plugin
Requires:       libdnf5-plugin-txnupd%{?_isa} = %{version}-%{release}

%description -n dnf5-plugin-txnupd
This package contains the plugin to implement transactional updates
as a dnf5 plugin. This plugin hooks into dnf5 to expose actions in the CLI.


%package -n libdnf5-plugin-txnupd
Summary:        Plugin for libdnf5 to implement transactional updates

# Replace the old plugin
Obsoletes:      %{name} < %{version}-%{release}
Provides:       %{name} = %{version}-%{release}
Provides:       %{name}%{?_isa} = %{version}-%{release}

# Do not permit normal DNF snapper plugin on the same system
Conflicts:      dnf5-actions-snapper

# We need the transactional update dracut module
Requires:       dracut-transactional-update

# Either DNF5 or PackageKit can be used as frontends
Requires:       (dnf5 or PackageKit)
# This is intended to be used with PackageKit using DNF
Requires:       (PackageKit-backend-dnf5 if PackageKit)
# To ensure directories for configuration files are in place
Requires:       dnf-data

# Stricter dependency to keep things sane
%requires_ge %(rpm --qf "%%{name}" -qf "$(readlink -f %{_libdir}/libdnf5.so)")
%requires_ge %(rpm --qf "%%{name}" -qf "$(readlink -f %{_libdir}/libtukit.so)")

%description -n libdnf5-plugin-txnupd
This package contains the plugin to implement transactional updates
as a libdnf plugin. This plugin hooks into libdnf5 for DNF and
PackageKit to enable this functionality in normal use.


%prep
%autosetup -p1


%conf
%cmake


%build
%make_build -C build


%install
%make_install -C build

# Add configuration to mark this package as protected by libdnf
mkdir -p %{buildroot}%{_sysconfdir}/dnf/protected.d
echo "libdnf5-plugin-txnupd" > %{buildroot}%{_sysconfdir}/dnf/protected.d/txnupd.conf


%files -n dnf5-plugin-txnupd
%license LICENSE
%doc README.md
%{_libdir}/dnf5/plugins/txnupd.so
%{_mandir}/man8/dnf5-txnupd.8*


%files -n libdnf5-plugin-txnupd
%license LICENSE
%doc README.md
%{_libdir}/libdnf5/plugins/txnupd.so
%{_sysconfdir}/dnf/protected.d/txnupd.conf
%dir %{_datadir}/dnf5
%{_datadir}/dnf5/libdnf.plugins.conf.d/txnupd.conf
%{_mandir}/man5/dnf5-txnupd.conf.5*


%changelog
