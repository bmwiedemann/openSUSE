#
# spec file for package rmpc
#
# Copyright (c) 2025 mantarimay
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


%bcond_without test
Name:           rmpc
Version:        0.8.0
Release:        0
Summary:        Rusty Music Player Client for MPD
License:        BSD-3-Clause
URL:            https://github.com/mierak/rmpc
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        vendor.tar.zst
BuildRequires:  cargo-packaging
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  rust >= 1.74
Recommends:     mpd
Recommends:     yt-dlp

%description
RMPC is a beautiful, modern and configurable terminal based Music Player
Daemon client with album art support. It is heavily inspired by ncmpcpp
and ranger/lf file managers.

%prep
%autosetup -a1 -p1

%build
%{cargo_build}

%install
install -Dm755 target/release/%{name} -t %{buildroot}%{_bindir}
install -Dm644 target/man/%{name}.1 -t %{buildroot}%{_mandir}/man1
install -Dm644 target/completions/%{name}.bash -t \
    %{buildroot}%{_datadir}/bash-completion/completions
install -Dm644 target/completions/%{name}.fish -t \
    %{buildroot}%{_datadir}/fish/vendor_completions.d
install -Dm644 target/completions/_%{name} -t \
    %{buildroot}%{_datadir}/zsh/site-functions

%if %{with test}
%check
%{cargo_test} -- \
    --skip=config::utils::tests::home_dir_not_present::_yes_yes_expects
%endif

%files
%license LICEN*
%doc README* CHANGELOG.md
%{_bindir}/%{name}
%{_mandir}/man*/%{name}.*
%{_datadir}/bash-completion/completions
%{_datadir}/fish
%{_datadir}/zsh

%changelog
