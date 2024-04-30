#
# spec file for package artem
#
# Copyright (c) 2024 mantarimay
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


Name:           artem
Version:        3.0.0
Release:        0
Summary:        A CLI program to convert images to ASCII art
License:        MPL-2.0
URL:            https://github.com/FineFindus/artem
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        vendor.tar.zst
BuildRequires:  cargo-packaging

%description
Artem is a small cli program, written in rust, to easily convert images to
ascii art, named after the latin word for art. By default it tries to use
truecolor, if the terminal does not support truecolor, it falls back to 16
Color ANSI. When the ascii image is written to a file, the image will not
use colors. It supports .jpeg, .png, .gif, .webp and many more.

%prep
%autosetup -a1 -p1

%build
%{cargo_build}

%install
install -Dm755 target/release/%{name} -t \
    %{buildroot}%{_bindir}
install -Dm644 target/release/build/%{name}-*/out/%{name}.1 -t \
    %{buildroot}%{_mandir}/man1
install -Dm644 target/release/build/%{name}-*/out/%{name}.bash -t \
    %{buildroot}%{_datadir}/bash-completion/completions
install -Dm644 target/release/build/%{name}-*/out/%{name}.fish -t \
    %{buildroot}%{_datadir}/fish/vendor_completions.d
install -Dm644 target/release/build/%{name}-*/out/_%{name} -t \
    %{buildroot}%{_datadir}/zsh/site-functions

%check

%files
%license LICEN*
%doc README* CHANGELOG.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.*
%{_datadir}/bash-completion/completions
%{_datadir}/fish
%{_datadir}/zsh

%changelog

