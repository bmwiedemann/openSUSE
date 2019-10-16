#
# spec file for package python-soundcloud
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-soundcloud
Version:        0.5.0
Release:        0
Summary:        A friendly wrapper library for the Soundcloud API
License:        BSD-2-Clause
URL:            https://github.com/soundcloud/soundcloud-python
Source:         https://files.pythonhosted.org/packages/source/s/soundcloud/soundcloud-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module fudge >= 1.0.3}
BuildRequires:  %{python_module nose}
BuildRequires:  %{python_module requests >= 0.14.0}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module simplejson >= 2.0}
BuildRequires:  %{python_module six}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-fudge >= 1.0.3
Requires:       python-requests >= 0.14.0
Requires:       python-simplejson >= 2.0
Requires:       python-six
%python_subpackages

%description
A friendly wrapper around the `Soundcloud API`_.

.. _Soundcloud API: http://developers.soundcloud.com/

%prep
%setup -q -n soundcloud-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_expand %{_bindir}/nosetests

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/*

%changelog
