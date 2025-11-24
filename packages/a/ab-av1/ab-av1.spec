#
# spec file for package ab-av1
#
# Copyright (c) 2025 SUSE LLC
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


Name:           ab-av1
Version:        0.10.2
Release:        0
Summary:        An AV1 video encoding wrapper
License:        MIT
URL:            https://github.com/alexheretic/ab-av1
Source0:        %{name}-%{version}.tar
Source1:        vendor.tar.zst
BuildRequires:  cargo-packaging
BuildRequires:  rust+cargo >= 1.86
Requires:       ffmpeg >= 5
ExclusiveArch:  %{rust_tier1_arches}

%description
AV1 video encoding tool with VMAF sampling & automatic encoder CRF
calculation. It uses ffmpeg and SVT-AV1.

%prep
%autosetup -p1 -a1

%build
%{cargo_build}

%install
%{cargo_install}
mkdir -p shell-completion
%{buildroot}/%{_bindir}/%{name} print-completions bash > shell-completion/bash
%{buildroot}/%{_bindir}/%{name} print-completions fish > shell-completion/fish
%{buildroot}/%{_bindir}/%{name} print-completions zsh > shell-completion/zsh
install -D -m 0644 shell-completion/bash %{buildroot}%{_datadir}/bash-completion/completions/%{name}
install -D -m 0644 shell-completion/fish %{buildroot}%{_datadir}/fish/vendor_completions.d/%{name}.fish
install -D -m 0644 shell-completion/zsh %{buildroot}%{_datadir}/zsh/site-functions/_%{name}

%check
%{cargo_test}

%files
%license LICENSE
%doc README.md CHANGELOG.md
%{_bindir}/%{name}
%dir %{_datadir}/fish
%dir %{_datadir}/fish/vendor_completions.d
%dir %{_datadir}/zsh
%dir %{_datadir}/zsh/site-functions
%{_datadir}/bash-completion/completions/%{name}
%{_datadir}/fish/vendor_completions.d/%{name}.fish
%{_datadir}/zsh/site-functions/_%{name}

%changelog
