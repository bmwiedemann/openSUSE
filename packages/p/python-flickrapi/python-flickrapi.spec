#
# spec file for package python-flickrapi
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
Name:           python-flickrapi
Version:        2.4.0
Release:        0
Summary:        Python interface to Flickr
License:        Python-2.0
Group:          Development/Libraries/Python
URL:            http://stuvel.eu/projects/flickrapi
Source0:        https://files.pythonhosted.org/packages/source/f/flickrapi/flickrapi-%{version}.tar.gz
# https://github.com/sybrenstuvel/flickrapi/commit/e47e62df304d36ae81c483230bb41e6f4dde8bfd
Patch0:         python-flickrapi-no-python2.patch
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module poetry}
BuildRequires:  %{python_module requests-oauthlib >= 0.4.2}
BuildRequires:  %{python_module requests-toolbelt >= 0.3.1}
BuildRequires:  %{python_module requests >= 2.4.3}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-requests >= 2.4.3
Requires:       python-requests-oauthlib >= 0.4.2
Requires:       python-requests-toolbelt >= 0.3.1
BuildArch:      noarch
%ifpython2
Provides:       python-flickrapi-doc = %{version}
Obsoletes:      python-flickrapi-doc < %{version}
%endif
%python_subpackages

%description
The easiest to use, most complete, and most actively developed
Python interface to the Flickr API. It includes support for
authorized and non-authorized access, uploading and replacing
photos, and all Flickr API functions.

%prep
%setup -q -n flickrapi-%{version}
%patch0 -p1
sed -i "1d" flickrapi/__init__.py # Fix non-executable script

%build
%pyproject_wheel

%install
%pyproject_install
rm -rf %{buildroot}%{python_sitelib}/*.txt # Remove wrongly installed documentation
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%license LICENSE.txt
%doc README.md
%{python_sitelib}/*

%changelog
