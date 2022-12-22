#
# spec file for package python-sorl-thumbnail
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define skip_python2 1
Name:           python-sorl-thumbnail
Version:        12.7.0
Release:        0
Summary:        Thumbnails for Django
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/jazzband/sorl-thumbnail
Source:         https://files.pythonhosted.org/packages/source/s/sorl-thumbnail/sorl-thumbnail-%{version}.tar.gz
BuildRequires:  %{python_module django-codemod}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  lsof
BuildRequires:  python-rpm-macros
Requires:       python-Django >= 2
Recommends:     ImageMagick
Recommends:     python-dbm
Suggests:       python-Wand
Suggests:       python-ImageMagick
Suggests:       vips-tools
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module Django >= 2}
BuildRequires:  %{python_module Wand}
BuildRequires:  %{python_module boto if python-base < 3.10}
BuildRequires:  %{python_module dbm}
BuildRequires:  %{python_module pytest-django}
BuildRequires:  %{python_module redis}
BuildRequires:  %{pythons}
BuildRequires:  ImageMagick
BuildRequires:  redis
BuildRequires:  vips-tools
# /SECTION
%python_subpackages

%description
Thumbnails for Django.

Features at a glance
---------------------
- Storage support
- Pluggable Engine support (PIL, pgmagick)
- Pluggable Key Value Store support (redis, cached db)
- Pluggable Backend support
- Admin integration with possibility to delete
- Dummy generation
- Flexible, simple syntax, generates no html
- ImageField for model that deletes thumbnails
- CSS style cropping options
- Margin calculation for vertical positioning

%prep
%setup -q -n sorl-thumbnail-%{version}

djcodemod run --removed-in 4.0 tests/*/urls.py

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export LANG=en_US.UTF-8

PYTHONPATH=.
export DJANGO_SETTINGS_MODULE=tests.settings.pil
# TestDescriptors: gh#jazzband/sorl-thumbnail#673
# TemplateTestCaseB & test_image_file_deserialize: three tests use online resources
skip_tests="TestDescriptors or test_image_file_deserialize or (TemplateTestCaseB and (test_portrait or test_url))"
%pytest -rs -k "not ($skip_tests)"
export DJANGO_SETTINGS_MODULE=tests.settings.imagemagick
# test_orientation skipped because of gh#jazzband/sorl-thumbnail#676
%pytest -rs -k "not ($skip_tests or test_orientation)"
export DJANGO_SETTINGS_MODULE=tests.settings.dbm
%pytest -rs -k "not ($skip_tests)"
export DJANGO_SETTINGS_MODULE=tests.settings.imagemagick
%pytest -rs -k "not ($skip_tests or test_templatetags)"
export DJANGO_SETTINGS_MODULE=tests.settings.wand
%pytest -rs -k "not ($skip_tests)"

# pgmagick is not installed in all environments
%{python_expand if [ -d %{$python_sitearch}/pgmagick/ ]; then
  export DJANGO_SETTINGS_MODULE=tests.settings.pgmagick
  $python -m pytest -rs -k "not ($skip_tests)"
fi
}

%{_sbindir}/redis-server &
export DJANGO_SETTINGS_MODULE=tests.settings.redis
%pytest -rs -k "not ($skip_tests)"

%files %{python_files}
%doc AUTHORS CHANGES.rst README.rst
%license LICENSE
%{python_sitelib}/sorl/
%{python_sitelib}/*sorl[-_]thumbnail*/

%changelog
