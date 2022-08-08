#
# spec file for package python-rpm-packaging
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


Name:           python-rpm-packaging
Version:        20210526+a18ca48
Release:        0
Summary:        RPM dependency generator for Python
Group:          Development/Languages/Python
License:        GPL-2.0-or-later
URL:            https://github.com/rpm-software-management/python-rpm-packaging
Source0:        %{name}-%{version}.tar.xz
Patch0:         python3.patch
Patch1:         disable-distrequires.patch
BuildArch:      noarch
Provides:       rpm-build-python = 4.17.1
Obsoletes:      rpm-build-python < 4.17.1
Requires:       python3-base
# boo#1178257
Requires:       python3-packaging
# To avoid widespread breakage by package mistakenly ignoring
# their requirement of python-rpm-macros (bsc#1180125)
Requires:       python-rpm-macros

%description
Tools for packaging Python projects with rpm

%prep
%autosetup -p1

%build
true

%install
mkdir -p %{buildroot}%{_fileattrsdir}
install -Dm0644 fileattrs/* %{buildroot}%{_fileattrsdir}
install -Dm0755 scripts/* %{buildroot}%{_rpmconfigdir}

%files
%license COPYING
%doc README
%{_fileattrsdir}/python.attr
%{_fileattrsdir}/pythondist.attr
%{_rpmconfigdir}/brp-python-bytecompile
%{_rpmconfigdir}/brp-python-hardlink
%{_rpmconfigdir}/pythondistdeps.py


%changelog
