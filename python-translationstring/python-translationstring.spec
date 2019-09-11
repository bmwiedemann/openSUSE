#
# spec file for package python-translationstring
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2015 LISA GmbH, Bingen, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-translationstring
Version:        1.3
Release:        0
Summary:        Utility library for i18n relied on by various Repoze and Pyramid packages
License:        SUSE-Repoze
Group:          Development/Languages/Python
Url:            https://github.com/Pylons/translationstring
Source:         https://files.pythonhosted.org/packages/source/t/translationstring/translationstring-%{version}.tar.gz
# PATCH-FIX-UPSTREAM use_pylons_theme.patch -- Use pylons_sphinx_theme from external package
Patch0:         use_pylons_theme.patch
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  git
BuildRequires:  python-rpm-macros
# SECTION documentation requirements
BuildRequires:  python3-Sphinx
BuildRequires:  python3-pylons-sphinx-themes
# /SECTION
BuildArch:      noarch
%python_subpackages

%description
A library used by various Pylons Project packages for internationalization
(i18n) duties related to translation.

This package provides a translation string class, a translation string factory
class, translation and pluralization primitives, and a utility that helps
Chameleon templates use translation facilities of this package. It does not
depend on Babel, but its translation and pluralization services are meant to
work best when provided with an instance of the babel.support.Translations class.

%package     -n %{name}-doc
Summary:        Documentation files for %{name}
Group:          Development/Languages/Python
Requires:       %{name} = %{version}
Provides:       %{python_module translationstring-doc = %{version}}

%description -n %{name}-doc
This package contains documentation files for %{name}.

%prep
%setup -q -n translationstring-%{version}
%patch0 -p1
# drop build date from doc to fix build-compare
sed -i "s/\(html_last_updated_fmt = \).*/\\1None/" docs/conf.py
rm -rf translationstring.egg-info

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

# Need package installed before building docs
pushd docs && PYTHONPATH=%{buildroot}%{python3_sitelib} make html && rm _build/html/.buildinfo
popd

%check
%python_exec setup.py test

%files %{python_files}
%defattr(-,root,root,-)
%doc CONTRIBUTORS.txt COPYRIGHT.txt LICENSE.txt README.rst
%{python_sitelib}/*

%files -n %{name}-doc
%defattr(-,root,root,-)
%doc docs/_build/html

%changelog
