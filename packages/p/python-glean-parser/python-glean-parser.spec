#
# spec file for package python-glean-parser
#
# Copyright (c) 2022 SUSE LLC
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


Name:           python-glean-parser
Version:        6.3.0
Release:        0
Summary:        Parser tools for Mozilla's Glean telemetry
License:        MPL-2.0
URL:            https://github.com/mozilla/glean_parser
Source:         https://files.pythonhosted.org/packages/source/g/glean_parser/glean_parser-%{version}.tar.gz
Patch1:         remove-pytest.patch
Patch2:         fix-yaml-lint.patch
BuildRequires:  %{python_module setuptools_scm >= 7}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Jinja2 >= 2.10.1
Requires:       python-MarkupSafe >= 1.1.1
Requires:       python-PyYAML >= 5.3.1
Requires:       python-appdirs >= 1.4
Requires:       python-click >= 7
Requires:       python-diskcache >= 4
Requires:       python-jsonschema >= 3.0.2
Requires:       python-yamllint >= 1.18.0
Requires(post): update-alternatives
Requires(postun):update-alternatives
Suggests:       python-iso8601 >= 0.1.10
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module Jinja2 >= 2.10.1}
BuildRequires:  %{python_module MarkupSafe >= 1.1.1}
BuildRequires:  %{python_module PyYAML >= 5.3.1}
BuildRequires:  %{python_module appdirs >= 1.4}
BuildRequires:  %{python_module click >= 7}
BuildRequires:  %{python_module diskcache >= 4}
BuildRequires:  %{python_module jsonschema >= 3.0.2}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module yamllint >= 1.18.0}
# /SECTION
%python_subpackages

%description
Parser tools for Mozilla's Glean telemetry

%prep
%setup -q -n glean_parser-%{version}
%patch1 -p1
%patch2 -p1

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/glean_parser
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%post
%python_install_alternative glean_parser

%postun
%python_uninstall_alternative glean_parser

%files %{python_files}
%python_alternative %{_bindir}/glean_parser
%{python_sitelib}/glean_parser
%{python_sitelib}/glean_parser-%{version}*-info

%changelog
