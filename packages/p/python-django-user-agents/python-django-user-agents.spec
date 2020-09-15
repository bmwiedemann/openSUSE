#
# spec file for package python-django-user-agents
#
# Copyright (c) 2020 SUSE LLC
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define skip_python2 1
Name:           python-django-user-agents
Version:        0.4.0
Release:        0
Summary:        Django identification of visitors information
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/selwin/django-user_agents
Source:         https://files.pythonhosted.org/packages/source/d/django-user_agents/django-user_agents-%{version}.tar.gz
BuildRequires:  %{python_module Django}
BuildRequires:  %{python_module pytest-django}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module user-agents}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Django
Requires:       python-user-agents
BuildArch:      noarch
%python_subpackages

%description
A django package that allows easy identification of visitor's browser, OS and device information,
including whether the visitor uses a mobile phone, tablet or a touch capable device. Under the hood,
it uses `user-agents <https://github.com/selwin/python-user-agents>`_.

%prep
%setup -q -n django-user_agents-%{version}
mkdir -p django_user_agents/tests/templates/
touch django_user_agents/tests/templates/test.html
cat > ./django_user_agents/tests/templates/test_filters.html << EOF
{% load user_agents %}

{% if request|is_mobile or request|is_pc or request|is_tablet or request|is_bot or request|is_touch_capable %}
    Just making sure all the filters can be used without errors
{% endif %}
EOF

%build
%python_build

%install
%python_install
%{python_expand rm -r %{buildroot}%{$python_sitelib}/django_user_agents/tests/
%fdupes %{buildroot}%{$python_sitelib}
}

%check
export PYTHONPATH=${PWD}
export DJANGO_SETTINGS_MODULE=django_user_agents.tests.settings
%pytest --pyargs django_user_agents.tests.tests

%files %{python_files}
%doc README.rst
%license LICENSE.txt
%{python_sitelib}/*

%changelog
