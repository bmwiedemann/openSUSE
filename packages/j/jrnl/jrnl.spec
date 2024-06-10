#
# spec file for package jrnl
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


%define pythons python3

Name:           jrnl
Version:        4.1
Release:        0
Summary:        Collect your thoughts and notes without leaving the command line
License:        GPL-3.0-only
URL:            https://jrnl.sh
Source0:        https://files.pythonhosted.org/packages/source/j/jrnl/jrnl-%{version}.tar.gz
Source99:       keyring_note.md
#PATCH-FIX-OPENSUSE jrnl-dateutil.patch malcolmlewis@opensuse.org -- Fix dateutil naming convention.
Patch0:         jrnl-dateutil.patch
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  python3-pip
BuildRequires:  python3-poetry-core >= 1.0.0
## MANUAL BEGIN
Requires:       python3-colorama
Requires:       python3-cryptography
Requires:       python3-dateutil
Requires:       python3-keyring
Requires:       python3-parsedatetime
Requires:       python3-pyxdg
Requires:       python3-rich
Requires:       python3-ruamel.yaml
Requires:       python3-tzlocal
## MANUAL END
BuildArch:      noarch

%description
Simple journal application for the command line. You can use it to
easily create, search, and view journal entries. Journals are stored
as human-readable plain text, and can also be encrypted using AES
encryption.

%prep
%autosetup -p1
cp %{S:99} .

%build
%pyproject_wheel

%install
%pyproject_install
%fdupes %{buildroot}%{python_sitelib}

%files
%doc README.md keyring_note.md
%license LICENSE.md
%{_bindir}/jrnl
%{python_sitelib}/jrnl
%{python_sitelib}/jrnl-%{version}.dist-info

%changelog
