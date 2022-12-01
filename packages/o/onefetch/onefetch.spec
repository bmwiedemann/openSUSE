#
# spec file for package onefetch
#
# Copyright (c) 2022 SUSE LLC
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


Name:           onefetch
Version:        2.14.2~0
Release:        0
Summary:        Git repository summary on your terminal
License:        GPL-2.0-only AND MIT
Group:          System/X11/Terminals
URL:            https://github.com/o2sh/onefetch
Source0:        %{name}-%{version}.tar.xz
Source1:        vendor.tar.xz
Source2:        cargo_config
BuildRequires:  cargo-packaging
BuildRequires:  cmake
BuildRequires:  rust

%description
Onefetch is a command line tool that displays information about your Git repository directly on your terminal.

%prep
%setup -q
%setup -q -D -T -a 1
mkdir -p .cargo
cp %{SOURCE2} .cargo/config

%build
# bypass error https://bugzilla.opensuse.org/show_bug.cgi?id=1175502
# to avoid cargo reported error if config.guess has been changed
# by build macro.
%ifarch ppc64le
guessname='src/libbacktrace/config.guess'
cfgguess="./vendor/backtrace-sys/$guessname"
chkjson='./vendor/backtrace-sys/.cargo-checksum.json'
if [[ -f $cfgguess ]] && [[ -f $chkjson ]]; then
  chksum=`sha256sum $cfgguess |sed -e 's/ .*//'`
  grep -q $guessname $chkjson && grep -q $chksum $chkjson || sed -i -e "s#\($guessname.:.\)[0-9a-f]*#\1$chksum#" $chkjson
fi
%endif
%{cargo_build}

%install
#install -Dm0755 target/release/onefetch %{buildroot}%{_bindir}/onefetch
%{cargo_install}

%files
%license LICENSE.md
%doc README.md
%{_bindir}/onefetch

%changelog
