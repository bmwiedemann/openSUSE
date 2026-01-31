#
# spec file for package python-ebooklib
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


%define         _name ebooklib
Name:           python-ebooklib
Version:        0.20
Release:        0
Summary:        Ebook library which can handle EPUB2/EPUB3 format
License:        AGPL-3.0-or-later
URL:            https://github.com/aerkalov/ebooklib
Source0:        https://files.pythonhosted.org/packages/source/e/%{_name}/%{_name}-%{version}.tar.gz
Patch0:         remove-six.patch
BuildRequires:  %{python_module lxml}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pygments}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  python-rpm-macros
Requires:       python-lxml
%if 0%{?suse_version} < 1600
ExclusiveArch:  do_not_build
%else
BuildArch:      noarch
%endif
%python_subpackages

%description
%{summary}.

%prep
%autosetup -p1 -n %{_name}-%{version}

%build
%pyproject_wheel

%install
%pyproject_install

%files %{python_files}
%license LICENSE.txt
%doc AUTHORS.txt CHANGES.txt README.md
%{python_sitelib}/%{_name}
%{python_sitelib}/%{_name}-%{version}.dist-info

%changelog
