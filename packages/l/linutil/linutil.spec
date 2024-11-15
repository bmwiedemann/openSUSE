#
# spec file for package linutil
#
# Copyright (c) 2024 SUSE LLC
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


%global crate linutil
%global _description %{expand:
Chris Titus Tech's Linux Toolbox - Linutil is a distro-agnostic toolbox
designed to simplify everyday Linux tasks.}
%bcond_without check
Name:           linutil
Version:        2024.10.31~0
Release:        0
Summary:        Linutil is a toolbox designed to simplify everyday Linux tasks
URL:            https://github.com/ChrisTitusTech/linutil
Source:         %{name}-%{version}.tar.zst
Source1:        vendor.tar.zst
BuildRequires:  cargo >= 1.80
BuildRequires:  cargo-packaging
BuildRequires:  desktop-file-utils
License:        MIT

%description %{_description}

%files
%license LICENSE
%doc README.md
%doc man/*
%doc  docs/*
%doc  ./tui/cool_tips.txt
%{_datadir}/icons/linutil.png
%{_bindir}/linutil
%{_datadir}/applications/*.desktop

%prep
%autosetup -p1 -a1
#remove [patch.crates-io]
sed -i '14d' Cargo.toml
sed -i '15d' Cargo.toml

%build
%{cargo_build} --all

%install
%{cargo_install -p tui}
mkdir %{buildroot}%{_datadir}/icons/ -p
cp ./docs/assets/favicon.png %{buildroot}%{_datadir}/icons/linutil.png
desktop-file-install --dir=%{buildroot}%{_datadir}/applications  \
                                    --set-key=Exec  --set-value=%{_bindir}/linutil   \
                                    --set-key=Icon  --set-value=%{_datadir}/icons/linutil.png    \
                                    ./linutil.desktop
%if %{with check}
%check
%{cargo_test}
%endif

%changelog
