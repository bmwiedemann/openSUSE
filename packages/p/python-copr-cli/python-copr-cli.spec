#
# spec file for package python-copr-cli
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


Name:           python-copr-cli
Version:        1.104
Release:        0
Summary:        Copr cli
License:        GPL-2.0-or-later
URL:            https://pagure.io/copr/copr
Source:         https://files.pythonhosted.org/packages/source/c/copr-cli/copr-cli-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Jinja2
Requires:       python-copr >= 1.116
Requires:       python-filelock
Requires:       python-future
Requires:       python-humanize
Requires:       python-requests-gssapi
Requires:       python-responses
Requires:       python-simplejson
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module Jinja2}
BuildRequires:  %{python_module copr >= 1.116}
BuildRequires:  %{python_module filelock}
BuildRequires:  %{python_module future}
BuildRequires:  %{python_module humanize}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests-gssapi}
BuildRequires:  %{python_module responses}
BuildRequires:  %{python_module simplejson}
# /SECTION
%python_subpackages

%description
CLI tool to run copr.

%prep
%setup -q -n copr-cli-%{version}
sed -i '1{/#!/d}' copr_cli/package_build_order.py

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/copr-cli
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%post
%python_install_alternative copr-cli

%postun
%python_uninstall_alternative copr-cli

%files %{python_files}
%license LICENSE
%python_alternative %{_bindir}/copr-cli
%{python_sitelib}/copr_cli
%{python_sitelib}/copr_cli-%{version}*-info

%changelog
