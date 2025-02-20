#
# spec file for package lieer
#
# Copyright (c) 2025 SUSE LLC
# Copyright (c) 2025 Ricardo B. Marlière <rbm@opensuse.org>
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


%define pythons python3

Name:           lieer
Version:        1.6+21
Release:        0
Summary:        Email-fetching, sending, and two-way tag sync between notmuch and GMail
License:        GPL-3.0-or-later
Group:          Productivity/Networking/Email/Utilities
URL:            http://lieer.gaute.vetsj.com/
Source0:        %{name}-%{version}.tar.xz
# PATCH-FIX-OPENSUSE Remove usage of /usr/bin/env shebangs
Patch1:         Fix-shebangs-to-remove-env-dependency.patch
BuildRequires:  %{python_module base}
BuildRequires:  %{python_module google-api-python-client}
BuildRequires:  %{python_module google-auth-oauthlib}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module tqdm}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       %{python_module google-api-python-client}
Requires:       %{python_module google-auth-oauthlib}
Requires:       %{python_module tqdm}
Requires:       notmuch
BuildArch:      noarch
%python_subpackages

%description
This program can pull, and send, email and labels (and changes to labels) from
a GMail account and store them locally in a maildir with the labels
synchronized with a notmuch database. The changes to tags in the notmuch
database may be pushed back remotely to your GMail account.

%prep
%autosetup -p1

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
chmod +x %{buildroot}/%{python_sitelib}/lieer/gmailieer.py

%files %{python_files}
%doc README.md
%license LICENSE.md
%{_bindir}/gmi
%{python_sitelib}/lieer*
%exclude %{python_sitelib}/tests

%changelog
