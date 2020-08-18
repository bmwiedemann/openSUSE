#
# spec file for package python-xapian-haystack
#
# Copyright (c) 2020 SUSE LLC
# Copyright (c) 2020 Stasiek Michalski <hellcp@opensuse.org>.
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
%global modname xapian-haystack
%define skip_python2 1
Name:           python-%{modname}
Version:        2.1.1
Release:        0
Summary:        Backend of Django-Haystack for the Xapian search engine
License:        GPL-2.0-only
URL:            https://github.com/notanumber/xapian-haystack
Source:         https://files.pythonhosted.org/packages/source/x/xapian-haystack/%{modname}-%{version}.tar.gz
BuildRequires:  %{python_module Django >= 1.8}
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module django-haystack >= 2.5.1}
Requires:       python-Django >= 1.8
Requires:       python-django-haystack >= 2.5.1
BuildArch:      noarch
%python_subpackages

%description
Xapian-haystack is a backend of Django-Haystack for the Xapian search engine.

%prep
%setup -q -n %{modname}-%{version}

%build
%python_build

%install
%python_install

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/*

%changelog
