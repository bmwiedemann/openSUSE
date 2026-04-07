#
# spec file for package python-django-widget-tweaks
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


Name:           python-django-widget-tweaks
Version:        1.5.1
Release:        0
Summary:        Django form field rendering in templates
License:        MIT
URL:            https://github.com/jazzband/django-widget-tweaks
Source:         https://files.pythonhosted.org/packages/source/d/django-widget-tweaks/django_widget_tweaks-%{version}.tar.gz
BuildRequires:  %{python_module Django >= 4.2}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Django >= 4.2
BuildArch:      noarch
%python_subpackages

%description
Tweak the form field rendering in templates, not in python-level form definitions.

%prep
%setup -q -n django_widget_tweaks-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec -m django test -v2 --settings=tests.settings

%files %{python_files}
%doc CHANGES.rst README.rst
%license LICENSE
%{python_sitelib}/widget_tweaks
%{python_sitelib}/django_widget_tweaks-%{version}.dist-info

%changelog
