#
# spec file for package ulp-macros
#
# Copyright (c) 2023 SUSE LLC
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


Name:           ulp-macros
Version:        1.0
Release:        0
Summary:        Macros for enabling Userspace Live Patching into processes
URL:            https://github.com/SUSE/libpulp
License:        LGPL-2.1-or-later
Group:          Development
Source1:        ulp.macros
Source2:        LICENSE
BuildArch:      noarch

%description
This package contain macros for enabling Userspace Live Patching into packages

%prep

%build

%install
install -D -m 0644 %{S:1}   %{buildroot}%{_rpmmacrodir}/macros.ulp
install -D -m 0644 %{S:2}   %{buildroot}/usr/share/licenses/ulp-macros/LICENSE

%files
%{_rpmmacrodir}/macros.ulp
%license LICENSE

%check

%changelog
