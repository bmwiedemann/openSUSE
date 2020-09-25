#
# spec file for package git-delta
#
# Copyright (c) 2020 SUSE LLC
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


Name:           git-delta
Version:        0.4.3
Release:        0
Summary:        A syntax-highlighter for git and diff output
License:        MIT
URL:            https://github.com/dandavison/delta
Source0:        https://github.com/dandavison/delta/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        vendor.tar.xz
BuildRequires:  clang-devel
BuildRequires:  rust-packaging

%description
Delta provides language syntax-highlighting, within-line insertion/deletion detection, and restructured diff output for git on the command line.

%prep
%setup -qa 1 -n delta-%{version}
%define cargo_registry $(pwd)/vendor
%{cargo_prep}

# For ppc64, aarch64 and riscv64, there is a hook running, that touches this file, which is checksummed
%ifarch aarch64 ppc64 ppc64le riscv64
cp $(pwd)/vendor/backtrace-sys/src/libbacktrace/config.sub $(pwd)/vendor/backtrace-sys/src/libbacktrace/config.sub.save
cp $(pwd)/vendor/backtrace-sys/src/libbacktrace/config.guess $(pwd)/vendor/backtrace-sys/src/libbacktrace/config.guess.save
%endif

%build
%ifarch aarch64 ppc64 ppc64le riscv64
mv $(pwd)/vendor/backtrace-sys/src/libbacktrace/config.sub.save $(pwd)/vendor/backtrace-sys/src/libbacktrace/config.sub
mv $(pwd)/vendor/backtrace-sys/src/libbacktrace/config.guess.save $(pwd)/vendor/backtrace-sys/src/libbacktrace/config.guess
%endif
%cargo_build

%check
%cargo_test

%install
%cargo_install
# There is already a package "delta" so we have to rename it
mv %{buildroot}%{_bindir}/delta %{buildroot}%{_bindir}/%{name}

# install bash completion
install -D -m 0644 %{_builddir}/delta-%{version}/etc/completion/completion.bash %{buildroot}%{_datadir}/bash-completion/completions/%{name}

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_datadir}/bash-completion/completions/%{name}

%changelog
