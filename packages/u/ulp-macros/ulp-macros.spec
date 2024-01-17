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
# FIXME: Select a correct license from https://github.com/openSUSE/spec-cleaner#spdx-licenses
License:        MIT
# FIXME: use correct group, see "https://en.opensuse.org/openSUSE:Package_group_guidelines"
Group:          Development
Source1:        ulp.macros
BuildArch:      noarch

%description
This package contain macros for enabling Userspace Live Patching into packages

%prep

%build

%install
install -D -m 0644 %{S:1}   %{buildroot}%{_rpmmacrodir}/macros.ulp

%files
%{_rpmmacrodir}/macros.ulp

%changelog

