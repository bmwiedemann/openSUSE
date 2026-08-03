#
# spec file for package himalaya
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


%global _lto_cflags %{_lto_cflags} -ffat-lto-objects
# https://docs.rs/crate/himalaya/2.0.0/features
%global himalaya_features maildir

Name:           himalaya
Version:        2.0.0
Release:        0
Summary:        Command-line interface for email management
#SourceLicense:  MIT
License:        AGPL-3.0-only AND AGPL-3.0-or-later AND GPL-2.0-or-later AND MIT AND bzip2-1.0.6 AND MPL-2.0 AND CC-BY-3.0 AND BSD-4-Clause AND OpenSSL AND OFL-1.1
URL:            https://github.com/pimalaya/himalaya
Source0:        %{name}-%{version}.tar.zst
Source1:        vendor.tar.zst
BuildRequires:  cargo-packaging
BuildRequires:  desktop-file-utils
BuildRequires:  hicolor-icon-theme
BuildRequires:  notmuch-devel
BuildRequires:  pkgconfig
BuildRequires:  rust+cargo >= 1.82
BuildRequires:  pkgconfig(gpgme)
BuildRequires:  pkgconfig(libssl)
ExclusiveArch:  %{rust_tier1_arches}

%description
Command-line interface for email management.

%prep
%autosetup -a1 -p1

desktop-file-edit --remove-category=Application --add-category=Email \
	--set-icon=%{name} --remove-key=DesktopName assets/%{name}.desktop

%build
%{cargo_build} --features "%{himalaya_features}"

%install
install -D -m 0755 -t %{buildroot}%{_bindir} target/release/%{name}
install -D -m 0644 -t %{buildroot}%{_datadir}/applications assets/%{name}.desktop
install -D -m 0644 logo.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg

install -d -m 0755 %{buildroot}%{_datadir}/bash-completion/completions \
	%{buildroot}%{_datadir}/fish/vendor_completions.d \
	%{buildroot}%{_datadir}/zsh/site-functions %{buildroot}%{_mandir}/man1
./target/release/%{name} completion bash > %{buildroot}%{_datadir}/bash-completion/completions/%{name}
./target/release/%{name} completion fish > %{buildroot}%{_datadir}/fish/vendor_completions.d/%{name}.fish
./target/release/%{name} completion zsh  > %{buildroot}%{_datadir}/zsh/site-functions/_%{name}
./target/release/%{name} man %{buildroot}%{_mandir}/man1

%check
# there are currently no tests available (v1.2.0)
#%%{cargo_test} --features "%%{himalaya_features}"
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%files
%license LICENSE-MIT LICENSE-APACHE
%doc CHANGELOG.md README.md config.sample.toml
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_mandir}/man1/%{name}*.1%{?ext_man}
%dir %{_datadir}/bash-completion
%dir %{_datadir}/bash-completion/completions
%{_datadir}/bash-completion/completions/%{name}
%dir %{_datadir}/fish
%dir %{_datadir}/fish/vendor_completions.d
%{_datadir}/fish/vendor_completions.d/%{name}.fish
%dir %{_datadir}/zsh
%dir %{_datadir}/zsh/site-functions
%{_datadir}/zsh/site-functions/_%{name}

%changelog
