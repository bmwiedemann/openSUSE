#
# spec file for package zenith
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


Name:           zenith
Version:        0.14.3
Release:        0
Summary:        Sort of like top or htop but with zoom-able charts
License:        MIT
URL:            https://github.com/bvaisvil/zenith
Source0:        %{name}-%{version}.tar.zst
Source1:        vendor.tar.zst
Patch0:         001-strip-cargo-config.patch
BuildRequires:  cargo-packaging
BuildRequires:  clang-devel
# Disable this line if you wish to support all platforms.
# In most situations, you will likely only target tier1 arches for user facing components.
ExclusiveArch:  %{rust_tier1_arches}

%description
Sort of like top or htop but with zoom-able charts, CPU, GPU, network, and disk usage

%prep
# The number passed to -a (a stands for "after") should be equivalent to the Source tag number
# of the vendor tarball, 1 in this case (from Source1).
%autosetup -p1 -a1
# Remove exec bits to prevent an issue in fedora shebang checking. Uncomment only if required.
# find vendor -type f -name \*.rs -exec chmod -x '{}' \;

%build
%{cargo_build}

%check
%{cargo_test}

%install
install -D -d -m 0755 %{buildroot}%{_bindir}
install -m 0755 %{_builddir}/%{name}-%{version}/target/release/%{name} %{buildroot}%{_bindir}/%{name}

%files
%license LICENSE
%{_bindir}/%{name}

%changelog
