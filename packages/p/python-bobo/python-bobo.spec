#
# spec file for package python-bobo
#
# Copyright (c) 2024 SUSE LLC
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


Name:           python-bobo
Version:        2.4.0
Release:        0
Summary:        Web application framework for the impatient
License:        ZPL-2.1
URL:            http://bobo.readthedocs.io/
Source:         https://files.pythonhosted.org/packages/source/b/bobo/bobo-%{version}.tar.gz
#PATCH-FIX-UPSTREAM part of https://github.com/zopefoundation/bobo/pull/23 Drop support for Python 2.7 up to 3.6.
Patch:          drop-py27.patch
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-WebOb
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
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
%autosetup -p1 -n bobo-%{version}

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
%{python_sitelib}/bobo*.py
%{python_sitelib}/bobo-%{version}*info
%pycache_only %{python_sitelib}/__pycache__/bobo*.pyc

%changelog
