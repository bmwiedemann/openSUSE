#
# spec file for package diff-so-fancy
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


Name:           diff-so-fancy
Version:        1.4.3
Release:        0
Summary:        Strives to make your diffs human readable
License:        MIT
BuildArch:      noarch
Group:          Productivity/Text/Utilities
URL:            https://github.com/so-fancy/diff-so-fancy
Source0:        https://github.com/so-fancy/diff-so-fancy/archive/v%{version}.tar.gz
Requires:       perl

%description
diff-so-fancy strives to make your diffs human readable instead of machine readable. This helps improve code quality and helps you spot defects faster.

%prep
%setup -q -n %{name}-%{version}

%build

%install
mkdir -p %{buildroot}%{_datadir}/diff-so-fancy
mv lib/* third_party %{buildroot}%{_datadir}/diff-so-fancy/
chmod -x %{buildroot}%{_datadir}/diff-so-fancy/third_party/*/*.pl
sed -i '#!\/usr\/bin/d' %{buildroot}%{_datadir}/diff-so-fancy/third_party/*/*.pl
sed -i '0 , /^$/ d' %{buildroot}%{_datadir}/diff-so-fancy/third_party/*/*.pl
sed -i 's@/usr/bin/env perl@/usr/bin/perl@' {diff-so-fancy,%{buildroot}%{_datadir}/diff-so-fancy/third_party/build_fatpack/diff-so-fancy}
sed -i 's|^use lib .*$|use lib "/usr/share/diff-so-fancy";|' diff-so-fancy
install -Dm 0755 -t %{buildroot}%{_bindir}/ diff-so-fancy

%files
%license LICENSE
%doc README.md history.md
%{_bindir}/diff-so-fancy
%{_datadir}/*

%changelog
