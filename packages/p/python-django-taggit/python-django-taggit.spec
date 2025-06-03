#
# spec file for package python-django-taggit
#
# Copyright (c) 2025 SUSE LLC
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


%define mod_name django-taggit
%{?sle15_python_module_pythons}
BuildArch:      noarch
Name:           python-%{mod_name}
Version:        5.0.1
Release:        0
Summary:        Django-taggit is a reusable Django application for simple tagging
License:        BSD-3-Clause-Clear
Group:          Development/Languages/Python
URL:            https://github.com/alex/django-taggit
Source:         https://pypi.python.org/packages/source/d/django-taggit/%{mod_name}-%{version}.tar.gz
BuildRequires:  %{python_module Django >= 4.2}
BuildRequires:  %{python_module djangorestframework}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytz}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Django >= 4.2
Recommends:     %{name}-lang = %{version}
%ifpython3 && ! 0%{?skip_python3}
%lang_package -n %{python3_prefix}-django-taggit
%endif
%python_subpackages

%description
Django-taggit is a reusable Django application for simple tagging.

%prep
%setup -q -n django-taggit-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%find_lang django
%python_expand grep -F %{$python_sitelib} django.lang > django_%{$python_bin_suffix}.lang
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_expand $python -m django test -v 2 --settings=tests.settings

%files %{python_files}
%license LICENSE
%doc AUTHORS CHANGELOG.rst README.rst
%{python_sitelib}/taggit/
%{python_sitelib}/django[-_]taggit*/
%exclude %{python_sitelib}/taggit/locale

%ifpython3 && ! 0%{?skip_python3}
%files -n %{python3_prefix}-django-taggit-lang -f django_%{python3_bin_suffix}.lang
%{python3_sitelib}/taggit/locale
%endif

%changelog
