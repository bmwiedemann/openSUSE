#
# spec file for package python-dash-html-components
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


Name:           python-dash-html-components
Version:        2.0.0
Release:        0
Summary:        Vanilla HTML components for Dash - Legacy
License:        MIT
URL:            https://github.com/plotly/dash-html-components
Source:         https://files.pythonhosted.org/packages/source/d/dash-html-components/dash_html_components-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
Vanilla HTML components for Dash

As of Dash 2, the development of dash-html-components has been moved to the main Dash repo

This package exists for backward compatibility as Dash still lists it as requirement. It
has no further functionality than displaying a deprecation message.

%prep
%setup -q -n dash_html_components-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitelib}/dash_html_components
%{python_sitelib}/dash_html_components-%{version}*-info

%changelog
