#
# spec file for package python-liblore
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%{?sle15_python_module_pythons}
Name:           python-liblore
Version:        0.8.1
Release:        0
Summary:        Python library for public-inbox.org
License:        GPL-2.0-or-later
URL:            https://git.kernel.org/pub/scm/utils/liblore/liblore.git/
Source0:        https://git.kernel.org/pub/scm/utils/liblore/liblore.git/snapshot/liblore-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module pytest-asyncio}
BuildRequires:  %{python_module responses}
BuildRequires:  %{python_module typing-extensions}
# /SECTION
Requires:       python-requests
%python_subpackages

%description
A Python library for working with https://public-inbox.org/ servers,
particularly https://lore.kernel.org/. It fetches email threads, parses mbox
files, and provides utilities for working with email messages from mailing list
archives.

%prep
%autosetup -n liblore-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}/%{$python_sitelib}/liblore

%check
%pytest

%files %{python_files}
%doc CHANGELOG README.md
%license LICENSES
%{python_sitelib}/liblore
%{python_sitelib}/liblore-%{version}*-info

%changelog
