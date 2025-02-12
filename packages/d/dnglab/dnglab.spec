#
# spec file for package dnglab
#
# Copyright (c) 2025 SUSE LLC
# Copyright (c) 2025 Atri Bhattacharya <badshah400@opensuse.org>
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

Name:           dnglab
Version:        0.6.3
Release:        0
Summary:        Camera RAW to DNG file format converter
License:        LGPL-2.1-only
URL:            https://github.com/dnglab/dnglab
Source0:        %{name}-%{version}.tar.zst
Source1:        vendor.tar.zst
# PATCH-FEATURE-OPENSUSE dnglab-renamed-exec-usage-msg.patch badshah400@gmail.com -- Adapt usage message to renamed binary
Patch0:         dnglab-renamed-exec-usage-msg.patch
BuildRequires:  cargo
BuildRequires:  cargo-packaging
BuildRequires:  rust >= 1.79

%description
%{name} provides a command line tool to convert camera RAW files to Digital
Negative Format (DNG).

%package bash-completion
Summary:        This package provides tab completion for dnglab on the bash shell
Requires:       %{name} = %{version}
Requires:       bash-completion
Supplements:    (%{name} and bash-completion)
BuildArch:      noarch

%description bash-completion
%{name} provides a command line tool to convert camera RAW files to Digital
Negative Format (DNG).

This package provides tab completion for %{name} on the bash shell.

%package fish-completion
Summary:        This package provides tab completion for dnglab on the fish shell
Requires:       %{name} = %{version}
Requires:       fish
Supplements:    (%{name} and fish)
BuildArch:      noarch

%description fish-completion
%{name} provides a command line tool to convert camera RAW files to Digital
Negative Format (DNG).

This package provides tab completion for %{name} on the fish shell.

%prep
%autosetup -p1 -a1

%build
%{cargo_build} --all

%install
%{cargo_install -p bin/dnglab}
%{cargo_install -p rawler}

# Shell completions
## Bash
mkdir -p %{buildroot}%{_datadir}/bash-completion/completions
cp ./bin/dnglab/completions/{_dnglab,dnglab.bash} %{buildroot}%{_datadir}/bash-completion/completions/
## Fish
mkdir -p %{buildroot}%{_datadir}/fish/vendor_completions.d
cp ./bin/dnglab/completions/dnglab.fish %{buildroot}%{_datadir}/fish/vendor_completions.d/

# Man files
mkdir -p %{buildroot}%{_mandir}/man1
cp ./bin/dnglab/manpages/*.1 %{buildroot}%{_mandir}/man1/

# Rename generic binary names to avoid current and future file-naming conflicts
mv %{buildroot}%{_bindir}/benchmark %{buildroot}%{_bindir}/%{name}-benchmark
mv %{buildroot}%{_bindir}/identify %{buildroot}%{_bindir}/%{name}-identify

%check
%{cargo_test}

%files
%license LICENSE
%{_bindir}/%{name}
%{_bindir}/%{name}-benchmark
%{_bindir}/%{name}-identify
%{_mandir}/man1/*.1%{?ext_man}

%files bash-completion
%{_datadir}/bash-completion/completions/*

%files fish-completion
%{_datadir}/fish/

%changelog
