#
# spec file for package perl-rpm-packaging
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


Name:           perl-rpm-packaging
Version:        1.1
Release:        0
Summary:        RPM dependency generator for Perl
Group:          Development/Languages/Python
License:        GPL-2.0-or-later
URL:            https://github.com/rpm-software-management/perl-rpm-packaging
Source0:        https://github.com/rpm-software-management/perl-rpm-packaging/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch1:         fileattrs.diff
BuildArch:      noarch
Requires:       perl
Provides:       rpm-build-perl = 4.19.1.1
Obsoletes:      rpm-build-perl < 4.19.1.1

%description
Tools for packaging Perl projects with rpm

%prep
%autosetup -p0

%build
true

%install
mkdir -p %{buildroot}%{_fileattrsdir}
install -Dm0644 fileattrs/* %{buildroot}%{_fileattrsdir}
install -Dm0755 scripts/* %{buildroot}%{_rpmconfigdir}

%files
%doc README.md
%{_fileattrsdir}/perl.attr
%{_fileattrsdir}/perllib.attr
%{_rpmconfigdir}/perl.prov
%{_rpmconfigdir}/perl.req

%changelog
