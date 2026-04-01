#
# spec file for package python-diagnostic
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


Name:           python-diagnostic
Version:        3.0.0
Release:        0
Summary:        Present errors that contain causes better understand what happened
License:        MIT
URL:            https://github.com/pradyunsg/diagnostic
Source:         https://github.com/pradyunsg/diagnostic/archive/refs/tags/%{version}.tar.gz#/diagnostic-%{version}-gh.tar.gz
BuildRequires:  %{python_module flit-core >= 3.2}
BuildRequires:  %{python_module pip}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module docutils}
BuildRequires:  %{python_module PyYAML}
BuildRequires:  %{python_module markdown-it-py}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module rich}
# /SECTION
BuildRequires:  fdupes
Requires:       python-docutils
Requires:       python-markdown-it-py
Requires:       python-rich
Suggests:       python-docutils
BuildArch:      noarch
%python_subpackages

%description
`diagnostic` makes it easier to build command line tools with great error reporting.

%prep
%autosetup -p1 -n diagnostic-%{version}

%build
%pyproject_wheel

%check
%pytest

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%doc README.md
%license LICENSE LICENSE
%{python_sitelib}/diagnostic
%{python_sitelib}/diagnostic-%{version}.dist-info

%changelog
