#
# spec file for package qrtool
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


Name:           qrtool
Version:        0.10.6
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

%install
install -Dm755 target/release/%{name} -t %{buildroot}%{_bindir}
install -Dm644 target/release/build/qrtool*/out/*.? -t %{buildroot}%{_mandir}/man1

%check

%files
%license LICENSE*
%doc README* CHANGELOG.adoc
%{_bindir}/%{name}
%{_mandir}/man1/qrtool*

%changelog
