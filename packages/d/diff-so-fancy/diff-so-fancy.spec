#
# spec file for package diff-so-fancy
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


%define bats_core_version    1.13.0
%define bats_support_version 0.3.0
%define bats_assert_version  2.2.0

Name:           diff-so-fancy
Version:        1.4.10
Release:        0
Summary:        Strives to make your diffs human readable
License:        MIT
BuildArch:      noarch
Group:          Productivity/Text/Utilities
URL:            https://github.com/so-fancy/diff-so-fancy
Source0:        https://github.com/so-fancy/diff-so-fancy/archive/v%{version}.tar.gz#/diff-so-fancy-%{version}.tar.gz
Source1:        https://github.com/bats-core/bats-core/archive/refs/tags/v%{bats_core_version}.tar.gz#/bats-core-%{bats_core_version}.tar.gz
Source2:        https://github.com/bats-core/bats-support/archive/refs/tags/v%{bats_support_version}.tar.gz#/bats-support-%{bats_support_version}.tar.gz
Source3:        https://github.com/bats-core/bats-assert/archive/refs/tags/v%{bats_assert_version}.tar.gz#/bats-assert-%{bats_assert_version}.tar.gz
BuildRequires:  git-core
Requires:       perl

%description
diff-so-fancy strives to make your diffs human readable instead of machine readable. This helps improve code quality and helps you spot defects faster.

%prep
%setup -q -a 1 -a 2 -a 3 -n %{name}-%{version}
rm -rf test/bats test/test_helper/bats-support test/test_helper/bats-assert
mv bats-core-%{bats_core_version} test/bats
mv bats-support-%{bats_support_version} test/test_helper/bats-support
mv bats-assert-%{bats_assert_version} test/test_helper/bats-assert

%build

%install
mkdir -p %{buildroot}%{_datadir}/diff-so-fancy
cp -a lib/* third_party %{buildroot}%{_datadir}/diff-so-fancy/
chmod -x %{buildroot}%{_datadir}/diff-so-fancy/third_party/*/*.pl
sed -i '#!\/usr\/bin/d' %{buildroot}%{_datadir}/diff-so-fancy/third_party/*/*.pl
sed -i '0 , /^$/ d' %{buildroot}%{_datadir}/diff-so-fancy/third_party/*/*.pl
sed -i 's@/usr/bin/env perl@/usr/bin/perl@' diff-so-fancy
sed -i 's|^use lib .*$|use lib "/usr/share/diff-so-fancy";|' diff-so-fancy
install -Dm 0755 -t %{buildroot}%{_bindir}/ diff-so-fancy

%check
export PERL5LIB="%{_builddir}/%{name}-%{version}/lib${PERL5LIB:+:${PERL5LIB}}"
./test/bats/bin/bats test

%files
%license LICENSE
%doc README.md
%{_bindir}/diff-so-fancy
%{_datadir}/diff-so-fancy

%changelog
