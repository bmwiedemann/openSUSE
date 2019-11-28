#
# spec file for package pam-test
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           pam-test
Version:        0.0+git.20161214
Release:        0
Summary:        Test of a PAM stack for authentication and password change
License:        GPL-2.0-only
URL:            https://github.com/pbrezina/pam-test
Buildrequires:  pam-devel
Source:         %{name}-%{version}.tar.xz

%description
This application can be used to test a PAM stack for authentication and
password change.

%prep
%setup -q

%build
cc %{optflags} -o pam_test src/main.c -lpam -lpam_misc

%install
install -Dpm 0755 pam_test \
  %{buildroot}%{_bindir}/pam_test

%files
%doc README.md
%{_bindir}/pam_test

%changelog
