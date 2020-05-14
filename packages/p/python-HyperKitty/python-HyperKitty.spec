#
# spec file for package python-HyperKitty
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
Name:           python-HyperKitty
Version:        1.3.2
Release:        0
Summary:        A web interface to access GNU Mailman v3 archives
License:        GPL-3.0-only
URL:            https://gitlab.com/mailman/hyperkitty
Source:         https://files.pythonhosted.org/packages/source/H/HyperKitty/HyperKitty-%{version}.tar.gz
# https://gitlab.com/mailman/hyperkitty/-/commit/03c99ad5beefeac4474b5a00c840fd9debccba02
Patch0:         python-HyperKitty-remove-legacy-use-of-available_attrs.patch
BuildRequires:  %{python_module isort}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Django >= 1.11
Requires:       python-django-compressor >= 1.3
Requires:       python-django-extensions >= 1.3.7
Requires:       python-django-gravatar2 >= 1.0.6
Requires:       python-django-haystack >= 2.8.0
Requires:       python-django-mailman3 >= 1.2.0
Requires:       python-django-q >= 1.0.0
Requires:       python-djangorestframework >= 3.0.0
Requires:       python-flufl.lock
Requires:       python-libsass
Requires:       python-mailmanclient >= 3.1.1
Requires:       python-networkx >= 1.9.1
Requires:       python-python-dateutil >= 2.0
Requires:       python-pytz >= 2012
Requires:       python-robot-detection >= 0.3
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module Django >= 1.11}
BuildRequires:  %{python_module Whoosh >= 2.5.7}
BuildRequires:  %{python_module beautifulsoup4 >= 4.3.2}
BuildRequires:  %{python_module django-compressor >= 1.3}
BuildRequires:  %{python_module django-extensions >= 1.3.7}
BuildRequires:  %{python_module django-gravatar2 >= 1.0.6}
BuildRequires:  %{python_module django-haystack >= 2.8.0}
BuildRequires:  %{python_module django-mailman3 >= 1.2.0}
BuildRequires:  %{python_module django-q >= 1.0.0}
BuildRequires:  %{python_module djangorestframework >= 3.0.0}
BuildRequires:  %{python_module elasticsearch}
BuildRequires:  %{python_module flufl.lock}
BuildRequires:  %{python_module mailmanclient >= 3.1.1}
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module networkx >= 1.9.1}
BuildRequires:  %{python_module pytest-django}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module python-dateutil >= 2.0}
BuildRequires:  %{python_module pytz >= 2012}
BuildRequires:  %{python_module robot-detection >= 0.3}
# /SECTION
%python_subpackages

%description
A web interface to access GNU Mailman v3 archives.

%prep
%setup -q -n HyperKitty-%{version}
%patch0 -p1

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export DJANGO_SETTINGS_MODULE="hyperkitty.tests.settings_test"
export PYTHONPATH='.'
%python_exec example_project/manage.py test

%files %{python_files}
%doc AUTHORS.txt README.rst example_project doc/*.rst
%license COPYING.txt
%{python_sitelib}/*

%changelog
