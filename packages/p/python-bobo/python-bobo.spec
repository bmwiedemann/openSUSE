#
# spec file for package python-bobo
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
%bcond_without test
Name:           python-bobo
Version:        2.4.0
Release:        0
Summary:        Web application framework for the impatient
License:        ZPL-2.1
Group:          Development/Languages/Python
URL:            http://bobo.readthedocs.io/
Source:         https://files.pythonhosted.org/packages/source/b/bobo/bobo-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-WebOb
Requires:       python-six
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
# SECTION test requirements
%if %{with test}
BuildRequires:  %{python_module WebOb}
BuildRequires:  %{python_module bobodoctestumentation >= 2.4.0}
BuildRequires:  %{python_module six}
%endif
# /SECTION
%python_subpackages

%description
Bobo is a framework for creating WSGI web applications.
It addresses two problems: mapping URLs to objects,
and calling objects to generate HTTP responses.

Bobo doesn't have a templating language, a database integration layer,
nor a number of other features that are better provided by WSGI
middle-ware or application-specific libraries.

Bobo builds on other frameworks, most notably WSGI and WebOb.

%prep
%setup -q -n bobo-%{version}

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/bobo
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%post
%python_install_alternative bobo

%postun
%python_uninstall_alternative bobo

%files %{python_files}
%doc CHANGES.rst README.rst
%python_alternative %{_bindir}/bobo
%{python_sitelib}/*

%changelog
