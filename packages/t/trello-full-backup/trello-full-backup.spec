#
# spec file for package trello-full-backup
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


Name:           trello-full-backup
Version:        0.3.1
Release:        0
Summary:        Trello backup script
License:        MIT
Group:          Productivity/Archiving/Backup
URL:            https://github.com/jtpio/trello-full-backup
Source:         https://files.pythonhosted.org/packages/source/t/trello-full-backup/trello-full-backup-%{version}.tar.gz
Source1:        LICENSE
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  python3-setuptools
Requires:       python3-requests
BuildArch:      noarch

%description
This tool backups everything from Trello:

 * boards, open and closed, as JSON files
 * lists, open and archived, as JSON files
 * cards, open and archived, as JSON files
 * attachments, downloaded as raw files

The script also creates a folder tree structure corresponding to
the way data is organized. This is to make it more convenient to
navigate locally between folders, as it mimics the flow from
the web and mobile apps.

%prep
%setup -q

%build
install -m 644 %{SOURCE1} .
%python3_build

%install
%python3_install
%fdupes %{buildroot}%{python3_sitelib}

%files
%doc README.rst
%license LICENSE
%{_bindir}/trello-full-backup
%{python3_sitelib}/*

%changelog
