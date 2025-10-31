#
# spec file for package qrtool
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


%ifarch s390x
%bcond_with test
%else
%bcond_without test
%endif
Name:           qrtool
Version:        0.13.1
Release:        0
Summary:        An utility for encoding or decoding QR code
License:        MIT AND CC-BY-4.0 AND Apache-2.0
Group:          Productivity/Graphics/Visualization/Other
URL:            https://github.com/sorairolake/qrtool
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        vendor.tar.zst
BuildRequires:  cargo-packaging
BuildRequires:  rubygem(asciidoctor)

%description
qrtool is a command-line utility for encoding or decoding QR code.

%prep
%autosetup -a1 -p1

%build
%{cargo_build}

asciidoctor -b manpage "docs/man/man1/%{name}.1.adoc"
asciidoctor -b manpage "docs/man/man1/%{name}-encode.1.adoc"
asciidoctor -b manpage "docs/man/man1/%{name}-decode.1.adoc"
asciidoctor -b manpage "docs/man/man1/%{name}-completion.1.adoc"

comp="target/release/%{name} completion"
$comp bash >"target/release/%{name}.bash"
$comp fish >"target/release/%{name}.fish"
$comp zsh >"target/release/_%{name}"

%install
install -Dm755 target/release/%{name} -t %{buildroot}%{_bindir}

install -Dm644 docs/man/man1/%{name}*.1 -t \
    %{buildroot}%{_mandir}/man1/

install -Dm644 target/release/%{name}.bash -t \
    %{buildroot}%{_datadir}/bash-completion/completions
install -Dm644 target/release/%{name}.fish -t \
    %{buildroot}%{_datadir}/fish/vendor_completions.d
install -Dm644 target/release/_%{name} -t \
    %{buildroot}%{_datadir}/zsh/site-functions

%if %{with test}
%check
%{cargo_test}
%endif

%files
%license LICENSE-*
%doc README* CHANGELOG.adoc
%{_bindir}/%{name}
%{_mandir}/man1/qrtool*
%{_datadir}/bash-completion/completions
%{_datadir}/fish
%{_datadir}/zsh

%changelog
