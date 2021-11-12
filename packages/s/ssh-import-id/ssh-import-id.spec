# spec file for package ssh-import-id
#
# Copyright (c) 2021 SUSE LLC
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

Name:           ssh-import-id
Version:        5.11
Release:        0
Summary:        Authorize SSH public keys from online identities
License:        GPL-3.0
URL:            https://launchpad.net/ssh-import-id
Source0:        https://launchpad.net/%{name}/trunk/%{version}/+download/%{name}-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  python-rpm-generators
%{?python_enable_dependency_generator}
BuildRequires:  python3-setuptools
Requires:       openssh-common
BuildArch:      noarch
Patch1:         ssh-import-id-remove-shebang.patch

%description
A command-line utility that imports SSH public keys to your authorized_keys
file from online services like GitHub and Launchpad.

%prep
%autosetup -p0

%build
export LC_ALL=en_US.utf8
%python3_build

%install
%python3_install
install -Dm0644 usr/share/man/man1/ssh-import-id.1 %{buildroot}%{_mandir}/man1/ssh-import-id.1
%python_expand %fdupes %{buildroot}%{python3_sitelib}/

%files
%doc README.md
%license LICENSE
%{_bindir}/ssh-import-id
%{_bindir}/ssh-import-id-gh
%{_bindir}/ssh-import-id-lp
%{_mandir}/man1/ssh-import-id.1%{?ext_man}
%{python3_sitelib}/*

%changelog
