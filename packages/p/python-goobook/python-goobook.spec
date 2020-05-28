#
# spec file for package python-goobook
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


%define skip_python2 1
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-goobook
Version:        3.4
Release:        0
Summary:        Search your google contacts from the command-line or mutt
License:        GPL-3.0-only
URL:            https://gitlab.com/goobook/goobook
Source:         https://files.pythonhosted.org/packages/source/g/goobook/goobook-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-google-api-python-client >= 1.6.4
Requires:       python-oauth2client >= 1.5.0
Requires:       python-simplejson >= 2.1.0
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
%python_subpackages

%description
Search your google contacts from the command-line or mutt.

The purpose of GooBook is to make it possible to use your Google Contacts from
the command-line and from MUAs such as Mutt. It can be used from Mutt the same
way as abook.

%prep
%setup -q -n goobook-%{version}
sed -i '/^#!\/usr\/bin\/env python/d' goobook/application.py

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/goobook
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%post
%python_install_alternative goobook

%postun
%python_uninstall_alternative goobook

%files %{python_files}
%doc CHANGES.rst README.rst
%license LICENSE.txt
%python_alternative %{_bindir}/goobook
%{python_sitelib}/*

%changelog
